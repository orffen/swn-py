#!/usr/bin/env python3
#
# alien.py
# SWN Alien Generator
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

class Alien:
    """
    This class generates an alien race from tables/alien.json,
    which has the following attributes:
    
    - body_type (string)
    - social_structure (string)
    - lenses (array)

    """
    def __init__(self):
        with open("tables/alien.json", "r") as file:
            alien                 = json.load(file)
            self.body_type        = str(random.choice(alien["body_type"]))
            self.social_structure = str(
                    random.choice(alien["social_structure"]))
            self.lenses = []
            for i in range(random.choice([1, 2, 2, 3, 4])):
                self.lenses.append(str(random.choice(alien["lens"])))

    def __str__(self):
        r = [
                "Body type: "        + self.body_type,
                "Social Structure: " + self.social_structure,
                "Lenses: "           + ", ".join(self.lenses)
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
        print(Alien())

