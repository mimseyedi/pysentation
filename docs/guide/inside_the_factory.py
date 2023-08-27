#pysentation{

#>slide
#-title: Introduction of pysentation
#-interpretable:False

#:Hello! In this set of slides, we are going to have a presentation of how pysentation works.
#:In general, pysentation consists of the following three classes:
class Pysentation:
    ...

class PysentationSlide:
    ...

class PysentationScreen:
    ...
#:In the following, we will explain and review these three classes, which are the main core of pysentation.
#>slide
#-title: The general idea of pysentation
#-interpretable:False

#:In general, the task of [bold yellow]pysentation[/bold yellow] is to display a series of [italic]slides[/italic] on one [italic]screen[/italic]. A screen that [green]controls[/green] the slides.
#:But before creating a screen that holds and controls a set of slides, it is necessary to [blue]interpret[/blue] the source either in the form of a Python file [underline red](.py)[/underline red], or a [italic]converted[/italic] file with the [underline red](.pysent)[/underline red] suffix, and build the slides and the screen.
#:This task is the responsibility of an object of the [italic magenta]Pysentation[/italic magenta] class:
class Pysentation:

    def __init__(self, source: str|Path) -> None:
        ...

    def extract_props(slide: list[str], slide_number: str) -> dict:
        ...

    def extract_content(slide: list[str]) -> list[str]:
        ...

    def validator(self, slide: list[str], slide_number: str) -> PysentationSlide:
        ...

    def build(self) -> PysentationScreen:
        ...
#>slide
#-title: Interpretation of the pysentation file
#-interpretable:False

#:The main method of an object of the [italic magenta]Pysentation[italic magenta] class is the [red]build[/red] method.
#:After the [italic]pysentation file[/italic] is validated in the object initialization phase, the [red]build[/red] method will [blue]interpret[/blue] the file step by step.
#:The first step is to find the [bold yellow]pysentation scope[/bold yellow] and read it:
class Pysentation:

    def read_source(self) -> str:
        ...

    @staticmethod
    def detector(source: str) -> tuple[bool, str|PysentationError]:
        ...
#:If the [bold yellow]pysentation scope[/bold yellow] is not found or the [italic]range[/italic] is not measured, [red]ScopeDetectionError[/red] errors will be raised.

#>slide
#-title: The seperator method
#-interpretable:False

#:The next step is to [green]separate[/green] the slides in the [bold yellow]pysentation scope[/bold yellow]:
@staticmethod
def separator(source_code: str) -> list[str]:
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
#>slide
#-title: Extracting properties
#-interpretable:False

#:The next step is [underline green]extracting the properties[/underline green] of the slides. This is the task of the [bold red]extract_props[/bold red] method:
@staticmethod
def extract_props(slide: list[str], slide_number: str) -> dict:
    ...
    if prop == 'color':
        try:
            Style(color=value)
        except ColorParseError:
            raise PropertyError(
                (f"The '{value}' in slide {slide_number}, line {lineno} is not a valid color for '{prop}' property.\n"
                 "Acceptable colors: https://github.com/mimseyedi/pysentation#colors")
            )
    elif prop in ["interpretable", 'expand']:
        if value.strip() not in ['True', 'False']:
            raise PropertyError(
                f"The value of '{prop}' property in slide {slide_number}, line {lineno} must be in bool[True/False] type."
            )
        else:
            value = 'True' if value.strip() == 'True' else ''

    props[prop] = value.strip()
    ...
#>slide
#-title: Extracting contents
#-interpretable:False

#:After the properties, the [underline green]content[/underline green] should be extracted.
#:The content consists of [green]comments[/green] and [blue]codes[/blue].
@staticmethod
def extract_content(slide: list[str]) -> list[str]:

    content: list = []

    for index, line in enumerate(slide, start=1):
        if not line.strip().startswith(PYSENTATION_PROPERTY):
            if line.strip().startswith(PYSENTATION_COMMENT):
                try:
                    render(line.strip())
                except MarkupError:
                    raise CommentRenderingError(
                        f"Written comment cannot be rendered -> '{line.strip()[2:]}'"
                    )

            content.append(line)

    return content
#>slide
#-title: Make a slide
#-interpretable:False

#:After extracting the required data, the [bold red]validator[/bold red] method creates an object of the [italic magenta]PysentationSlide[/italic magenta] class and returns it if there is no problem in getting and reading the data from source.
def validator(self, slide: list[str], slide_number: str) -> PysentationSlide:
    props: dict = self.extract_props(
        slide=slide,
        slide_number=slide_number
    )
    content: list = self.modified_content(
        content=self.extract_content(
            slide=slide
        )
    )
    return PysentationSlide(
        content=content,
        slide_number=slide_number,
        **props
    )
#>slide
#-title: Build the screen
#-interpretable:False

#:The [bold red]build[/bold red] method, after receiving the slides that are [underline]validated[/underline], creates an object of the [italic magenta]PysentationScreen[/italic magenta] class and places the slides in it and [red]returns[/red] the prepared screen:
def build(self) -> PysentationScreen:
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
#>slide
#-title: About the screen
#-interpretable:False

#:The [red]screens[/red] consist of a set of [italic magenta]slides[/italic magenta] and have the ability to access the slides and [green]control[/green] them:
class PysentationScreen:
    def __init__(self, slides: list[PysentationSlide]) -> None: ...

    def display(self) -> None: ...

    def next_slide(self) -> None: ...

    def previous_slide(self) -> None: ...

    def highlight_top_line(self) -> None: ...

    def highlight_bottom_line(self) -> None: ...

    def first_slide(self) -> None: ...

    def last_slide(self) -> None: ...

    def start_from(self, slide_index: int) -> None: ...

    def search_by_index(self, index: str) -> None: ...

    def set_color(self, color: str) -> None: ...
#:For more: [underline blue]https://github.com/mimseyedi/pysentation/blob/master/pysentation/module.py#L275[/underline blue]

#>slide
#-title: An introduction about slides
#-interpretable:False

#:Slides have special [bold magenta]properties[/bold magenta]:
class PysentationSlide:
    def __init__(
            self,
            content: list[str|Syntax|Panel],
            slide_number: str,
            title: TextType | str = None,
            title_align: AlignMethod | str = 'center',
            color: StyleType = 'none',
            expand: bool = True,
            theme: str | SyntaxTheme = 'gruvbox-dark',
            interpretable: bool = True,
    ) -> None:
#:These features are all [italic blue]components[/italic blue] and [italic blue]settings[/italic blue] of slides that can be [underline]changed[/underline] and [underline]interpreted[/underline].

#>slide
#-title: Slide methods
#-interpretable:False

#:Each object of the [italic magenta]PysentationSlide[/italic magenta] class has the following [red]methods[/red] to control and perform tasks related to its presentation:
class PysentationSlide:
    def render(self) -> Panel:
        ...

    def go_up(self) -> None:
        ...

    def go_down(self) -> None:
        ...

    @staticmethod
    def interpret(source: str) -> tuple[bool, str]:
        ...

    def reset_slide(self) -> None:
        ...
#:For more: [underline blue]https://github.com/mimseyedi/pysentation/blob/master/pysentation/module.py#L47[/underline blue]

#>slide
#-title: The render method
#-interpretable:False
#:The main method of each slide is the [red]render[/red] method. This method is responsible for returning a [bold red]rich.panel[/bold red] that contains information and slide settings.
def render(self) -> rich.Panel:
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
#:Finally, the rendered slide as a [bold red]rich.panel[/bold red] can be displayed by the [magenta]print[/magenta] method of the [bold red]rich[/bold red] module.

#>slide
#-title: Last word
#-interpretable: False
"""
██████╗ ██╗   ██╗███████╗███████╗███╗   ██╗████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝ ███████╗█████╗  ██╔██╗ ██║   ██║   ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║        ██║   ███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""
#:Finally, with the help of [red]slide[/red] and [red]screen[/red] [underline]methods[/underline], these slides can be [magenta]rendered[/magenta] and displayed.
#:[bold yellow]pysentation[/bold yellow], like many other programs, stands on the shoulders of [italic blue]bigger giants[/italic blue], and in this project in particular, the [bold red]rich[/bold red] module provides the possibility to process and display information in an attractive and fast way at the terminal level.
#:[bold yellow]pysentation[bold yellow] is actually a special [underline]form[/underline] of how to use the features of the [bold red]rich[/bold red] module.
#:rich module Github repo: [underline blue]https://github.com/Textualize/rich[/underline blue]
#pysentation}