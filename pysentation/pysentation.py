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
from getkey import getkey, keys
from module import Pysentation, PysentationScreen
from errors import PysentationError


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


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.argument('python_file', required=False, nargs=-1)
@click.option('-v', '--version', is_flag=True, help='Displays the current version of pysentation installed on the system.')
def main(**options):
    """
    """
    pass


if __name__ == '__main__':
    main()
