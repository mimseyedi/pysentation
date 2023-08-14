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

## Slides <a class="anchor" id="slides"></a>

## Properties <a class="anchor" id="props"></a>

## Title <a class="anchor" id="title"></a>

## Title align <a class="anchor" id="title_align"></a>

## Color <a class="anchor" id="color"></a>

## Theme <a class="anchor" id="theme"></a>

## Expand <a class="anchor" id="expand"></a>

## Interpretable <a class="anchor" id="interpretable"></a>

## Comments <a class="anchor" id="comments"></a>

## Codes <a class="anchor" id="codes"></a>

## Slideshow screen <a class="anchor" id="slideshow"></a>

## Hot keys <a class="anchor" id="hot_keys"></a>

## Options <a class="anchor" id="options"></a>

## Colors and themes <a class="anchor" id="colors_and_themes"></a>

## Colors <a class="anchor" id="colors"></a>
| Color with name                                         | Number | Hex | RGB  |
|---------------------------------------------------------|--------| --- |------|
| <p style="background-color: #000000">black</p>          | 0      |-|-|
|![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) |1|-|-|
| <p style="background-color: #800000">red</p>            | 1      |-|-|
| <p style="background-color: #008000">green</p>          | 2      |-|-|
| <p style="background-color: #808000">yellow</p>         | 3      |-|-|
| <p style="background-color: #000080">blue</p>           | 4      |-|-|
| <p style="background-color: #800080">magenta</p>        | 5      |-|-|
| <p style="background-color: #008080">cyan</p>           | 6      |-|-|
| <p style="background-color: #c0c0c0">white</p>          | 7      |-|-|
| <p style="background-color: #808080">bright_black</p>   | 8      |-|-|
| <p style="background-color: #ff0000">bright_red</p>     | 9      |-|-|
| <p style="background-color: #00ff00">bright_green</p>   | 10     |-|-|
| <p style="background-color: #ffff00">bright_yellow</p>  | 11     |-|-|
| <p style="background-color: #0000ff">bright_blue</p>    | 12     |-|-|
| <p style="background-color: #ff00ff">bright_magenta</p> | 13     |-|-|
| <p style="background-color: #00ffff">bright_cyan</p>    | 14     |-|-|
| <p style="background-color: #ffffff">bright_white</p>   | 15     |-|-|
## Themes <a class="anchor" id="themes"></a>

## Bugs/Requests <a class="anchor" id="bugs_requests"></a>

## License <a class="anchor" id="license"></a>