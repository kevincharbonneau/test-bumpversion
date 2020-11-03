import pandas as pd
from unittest import main, TestCase
from pandas.testing import assert_frame_equal

from test_bumpversion import make_a_small_dataframe

class TestBump(TestCase):
    def test_make_a_small_dataframe(self):
        df1 = pd.DataFrame({ 'a': [1, 4, 7], 'b': [2, 5, 8], 'c': [3, 6, 9] })
        df2 = make_a_small_dataframe()
        assert_frame_equal(df1, df2)

if __name__ == "__main__":
    main()
