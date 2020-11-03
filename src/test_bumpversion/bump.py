import numpy as np
import pandas as pd


def make_a_small_dataframe():
    return pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
