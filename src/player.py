"""Module for Lesson 02, Exam.

Player view.
This contains the Class which creates the player.
Also handles interaction, like movement.
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


import emoji


# Note that these functions are located in a different
# directory
from my_funct_dir.my_base_functions import press_continue


# pylint: disable=import-error
from .pickups import (pickup_list, chest_list, key_list,
                     fertile_generate)
# pylint: enable=import-error


class Player:
    """Use for Class Player."""

    grace_cnt = 0
    steps = 0

    def __init__(self, x, y):
        """Use to create an object of Player."""
        self.pos_x = x
        self.pos_y = y
        self.score = 0
        self.inventory = []
        self.use_neg = False


    def print_status(self, game_grid):
        """Use to display the board grid and number of points."""
        print(f'\n>>> {emoji.emojize(':strawberry:')} '
              f'Fruit Loop {emoji.emojize(':watermelon:')} <<<')
        print('--------------------------------------\n')
        print(f'You have {self.score} points.\n'
              f'You have used {self.steps} moves.\n')
        print(game_grid)


    def set_lava_handling(self, lava_neg):
        """Use to handle lava score reduction.

        Checks if 0 shall be the lowest allowed score,
        or if (unlimited) negative values are allowed.
        """
        self.use_neg = lava_neg


    def move(self, dx, dy):
        """Use to move the player.

        dx = horizontal movement, from left to right.
        dy = vertical movement, from up to down.
        """
        self.pos_x += dx
        self.pos_y += dy


    def can_move(self, x, y, grid):
        """Use to check that you can move.

        # Exam Version 1: C (Player not allowed
        to walk through walls).
        """
        check_x = self.pos_x + x
        check_y = self.pos_y + y
        check_wall = grid.get(check_x, check_y)

        # Return True if no wall is found
        if check_wall in (grid.wall, grid.unstable_wall):
            print('\nNot allowed to walk through walls!')
            press_continue()
            return False
        return True


    def handle_lava_score(self, grace):
        """Use to handle score for The Floor is Lava.

        If on "Grace Period", does not lose points.
        """
        if grace:
            # Found an item, add grace period of 5
            self.grace_cnt = 5
        else:
            if self.grace_cnt > 0:
                self.grace_cnt -= 1
            else:
                # Handle "The Floor is Lava"
                # Exam Version 1: G (Lose 1 point per step)
                self.score -= 1
                # If gamer has opted to not allow score below 0,
                # Ensure this happens
                if not self.use_neg and self.score < 0:
                    self.score += 1
        print(f'Grace period is at {self.grace_cnt}')


    def check_trap(self, name, value):
        """Use to handle if gamer walks into a trap.

        Exam Version 2: I (Add traps to the board)
        """
        print(f'Oh no, you found a {name}!\n'
              f'You lost {value} points.')
        if self.score >= 10 or self.use_neg:
            self.score += value
        else:
            self.score = 0


    def check_chest(self, g, name, value):
        """Use to handle if gamer finds a chest.

        Exam Version 2: K (Add chests to the board)
        """
        if key_list[0].name in self.inventory:
            self.score += value
            print(f'You found a {name}, '
                  f'+{value} points.')
            # Clear the picked up item on board
            g.clear(self.pos_x, self.pos_y)
            # Add to inventory
            self.inventory.append(name)
            # Remove key from inventory (first occurrence)
            self.inventory.remove(key_list[0].name)
        else:
            print(f'You found a {name}, '
                  f'but sadly you have not picked up any '
                  f'{key_list[0].name}.')
            press_continue()


    def check_key(self, g, name):
        """Use to handle of gamer finds a key.

        Exam Version 2: K (Add keys to the board)
        """
        print(f'You found a {name}!\n'
              f'Can you also find a {chest_list[0].type}?')
        # Clear the picked up item on board
        g.clear(self.pos_x, self.pos_y)
        # Add to inventory
        self.inventory.append(name)
        press_continue()


    def move_happening(self, x, y, g, item):
        """Use to check if something happens when player move.

        Check if an item is picked up, and if so add to
        inventory, plus print info to user.
        Also handles "The Floor is Lava" score reduction,
        unless gamer is on "Grace Period".
        """
        # Exam Version 3: O (When you pick something up, you can
        # move 5 steps without lava damage - Grace Period)
        grace_moves = False
        # Only check if player picked something up, and only
        # move player, if possible to move
        if self.can_move(x, y, g):
            # Check if there is an item on coordinates
            maybe_item = g.get(self.pos_x + x,
                               self.pos_y + y)
            # Move player
            self.move(x, y)
            self.steps += 1

            # Check if there is something to pick up
            if isinstance(maybe_item, item):
                print('')
                # we found something, handle score
                if maybe_item.type == pickup_list[0].type:
                    self.score += maybe_item.value
                    print(f"You found a {maybe_item.name}, "
                          f"+{maybe_item.value} points.")
                    # Clear the picked up item on board
                    g.clear(self.pos_x, self.pos_y)
                    # Exam Version 1: E (Added to inventory)
                    self.inventory.append(maybe_item.name)
                    grace_moves = True
                elif maybe_item.type == chest_list[0].type:
                    self.check_chest(g, maybe_item.name,
                                     maybe_item.value)
                elif maybe_item.type == key_list[0].type:
                    self.check_key(g, maybe_item.name)
                else:
                    self.check_trap(maybe_item.name, maybe_item.value)
                print('')

            # Handle "The Floor is Lava"
            self.handle_lava_score(grace_moves)

            # Handle fertile addition
            if self.steps % 25 == 0:
                fertile_generate(g)
                press_continue()
