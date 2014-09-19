#!/usr/bin/env python3
#
# faction.py
# SWN Faction Generator
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

class Faction:
    """
    This class generates a faction which has the following attributes:

    - type (string)
    - hit_points (integer)
    - force (integer)
    - cunning (integer)
    - wealth (integer)
    - tags (array)
    - assets (array)

    """
    def __init__(self):
        with open("tables/faction.json", "r") as file:
            faction         = json.load(file)
            self.type       = random.choice(["minor", "major", "hegemon"])
            self.hit_points = int(faction[self.type]["hit_points"])
            self.tags = []
            for i in range(random.choice([1] * 4 + [2])):
                self.tags.append(str(random.choice(faction["tags"])))

            stats           = list(faction[self.type]["stats"])
            random.shuffle(stats)
            #TODO: better way of doing the below?
            stats[0] = ["force", int(stats[0])]
            stats[1] = ["cunning", int(stats[1])]
            stats[2] = ["wealth", int(stats[2])]
            stats = {k: v for k, v in stats} # convert to dictionary
            bigstat = max(stats, key=stats.get) # get largest stat
            self.force   = stats["force"]
            self.cunning = stats["cunning"]
            self.wealth  = stats["wealth"]

            self.assets = []
            #TODO: need to check the logic on the below
            for i in range(int(faction[self.type]["assets"][0])):
                number = str(random.choice(range(stats[bigstat])) + 1)
                self.assets.append("{!s}/{} {!s}".format(
                    random.choice(list(faction[bigstat][number])),
                    bigstat.capitalize(),
                    number
                ))
            for i in range(int(faction[self.type]["assets"][1])):
                # exclude the biggest stat
                stat = list(stats.keys())
                stat.remove(bigstat)
                stat = random.choice(stat)
                number = str(random.choice(range(stats[stat])) + 1)
                self.assets.append("{!s}/{} {!s}".format(
                    random.choice(list(faction[stat][number])),
                    stat.capitalize(),
                    number
                ))

            self.type = self.type.capitalize() # format for output

    def __str__(self):
        r = [
            "Type: "       + self.type,
            "Hit Points: " + str(self.hit_points),
            "Force: "      + str(self.force),
            "Cunning: "    + str(self.cunning),
            "Wealth: "     + str(self.wealth),
            "Tags: "       + ", ".join(self.tags),
            "Assets: "     + ", ".join(self.assets)
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
        print(Faction())

