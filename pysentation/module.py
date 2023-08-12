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
import sys
import traceback
from pathlib import Path
from rich.box import HEAVY
from rich.panel import Panel
from rich.console import Group
from rich import print as cprint
from rich.color import ColorParseError
from rich.style import StyleType, Style
from rich.markup import render, MarkupError
from rich.syntax import Syntax, SyntaxTheme
from rich.text import TextType, AlignMethod
from signs import (
    PYSENTATION_STARTING_BLOCK,
    PYSENTATION_ENDING_BLOCK,
    PYSENTATION_SLIDE,
    PYSENTATION_PROPERTY,
    PYSENTATION_COMMENT,
)
from errors import (
    PysentationError,
    PysentationInitError,
    PysentationScopeRangeError,
    PysentationPropertyError,
    PysentationCommentError,
    PysentationFileNotFoundError,
    PysentationIsADirectoryError,
    PysentationNotAPythonFileError,
    PysentationEmptyScreenError,
)


class PysentationSlide:
    """
    PysentationSlide refers to slides that have the separated contents of a Python file
    and can be displayed in the form of a slide with the help of a PysentationScreen.

    Args:
        content (list[str|Syntax|Panel]): The content to be displayed on the slide. These contents include text and Python code.
        slide_number (str): Slide number. This number can specify the number of slides in a PysentationScreen.
        title (TextType|str): The title of the slide that will be displayed at the top. Its default value is "none".
        title_align (AlignMethod|str): The location is the title of the slide. You can choose between three ['left', 'center', 'right] options.
        Its default value is equal to x, which results in displaying the title in the middle.
        color (StyleType): The color of the slide box and the values accepted by the rich module, StyleType can be attributed to it.
        Its default value is "none", which follows the terminal's default color.
        expand (bool): If its value is True, the width of the slide will be equal to the width of the terminal screen, and
        otherwise, the width of the slide will be adjusted according to the size of its contents. Its default value is True.
        code_bg_color (str): It sets the background color of the Python code display, and its default
        value is 'default', which matches the default color of the terminal.
        code_theme (str|SyntaxTheme): The theme highlights Python codes and its default value is 'gruvbox-dark'.
        It follows the strings and SyntaxTheme of the rich module.
        interpretable (bool): Can the codes in the slide be interpreted or not? The default value is True.
    """

    def __init__(
        self,
        content: list[str|Syntax|Panel],
        slide_number: str,
        title: TextType|str = None,
        title_align: AlignMethod|str = 'center',
        color: StyleType = 'none',
        expand: bool = True,
        code_bg_color: str = 'default',
        code_theme: str|SyntaxTheme = 'gruvbox-dark',
        interpretable: bool = True,
    ) -> None:
        pass

    def render(self) -> Panel:
        """
        The task of this method is to render the PysentationSlide and turn it into a panel of the rich module.
        By turning PysentationSlide into a panel, it is possible for the slide to be displayed correctly by a PysentationScreen object.

        :return: rich.Panel
        """
        pass

    def go_up(self) -> None:
        """
        With the help of this method, you can move between the lines of Python codes in the slide,
        and the task of this method is to go up among the Python codes in the slide.

        :return: None
        """
        pass

    def go_down(self) -> None:
        """
        With the help of this method, you can move between the lines of Python codes in the slide,
        and the task of this method is to go down among the Python codes in the slide.

        :return: None
        """
        pass

    @staticmethod
    def interpret(source: str) -> tuple[bool, str]:
        """
        The task of this method is to interpret the pieces of codes inside the slide and return
        the output of the interpreted code.

        :param source: The source code to be interpreted as a string.
        :return: tuple[bool, str]
        """
        pass

    def reset_slide(self) -> None:
        """
        The task of this method is to reset the slide and modify the variables related to the display to the initial value.
        Specifically self.__h_line and self.__code_index.

        :return: None
        """
        pass

    def __fix_syntax_highlighter(self) -> None:
        """
        The task of this method is to modify and replace the previously defined syntax highlighter with
        the syntax highlighter that includes the source properties.

        :return: None
        """
        pass

    def __add__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


class PysentationScreen:
    """
    PysentationScreen is a curtain to display PysentationSlides, which can manage and execute their display.

    Among the tasks of PysentationScreen, the following can be mentioned:
        - Show PysentationSlides
        - Move between PysentationSlides
        - Resetting the PysentationSlides
        - Changing and modifying PysentationSlides

    Args:
        slides (list[PysentationSlide...]): A list of PysentationSlides to be displayed.
    """

    def __init__(self, slides: list[PysentationSlide]) -> None:
        pass

    def display(self) -> None:
        """
        This method displays the PysentationSlide selected by self.__slideno.

        :return: None
        """
        pass

    def next_slide(self) -> None:
        """
        With the help of this method, you can move between PysentationSlide.
        The task of this method is to display the next PysentationSlide in the list.
        If there is no PysentationSlide, it does nothing.

        :return: None
        """
        pass

    def previous_slide(self) -> None:
        """
        With the help of this method, you can move between PysentationSlide.
        The task of this method is to display the previous PysentationSlide in the list.
        If there is no PysentationSlide, it does nothing.

        :return: None
        """
        pass

    def reset_slide(self) -> None:
        """
        The task of this method is to reset the current PysentationSlide.
        so that its values return to the initial state.

        :return: None
        """
        pass

    def reset_screen(self) -> None:
        """
        The task of this method is to reset the PysentationScreen.
        so that its values return to the initial state.
        Specifically reset self.__slideno.

        :return: None
        """
        pass

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass
