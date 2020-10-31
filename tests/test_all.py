import numpy as np
from rapport import *


def test_my_first_array():
    assert np.allclose(my_first_array(), np.array([0,1,2,3,4]))

def test_my_first_matrix():
    assert np.allclose(my_first_matrix(), np.array([[0,1,2,3,4], [5,6,7,8,9]]))