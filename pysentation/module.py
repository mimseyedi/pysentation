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
import pickle
import traceback
from pathlib import Path
from getkey import getkey
from rich.box import HEAVY
from rich.rule import Rule
from rich.table import Table
from rich.panel import Panel
from rich import print as cprint
from rich.console import Group, Align
from rich.color import ColorParseError
from rich.style import StyleType, Style
from rich.markup import render, MarkupError
from rich.syntax import Syntax, SyntaxTheme
from rich.text import TextType, AlignMethod
from .signs import (
    PYSENTATION_STARTING_BLOCK,
    PYSENTATION_ENDING_BLOCK,
    PYSENTATION_SLIDE,
    PYSENTATION_PROPERTY,
    PYSENTATION_COMMENT,
    PYSENTATION_LINE,
)
from .errors import (
    InterpretationError,
    ScreenError,
    ScopeDetectionError,
    PropertyError,
    CommentRenderingError,
    NotAPysentationFileError,
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
        theme (str|SyntaxTheme): The theme highlights Python codes and its default value is 'gruvbox-dark'.
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
        theme: str|SyntaxTheme = 'gruvbox-dark',
        interpretable: bool = True,
    ) -> None:
        self.content = content
        self.slide_number = slide_number
        self.title = title
        self.title_align = title_align
        self.color = color
        self.expand = expand
        self.theme = theme
        self.interpretable = interpretable
        self.__h_line: int = 1
        self.__code_index: int = 0


        for index, element in enumerate(self.content):
            if isinstance(element, Syntax):
                if self.interpretable:
                    status, response = self.interpret(source=element.code)

                    output_panel = Panel(
                        response.strip(),
                        style='none' if status else 'red',
                        title='Output' if status else '<Error>',
                        title_align='left'
                    )

                    self.content.insert(index + 1, "")
                    self.content.insert(index + 2, output_panel)

                element._theme = element.get_theme(self.theme)

        self.__codes: list = [
            element for element in self.content if isinstance(element, Syntax)
        ]

    def render(self) -> Panel:
        """
        The task of this method is to render the PysentationSlide and turn it into a panel of the rich module.
        By turning PysentationSlide into a panel, it is possible for the slide to be displayed correctly by a PysentationScreen object.

        :return: rich.Panel
        """

        return Panel(
            Group(
                *self.content
            ),
            box=HEAVY,
            title=self.title,
            style=self.color,
            title_align=self.title_align,
            subtitle=self.slide_number,
            expand=self.expand,
            highlight=False,
            padding=(1, 1, 1, 1),
        )

    def go_up(self) -> None:
        """
        With the help of this method, you can move between the lines of Python codes in the slide,
        and the task of this method is to go up among the Python codes in the slide.

        :return: None
        """

        if self.__codes:
            if self.__h_line > 1:
                self.__h_line -= 1
            else:
                if self.__code_index - 1 == -1:
                    self.__codes[self.__code_index].highlight_lines = {}
                    self.__code_index = len(self.__codes) - 1
                    self.__h_line = len(self.__codes[self.__code_index].code.split("\n"))
                else:
                    self.__codes[self.__code_index].highlight_lines = {}
                    self.__code_index -= 1
                    self.__h_line = len(self.__codes[self.__code_index].code.split("\n"))

            self.__codes[self.__code_index].highlight_lines = {self.__h_line}

    def go_down(self) -> None:
        """
        With the help of this method, you can move between the lines of Python codes in the slide,
        and the task of this method is to go down among the Python codes in the slide.

        :return: None
        """

        if self.__codes:
            if self.__h_line < len(self.__codes[self.__code_index].code.split("\n")):
                self.__h_line += 1
            else:
                if self.__code_index + 1 < len(self.__codes):
                    self.__codes[self.__code_index].highlight_lines = {}
                    self.__code_index += 1
                    self.__h_line = 1
                else:
                    self.__codes[self.__code_index].highlight_lines = {}
                    self.__code_index = 0
                    self.__h_line = 1

            self.__codes[self.__code_index].highlight_lines = {self.__h_line}

    @staticmethod
    def interpret(source: str) -> tuple[bool, str]:
        """
        The task of this method is to interpret the pieces of codes inside the slide and return
        the output of the interpreted code.

        :param source: The source code to be interpreted as a string.
        :return: tuple[bool, str]
        """

        output, output_file = None, Path(Path(__file__).parent, ".output.txt")
        c_stdout: sys.stdout = sys.stdout
        sys.stdout = open(file=output_file, mode='w+')

        try:
            exec(source)
            sys.stdout.close()
            sys.stdout = c_stdout

            with open(
                    file=output_file, mode='r'
            ) as output_file:
                output = output_file.read()

        except (OverflowError, SyntaxError, TabError, IndentationError) as error:
            sys.stdout.close()
            sys.stdout = c_stdout

            output = (f"Error Type: {error.__class__.__name__}\n"
                      f"Error Message: {error.msg} in line {error.lineno}\n"
                      f"{error.text.strip()}\n"
                      f"{'^' * len(error.text.strip())}")

        except BaseException:
            sys.stdout.close()
            sys.stdout = c_stdout

            ex_type, ex_value, ex_traceback = sys.exc_info()

            trace_back = traceback.extract_tb(ex_traceback)

            output = (f"Exception Type: {ex_type.__name__}\n"
                      f"Exception Message: {ex_value if ex_value.__str__() else 'None'}\n"
                      f"Scope {trace_back[1].name}, Line {trace_back[1].lineno}")
        finally:
            if output:
                if output.startswith("Exception") or output.startswith("Error"):
                    return False, output
                return True, output
            return True, 'None'

    def reset_slide(self) -> None:
        """
        The task of this method is to reset the slide and modify the variables related to the display to the initial value.
        Specifically self.__h_line and self.__code_index.

        :return: None
        """

        self.__h_line = 1
        self.__code_index = 0
        self.go_up()
        self.go_down()

    def __add__(self, other):
        return PysentationSlide(
            content=[*self.content, *other.content],
            slide_number=self.slide_number,
            title=self.title,
            title_align=self.title_align,
            color=self.color,
            expand=self.expand,
            theme=self.theme,
            interpretable=self.interpretable,
        )

    def __eq__(self, other):
        return True if self.content == other.content else False

    def __repr__(self):
        return (f"PysentationSlide("
                f"content={self.content}, "
                f"slide_number={self.slide_number}, "
                f"title={self.title}, "
                f"title_align={self.title_align}, "
                f"color={self.color}, "
                f"expand={self.expand}, "
                f"theme={self.theme}, "
                f"interpretable={self.interpretable}, "
                f"__codes={self.__codes}, "
                f"__code_index={self.__code_index}, "
                f"__h_line={self.__h_line})")

    def __str__(self):
        return f"PysentationSlide titled '{self.title}', with this content={self.content}"


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
        self.slides = slides
        self.__slideno: int = 0

    def display(self) -> None:
        """
        This method displays the PysentationSlide selected by self.__slideno.

        :return: None
        """

        os.system('clear' if os.name == 'posix' else 'cls')
        cprint(self.slides[self.__slideno].render())

    def next_slide(self) -> None:
        """
        With the help of this method, you can move between PysentationSlide.
        The task of this method is to display the next PysentationSlide in the list.
        If there is no PysentationSlide, it does nothing.

        :return: None
        """

        if self.__slideno < len(self.slides) - 1:
            self.__slideno += 1
            self.display()

    def previous_slide(self) -> None:
        """
        With the help of this method, you can move between PysentationSlide.
        The task of this method is to display the previous PysentationSlide in the list.
        If there is no PysentationSlide, it does nothing.

        :return: None
        """

        if self.__slideno > 0:
            self.__slideno -= 1
            self.display()

    def highlight_top_line(self) -> None:
        """
        The task of this method is to highlight the upper line of the syntax highlighter of the current slide.

        :return: None
        """

        self.slides[self.__slideno].go_up()
        self.display()

    def highlight_bottom_line(self) -> None:
        """
        The task of this method is to highlight the bottom line of the syntax highlighter of the current slide.

        :return: None
        """

        self.slides[self.__slideno].go_down()
        self.display()

    def first_slide(self) -> None:
        """
        The task of this method is to display the first slide on the screen.

        :return: None
        """

        self.__slideno = 0
        self.display()

    def last_slide(self) -> None:
        """
        The task of this method is to display the last slide on the screen.

        :return: None
        """

        self.__slideno = len(self.slides) - 1
        self.display()

    def start_from(self, slide_index: int) -> None:
        """
        The task of this method is to display the screen from the slide that the argument tells it.

        :param slide_index: The slide index in the screen.
        :return: None
        """

        if 0 <= slide_index < len(self.slides):
            self.__slideno = slide_index
            self.display()
        else:
            raise ScreenError(
                f"There is no slide with this number -> {slide_index + 1}"
            )

    def search_by_index(self, index: str) -> None:
        """
        The task of this method is to search the slide with the slide number and display it.

        :param index: The slide index or number in string (input) format.
        :return: None
        """

        if index.isdigit():
            _index = int(index)

            if 0 < _index <= len(self.slides):
                self.start_from(slide_index=_index - 1)
            else:
                self.display()
                cprint(
                    f"[bold red]Error:[/bold red] There is no slide with this number -> {_index}!"
                )
        else:
            self.display()
            cprint(
                "[bold red]Error:[/bold red] The slide number must be a positive integer."
            )

    def search_by_title(self, title: str) -> None:
        """
        The task of this method is to search the slide with the slide title and display it.

        :param title: The title of a slide.
        :return: None
        """

        titles: dict = {
            slide.title.strip().lower(): int(slide.slide_number.split("/")[0])
            for slide in self.slides
        }

        max_intersect, max_sentence = 0, ''

        for t in titles.keys():
            temp = set(t.split())
            x = len(
                temp.intersection(
                    set(title.lower().split())
                )
            )
            if x > max_intersect:
                max_intersect, max_sentence = x, t

        slide_number = titles.get(max_sentence)

        if slide_number is None:
            self.display()
            cprint(
                f"[bold red]Error:[/bold red] No slides with this title were found -> '{title}'"
            )
        else:
            self.start_from(slide_index=slide_number - 1)

    def set_color(self, color: str) -> None:
        """
        The task of this method is to change the color of all the slides on the screen by the argument it receives.

        :param color: The color name|number|hex|rgb in string format.
        :return: None
        """

        try:
            Style(color=color)
        except ColorParseError:
            raise ScreenError(
                (f"The '{color}' is not a valid color.\n"
                  "Acceptable colors: https://github.com/mimseyedi/pysentation#colors")
            )
        else:
            for slide in self.slides:
                slide.color = color

    def set_theme(self, theme: str) -> None:
        """
        The task of this method is to change the syntax highlighter theme of all the slides on the screen by the argument it receives.

        :param theme: Theme name in string format.
        :return: None
        """

        for slide in self.slides:
            slide.theme = theme
            for element in slide.content:
                if isinstance(element, Syntax):
                    element._theme = element.get_theme(theme)

    def disable_output(self) -> None:
        """
        The task of this method is to disable the code interpretation in all slides.

        :return: None
        """

        for slide in self.slides:
            slide.interpretable = False
            for index, element in enumerate(slide.content):
                if isinstance(element, Panel):
                    slide.content.pop(index)

    def get_property(self, slide_index: int) -> str:
        """
        The task of this method is to return the properties of the slide that the argument tells it.

        :param slide_index: The slide index in the screen.
        :return: str
        """

        if 0 <= slide_index < len(self.slides):
            slide: PysentationSlide = self.slides[slide_index]
            return (f"Title\t\t>>> {slide.title}\n"
                    f"Title align\t>>> {slide.title_align}\n"
                    f"Number\t\t>>> {slide.slide_number}\n"
                    f"Color\t\t>>> {slide.color}\n"
                    f"Theme\t\t>>> {slide.theme}\n"
                    f"Interpretable\t>>> {slide.interpretable}")
        else:
            raise ScreenError(
                f"There is no slide with this number -> {slide_index + 1}"
            )

    def get_slides(self) -> str:
        """
        The task of this method is to return the title of the slides along with their position.

        :return: str
        """

        return '\n'.join(
            [
                f"{index}/{len(self.slides)} {slide.title}"
                for index, slide in enumerate(self.slides, start=1)
            ],
        )

    def write_output(self, output_path: str|Path) -> None:
        """
        The task of this method is to write the output in the text file given the path by the argument.

        :param output_path: The path of output file in string or pathlib.Path format.
        :return: None
        """

        output_path: Path = output_path if isinstance(output_path, Path) else Path(os.getcwd(), output_path)

        if not output_path.exists():
            if not output_path.is_dir() and output_path.suffix == '.txt':
                with open(output_path, 'w+') as output_file:
                    for slide in self.slides:
                        cprint(slide.render(), file=output_file)
            else:
                raise ScreenError(
                    "The output file must not be a directory and must have a .txt suffix."
                )
        else:
            raise ScreenError(
                f"A file with this name already exists -> '{output_path}'"
            )

    def reset_slide(self) -> None:
        """
        The task of this method is to reset the current PysentationSlide.
        so that its values return to the initial state.

        :return: None
        """

        self.slides[self.__slideno].reset_slide()
        self.display()

    def reset_screen(self) -> None:
        """
        The task of this method is to reset the PysentationScreen.
        so that its values return to the initial state.
        Specifically reset self.__slideno.

        :return: None
        """

        self.__slideno = 0

        for slide in self.slides:
            slide.reset_slide()

        self.display()

    def display_hot_keys(self) -> None:
        """
        A guide slide to display the hot keys help table on the screen.

        :return: None
        """

        keys_table: Table = Table(
            'KEYS', 'ACTION',
            box=HEAVY,
            caption="Press the 'q' to exit.\n[underline]https://github.com/mimseyedi/pysentation[/underline]",
            caption_justify='left',
        )

        for key, info in {
            "Right →": "Next slide.",
            "Left ←": "Previous slide.",
            "Up ↑": "Highlight top line.",
            "Down ↓": "Highlight bottom line.",
            "f": "Go to first slide.",
            "l": "Go to last slide.",
            "r": "Reset the current slide.",
            "shift+r": "Reset the screen.",
            "j": "Jump to a slide by slide number.",
            "shift+s": "Search by slide title.",
            "shift+k": "Display The hot-keys guide.",
            "q": "Quit."
        }.items():
            keys_table.add_row(key, info)

        os.system('clear' if os.name == 'posix' else 'cls')

        _, row = os.get_terminal_size()
        new_line: int = (row - 19) // 2
        cprint('\n' * new_line, Align(keys_table, align='center'))

        try:
            while True:
                input_key = getkey()

                if input_key == 'q':
                    self.display()
                    break

        except KeyboardInterrupt:
            self.display()


    def __eq__(self, other):
        return True if self.slides == other.slides else False

    def __repr__(self):
        return (f"PysentationScreen("
                f"slides={self.slides}, "
                f"__slideno={self.__slideno})")

    def __str__(self):
        return f"PysentationScreen with these PysentationSlides={self.slides}"


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
        self.source = self.check_source(source_path=source)

    def read_source(self) -> str:
        """
        The task of this method is to read and validate the source to continue the process of
        converting the source to PysentationScreen.

        :return: str
        """

        if self.source.suffix == '.py':
            with open(file=self.source, mode='r') as source_file:
                source: str = source_file.read()
        else:
            with open(file=self.source, mode='rb') as source_file:
                source: str = pickle.load(source_file)

        status, response = self.detector(source=source)

        if not status:
            raise response

        return response

    @staticmethod
    def detector(source: str) -> tuple[bool, str|ScopeDetectionError]:
        """
        The task of this method is to find the scope and range of pysentation.

        :param source: The source path.
        :return: tuple[bool, str|PysentationError]
        """

        block, start_line, end_line = False, None, None

        for index, code in enumerate(source.split("\n")):
            if code.strip().startswith(PYSENTATION_STARTING_BLOCK):
                block = True
                start_line = index + 1

            if code.strip().startswith(PYSENTATION_ENDING_BLOCK) and block:
                end_line = index
                return True, '\n'.join(source.split("\n")[start_line: end_line])

        if start_line:
            return (
                False,
                ScopeDetectionError(
                    f"The pysentation scope is started on line '{start_line}' but never closed."
                )
            )
        return False, ScopeDetectionError("No scope of pysentation found.")

    @staticmethod
    def separator(source_code: str) -> list[str]:
        """
        The task of this method is to separate the slides in the source.

        :param source_code: The source contents.
        :return: list[str]
        """

        _source_code: list = list(
            map(
                lambda x: x + "\n",
                source_code.split("\n")
            )
        )

        slides, starting_zone, first = [], 0, True

        for index, line in enumerate(_source_code):
            if line.strip().startswith(PYSENTATION_SLIDE):
                if first:
                    first = False
                else:
                    slides.append(
                        ''.join(_source_code[starting_zone:index])
                    )
                starting_zone = index

        slides.append(''.join(_source_code[starting_zone:]))

        return slides

    @staticmethod
    def extract_props(slide: list[str], slide_number: str) -> dict:
        """
        The task of this method is to extract and validate the properties of a slide.

        :param slide: A text-base slide separated by the self.separator method
        :param slide_number: The number of slide in string [./.].
        :return: dict
        """

        props_items: list = [
            'title',
            'title_align',
            'color',
            'expand',
            'theme',
            'interpretable',
        ]

        props: dict = {}

        for lineno, line in enumerate(slide, start=1):
            if line.strip().startswith(PYSENTATION_PROPERTY):
                try:
                    prop, value = line.strip()[2:].split(":")[0], line.strip()[2:].split(":")[1]

                    if prop in props_items:
                        if value:
                            if prop == 'title':
                                try:
                                    render(value)
                                except MarkupError:
                                    raise CommentRenderingError(
                                        f"The title value '{value.strip()}' in slide {slide_number}, line {lineno} cannot be rendered!"
                                    )
                            elif prop == 'color':
                                try:
                                    render(value)
                                    Style(color=value)
                                except ColorParseError:
                                    raise PropertyError(
                                        (f"The '{value}' in slide {slide_number}, line {lineno} is not a valid color for '{prop}' property.\n"
                                         "Acceptable colors: https://github.com/mimseyedi/pysentation#colors")
                                    )
                                except MarkupError:
                                    raise PropertyError(
                                        f"The color value in slide {slide_number}, line {lineno} cannot be rendered!"
                                    )
                            elif prop in ["interpretable", 'expand']:
                                if value.strip() not in ['True', 'False']:
                                    raise PropertyError(
                                        f"The value of '{prop}' property in slide {slide_number}, line {lineno} must be in bool[True/False] type."
                                    )
                                else:
                                    value = True if value.strip() == 'True' else False

                            props[prop] = value.strip() if isinstance(value, str) else value

                        else:
                            raise PropertyError(
                                f"invalid/Empty value for '{prop}' property in slide {slide_number}, line {lineno}.",
                            )
                    else:
                        raise PropertyError(
                            f"There is no such property in slide {slide_number}, line {lineno} -> '{prop}'"
                        )

                except IndexError:
                    raise PropertyError(
                        f"Undefined property or invalid value in slide {slide_number}, line {lineno}."
                    )

        return props

    @staticmethod
    def extract_content(slide: list[str], slide_number: str) -> list[str]:
        """
        The task of this method is to extract and validate the content of a slide.

        :param slide: A text-base slide separated by the self.separator method
        :param slide_number: The number of slide in string [./.].
        :return: list[str]
        """

        content: list = []

        for index, line in enumerate(slide, start=1):
            if not line.strip().startswith(PYSENTATION_PROPERTY):
                if line.strip().startswith(PYSENTATION_COMMENT):
                    try:
                        render(line.strip()[2:])
                    except MarkupError as error:
                        raise CommentRenderingError(
                            error.__str__() + f" in slide {slide_number}, line {index}."
                        )

                content.append(line)

        if content:
            content.pop(0)

        return content

    @staticmethod
    def modified_content(content: list[str]) -> list:
        """
        The task of this method is to modify the initial content.

        :param content: Initial content created by self.extract_content method.
        :return: list
        """

        modified_content, codes, first_sh = [], '', True

        for index, line in enumerate(content):
            if line is None:
                modified_content.append("")
                continue

            if not line.strip().startswith((PYSENTATION_COMMENT, PYSENTATION_LINE,)):
                codes += line.rstrip() + "\n"
            else:
                if codes.strip():
                    if modified_content:
                        modified_content.append("")

                    modified_content.append(
                        Syntax(
                            code=codes.rstrip(),
                            lexer='python',
                            line_numbers=True,
                            start_line=1,
                            indent_guides=True,
                            background_color='default',
                            highlight_lines={1 if first_sh else None}
                        )
                    )
                    first_sh = False
                    modified_content.append("")

                    if line.strip() == PYSENTATION_LINE:
                        modified_content.append(
                            Rule(style='bold')
                        )
                    else:
                        modified_content.append(line.strip()[2:])
                else:
                    if modified_content:
                        modified_content.append("")

                    if line.strip() == PYSENTATION_LINE:
                        modified_content.append(
                            Rule(style='bold')
                        )
                    else:
                        modified_content.append(line.strip()[2:])


                codes: str = ''

        if codes.strip():
            if modified_content:
                modified_content.append("")

            modified_content.append(
                Syntax(
                    code=codes.rstrip(),
                    lexer='python',
                    line_numbers=True,
                    start_line=1,
                    indent_guides=True,
                    background_color='default',
                    highlight_lines={1 if first_sh else None}
                )
            )

        return modified_content

    def validator(self, slide: list[str], slide_number: str) -> PysentationSlide:
        """
        The task of this method is to fully validate a slide and create an object from PysentationSlide if the slide is approved.

        :param slide: A text-base slide separated by the self.separator method
        :param slide_number: Slide number in integer type.
        :return: PysentationSlide
        """

        props: dict = self.extract_props(
            slide=slide,
            slide_number=slide_number
        )
        content: list = self.modified_content(
            content=self.extract_content(
                slide=slide,
                slide_number=slide_number
            )
        )
        return PysentationSlide(
            content=content,
            slide_number=slide_number,
            **props
        )

    def build(self) -> PysentationScreen:
        """
        This is the main method. With the help of this method, the steps of creating an object from PysentationScreen
        are started and managed, until finally an object from PysentationScreen containing one or more objects from
        PysentationSlide is prepared and returned.

        :return: PysentationScreen[PysentationSlide...]
        """

        source: str = self.read_source()

        seperated_source: list = self.separator(
            source_code=source
        )

        slides: list = []
        for number, scope in enumerate(seperated_source):
            slide: PysentationSlide = self.validator(
                slide=scope.split("\n"),
                slide_number=f"{number+1}/{len(seperated_source)}"
            )
            slides.append(slide)

        if slides:
            screen: PysentationScreen = PysentationScreen(
                slides=slides
            )
            return screen

        raise ScreenError(
            "There are no slides to display on the screen."
        )

    @staticmethod
    def check_source(source_path: str|Path) -> Path:
        """
        The task of this method is to validate the source path and return validated path.

        :param source_path: The source path.
        :return: Path
        """

        _source_path: Path = source_path if isinstance(source_path, Path) \
            else Path(os.getcwd(), source_path)

        for condition, exception in {
            _source_path.suffix in ['.py', '.pysent']: NotAPysentationFileError(
                'The source must be a Python or pysentation file with (.py|.pysent) suffix.'
            ),
            _source_path.is_file(): IsADirectoryError(
                'The source must be a file, not a directory.'
            ),
            _source_path.exists(): FileNotFoundError(
                f'This file does not exist! -> {_source_path.name}'
            ),
        }.items():
            if not condition:
                raise exception

        return _source_path

    def __repr__(self):
        return f"Pysentation(source='{self.source}')"
