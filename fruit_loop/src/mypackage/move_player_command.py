"""Module for Lesson 02, Exam.

Use to handle move player commands.
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


def move_commands(command_check, player_active, g_active):
    """Use to check and handle commands for movement.

    A valid command was entered, as of:
    d: Move player to the right
    a: Move player to the left
    w: Move player up
    s: Move player down
    Can only move if there is no wall in the way.
    If attempting to move through a wall, it is not
    allowed.
    # Exam Version 1: B (Player can move in all 4 directions).
    """
    # Ensure movement will only happen in one direction, x or y
    x = 0
    y = 0
    # Check if allowed to move, or a wall
    if not player_active.can_move(x, y, g_active):
        x = 0
        y = 0
    # Move happens below, depending on command
    else:
        if command_check == 'd':  # move right
            x = 1
        elif command_check == 'a': # move left
            x = -1
        elif command_check == 'w': # move up
            y = -1
        elif command_check == 's': # move down
            y = 1

    return [x, y]
