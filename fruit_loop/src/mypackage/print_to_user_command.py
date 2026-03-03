"""Module for Lesson 02, Exam, print_to_user_command.

Use to handle print to user commands.
Regarding exam requirements, this file implements:
Version 1 - F
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


from mypackage.pickups import (pickup_list, trap_list,
                               chest_list, key_list)

from mypackage.my_base_functions import press_continue, y_or_n

# Access constants
from mypackage.constants import (UP, DOWN, LEFT, RIGHT,
                                 QUIT, EXIT,
                                 INVENTORY, HELP, PRINTINFO,
                                 HIGHLIGHT)


def print_commands(command_check, inventory_list, g):
    """Use to check and handle commands for print status.

    A valid command was entered, as of:
    i: Print user inventory
    h: Help == Print help info
    p: Print board symbol information
    Exam Version 1: F ('i' prints user inventory).
    """
    help_info = (f'\n--------------------------------------\n\n'
                 f'Your available commands are\n\n'
                 f'{UP.upper()}: Move up\n'
                 f'{DOWN.upper()}: Move down\n'
                 f'{LEFT.upper()}: Move left\n'
                 f'{RIGHT.upper()}: Move right\n\n'
                 f'{INVENTORY.upper()}: Print inventory\n'
                 f'{HELP.upper()}: Display commands\n\n'
                 f'{PRINTINFO.upper()}: Display board symbol '
                 f'information\n\n'
                 f'{QUIT.upper()}: Quit (quit game)\n'
                 f'{EXIT.upper()}: Exit (exit game)\n'
                 f'\n--------------------------------------')
    if command_check == INVENTORY:  # print inventory
        if not inventory_list:
            print('\nThe inventory is empty.')
        else:
            print('\nInventory')
            for i, item in enumerate(inventory_list):
                print(f'{i + 1}: {item}')
    elif command_check == HELP: # print help
        print(help_info)
    elif command_check == PRINTINFO: # Print board symbol info
        print_symbols(g)

    press_continue()


def print_symbols(g):
    """Use to print information about board symbols."""
    print(f'\nYou are the player on the board, starting in the '
          f'middle, look for your marker:'
          f'{HIGHLIGHT + g.gamer + HIGHLIGHT}\n\n'
          f'Around the edges are impassable walls, signified '
          f'by the following:'
          f'{HIGHLIGHT + g.wall + HIGHLIGHT}\n\n'
          f'There are a few internal walls, which cannot be '
          f'passed, unless you have found a pickaxe. These '
          f'internal walls looks like this:'
          f'{HIGHLIGHT + g.unstable_wall + HIGHLIGHT}\n\n'
          f'The goal of this exciting game is to pick up things '
          f'from the board, items can be found where you see:'
          f'{HIGHLIGHT + pickup_list[0].symbol + HIGHLIGHT}\n\n'
          f'There are chests on the board, marked with'
          f'{HIGHLIGHT + chest_list[0].symbol + HIGHLIGHT.rstrip()},'
          f' to be able to pick up a chest, you '
          f'first need a key, these are marked with'
          f'{HIGHLIGHT + key_list[0].symbol + HIGHLIGHT}\n\n'
          f'Try to avoid the traps, marked with'
          f'{HIGHLIGHT + trap_list[0].symbol + HIGHLIGHT}')


def print_welcome_info(g):
    """Use to print initial welcome information.

    Also asks user if negative values are to be used, or not.
    """
    # Ask if to allow negative values
    ask_negative = ('Do you wish to allow negative values, '
                    '(y)es or (n)o: ')

    # Print welcome message and info
    print('\nWelcome to an exciting game: Fruit Loop!')
    print_commands(HELP, [], g)

    print(f'For help with commands, please select "{HELP.upper()}" '
          f'as your command.')
    press_continue()
    print(f'Due to "The Floor is Lava", you will lose one (-1) '
          f'point for each movement.\n'
          f'Also, traps will have you lose {trap_list[0].value} '
          f'points, they are marked on the map with: '
          f'{trap_list[0]}\n'
          f'Either 0 can be the lowest score, or you can have '
          f'negative score.')
    press_continue()

    check_neg = y_or_n(ask_negative)

    if check_neg == 'y':
        print('\nOK, negative values are possible!')
        return True
    print('\nOK, 0 will be the lowest value for score.')
    return False
