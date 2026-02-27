"""Module for Lesson 02, Exam.

Main view.
This is the file from which you run the game.
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


# pylint: disable=import-error
from grid import Grid
from player import Player

import pickups

# Use to handle player movement
from move_player_command import move_commands

# Use for printing inventory and help info
from print_to_user_command import print_commands, print_welcome_info
# pylint: enable=import-error


# Note that these functions are located in a different
# directory
from my_funct_dir.my_base_functions import press_continue, press_exit


def main():
    """Use as module for Main.

    Exam: The Game "Fruit Loop".
    """
    # Set the width of the board
    width = 37
    # Set the height of the board
    height = 13

    # Exam Version 1: A (Player starts in middle of board)
    # Set the player start position in the middle of the board
    player = Player(x = width // 2, y = height // 2)

    # Easier access to inventory (empty at start)
    inventory = player.inventory

    # Create board
    g = Grid(player, width, height)
    # Place player on the board
    g.set_player(player)
    # Create walls around the board + some inside
    g.make_walls()
    # Randomly create and place items on board
    pickups.randomize(g)


    # List of move player commands
    player_move_commands = ['a', 's', 'd', 'w']

    # List of exit commands
    exit_commands = ['q', 'x']

    # List of print info commands
    print_info_commands = ['i', 'h', 'p']

    # Default value for command
    command = 'a'

    # Print welcome info and check if to use negative values
    # use_neg is True if to allow below 0 score, else False
    use_neg = print_welcome_info(g)
    player.set_lava_handling(use_neg)
    press_continue()


    # Loop until user enters Q or X
    while command not in exit_commands:
        # Print the board and current score
        player.print_status(g)

        # Ask user for command
        command = input('Enter your command (one character only), '
                        'then press enter to continue: ')
        # Lower case only, first character only
        command = command.casefold()[:1]

        # Check if any commands as of: W, A, S, D
        if command in player_move_commands:
            # Get coordinates based on command, if possible to move
            coordinates = move_commands(command, player, g)
            x_c = coordinates[0]
            y_c = coordinates[1]

            # Handle any movement and update score
            player.move_happening(x_c, y_c, g, pickups.Item)
        # Check if command as of: I, H, P
        elif command in print_info_commands:
            print_commands(command, inventory, g)
        elif command not in exit_commands:
            print('\nThat command is not known.\n'
                  'Please use "h" to check what the valid commands are.')
            press_continue()


    # When exiting the while loop, we end up here: Game Over!
    print(f'\nThank you for playing Fruit Loop!\n'
          f'You ended with {player.score} points.\n'
          f'In total you used {player.steps} moves.')
    press_exit()


if __name__ == "__main__":
    main()
