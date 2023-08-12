"""
██████╗ ██╗   ██╗███████╗███████╗███╗   ██╗████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝ ███████╗█████╗  ██╔██╗ ██║   ██║   ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║        ██║   ███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

pysentation Github repository: https://github.com/mimseyedi/pysentation
"""


import click
from getkey import getkey, keys
from module import Pysentation, PysentationScreen


def screen_manager(screen: PysentationScreen) -> None:
    """

    :param screen: An object from PysentationScreen.
    :return: None
    """
    try:
        while True:
            input_key = getkey()

            match input_key:
                case keys.UP:
                    pass
                case keys.DOWN:
                    pass
                case keys.LEFT:
                    pass
                case keys.RIGHT:
                    pass
                case 'r':
                    pass
                case 'f':
                    pass
                case 'l':
                    pass
                case 'q':
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
