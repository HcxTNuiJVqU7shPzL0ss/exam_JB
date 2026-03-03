"""Module for tests, src.mypackage directory file: grid.

Exam Version 3 - S --> Use TDD to test some of the functions
(or methods) in the code.
Regarding exam requirements, this file implements:
Version 3 - S
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


# Access constants
from mypackage.constants import WIDTH, HEIGHT
# Access Grid and test file p (player)
from ..src.mypackage.grid import Grid
from .test_player import p


g = Grid(p, WIDTH, HEIGHT)


def test_get__empty():
    """Use to unit test Grid method get.

    Check that a specific position is empty.
    """
    x = p.pos_x
    y = p.pos_y
    expected = g.empty
    actual = g.get(x, y)
    assert actual == expected


def test_set__gamer():
    """Use to unit test Grid method set.

    Place character for gamer on position, check
    that it is returned.
    """
    x = p.pos_x
    y = p.pos_y
    expected = g.gamer
    g.set(x, y, expected)
    actual = g.get(x, y)
    assert actual == expected

    # Reset to empty
    g.set(x, y, g.empty)


def test_set_player__dummy():
    """Use to unit test Grid method set_player.

    Assigns a dummy value, checks this has updated.
    """
    dummy = 'dummy'
    g.set_player(dummy)
    assert g.player == dummy

    # Reset
    g.set_player(p)


def test_clear__to_empty():
    """Use to unit test Grid method clear.

    First, store data and check it is correct.
    Next, clear that data, check that it is now changed
    to represent empty.
    """
    x = p.pos_x
    y = p.pos_y

    # First create non-empty data
    dummy = g.gamer
    g.set(x, y, dummy)
    actual = g.get(x, y)
    assert actual == dummy

    # Clear data, check this has been done
    g.clear(x, y)
    assert g.get(x, y) == g.empty


def test_make_walls__check_walls():
    """Use to unit test Grid method make_walls.

    Build the walls, then check that it has placed
    walls on all correct positions.
    Additionally, check that all other positions
    are marked as empty.
    """
    # Create the walls
    g.make_walls()

    # Save all coordinates containing walls in a set
    walls = set()

    # Outer vertical walls check
    for y in range(HEIGHT):
        assert g.get(0, y) == g.wall
        walls.add((0, y))
        assert g.get(WIDTH - 1, y) == g.wall
        walls.add((WIDTH - 1, y))

    # Outer horizontal walls check
    for x in range(1, WIDTH - 1):
        assert g.get(x, 0) == g.wall
        walls.add((x, 0))
        assert g.get(x, HEIGHT - 1) == g.wall
        walls.add((x, HEIGHT - 1))

    # Inner vertical unstable walls check
    for k in range(3, HEIGHT // 2):
        assert g.get(10, k) == g.unstable_wall
        walls.add((10, k))

    # Inner horizontal unstable walls check
    for m in range(13, WIDTH - 7):
        assert g.get(m, 8) == g.unstable_wall
        walls.add((m, 8))

    # Check all other coordinates are empty
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x, y) not in walls:
                assert g.get(x, y) == g.empty

    # Reset, remove walls, all empty board
    for x in range(WIDTH):
        for y in range(HEIGHT):
            g.clear(x, y)

    # Check all is now empty again
    for x in range(WIDTH):
        for y in range(HEIGHT):
            assert g.get(x, y) == g.empty


def test_get_random_x():
    """Use to unit test Grid method get_random_x.

    Run 100 times, just because.
    """
    start = 1
    for _ in range(start, 101):
        got_x = g.get_random_x()
        assert start <= got_x < WIDTH


def test_get_random_y():
    """Use to unit test Grid method get_random_y.

    Run 100 times, just because.
    """
    start = 1
    for _ in range(start, 101):
        got_y = g.get_random_y()
        assert start <= got_y < HEIGHT


def test_get_empty__true():
    """Use to unit test Grid method get_empty.

    Ensure the position is empty, check that True is returned.
    """
    x = p.pos_x
    y = p.pos_y
    expected = g.empty
    g.set(x, y, expected)
    actual = g.get(x, y)
    assert actual == expected

    # Test is_empty --> True
    actual = g.is_empty(x, y)
    assert actual is True


def test_get_empty__false():
    """Use to unit test Grid method get_empty.

    Ensure the position is not empty,
    check that False is returned.
    """
    x = p.pos_x
    y = p.pos_y
    expected = g.gamer
    g.set(x, y, expected)
    actual = g.get(x, y)
    assert actual == expected

    # Test is_empty --> False
    actual = g.is_empty(x, y)
    assert actual is False

    # Reset to empty
    g.set(x, y, g.empty)

    # Test is_empty --> True
    actual = g.is_empty(x, y)
    assert actual is True
