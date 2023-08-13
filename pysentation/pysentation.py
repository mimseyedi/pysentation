"""
██████╗ ██╗   ██╗███████╗███████╗███╗   ██╗████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝ ███████╗█████╗  ██╔██╗ ██║   ██║   ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║        ██║   ███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

pysentation Github repository: https://github.com/mimseyedi/pysentation
"""


import os
import click
from pathlib import Path
from getkey import getkey, keys
from rich import print as cprint
from module import Pysentation, PysentationScreen
from errors import PysentationError
from _version import __version__


def screen_manager(screen: PysentationScreen) -> None:
    """
    The task of this function is to execute and manage the screen.
    This function accepts an argument, which is an object of PysentationScreen and manages the screen according to
    the defined control keys.

    -These keys are as follows:

        'right'      >>> next slide
        'left'       >>> previous slide
        'up'         >>> highlight top line
        'down'       >>> highlight bottom line
        'r'          >>> reset the current slide
        'shift+r'    >>> reset the screen
        'f'          >>> go to first slide
        'l'          >>> go to last slide
        'q'          >>> quit

    :param screen: An object from PysentationScreen.
    :return: None
    """

    try:
        while True:
            input_key = getkey()

            match input_key:
                case keys.RIGHT:
                    screen.next_slide()
                case keys.LEFT:
                    screen.previous_slide()
                case keys.UP:
                    screen.highlight_top_line()
                case keys.DOWN:
                    screen.highlight_bottom_line()
                case 'r':
                    screen.reset_slide()
                case 'R':
                    screen.reset_screen()
                case 'f':
                    screen.first_slide()
                case 'l':
                    screen.last_slide()
                case 'q':
                    os.system('clear' if os.name == 'posix' else 'cls')
                    break

    except KeyboardInterrupt:
        pass


def options_manager(screen: PysentationScreen, options: dict) -> None:
    """
    The task of this function is to manage and prioritize options.
    This function connects options to executive operations according to their priority and can handle a set of options at the same time.

    :param screen: main screen, an object from PysentationScreen.
    :param options: Acceptable options in dictionary format.
    :return: None
    """

    if 'output' in options.keys():
        if options.get('color'):
            screen.set_color(color=options.get('color'))

        if options.get('theme'):
            screen.set_theme(theme=options.get('theme'))

        if options.get('disable'):
            screen.disable_output()

        screen.write_output(output_path=options.get('output'))
    else:
        if 'slides' in options.keys() or 'property' in options.keys():
            for option, value in options.items():
                if option == 'slides':
                    cprint(screen.get_slides())
                elif option == 'property':
                    cprint(
                        screen.get_property(
                            slide_index=int(value) - 1
                        )
                    )
        else:
            if options.get('color'):
                screen.set_color(color=options.get('color'))

            if options.get('theme'):
                screen.set_theme(theme=options.get('theme'))

            if options.get('disable'):
                screen.disable_output()

            if options.get('from'):
                screen.start_from(slide_index=options.get('start') - 1)
            else:
                screen.display()

            screen_manager(screen=screen)


@click.command(
    context_settings={'help_option_names': ['-h', '--help']},
    epilog="pysentation Github repo: https://github.com/mimseyedi/pysentation"
)
@click.argument('python_file', required=False, nargs=-1)
@click.option('-f', '--from', nargs=1, type=int, help='Start showing the screen from the selected slide.')
@click.option('-c', '--color', nargs=1, help='Set color for all slides.')
@click.option('-t', '--theme', nargs=1, help='Set syntax highlighter theme for all slides.')
@click.option('-d', '--disable', is_flag=True, help='Disable code interpretation for all slides.')
@click.option('-p', '--property', nargs=1, type=int, help='Display the properties of the selected slide.')
@click.option('-s', '--slides', is_flag=True, help='Display the slides on the screen with their position.')
@click.option('-o', '--output', nargs=1, type=Path, help='Writing all slides in order in a text file.')
@click.option('-v', '--version', is_flag=True, help='Display the current version of pysentation installed on the system.')
def main(**options):
    """
    pysentation is a CLI tool for displaying Python presentations.\n
    Hot keys to manage screen:\n
    \b
    right    Next slide.
    left     Previous slide.
    up       Highlight top line.
    down     Highlight bottom line.
    r        Reset the current slide.
    shift+r  Reset the screen.
    f        Go to first slide.
    l        Go to last slide.
    q        Quit.
    """

    if options['version'] and not options['python_file']:
        click.echo(__version__)

    elif options['python_file']:
        if options['version']:
            click.echo(
                "Usage: pysentation [OPTIONS] [PYTHON_FILE]...\nTry 'pysentation --help' for help.\n\nError: -v, --version option cannot be used at this stage.")
        else:
            pysentation_obj = Pysentation(
                source=options['python_file'][0]
            )
            try:
                screen: PysentationScreen = pysentation_obj.build()

                options_manager(
                    screen=screen,
                    options={
                        option: value
                        for option, value in options.items()
                        if value is not None and value is not False and option != 'python_file'
                    }
                )
            except PysentationError as error:
                cprint(
                    f"[bold red]Error:[/bold red] {error}"
                )
    else:
        click.echo(
            "Usage: pysentation [OPTIONS] [PYTHON_FILE]...\nTry 'pysentation --help' for help.\n\nError: Missing argument 'PYTHON_FILE...'.")


if __name__ == '__main__':
    main()
