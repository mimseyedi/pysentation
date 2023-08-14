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
| Color                                                     | Name             | Number | Hex | RGB  |
|-----------------------------------------------------------|------------------|--------| --- |------|
| ![#000000](https://placehold.co/205x70/000000/000000.png) | "black"          | -      |-|
| ![#800000](https://placehold.co/205x70/800000/800000.png)  | "red"            | -      |-|
| ![#008000](https://placehold.co/205x70/008000/008000.png)  | "green"          | -      |-|
| ![#808000](https://placehold.co/205x70/808000/808000.png)  | "yellow"         | -      |-|
| ![#000080](https://placehold.co/205x70/000080/000080.png)  | "blue"           | -      |-|
| ![#800080](https://placehold.co/205x70/800080/800080.png)  | "magenta"        | -      |-|
| ![#008080](https://placehold.co/205x70/008080/008080.png)  | "cyan"           | -      |-|
| ![#c0c0c0](https://placehold.co/205x70/c0c0c0/c0c0c0.png)  | "white"          | -      |-|
| ![#808080](https://placehold.co/205x70/808080/808080.png)  | "bright_black"   | -      |-|
| ![#ff0000](https://placehold.co/205x70/ff0000/ff0000.png)  | "bright_red"     | -      |-|
| ![#00ff00](https://placehold.co/205x70/00ff00/00ff00.png)  | "bright_green"   | -      |-|
| ![#ffff00](https://placehold.co/205x70/ffff00/ffff00.png)  | "bright_yellow"  | -      |-|
| ![#0000ff](https://placehold.co/205x70/0000ff/0000ff.png)  | "bright_blue"    | -      |-|
| ![#ff00ff](https://placehold.co/205x70/ff00ff/ff00ff.png)  | "bright_magenta" | -      |-|
| ![#00ffff](https://placehold.co/205x70/00ffff/00ffff.png)  | "bright_cyan"    | -      |-|
| ![#ffffff](https://placehold.co/205x70/ffffff/ffffff.png)  | "bright_white"   | -      |-|
## Themes <a class="anchor" id="themes"></a>

## Bugs/Requests <a class="anchor" id="bugs_requests"></a>

## License <a class="anchor" id="license"></a>