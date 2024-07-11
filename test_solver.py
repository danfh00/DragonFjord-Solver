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
