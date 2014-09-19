#!/usr/bin/env python3
#
# animal.py
# SWN Animal Generator
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

class Animal:
    """
    This class generates an animal from tables/animal.json,
    which has the following attributes:
    
    - template (string)
    - traits (array)
    - group_size (integer)

    """
    def __init__(self):
        with open("tables/animal.json", "r") as file:
            animal          = json.load(file)
            self.template   = str(random.choice(animal["template"]))
            self.group_size = random.choice(range(1, 7))
            if self.template == "Hybrid":
                num_templates = random.choice([2, 2, 3])
                templates = set()
                while len(templates) < num_templates:
                    new_template = str(random.choice(animal["template"]))
                    if new_template != "Hybrid":
                        templates.add(new_template)
                self.traits = []
                for i in templates:
                    self.traits.append(
                            str(random.choice(animal["trait"][i.lower()]))
                    )
                self.template = "/".join(templates)
            else:
                self.traits = [
                        str(random.choice(
                            animal["trait"][self.template.lower()]))
                ]

    def __str__(self):
        r = [
                "Template: "   + self.template,
                "Traits: "     + ", ".join(self.traits),
                "Group size: " + str(self.group_size)
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
        print(Animal())

