#!/usr/bin/env python3
#
# trade.py
# SWN Trade Generator
#
# Copyright (c) 2014 Niels Jensen <niels@nielsjensen.info>
#
# This file is subbmited for consideration to be part of the SWN Toolbox.
# Usage:
#   python trade.py
#       will produce a random market for a 1 x TL4 classed world
#
#   python trade.py <number of markets> <TL of world>
#       example: python trade.py 2 3
#           will produce 2 x random markets TL3 classed worlds
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

class Trade:
    """
    This class generates a society from tables/society.json,
    which has the following attributes:
    
    - colonization_reason (string)
    - initial_government_type (string)
    - traits (array)
    - conflict (string)
    - evolution (string)

    """
    def __init__(self, techlevel):
        with open("tables/trade.json", "r") as file:
            trade_goods = json.load(file)
            self.selling = []
            for i in range(random.choice([2, 2, 3, 3, 3, 3, 4])):
                trade_item = str(random.choice(trade_goods["trade_item"][techlevel]))
                price = int(trade_goods["item_detail"][trade_item]["base_price"])
                amount_available = self.roll_die(str(trade_goods["item_detail"][trade_item]["tons"]))
                self.selling.append("{amount_available} x {trade_item}: {price} credits".format(**locals()))
                trade_goods["trade_item"][techlevel].remove(trade_item)
            self.wanted = []
            for i in range(random.choice([2, 2, 3, 3, 3, 3, 4])):
                trade_item = str(random.choice(trade_goods["trade_item"][techlevel]))
                base_price = (trade_goods["item_detail"][trade_item]["base_price"])
                price = int(float(base_price
                            * (self.roll_die(str(trade_goods["item_detail"][trade_item]["wanted_value"]))
                               / 100)))
                self.wanted.append("{trade_item}: {price} credits".format(**locals()))
                trade_goods["trade_item"][techlevel].remove(trade_item)
            self.unwanted = []
            for i in range(random.choice([1, 2, 3])):
                if len(trade_goods["trade_item"][techlevel]) > 0:
                    trade_item = str(random.choice(trade_goods["trade_item"][techlevel]))
                    base_price = (int(trade_goods["item_detail"][trade_item]["base_price"]))
                    price = int(float(base_price
                                * (self.roll_die(str(trade_goods["item_detail"][trade_item]["unwanted_value"]))
                                   / 100)))
                    self.unwanted.append("{trade_item}: {price} credits".format(**locals()))
                    trade_goods["trade_item"][techlevel].remove(trade_item)
            self.trade = []
            for i in trade_goods["trade_item"][techlevel]:
                trade_item = str(random.choice(trade_goods["trade_item"][techlevel]))
                base_price = (int(trade_goods["item_detail"][trade_item]["base_price"]))
                if random.choice([1, 2]) == 1:
                    price = int(float(base_price
                                - (base_price
                                   * (self.roll_die(str(trade_goods["item_detail"][trade_item]["standard_value"]))
                                      / 100))))
                else:
                    price = int(float(base_price
                                + (base_price
                                * (self.roll_die(str(trade_goods["item_detail"][trade_item]["standard_value"]))
                                    / 100))))
                self.trade.append("{trade_item}: {price} credits".format(**locals()))
                trade_goods["trade_item"][techlevel].remove(trade_item)

    def roll_die(self, rollvalue):
        totalroll = 0
        if '*' in rollvalue:
            dice_detail = rollvalue.split('*')
            dice_breakdown = dice_detail[0].split('d')
            no_of_die = int(dice_breakdown[0])
            no_of_sides = int(dice_breakdown[1])
            multiplier = int(dice_detail[1])
            for r in range(no_of_die):
                totalroll += random.randint(1, no_of_sides)
            return totalroll * multiplier
        elif '+' in rollvalue:
            dice_detail = rollvalue.split('+')
            dice_breakdown = dice_detail[0].split('d')
            no_of_die = int(dice_breakdown[0])
            no_of_sides = int(dice_breakdown[1])
            addition = int(dice_detail[1])
            for r in range(no_of_die):
                totalroll += random.randint(1, no_of_sides)
            return totalroll + addition
        else:
            dice_breakdown = rollvalue.split('d')
            no_of_die = int(dice_breakdown[0])
            no_of_sides = int(dice_breakdown[1])
            for r in range(no_of_die):
                totalroll += random.randint(1, no_of_sides)
            return totalroll

    def __str__(self):
        r = [
                "\n"
                "World Market:\n===========================\n"
                "\n"
                "Selling:\n----------------\n"
                "Price Per Ton: " + "\n               ".join(self.selling),
                "\n"
                "\n"
                "Purchase Prices:\n----------------\n"
                "Wanted:   " + "\n          ".join(self.wanted),
                "\n"
                "Unwanted: "+ "\n          ".join(self.unwanted),
                "\n"
                "Other:    " + "\n          ".join(self.trade)
        ]
        return "\n".join(r)


if __name__ == "__main__":
    try:
        times = int(sys.argv[1])
        tech_level = "TL" + sys.argv[2]
    except:
        times = 1
        tech_level = "TL4"
    for i in range(times):
        if i != 0:
            print("-----------+-+-+-----------")
        print(Trade(tech_level))

