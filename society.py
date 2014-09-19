#!/usr/bin/env python3
#
# society.py
# SWN Society Generator
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

class Society:
    """
    This class generates a society from tables/society.json,
    which has the following attributes:
    
    - colonization_reason (string)
    - initial_government_type (string)
    - traits (array)
    - conflict (string)
    - evolution (string)

    """
    def __init__(self):
        with open("tables/society.json", "r") as file:
            society = json.load(file)
            self.colonization_reason = str(
                    random.choice(society["colonization_reason"]))
            self.initial_government_type = str(
                    random.choice(society["government_type"]))
            self.conflict = str(random.choice(society["conflict"]))
            govt = self.initial_government_type.lower().split()
            govt = "_".join(govt)
            self.evolution = str(random.choice(society["evolution"][govt]))
            self.traits = []
            for i in range(random.choice([2, 3])):
                self.traits.append(str(random.choice(society["trait"])))

    def __str__(self):
        r = [
                "Colonization Reason: "     + self.colonization_reason,
                "Initial Government Type: " + self.initial_government_type,
                "Traits: "                  + ", ".join(self.traits),
                "Conflict: "                + self.conflict,
                "Evolution: "               + self.evolution
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
        print(Society())

