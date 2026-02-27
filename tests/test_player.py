"""Module for tests, src directory file: player.

Exam Version 3 - S --> Use TDD to test some of the functions
(or methods) in the code.
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
from ..src.player import Player
# pylint: enable=import-error


X_START = 0
Y_START = 0
GRACE_START = 0
STEPS_START = 0
SCORE_START = 0
NEG_START = False

p = Player(x=X_START, y=Y_START) # Supply x and y


def test_print_status__dummy_values(capsys):
    """Use to run simple test of print_status.

    Use capsys to capture stdout/stderr output.
    Test Player method "print_status"
    """
    p.print_status(game_grid='dummy') # Dummy for print

    captured = capsys.readouterr()
    output = captured.out

    # Test that first print happens
    assert 'Fruit Loop' in output
    # Second print
    assert '------------' in output
    # Two asserts for the third print
    assert f'You have {SCORE_START} points' in output
    assert f'You have used {STEPS_START} moves' in output
    # Test fourth / last (dummy) print
    assert 'dummy' in output


def test_lava_handling__false():
    """Use to check setting negative values to False.

    Test Player method "lava_handling"
    """
    expected = NEG_START
    p.set_lava_handling(lava_neg=expected)
    actual = p.use_neg
    assert actual == expected


def test_lava_handling__true():
    """Use to check setting negative values to True.

    Test Player method "lava_handling"
    """
    expected = not NEG_START
    p.set_lava_handling(lava_neg=expected)
    actual = p.use_neg
    assert actual is expected

    # Reset to default
    p.set_lava_handling(lava_neg=NEG_START)
    actual = p.use_neg
    assert actual is NEG_START


def test_move__x1_y2():
    """Use to simulate move to x=1 and y=2.

    Test Player method "move"
    """
    # Check default is at 0 for both
    assert p.pos_x == X_START
    assert p.pos_y == Y_START

    # Change coordinates
    expected_x = 1
    expected_y = 2
    p.move(dx=expected_x, dy=expected_y)
    # Check that change happened
    assert p.pos_x == expected_x
    assert p.pos_y == expected_y

    # Reset to default
    p.move(dx=-expected_x, dy=-expected_y)
    # Check that change happened
    assert p.pos_x == X_START
    assert p.pos_y == Y_START


def test_handle_lava_score__no_grace_no_negative_default(capsys):
    """Use to test Player metod handle_lava_score.

    No grace period.
    Negative values are not allowed.
    Default "start" values.
    """
    # Check default
    assert p.grace_cnt == GRACE_START
    assert p.score == SCORE_START
    assert p.use_neg is NEG_START

    # Call the method without finding an item
    p.handle_lava_score(grace=NEG_START)

    # Check grace_cnt and score still at 0
    assert p.grace_cnt == GRACE_START
    assert p.score == SCORE_START

    captured = capsys.readouterr()
    output = captured.out

    # Test that print happens
    assert f'is at {GRACE_START}' in output

    # With grace_cnt at 0, negative not allowed,
    # check that score does not decrease
    for i in range(1, 11):
        p.handle_lava_score(grace=False)
        assert p.score == SCORE_START


def test_handle_lava_score__yes_grace_yes_negative_fake_score(capsys):
    """Use to test Player method handle_lava_score.

    Yes, grace period.
    Yes, negative values allowed.
    Fake score.
    """
    grace_set = 5
    fake_score_set = 1

    # Call the method when finding an item
    p.handle_lava_score(grace=True)

    # Check that grace_cnt is now as set
    assert p.grace_cnt == grace_set

    captured = capsys.readouterr()
    output = captured.out

    # Test that print happens
    assert f'is at {grace_set}' in output


    # Change to allow negative values, and fake a score
    p.use_neg = True
    p.score = fake_score_set

    for i in range(1, 6):
        # Call the method without finding an item
        p.handle_lava_score(grace=False)

        # Check that grace_cnt decreases
        assert p.grace_cnt == grace_set - i
        # Check that score does not decrease
        assert p.score == fake_score_set

        captured = capsys.readouterr()
        output = captured.out

        # Test that print happens
        assert f'is at {p.grace_cnt}' in output

    for i in range(1, 3):
        # With grace_cnt now at 0, check that score decrease
        p.handle_lava_score(grace=False)
        assert p.score == fake_score_set - i

    # Back to default
    p.score = SCORE_START
    p.grace_cnt = GRACE_START
    p.use_neg = NEG_START


def test_check_trap__dummy_no_points_no_negative(capsys):
    """Use to run simple test of Player method check_trap.

    Use capsys to capture stdout/stderr output.
    No score, negative points not allowed.
    Check that print happens and score is not changed.
    """
    # Check that default score and use_neg is set
    assert p.score == SCORE_START
    assert p.use_neg == NEG_START

    # Set dummy for test
    dummy_name = 'trap'
    dummy_value = -10
    p.check_trap(name=dummy_name, value=dummy_value)

    captured = capsys.readouterr()
    output = captured.out

    # Test that first print happens
    assert f'found a {dummy_name}' in output
    # Second print
    assert f'lost {dummy_value} points' in output

    # Check that score did not change
    assert p.score == SCORE_START


def test_check_trap__dummy_with_points_no_negative():
    """Use to run simple test of Player method check_trap.

    With fake score, though negative points not allowed.
    Check that print happens and score is handled correct.
    """
    # Check that default score and use_neg is set
    assert p.score == SCORE_START
    assert p.use_neg == NEG_START

    # Set dummy for test, score less than 10
    dummy_score = 5
    dummy_name = 'trap'
    dummy_value = -10

    p.score = dummy_score
    assert p.score == dummy_score

    p.check_trap(name=dummy_name, value=dummy_value)

    # Check that score is now 0
    assert p.score == SCORE_START


    # Set again, with score more than 10
    dummy_score = 11

    p.score = dummy_score
    assert p.score == dummy_score

    p.check_trap(name=dummy_name, value=dummy_value)

    # Check that score decreased by trap (dummy) value
    assert p.score == dummy_score + dummy_value


    # Reset score to start value
    p.score = SCORE_START
    assert p.score == SCORE_START
