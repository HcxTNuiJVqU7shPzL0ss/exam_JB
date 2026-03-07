"""Module for Lesson 02, Exam, pickups.

Pickups view.
Regarding exam requirements, this file implements:
Version 1 - D
Version 2 - I
Version 2 - J
Version 2 - K
Version 2 - L
"""

#####################################################################
# Copyright 2026 gnoff
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#####################################################################


import random


from dataclasses import dataclass


# Access constants
from mypackage.constants import (OG_T, OG_V, OG_V_F, OG_S,
                                 TRAP_T, TRAP_V, TRAP_S,
                                 CHEST_T, CHEST_V, CHEST_S,
                                 KEY_T, KEY_N, KEY_V, KEY_S,
                                 PICK_T, PICK_N, PICK_V, PICK_S,
                                 FERT_T, FERT_V, FERT_S)


# Use a dataclass since not enough public functions
# as to properly use a "regular" Class
@dataclass
class Item:
    """Use to represent items that can be picked up."""

    def __init__(self, type_i = OG_T, name = '',
                 value = OG_V, symbol = OG_S):
        """Use to initialize an object.

        # Exam Version 1: D (Value is 20 for fruits, not 10)
        Note that what is not botanically considered a fruit
        is still worth the default 10 points.
        """
        self.type = type_i
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        """Use to print item symbol on the board."""
        return self.symbol


# Use to add OG fruits and veggies, etc.
# These give points if/when picked up
# Exam Version 1: D (Value is 20 for fruits, not 10)
# As of random AI and google, the following are
# considered to be fruits (from a botanical perspective):
# apple, strawberry, cherry, watermelon, cucumber
# The others keep the default 10 points
pickup_list = [Item(name = 'Carrot'),  # Root veggie
               Item(name = 'Apple', value = OG_V_F),
               Item(name = 'Strawberry', value = OG_V_F),
               Item(name = 'Cherry', value = OG_V_F),
               Item(name = 'Watermelon', value = OG_V_F),
               Item(name = 'Radish'),  # Root veggie
               Item(name = 'Cucumber', value = OG_V_F),
               Item(name = 'Meatball')  # Protein
               ]

# Use to add traps on the grid
# Exam Version 2: I (Add traps to the board, -10 points, traps shall
# remain on the board so gamer can fall into it multiple times)
trap_list = [Item(type_i = TRAP_T, name = 'Bear trap',
                  value = TRAP_V, symbol = TRAP_S),
             Item(type_i = TRAP_T, name = 'Bird snare',
                  value = TRAP_V, symbol = TRAP_S)]

# Use to add chests on the grid
# Exam Version 2: K (Add chests to the board)
# If you land on a chest, and have at least one key in inventory,
# you will pick up the chest, value 100 points
# The key will be used up
chest_list = [Item(type_i = CHEST_T, name = 'Earth Chest',
                   value = CHEST_V, symbol = CHEST_S),
              Item(type_i = CHEST_T, name = 'Wind Chest',
                   value = CHEST_V, symbol = CHEST_S)]

# Use to add keys on the grid
# Exam Version 2: K (Add keys to the board)
# If you land on a chest, and have at least one key in inventory,
# you will pick up the chest
# The key will be used up
key_list = [Item(type_i = KEY_T, name = KEY_N,
                 value = KEY_V, symbol = KEY_S),
            Item(type_i = KEY_T, name = KEY_N,
                  value = KEY_V, symbol = KEY_S)]

# Used to add pickaxes (spade) to the grid
# Exam Version 2: J (Add pickaxes to the board)
# Next time you walk into a wall, the pickaxe is used,
# and the wall is removed.
# Note: Only "unstable walls" can be removed, not the
# walls around the board.
# 2 pickaxes are available, less than the amount of
# unstable walls.
pickaxe_list = [Item(type_i = PICK_T, name = PICK_N,
                     value = PICK_V, symbol = PICK_S),
                Item(type_i = PICK_T, name = PICK_N,
                     value = PICK_V, symbol = PICK_S)]

# Use to collect all (at start) board items in one list
place_list = (pickup_list + trap_list + chest_list +
              key_list + pickaxe_list)

# Used for fertile addons
# Exam Version 2: L (Every 25 step adds new points item to board)
fertile = [Item(type_i = FERT_T, name = 'Mango',
                value = FERT_V, symbol = FERT_S),
           Item(type_i = FERT_T, name = 'Lime',
                value = FERT_V, symbol = FERT_S),
           Item(type_i = FERT_T, name = 'Orange',
                value = FERT_V, symbol = FERT_S)
           ]


def place_items(grid, addon, fertile_y):
    """Use to create items on random positions.

    At startup:
    Place the items from the "place_list" on the board grid.
    When fertile happens:
    Place the generated fertile item.
    """
    while True:
        # Randomly generate a position until there is
        # one not previously used
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            # Add fertile
            if fertile_y:
                grid.set(x, y, addon)
                print(f'\nNew item {addon} has been added to: '
                      f'x:{x}, y:{y}!')
            # Add items at start
            else:
                grid.set(x, y, addon)
            # Abort the while loop
            break


def randomize(grid):
    """Use to create items on random positions.

    Place the items from the "place_list" on the board grid.
    """
    for item in place_list:
        place_items(grid, item, False)


def fertile_generate(grid):
    """Use to place fertile items.

    Exam Version 2: L (Every 25 step adds new points item to board)
    """
    new_fruit = random.choice(fertile)
    place_items(grid, new_fruit, True)
