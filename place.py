#!/usr/bin/env python3
#
# place.py
# SWN Place Generator
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

class Place:
    """
    This class generates a place from tables/place.json,
    which has the following attributes:

    - hazard (string)
    - specific_example (string)
    - possible_danger (string)
    - reward (string)
    - civilized_ongoings (string)
    - wilderness_ongoings (string)

    """
    def __init__(self):
        with open("tables/place.json", "r") as file:
            place = json.load(file)
            self.hazard = str(
                random.choice(list(place["hazard"].keys())))
            self.specific_example = str(
                random.choice(place["hazard"][self.hazard][0]))
            self.possible_danger = str(
                random.choice(place["hazard"][self.hazard][1]))
            self.reward = str(random.choice(place["reward"]))
            self.civilized_ongoings = str(random.choice(place["civilized_ongoings"]))
            self.wilderness_ongoings = str(random.choice(place["wilderness_ongoings"]))

    def __str__(self):
        r = [
            "Hazard: " + self.hazard,
            "Specific Example: " + self.specific_example,
            "Possible Danger: " + self.possible_danger,
            "Reward: " + self.reward,
            "Civilized Ongoings: " + self.civilized_ongoings,
            "Wilderness Ongoings: " + self.wilderness_ongoings
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
        print(Place())
