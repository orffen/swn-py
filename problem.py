#!/usr/bin/env python3
#
# problem.py
# SWN Problem Generator
#
# Copyright (c) 2021 Steve Simenic <orffen@orffenspace.com>
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

class Problem:
    """
    This class generates a problem from tables/problem.json,
    which has the following attributes:

    - conflict_type (string)
    - situation (string)
    - focus (string)
    - restraint (string)
    - twist (string)

    """
    def __init__(self):
        with open("tables/problem.json", "r") as file:
            problem = json.load(file)
            self.conflict_type = str(
                random.choice(list(problem["conflict_type"].keys())))
            self.situation = str(
                random.choice(problem["conflict_type"][self.conflict_type][0]))
            self.focus = str(
                random.choice(problem["conflict_type"][self.conflict_type][1]))
            self.restraint = str(random.choice(problem["restraint"]))
            self.twist = str(random.choice(problem["twist"]))

    def __str__(self):
        r = [
            "Conflict Type: " + self.conflict_type,
            "Situation: " + self.situation,
            "Focus: " + self.focus,
            "Restraint: " + self.restraint,
            "Twist: " + self.twist
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
        print(Problem())
