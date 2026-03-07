"""Module for Lesson 02, Exam, player.

Player view.
This contains the Class which creates the player.
Also handles interaction, like movement.
Regarding exam requirements, this file implements:
Version 1 - C
Version 1 - E
Version 1 - G
Version 2 - I
Version 2 - J
Version 2 - K
Version 3 - O
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


from mypackage.pickups import (pickup_list, chest_list, key_list,
                               pickaxe_list, fertile_generate,
                               fertile)

from mypackage.my_base_functions import press_continue

# Access constants
from mypackage.constants import (GRACE_START, STEPS_START,
                                 SCORE_START, NEG_START,
                                 GRACE_SET)


class Player:
    """Use for Class Player."""

    grace_cnt = GRACE_START
    steps = STEPS_START

    def __init__(self, x, y):
        """Use to create an object of Player.

        Initialize the attributes of a Player object when the object
        is formed.
        Constructor (initializer) automatically called when
        creating a new instance of this class.
        """
        self.pos_x = x
        self.pos_y = y
        self.score = SCORE_START
        self.inventory = []
        self.use_neg = NEG_START


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


    def can_move(self, x, y, g):
        """Use to check that you can move.

        Exam Version 1: C (Player not allowed
        to walk through walls).
        """
        check_x = self.pos_x + x
        check_y = self.pos_y + y
        check_wall = g.get(check_x, check_y)

        wall_print = '\nNot allowed to walk through walls!'
        breach_print = (f'\nYou have breached an unstable wall!\n'
                        f'Your {pickaxe_list[0].name} has been '
                        f'used.')

        # Return True if no wall is found
        if check_wall in (g.wall, g.unstable_wall):
            # Either no pickaxe found, or impassable wall
            if (pickaxe_list[0].name not in self.inventory or
                    check_wall == g.wall):
                print(wall_print)
                press_continue()
                return False

            # Pickaxe found and move to unstable wall
            # Breach and move
            print(breach_print)
            # Clear the breached wall on board
            g.clear(check_x, check_y)
            # Remove pickaxe from inventory (first occurrence)
            self.inventory.remove(pickaxe_list[0].name)
            press_continue()
            return True

        return True


    def handle_lava_score(self, grace):
        """Use to handle score for The Floor is Lava.

        If on "Grace Period", does not lose points.
        Exam Version 1: G (Lose 1 point per step)
        """
        if grace:
            # Found an item, add grace period of 5
            self.grace_cnt = GRACE_SET
        else:
            if self.grace_cnt > 0:
                self.grace_cnt -= 1
            else:
                # Handle "The Floor is Lava"
                # Exam Version 1: G (Lose 1 point per step)
                self.score -= 1
                # If gamer has opted to not allow score below 0,
                # ensure this happens
                if not self.use_neg and self.score < 0:
                    self.score += 1
        print(f'\nGrace period is at {self.grace_cnt}')


    def check_trap(self, name, value):
        """Use to handle if gamer walks into a trap.

        Exam Version 2: I (Add traps to the board)
        """
        print(f'Oh no, you found a {name}!\n'
              f'You lost {value} points.')
        if self.score >= abs(value) or self.use_neg:
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


    def check_key_pickaxe(self, g, name):
        """Use to handle if gamer finds a key or a pickaxe.

        Exam Version 2: K (Add keys to the board)
        Exam Version 2: J (Add pickaxes to the board)
        """
        print(f'You found a {name}!')
        if name == key_list[0].name:
            print(f'Can you also find a {chest_list[0].type}?')
        else:
            print('You can now breach one (1) unstable wall.')

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
        Exam Version 1: E (Added to inventory)
        Exam Version 3: O (When you pick something up, you can
        move 5 steps without lava damage - Grace Period)
        """
        # Exam Version 3: O (When you pick something up, you can
        # move 5 steps without lava damage - Grace Period)
        grace_moves = False

        # Check if there is an item on coordinates
        maybe_item = g.get(self.pos_x + x,
                           self.pos_y + y)

        # Move player, if coordinates not (0,0)
        if not (x == 0 and y == 0):
            self.move(x, y)
            self.steps += 1

            # Check if there is something to pick up
            if isinstance(maybe_item, item):
                print('')
                # we found something, handle score
                if maybe_item.type in (pickup_list[0].type,
                                       fertile[0].type):
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
                elif maybe_item.type in (key_list[0].type,
                                         pickaxe_list[0].type):
                    self.check_key_pickaxe(g, maybe_item.name)
                else:
                    self.check_trap(maybe_item.name, maybe_item.value)
                print('')

            # Handle "The Floor is Lava"
            self.handle_lava_score(grace_moves)

            # Handle fertile addition every 25th step
            if self.steps % 25 == 0:
                fertile_generate(g)
                press_continue()
