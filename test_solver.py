from unittest.mock import MagicMock, patch
from datetime import date

import pytest

from solver import (
    make_todays_grid,
    can_place,
    place,
    print_grid,
    rotate,
    mirror,
    get_orientations,
    recursion
)


@pytest.mark.parametrize("test_date, expected_grid_fixture", [
    (date(2023, 1, 1), "fake_jan_1_grid"),
    (date(2010, 6, 29), "fake_jun_29_grid"),
])
@patch("solver.date")
def test_make_todays_grid(mock_date, test_date, expected_grid_fixture, request):
    mock_date.today.return_value = test_date
    expected_grid = request.getfixturevalue(expected_grid_fixture)

    assert make_todays_grid() == expected_grid


@pytest.mark.parametrize("in_grid_fixture, block_fixture, x, y, expected_output", [
    ("fake_jan_1_grid", "b_shape", 2, 2, True),
    ("fake_jan_1_grid", "r_shape", 1, 1, True),
    ("fake_jan_1_grid", "b_shape", 0, 0, False),
    ("fake_jun_29_grid", "b_shape", 1, 1, True),
    ("fake_jun_29_grid", "b_shape", 1, 5, False),
    ("fake_jun_29_grid", "r_shape", 4, 3, True),
    ("fake_aug_10_grid", "r_shape", 0, 0, True),
    ("fake_aug_10_grid", "r_shape", 1, 2, True),
    ("fake_aug_10_grid", "b_shape", 10, 10, False),

])
def test_can_place(in_grid_fixture, block_fixture, x, y,  expected_output, request):
    in_grid = request.getfixturevalue(in_grid_fixture)
    block = request.getfixturevalue(block_fixture)

    assert can_place(in_grid, block, x, y) == expected_output
