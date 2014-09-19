# SWN Toolbox

## Introduction

The SWN Toolbox is a collection of [Python](https://www.python.org) scripts
designed to speed up random generation of various Stars Without Number things.
It is aimed primarily at Game Masters.

The scripts are written in Python; you'll need an installation of Python on your
system to run them. Python is available at <http://www.python.org>.

The SWN Toolbox is [hosted on GitHub](https://github.com/orffen/pyswn).

## Installation

No installation is required; simply extract the file into a folder of your
choice. The .py files can be run directly from the command-line, e.g.:

- python alien.py

If you're running in a Windows environment, you most likely don't have
Python installed. You can download Python for free from <http://www.python.org>.

## Usage

In this release, each script is designed to be run directly from the
command-line.

Every script in the collection supports a single command-line argument:

- a number, which specifies the amount of items to generate.

For example: "python alien.py 3" will generate 3 alien races.

## Extending the SWN Toolbox

The scripts use the tables in the subdirectory, which are simple
[JSON](http://www.json.org) files.

You can edit them to add more entries to be randomly-selected by the scripts.

## License

The SWN Toolbox

Copyright (c) 2014 Steve Simenic <orffen@orffenspace.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
