"""Module for Lesson 02, Exam.

Grid view.
This contains the Class which builds the board.
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


class Grid:
    """Use to represent the board.

    It is possible to change the standard size and signs for
    different squares.
    """

    empty = '.'             # Indicates an empty square
    wall = '■'              # Indicates a wall
    unstable_wall = '#'     # Indicates a wall that may be breached
    gamer = '@'             # Indicates the current gamer

    def __init__(self, player, width, height):
        """Use to create an object of the Class Grid."""
        # The board if stored in a list of lists.
        # List comprehension is used to place the sign for
        # "empty" on each place on the board.
        self.width = width
        self.height = height
        self.data = [[self.empty for _ in range(self.width)]
                     for _ in range(self.height)]
        self.player = player


    def get(self, x, y):
        """Use to get what is on a certain position."""
        return self.data[y][x]

    def set(self, x, y, value):
        """Use to change what is on a certain position."""
        self.data[y][x] = value

    def set_player(self, player):
        """Use to handle player."""
        self.player = player

    def clear(self, x, y):
        """Use to remove an item from a position."""
        self.set(x, y, self.empty)

    def __str__(self):
        """Use so the board can be displayed with print(grid)."""
        xs = ''
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += self.gamer
                else:
                    xs += str(row[x])
            xs += '\n'
        return xs


    def make_walls(self):
        """Use to create walls."""
        # First two are for walls around the board
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

        # Creates extra "inner" walls
        # Exam Version 1: H (Use for loops in grid.py to create more
        # than one connecting walls, though without creating a
        # room which you cannot enter.)
        for k in range(3, self.height // 2):
            # Create a vertical wall, starting at 3, moving to
            # maximum half the board
            self.set(10, k, self.unstable_wall)
            self.set(self.width - 1, k, self.wall)

        for m in range(13, self.width - 7):
            # Create a horizontal wall, starting at 13, moving
            # to leave 7 spaces after (including the actual
            # "fixed" wall to the right).
            self.set(m, 8, self.unstable_wall)
            self.set(m, self.height - 1, self.wall)


    # Used in the file pickups.py
    def get_random_x(self):
        """Use to randomize an x-pos on the board."""
        return random.randint(1, self.width - 1)

    def get_random_y(self):
        """Use to randomize a y-pos on the board."""
        return random.randint(1, self.height - 1)

    def is_empty(self, x, y):
        """Use to return True if nothing on the square."""
        return self.get(x, y) == self.empty
