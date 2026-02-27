"""My base user defined functions."""

#####################################################################
#
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
#
#####################################################################


def press_continue():
    """Use to hit enter to continue."""
    input('\nPress Return (Enter) to continue.\n')


def press_exit():
    """Use to hit enter to exit."""
    input('\nPress Return (Enter) to exit.\n')


def press_goback():
    """Use to hit enter to go back."""
    input('\nPress Return (Enter) to go back.\n')


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
