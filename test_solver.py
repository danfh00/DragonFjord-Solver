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

jan_1st_grid = [[" ", "2", "3", "4", "5", "6", " "],
                ["7", "8", "9", "10", "11", "12", " "],
                [" ", "2", "3", "4", "5", "6", "7"],
                ["8", "9", "10", "11", "12", "13", "14"],
                ["15", "16", "17", "18", "19", "20", "21"],
                ["22", "23", "24", "25", "26", "27", "28"],
                ["29", "30", "31", " ", " ", " ", " "]]

jun_29th_grid = [["1", "2", "3", "4", "5", " ", " "],
                 ["7", "8", "9", "10", "11", "12", " "],
                 ["1", "2", "3", "4", "5", "6", "7"],
                 ["8", "9", "10", "11", "12", "13", "14"],
                 ["15", "16", "17", "18", "19", "20", "21"],
                 ["22", "23", "24", "25", "26", "27", "28"],
                 [" ", "30", "31", " ", " ", " ", " "]]


@pytest.mark.parametrize("test_date, expected_grid", [
    (date(2023, 1, 1), jan_1st_grid),
    (date(2010, 6, 29), jun_29th_grid),
])
@patch("solver.date")
def test_make_todays_grid(mock_date, test_date, expected_grid):
    mock_date.today.return_value = test_date

    assert make_todays_grid() == expected_grid
