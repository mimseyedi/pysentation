[![pypi](https://img.shields.io/pypi/v/pysentation.svg)](https://pypi.org/project/pysentation/) [![support-version](https://img.shields.io/pypi/pyversions/pysentation)](https://img.shields.io/pypi/pyversions/pysentation) [![license](https://img.shields.io/github/license/mimseyedi/pysentation.svg)](https://github.com/mimseyedi/pysentation/blob/master/LICENSE) [![commit](https://img.shields.io/github/last-commit/mimseyedi/pysentation)](https://github.com/mimseyedi/pysentation/commits/master)

## Table of Contents: <a class="anchor" id="contents"></a>
* [Introduction](#intro) 
* [Installation](#install)
* [How to use pysentation?](#usage)
  * [pysentation file](#pysentation_file)
    * [pysentation scope](#scope)
    * [Slides](#slides)
    * [Properties](#props)
      * [Title](#title)
      * [Title align](#title_align)
      * [Color](#color)
      * [Theme](#theme)
      * [Expand](#expand)
      * [Interpretable](#interpretable)
    * [Comments](#comments)
    * [Codes](#codes)
  * [Slideshow screen](#slideshow)
    * [Hot keys](#hot_keys)
  * [Options](#options)
* [Colors and themes](#colors_and_themes)
  * [Colors](#colors)
  * [Theme](#theme)
* [Bugs/Requests](#bugs_requests)
* [License](#license)

## Introduction <a class="anchor" id="intro"></a>

pysentation is a CLI tool for displaying Python presentations.

pysentation, by taking a Python file written with simple but specific rules, can convert the contents of the Python file into a slide show and display it.

Follow the documentation or read <a href="#">this</a> section for more information.

## Installation <a class="anchor" id="install"></a>
You can use **pip** to install:
```
python3 -m pip install pysentation
```

And also to **upgrade**:
```
python3 -m pip install --upgrade pysentation
```

<br/>

If there is a **problem**, install the **requirement packages** separately as below and then try again.

First, download the `requirements.txt` file with **curl**:
```
curl -o requirements.txt https://raw.githubusercontent.com/mimseyedi/pysentation/master/requirements.txt
```

Then install the packages in the `requirements.txt` using **pip**:
```
python3 -m pip install -r requirements.txt
```

<br/>

You can still do it yourself without needing the `requirements.txt` file:
```
python3 -m pip install rich==13.4.1 getkey==0.6.5 click==8.1.3
```

## How to use pysentation? <a class="anchor" id="usage"></a>
There are two ways to use pysentation!

The first way is the **classic** way of reading the **document**. You may be surprised, but many people live with documents and love to read them. That's why this possibility is completely available for people who belong to this category, and if you like documents, it's better to continue right now.

But there is a **second way**! What could be better than **understanding** how to work with a program **while** you are **inside** it and **using** it? I like documents, but **believe** me, this method is much more **interesting**! Let **pysentation** introduce **itself** to you.

There are two very **simple** steps for this.

First of all, **download** this python file with the help of **curl**:
```
curl -o requirements.txt https://raw.githubusercontent.com/mimseyedi/pysentation/master/docs/guide/train_journey.py
```

Then after you install **pysentation**, run the file you downloaded with the **pysentation** command:
```
pysentation train_journey.py
```

Enjoy it!

## pysentation file <a class="anchor" id="pysentation_file"></a>
To use **pysentation**, you first need a **pysentation file**. The pysentation file is actually a **Python file**. But it follows **rules** that can be converted into a **slideshow** and interpreted by **pysentation CLI**.

## pysentation scope <a class="anchor" id="scope"></a>
A **pysentation** file consists of a **pysentation** scope. Specifying the scope of the pysentation is mandatory so that the **interpretation** can be done correctly:
```python
#pysentation{
...
#pysentation}
```

This **range** specifies the **presentation environment**. All pysentation **commands** and attributes in a **python file** are a python **comment**, but they have **special names** so that they can be **interpreted** correctly.

## Slides <a class="anchor" id="slides"></a>
Each **pysentation** consists of one or more **slides**. To make a **slide**, just do the following:
```python
#pysentation{

#>slide
...

#pysentation}
```
Now, after `#>slide`, you can **define** slide **properties** and slide **elements**, which we will explain below.

You can also define **several** slides in **one scope**:
```python
#pysentation{

#>slide
...

#>slide
...

#>slide
...

#pysentation}
```

## Properties <a class="anchor" id="props"></a>
Each slide has properties that can change the presentation of the slide. These properties are listed in the table below, which I will examine one by one in the following:

|Property| Action                                                                                                                                     | Definition form        |Default value|
|---|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------|---|
|Title| You can change the title of the slide with this property.                                                                                  | #-title: Slide's Title |none|
|Title align| You can change the slide title align with this property.                                                                                   | #-title_align: left    |center|
|Color| You can change the color of the slide with this property.                                                                                  | #-color: green         |default|
|Theme| You can change the theme of syntax highlighters of the slide with this property.                                                           | #-theme: github-dark   |gruvbox-dark|
|Expand| With this property, it can be specified that the slide box is the same width as the screen or stretched to the size of the slide elements. | #-expand: True         |True|
|Interpretable| With this property, it is possible to determine whether the codes inside the slide are interpreted and their output is displayed or not.   | #-interpretable: False |True|

**Note: Properties are case sensitive and must be written as defined.**

## Title <a class="anchor" id="title"></a>
This feature refers to the slide:
```python
#pysentation{

#>slide
#-title: First slide

#pysentation}
```

Output:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ First slide ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                             ┃
┃                                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1/1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Title align <a class="anchor" id="title_align"></a>
This property specifies the **location** of the slide **title** and it can be defined in **three** modes: `right`, `center` and `left` **(The default value is `center`)**:
```python
#pysentation{

#>slide
#-title: First slide
#-title_align: left

#pysentation}
```

Output:
```
┏━ First slide ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                             ┃
┃                                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1/1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```


## Color <a class="anchor" id="color"></a>
This property refers to the **color** of the slide and its **components** **(The default value is equal to `default` or color of the terminal font)**:
![img2](https://raw.githubusercontent.com/mimseyedi/pysentation/master/docs/images/slide-color-example.png)

Click <a href="#colors">here</a> to view the available colors.

## Theme <a class="anchor" id="theme"></a>
This property refers to the **theme** of the **syntax highlighters** in the slide **(The default value is `gruvbox-dark`)**:
![img3](https://raw.githubusercontent.com/mimseyedi/pysentation/master/docs/images/theme-example.png)

Click <a href="#themes">here</a> to view the available themes.

## Expand <a class="anchor" id="expand"></a>
By setting this property to `True` or `False`, you can specify whether the **size** of the slide is the same as the size of the **screen** or the size of the **elements** inside it **(The default value is `True`)**:

```python
#pysentation{

#>slide
#-expand: False

#pysentation}
```

## Interpretable <a class="anchor" id="interpretable"></a>
If this property is `True`, all the **codes** inside a slide will be **interpreted separately** with the help of **Python interpreter** and the **output** will be **displayed** under them in a **separate box**. But if its value is `False`, it will not do this **(The default value is `True`)**:

```python
#pysentation{

#>slide
#-interpretable: False

#pysentation}
```

## Comments <a class="anchor" id="comments"></a>
The comments are actually the explanations that we can see in the slides. The content of the comments can be anything and can be given different modes according to the styles of the rich module.

Comments start with `#:`: 
```python
#pysentation{

#>slide
#-title: Wonderful slide
#: Hello!, this is my wonderfull slide.
#: Yes, you see right! I am a comment that can be displayed!
#: Also, I can make the word [yellow]"can"[/yellow] yellow like this.

#pysentation}
```

Output:
![img4](https://raw.githubusercontent.com/mimseyedi/pysentation/master/docs/images/slide-comment-example.png)

## Codes <a class="anchor" id="codes"></a>
The codes have no special characteristics and can be easily written and interpreted if needed:
```python
#pysentation{

#>slide
#-title: Legal age
#: Here is a simple example of if and else statements:
age = 19
if age >= 18:
    print("Access Granted!")
else:
    print("Access Denied! Underage")
    
#pysentation}
```

Output:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Legal age ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                             ┃
┃  Here is a simple example of if and else statements:                                        ┃
┃                                                                                             ┃
┃ ❱ 1 age = 19                                                                                ┃
┃   2 if age >= 18:                                                                           ┃
┃   3 │   print("Access Granted!")                                                            ┃
┃   4 else:                                                                                   ┃
┃   5 │   print("Access Denied! Underage")                                                    ┃
┃   6                                                                                         ┃
┃                                                                                             ┃
┃ ╭─ Output ────────────────────────────────────────────────────────────────────────────────╮ ┃
┃ │ Access Granted!                                                                         │ ┃
┃ ╰─────────────────────────────────────────────────────────────────────────────────────────╯ ┃
┃                                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1/1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

Even if the code raises an exception, the error message will be displayed:
```python
#pysentation{

#>slide
#-title: About [italic]ERRORS[/italic] and how to display them
#: Pay attention to the following example of how errors are displayed:
def div(a, b):
    return a / b
# Division by zero
print(div(4, 0))
#pysentation}
```

Output:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━ About ERRORS and how to display them ━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                             ┃
┃  Pay attention to the following example of how errors are displayed:                        ┃
┃                                                                                             ┃
┃ ❱ 1 def div(a, b):                                                                          ┃
┃   2 │   return a / b                                                                        ┃
┃   3 # Division by zero                                                                      ┃
┃   4 print(div(4, 0))                                                                        ┃
┃                                                                                             ┃
┃ ╭─ <Error> ───────────────────────────────────────────────────────────────────────────────╮ ┃
┃ │ Exception Type: ZeroDivisionError                                                       │ ┃
┃ │ Exception Message: division by zero                                                     │ ┃
┃ │ Scope <module>, Line 4                                                                  │ ┃
┃ ╰─────────────────────────────────────────────────────────────────────────────────────────╯ ┃
┃                                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1/1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Slideshow screen <a class="anchor" id="slideshow"></a>

## Hot keys <a class="anchor" id="hot_keys"></a>

## Options <a class="anchor" id="options"></a>

## Colors and themes <a class="anchor" id="colors_and_themes"></a>

## Colors <a class="anchor" id="colors"></a>
This is a list of **16** main colors that you can **use** in pysentation. You can see the information of more diverse colors from <a href="https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors">here</a>.

**Note: To use any color, you can mention its name, number, hex code and rgb number.**

| Color                                                     | Name             | Number | Hex | RGB  |
|-----------------------------------------------------------|------------------|--------| --- |------|
| ![#000000](https://placehold.co/205x20/000000/000000.png) | "black"          | 0      |-|-|
| ![#800000](https://placehold.co/205x20/800000/800000.png) | "red"            | 1      |-|-|
| ![#008000](https://placehold.co/205x20/008000/008000.png) | "green"          | 2      |-|-|
| ![#808000](https://placehold.co/205x20/808000/808000.png) | "yellow"         | 3      |-|-|
| ![#000080](https://placehold.co/205x20/000080/000080.png) | "blue"           | 4      |-|-|
| ![#800080](https://placehold.co/205x20/800080/800080.png) | "magenta"        | 5      |-|-|
| ![#008080](https://placehold.co/205x20/008080/008080.png) | "cyan"           | 6      |-|-|
| ![#c0c0c0](https://placehold.co/205x20/c0c0c0/c0c0c0.png) | "white"          | 7      |-|-|
| ![#808080](https://placehold.co/205x20/808080/808080.png) | "bright_black"   | 8      |-|-|
| ![#ff0000](https://placehold.co/205x20/ff0000/ff0000.png) | "bright_red"     | 9      |-|-|
| ![#00ff00](https://placehold.co/205x20/00ff00/00ff00.png) | "bright_green"   | 10     |-|-|
| ![#ffff00](https://placehold.co/205x20/ffff00/ffff00.png) | "bright_yellow"  | 11     |-|-|
| ![#0000ff](https://placehold.co/205x20/0000ff/0000ff.png) | "bright_blue"    | 12     |-|-|
| ![#ff00ff](https://placehold.co/205x20/ff00ff/ff00ff.png) | "bright_magenta" | 13     |-|-|
| ![#00ffff](https://placehold.co/205x20/00ffff/00ffff.png) | "bright_cyan"    | 14     |-|-|
| ![#ffffff](https://placehold.co/205x20/ffffff/ffffff.png) | "bright_white"   | 15     |-|-|

## Themes <a class="anchor" id="themes"></a>
**Popular** and **high-quality** themes are listed so that you can **use** them. Visit <a href="https://pygments.org/styles/">here</a> for more.

**Note: To use these themes, you must mention its full name, and in case of mistake, the default theme will be selected.**

| Name           | Light              | Dark               |
|----------------|--------------------|--------------------|
| bw             | :heavy_check_mark: |                    |
| sas            | :heavy_check_mark: |                    |
| staroffice     |                    | :heavy_check_mark: |
| xcode          | :heavy_check_mark: |                    |
| default        | :heavy_check_mark: |                    |
| monokai        |                    | :heavy_check_mark: |
| lightbulb      | :heavy_check_mark: |                    |
| github-dark    |                    | :heavy_check_mark: |
| rrt            |                    | :heavy_check_mark: |
| gruvbox-dark   |                    | :heavy_check_mark: |
| gruvbox-light  | :heavy_check_mark: |                    |
| solarized-light | :heavy_check_mark: |                    |
| solarized-dark |                    | :heavy_check_mark: |
| nord           |                    | :heavy_check_mark: |
| paraiso-light  | :heavy_check_mark: |                    |
| paraiso-dark   |                    | :heavy_check_mark: |
| autumn         | :heavy_check_mark: |                    |
| vim            |                    | :heavy_check_mark: |
| vs             | :heavy_check_mark: |                    |
| one-dark       |                    | :heavy_check_mark: |
| dracula        |                    | :heavy_check_mark: |

## Bugs/Requests <a class="anchor" id="bugs_requests"></a>
Please send **bug reports** and **feature** requests through <a href="https://github.com/mimseyedi/pysentation/issues">github issue tracker</a>.

## License <a class="anchor" id="license"></a>
**pysentation** is a **free** and **open source** project under the **GPL-3** LICENSE. Any **contribution** is welcome. You can do this by **registering** a **pull request**.