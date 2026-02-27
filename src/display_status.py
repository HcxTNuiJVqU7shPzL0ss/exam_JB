"""Module for Lesson 02, Exam.

View to print game status.
Moved function to player.
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


def print_status(game_grid, score):
    """Use to display the board grid and number of points."""
    print(f'>>> {emoji.emojize(':strawberry:')} '
          f'Fruit Loop {emoji.emojize(':watermelon:')} <<<')
    print('--------------------------------------\n')
    print(f'You have {score} points.\n')
    print(game_grid)
