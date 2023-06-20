import numpy as np
import numpy.typing as npt


# Q: Rotate matrix (n x n) 90 degrees.
#
# The question does not specify the direction (clockwise vs. counterclockwise).
# I assume counterclockwise direction, which is the standard for matrix rotation.


def rotate_matrix_1(x: npt.NDArray) -> npt.NDArray:
    """
    Rotate matrix 90% (counterclockwise) in a new returned matrix.

    Complexity:
    * Time: O(n**2)
    * Space: O(n**2)
    """
    y: npt.NDArray = np.ndarray(x.shape, x.dtype)

    assert (len(x.shape) == 2) and (x.shape[0] == x.shape[1]), f"Expect square matrix of size nxn -- Received array shape: {x.shape} (array: {x})"
    n = x.shape[0]

    for i in range(0, n):
        for j in range(0, n):
            # Rule: (i, j) -> (n-1-j, i)
            y[n - 1 - j, i] = x[i, j]

    return y


# -----------------------------------------------------------------------------

from Python3.__util__ import run_test_cases


_TEST_UP_TO_N = 10

TEST_CASES = list(
     map(lambda x: ((x, ), np.rot90(x)),
                      (np.arange(1, n**2 + 1).reshape(n, n) for n in range(1, _TEST_UP_TO_N+1))))


def test():
    run_test_cases(TEST_CASES,
                   rotate_matrix_1,
                   # Provide specific `equal`` function for array/matrix (numpy's equal implementation creates a new element-wise boolean matrix)
                   equal = lambda x, y: np.array_equal(x, y))
