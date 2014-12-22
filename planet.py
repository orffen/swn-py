#!/usr/bin/env python3
#
# planet.py
# SWN Planet Generator
# This script generates a complete planet with a world description,
# society, fauna, aliens (sometimes), a faction or two, a religion,
# some political parties and NPCs.
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

from adventure import Adventure
from alien import Alien
from animal import Animal
from architecture import Architecture
from corporation import Corporation
from faction import Faction
from heresy import Heresy
from npc import NPC
from political_party import PoliticalParty
from religion import Religion
from society import Society
from trade import Trade
from world import World
import random

if __name__ == "__main__":
    print(World())
    print("Predominant architectural feature: {}".format(Architecture()))
    print(Society())
    print("---")
    for i in range(random.choice([2, 3])):
        print("Animal:\n{}\n".format(Animal()))
    print("---")
    for i in range(random.choice([2, 3])):
        print("Political Party:\n{}\n".format(PoliticalParty()))
    print("---")
    for i in range(random.choice([2, 3])):
        print("Corporation:\n{}\n".format(Corporation()))
    print("---")
    for i in range(random.choice([1, 2])):
        print(random.choice([
            "Religion:\n{}\n".format(Religion()),
            "Heresy:\n{}\n".format(Heresy())
        ]))
    print("---")
    print("Local Faction: {}".format(Faction()))
    print("---")
    print("Prominent NPCs:")
    for i in range(random.choice([3, 4, 5])):
        print("-\n{}".format(NPC()))
    print("---")
    print("Adventure Seeds:")
    for i in range(3):
        print(Adventure())
    print(Trade())

