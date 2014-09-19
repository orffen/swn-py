#!/usr/bin/env python3
#
# world.py
# SWN World Generator
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

class World:
    """
    This class generates a world from tables/world.yaml,
    which has the following attributes:
    
    - atmosphere (string)
    - temperature (string)
    - biosphere (string)
    - population (string)
    - tech_level (string)
    - tags (array)

    """
    def __init__(self):
        with open("tables/world.json", "r") as file:
            world = json.load(file)
            self.atmosphere  = str(random.choice(world["atmosphere"]))
            self.temperature = str(random.choice(world["temperature"]))
            self.biosphere   = str(random.choice(world["biosphere"]))
            self.population  = str(random.choice(world["population"]))
            self.tech_level  = str(random.choice(world["tech_level"]))
            self.tags = []
            for i in range(2):
                self.tags.append(str(random.choice(world["tags"])))

    def __str__(self):
        r = [
                "Atmosphere: "  + self.atmosphere,
                "Temperature: " + self.temperature,
                "Biosphere: "   + self.biosphere,
                "Population: "  + self.population,
                "Tech Level: "  + self.tech_level,
                "Tags: "        + ", ".join(self.tags)
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
        print(World())

