"""Module for Lesson 02, Exam, Constants.

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

# Highlight in green
HIGHLIGHT = f'{' ' + Back.GREEN + ' ' + Back.RESET + ' '}'

# Move up
UP = 'w'
# Move down
DOWN = 's'
# Move left
LEFT = 'a'
# Move right
RIGHT = 'd'

# Quit game
QUIT = 'q'
# Exit game
EXIT = 'x'

# Inventory command
INVENTORY = 'i'
# Help command
HELP = 'h'
# Print symbol information
PRINTINFO = 'p'

# Grace period starts at 0
GRACE_START = 0
# Grace period set with this score
GRACE_SET = 5

# Number of steps taken starts at 0
STEPS_START = 0

# Gamer score starts at 0
SCORE_START = 0

# Default for allowing negative score is False
NEG_START = False
