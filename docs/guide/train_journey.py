#pysentation{

#>slide
#-title: Welcome
#:[yellow]Hello![/yellow] [bold green]Welcome to our train journey.[/bold green]
#:Here we are going to talk about pysentation and...
#:[red]wait...[/red]
#:Did you notice here? Of course, maybe it's not [magenta]interesting[/magenta] at all, but anyway, this is what makes the module [bold red]rich[/bold red], not [italic blue]pysentation[/italic blue]. Maybe both, I don't know...
#:I only know that here we are going to experience something very [cyan]cool[/cyan] together!
#:To understand how cool it is to press your finger on the right [blink]→[/blink] key.

#>slide
#-title: Magic keys
#:Hello again! But this time in a new page or slide!
#:Now you understand more why we are traveling by train, don't you? Each of these slides actually look like train wagons. You can switch between them. You learned how to go forward, now you can go back to the previous slide with the left [blink]←[/blink] key.
#:[bold red]Tip: You can move between the next and previous slides with the right and left keys![/bold red]

#>slide
#-title: Ridiculous argument
#-interpretable:False
#:What program have you seen so far that uses the [bold]right[/bold] and [bold]left[/bold] keys but not the [bold]top[/bold] and [bold]down[/bold] keys? Well, honestly, this is a very ridiculous argument and it is better not to take it seriously.
#:It can be said that this was just a [underline]ridiculous introduction[/underline] to tell you that the [bold]up[/bold] and [bold]down[/bold] keys work here.
#:Look at the code below and try to use the [bold red]up[/bold red] and [bold red]down[/bold red] keys. Nothing is better than [italic blink yellow]experiencing![/italic blink yellow]
def ridiculous_argument(grade: int) -> str:
    if grade > 100:
        return 'The earth is flat!'

    return 'blah blahhhhhh blahhh blahh...'

print(ridiculous_argument(grade=120))
#:Yes, as you can see, the use of these keys is to [underline]move between[/underline] the lines of codes that are in the slide.
#:Let's go, [italic green]there is still a long way to go![/italic green]

#>slide
#-title: Wise person
#-interpretable:False
#:Well, this time, without any jokes, it is better to say that there are some other keys and explain them easily like a [italic green]wise person...[/italic green]
#:If you want to [bold red]reset the slide[/bold red] and return the code line indicator to the initial state, you can use the [blink red]r[/blink red] key.
#:If you want to [bold red]reset the entire screen[/bold red] so that this happens to all slides, you can use [blink red]shift + r[/blink red].
#:There are two other keys, the first one takes you to the [bold red]first slide[/bold red], which is the [blink red]f[/blink red] key. And the second one will take you to the [bold red]last slide[/bold red] where you have to use the [blink red]l[/blink red] key.
#:There is also a [bold red]dangerous[/bold red] or [bold green]saving[/bold green] key called [blink red]q[/blink red] that throws you out of the screen! It is better to be polite and say that it will take you out of the screen or program.
#:But before you want to use these last 3 keys, I want to teach you a [yellow]trick[/yellow] on how to get back to where you were.
#   pysentation [PYTHON_FILE] -f [SLIDE_NUMBER]
#:This option helps that if you exit the program or go to the first or last slide, by exiting the program and entering the number of the slide you were on, you can directly see the slide you want!
#:You can use the [bold yellow]shift+k[/bold yellow] key to see the [blue]information[/blue] of all the keys. [underline green]Why don't you try it now?[/underline green]

#>slide
#-title: Rules
#:Well, everything was fine, right?
#:By now, you may have asked yourself how I [blink yellow]made[/blink yellow] this? [underline]No?[/underline] [red]So what were you thinking until now? let's move on...[/red]
#:If you thought that I wrote the code one by one to display these, you thought [italic red]wrong![/italic red] But somehow you thought [blue]right[/blue]... ahhh...
#:Well, I wrote the code, yes! But I wrote once so that I don't have to write many times! This is a more [green]correct sentence.[/green]
#:Well, [bold yellow]pysentation[/bold yellow] is actually a tool that can easily be used to make these slides! You just need to create a python file with the [underline yellow](.py)[/underline yellow] suffix and follow some very simple [green]rules[/green] in order to convert it into a pysentation file, then you give the python file to the pysentation interpreter to show you these beautiful and attractive slides.
#:[italic]But let's see what these [bold]rules[/bold] are![/italic]

#>slide
#-title: Scope
#:The first thing that [yellow]pysentation[/yellow] interpreter needs to be able to interpret your slides is to specify the [blink red]scope[/blink red] or [italic red]range[/italic red] of interpretation.
#:[bold green]#pysentation{[/bold green]
#:    ...
#:[bold green]#pysentation}[/bold green]
#:In fact, all your slides and the settings you want to apply are defined between these two [bold yellow]Python comments![/bold yellow]
#:I should also add that all the [bold yellow]settings[/bold yellow] and [bold yellow]elements[/bold yellow] inside the slides, except for the [bold red]codes[/bold red], are actually a [bold yellow]Python comment[/bold yellow]. Comments that have [blink green]special signs![/blink green] It's smart, isn't it?

#>slide
#-title: Slides
#:The next step is to make the [bold yellow]slide![/bold yellow]
#:To make a slide, just use this command: [bold red]#>slide[/bold red]
#:The slides don't need to be [blue]closed[/blue] and it is enough to specify their [bold yellow]starting point.[/bold yellow]
#:[bold green]#pysentation{[/bold green]
#:    [yellow]#>slide[/yellow]
#:        ...
#:[bold green]#pysentation}[/bold green]

#>slide
#-title: Properties/Title
#:Well, we have reached one of the most [red]important[/red] parts!
#:Each slide consists of several [bold yellow]properties.[/bold yellow] Features that can [green]affect[/green] the shape and function of the slide.
#:These properties start with the sign [bold yellow]#-[/bold yellow] and after this sign, their names come with a colon [bold yellow](:)[/bold yellow], which specifies their [blue]value.[/blue]
#:Let's see example of the property named title:
#:[bold yellow]#-title:[/bold yellow] [green]Properties/Title[/green]
#:This property specifies the [red]title[/red] of the slide. I also used this feature to name the title of the same slide that you are in now! [yellow]interesting[/yellow], does not it?

#>slide
#-title: Position
#-title_align: left
#:The next property is title_align!
#:With the help of this property, you can adjust the [bold blue]position[/bold blue] of the slide title in [underline]three[/underline] modes: [bold yellow]right[/bold yellow], [bold yellow]middle[/bold yellow] and [bold yellow]left[/bold yellow]!
#:By default, this property is set to [bold yellow]center[/bold yellow].
#:[bold yellow]#-title_align:[/bold yellow] [green]left[/green]
#:[italic red]Did you pay attention to the title of this slide?[/italic red]

#>slide
#-title: Coloring
#-color: yellow
#:Well, we have reached [blink red]color![/blink red]
#:This property can change the color of the slide and its [underline]elements![/underline] To refer to a specific [red]color[/red], if your [bold blue]terminal[/bold blue] supports that color, you can refer to its [bold green]name[/bold green], [bold green]code[/bold green], [bold green]Hex code[/bold green] and [bold red]r[/bold red][bold green]g[/bold green][bold blue]b[/bold blue] code of that color:
#:[bold]#-color:[/bold] [green]rgb(175,0,95)[/green]
#:These 16 main colors can be used:
#:┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#:┃Color   ┃Number┃Name          ┃
#:┃[on black]        [/on black]┃0     ┃black         ┃
#:┃[on red]        [/on red]┃1     ┃red           ┃
#:┃[on green]        [/on green]┃2     ┃green         ┃
#:┃[on yellow]        [/on yellow]┃3     ┃yellow        ┃
#:┃[on blue]        [/on blue]┃4     ┃blue          ┃
#:┃[on magenta]        [/on magenta]┃5     ┃magenta       ┃
#:┃[on cyan]        [/on cyan]┃6     ┃cyan          ┃
#:┃[on white]        [/on white]┃7     ┃white         ┃
#:┃[on bright_black]        [/on bright_black]┃8     ┃bright_black  ┃
#:┃[on bright_red]        [/on bright_red]┃9     ┃bright_red    ┃
#:┃[on bright_green]        [/on bright_green]┃10    ┃bright_green  ┃
#:┃[on bright_yellow]        [/on bright_yellow]┃11    ┃bright_yellow ┃
#:┃[on bright_blue]        [/on bright_blue]┃12    ┃bright_blue   ┃
#:┃[on bright_magenta]        [/on bright_magenta]┃13    ┃bright_magenta┃
#:┃[on bright_cyan]        [/on bright_cyan]┃14    ┃bright_cyan   ┃
#:┃[on bright_white]        [/on bright_white]┃15    ┃bright_white  ┃
#:┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#:To see more colors, be sure to see here: [underline blue]https://github.com/mimseyedi/pysentation#colors[/underline blue]

#>slide
#-title: Themes
#-theme: monokai
#-interpretable: False
#:Now it's the turn of the theme!
#:With the help of this property, you can change the theme of the highlighter codes in the slide:
#:[bold yellow]#-theme: monokai[/bold yellow]
class PysentationSlide:
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
#:This property helps to set your theme codes with your [italic]terminal.[/italic]
#:Default value of this property: [red]gruvbox-dark[/red]
#:To see the names of the themes, see here: [underline blue]https://github.com/mimseyedi/pysentation#themes[/underline blue]

#>slide
#-title: Expand
#-expand: False
#:Wait... Why is this here?
#:It is because of the [bold red]expand[/bold red] feature!
#:This property allows you to [blink yellow]adjust[/blink yellow]
#:the [italic blue]width[/italic blue] of the slide with the screen
#:or with the elements [underline red]inside[/underline red] it.
#:This property only accepts boolean value, [green on white]True[/green on white] or [green on white]False[/green on white],
#:and its default state is [red]True[/red].
#:[bold yellow]#-expand: False[/bold yellow]

#>slide
#-title: Interpretable
#-interpretable: False
#:There are times when you don't want to display the code output or codes inside the slide.
#:This is where you should use the [bold yellow]interpretable[/bold yellow] property.
#:[bold yellow]#-interpretable:[/bold yellow] [green]False[/green]
def say_hello(name: str) -> None:
    print(f"Hello {name}.")

say_hello("pysentation")
#:[italic bold]Code number 2:[/italic bold]
import sys

print(
    list(
        map(lambda a: int(a) / 2, sys.argv[1:])
    )
)
#:This property, like [red]expand[/red], only accepts two values, [green on white]True[/green on white] or [green on white]False[/green on white], and by default, its value is equal to [red]True[/red], which causes all the codes in the slide to be interpreted and their [underline]output displayed.[/underline]

#>slide
#-title: Comments
#-interpretable:False
#:The [bold yellow]comments[/bold yellow] are actually all the [underline]texts[/underline] you saw in these slides. Like what you are reading now.
#:Comments have a special [yellow]sign[/yellow] and start with [green on white]#:[/green on white]. After that, you can write whatever you want and it will be displayed:
#:[green]#:Hello there![/green]
#:And also you can style it:
# [bold yellow]I love pysentation![/bold yellow]
#:Output: [bold yellow]I love pysentation![/bold yellow]

#>slide
#-title: Codes
#:Codes are the only elements that do not require any signs! You can write them easily:
print("Hello world!")
#:You can put several of them in one slide, but there must be one or more comments/lines between them:
for i in range(2):
    print(i)
#:Ohum...
print(1_000_000_000)
#:Note: Each piece of code is interpreted separately!

#>slide
#-title: Lines
#:[bold green]Lines[/bold green] are the simplest [underline]elements[/underline] of slides. The task of these line elements is to [italic blue]draw[/italic blue] a [underline]horizontal[/underline] line to [bold]separate[/bold] the screen, and its sign is [bold yellow]#_line[/bold yellow].
#_line
print(
    ', '.join(
        list(
            map(
                lambda name: f'Hello {name}',
                ['Mahsa', 'Nika', 'Khodanoor', 'Sarina', 'Kian']
            )
        )
    )
)
#_line
for number in range(10_000_000):
    if number > 3:
        break

    print(number)

#>slide
#-title: Errors
#:If a code has an [bold red]error[/bold red], it will be displayed as follows:
def div(a, b):
    return a / b

print(div(4, 0))
#:[italic][yellow]Recommendation:[/yellow] Do not use functions like [blue]input[/blue] in the slides. This disrupts the slide show operation.[/italic]
#pysentation}
