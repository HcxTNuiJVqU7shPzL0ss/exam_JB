"""My base user defined functions."""

#####################################################################
#
# Copyright 2025-2026 gnoff
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
#
#####################################################################


import sys


def press_continue():
    """Use to hit enter to continue."""
    input('\nPress Return (Enter) to continue.\n')


def press_exit():
    """Use to hit enter to exit."""
    input('\nPress Return (Enter) to exit.\n')


def press_goback():
    """Use to hit enter to go back."""
    input('\nPress Return (Enter) to go back.\n')


def enter_int_range(input_string, low, high, any_range):
    """Use to get integer input (with range)."""
    while True:
        if any_range:
            print('\nRange is between: ', low, ' and ', high,
                  '.\n', sep='')
        int_s = input(input_string)
        try:
            int_i = int(int_s)
            if any_range:
                if low <= int_i <= high:
                    return int_i
                print('\nIncorrect range, try again.')
                press_goback()
                continue
            return int_i
        except ValueError:
            print('\nPlease use an integer!')
            press_goback()
            continue


def enter_int(input_string):
    """Use to get integer input (no range)."""
    while True:
        int_s = input(input_string)
        try:
            int_i = int(int_s)
            return int_i
        except ValueError:
            print('\nPlease use an integer!')
            press_goback()
            continue


def enter_string(input_string):
    """Use to prompt user for an input string."""
    while True:
        user_string = input(input_string)
        try:
            if len(user_string) > 0:
                return user_string
            print('\nNot enough characters, try again!')
            press_goback()
        except ValueError:
            print('\nPlease try again.')
            press_goback()
            continue


def enter_float(input_string):
    """Use to prompt user for a float input."""
    while True:
        float_s = input(input_string)
        try:
            float_f = float(float_s)
            return float_f
        except ValueError:
            print('\nPlease use a float!')
            press_goback()
            continue


def ask_y_or_n():
    """Use to ask if yes or no.

    Specifically with a pre-decided question.
    """
    while True:
        check_ans = input('Did it match/work, (y) yes or (n) no: ')
        yes_check = ('y', '(y)', '(y) yes', 'yes')
        no_check = ('n', '(n)', '(n) no', 'no')
        try:
            if check_ans.lower() in yes_check:
                print('\nAwesome!\n')
                break
            if check_ans.lower() in no_check:
                print('\nNope, exit')
                press_exit()
                sys.exit()
        except ValueError:
            print('\nPlease retry.\n')
            press_goback()
            continue


def y_or_n(in_string):
    """Use to ask if yes or no.

    Depends on incoming string what is asked.
    """
    while True:
        check_ans = input(in_string)
        yes_check = ('y', '(y)', '(y) yes', 'yes', 'y(es)', '(y)es')
        no_check = ('n', '(n)', '(n) no', 'no', 'n(o)', '(n)o')
        try:
            if check_ans.lower() in yes_check:
                return 'y'
            if check_ans.lower() in no_check:
                return 'n'
        except ValueError:
            print('\nPlease retry.\n')
            press_goback()
            continue
