"""
Test goes here

"""

from main import PDdescribe
import pandas as pd


def test_desc():
    """Function calling PDdescribe"""
    # Call the function to be tested
    result = PDdescribe('nba.csv')
    assert result.shape == (8, 4)
