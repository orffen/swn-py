#!/usr/bin/env python3
#
# religion.py
# SWN Religion Generator
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

class Religion:
    """
    This class generates a religion from tables/religion.json,
    which has the following attributes:
    
    - evolution (string)
    - leadership (string)
    - origin_tradition (string)

    """
    def __init__(self):
        with open("tables/religion.json", "r") as file:
            religion = json.load(file)
            self.evolution        = str(random.choice(religion["evolution"]))
            self.leadership       = str(random.choice(religion["leadership"]))
            self.origin_tradition = str(
                    random.choice(religion["origin_tradition"]))

    def __str__(self):
        r = [
                "Evolution: " + self.evolution,
                "Leadership: " + self.leadership,
                "Origin Tradition: " + self.origin_tradition
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
        print(Religion())

