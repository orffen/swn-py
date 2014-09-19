#!/usr/bin/env python3
#
# heresy.py
# SWN Heresy Generator
#
# Copyright (c) 2014 Steve Simenic <orffen@orffenspace.com>
#
# This file is part of the SWN Toolbox.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import json
import random
import sys

class Heresy:
    """
    This class generates an heresy from tables/heresy.json,
    which has the following attributes:
    
    - founder (string)
    - major_heresy (string)
    - attitude (string)
    - quirk (string)
    
    """
    def __init__(self):
        with open("tables/heresy.json", "r") as file:
            heresy = json.load(file)
            self.founder      = str(random.choice(heresy["founder"]))
            self.major_heresy = str(random.choice(heresy["major_heresy"]))
            self.attitude     = str(random.choice(heresy["attitude"]))
            self.quirk        = str(random.choice(heresy["quirk"]))

    def __str__(self):
        r = [
                "Founder: "      + self.founder,
                "Major Heresy: " + self.major_heresy,
                "Attitude: "     + self.attitude,
                "Quirk: "        + self.quirk
        ]
        return "\n".join(r)


if __name__ == "__main__":
    try:
        times = int(sys.argv[1])
    except:
        times = 1
    for i in range(times):
        if i != 0:
            print("-----------+-+-+-----------")
        print(Heresy())

