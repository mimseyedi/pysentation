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
        self.content = content
        self.slide_number = slide_number
        self.title = title
        self.title_align = title_align
        self.color = color
        self.expand = expand
        self.code_bg_color = code_bg_color
        self.code_theme = code_theme
        self.interpretable = interpretable
        self.__h_line: int = 1
        self.__code_index: int = 0
        self.__codes: list = [
            element for element in self.content if isinstance(element, Syntax)
        ]

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

class Pysentation:
    """
    An object of this class can read a Python source and create a PysentationScreen from a collection of PysentationSlide.
    By validating and confirming the parameters and rules of a Python file, written in pysentation style to create a Python presentation,
    any object of this class can return a screen to display slides. By using the build method, you can create a PysentationScreen
    according to the source and have access and control to display the slides.

    Args:
        source (str|Path): The address of the python file to be converted into a pysentation presentation.
    """

    def __init__(self, source: str|Path) -> None:
        pass

    def read_source(self) -> str:
        """
        The task of this method is to read and validate the source to continue the process of
        converting the source to PysentationScreen.

        :return: str
        """
        pass

    @staticmethod
    def detector(source: str) -> tuple[bool, str|PysentationError]:
        """
        The task of this method is to find the scope and range of pysentation.

        :param source: The source path.
        :return: tuple[bool, str|PysentationError]
        """
        pass

    @staticmethod
    def separator(source_code: str) -> list[str]:
        """
        The task of this method is to separate the slides in the source.

        :param source_code: The source contents.
        :return: list[str]
        """
        pass

    @staticmethod
    def extract_props(slide: list[str]) -> dict:
        """
        The task of this method is to extract and validate the properties of a slide.

        :param slide: A text-base slide separated by the self.separator method
        :return: dict
        """
        pass

    @staticmethod
    def extract_content(slide: list[str]) -> list[str]:
        """
        The task of this method is to extract and validate the content of a slide.

        :param slide: A text-base slide separated by the self.separator method
        :return: list[str]
        """
        pass

    @staticmethod
    def modified_content(content: list[str]) -> list:
        """
        The task of this method is to modify the initial content.

        :param content: Initial content created by self.extract_content method.
        :return: list
        """
        pass

    def validator(self, slide: list[str], slide_number: str) -> PysentationSlide:
        """
        The task of this method is to fully validate a slide and create an object from PysentationSlide if the slide is approved.

        :param slide: A text-base slide separated by the self.separator method
        :param slide_number: Slide number in integer type.
        :return: PysentationSlide
        """
        pass

    def build(self) -> PysentationScreen:
        """
        This is the main method. With the help of this method, the steps of creating an object from PysentationScreen
        are started and managed, until finally an object from PysentationScreen containing one or more objects from
        PysentationSlide is prepared and returned.

        :return: PysentationScreen[PysentationSlide...]
        """
        pass

    @staticmethod
    def check_source(source_path: str|Path) -> bool:
        """
        The task of this method is to validate the source path.

        :param source_path: The source path.
        :return: bool
        """
        pass

    def __repr__(self):
        pass
