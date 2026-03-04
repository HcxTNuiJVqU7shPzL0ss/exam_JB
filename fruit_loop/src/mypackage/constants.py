"""Module for Lesson 02, Exam, constants.

Used to store global constants.
PEP 8
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


from colorama import Back


# Width of the board
WIDTH = 37
# Height of the board
HEIGHT = 13

# Highlight in green for symbol print
HIGHLIGHT = f'{' ' + Back.GREEN + ' ' + Back.RESET + ' '}'

# Move up command
UP = 'w'
# Move down command
DOWN = 's'
# Move left command
LEFT = 'a'
# Move right command
RIGHT = 'd'

# Quit game command
QUIT = 'q'
# Exit game command
EXIT = 'x'

# Inventory command
INVENTORY = 'i'
# Help command
HELP = 'h'
# Print symbol information command
PRINTINFO = 'p'

# Grace period starts at 0
GRACE_START = 0
# Grace period set with this value
GRACE_SET = 5

# Number of steps taken starts at 0
STEPS_START = 0

# Gamer score starts at 0
SCORE_START = 0

# Default for allowing negative score is False
NEG_START = False

# Symbol for empty coordinate
EMPTY = '.'
# Symbol for impassable wall
WALL = '■'
# Symbol for unstable wall
US_WALL = '#'
# Symbol for gamer / player marker
GAMER = '@'

# OG items list
# Type
OG_T = 'og'
# Value
OG_V = 10
OG_V_F = 20
# Symbol
OG_S = '?'

# Traps items list
# Type
TRAP_T = 'trap'
# Value
TRAP_V = -10
# Symbol
TRAP_S = 't'

# Chest items list
# Type
CHEST_T = 'chest'
# Value
CHEST_V = 100
# Symbol
CHEST_S = 'c'

# Keys items list
# Type
KEY_T = 'key'
# Name
KEY_N = 'Skeleton Key'
# Value
KEY_V = 0
# Symbol
KEY_S = 'k'

# Pickaxe items list
# Type
PICK_T = 'pickaxe'
# Name
PICK_N = 'Pickaxe'
# Value
PICK_V = 0
# Symbol
PICK_S = 'p'

# Fertile items list
# Type
FERT_T = 'fertile'
# Value
FERT_V = 25
# Symbol
FERT_S = '*'
