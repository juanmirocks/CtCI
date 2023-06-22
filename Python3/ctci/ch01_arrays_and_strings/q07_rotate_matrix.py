import numpy as np
import numpy.typing as npt


# Q: Rotate matrix (n x n) 90 degrees.
#
# The question does not specify the direction (clockwise vs. counterclockwise).
# I assume counterclockwise direction, which is the standard for matrix rotation.
# Note: The book's solution does the rotation clockwise.


def rotate_matrix_1(x: npt.NDArray) -> npt.NDArray:
    """
    Rotate matrix 90° (counterclockwise) in a new returned matrix.

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


def rotate_matrix_2(x: npt.NDArray) -> npt.NDArray:
    """
    Rotate matrix 90° (counterclockwise) IN-PLACE (mutable/destructive function).

    Observations:
    * Rotating a (quadratic) matrix can be seen as rotating "ring" by "ring" (layers), from the outer rings to the inner rings of the matrix.
    * Elements can be changed in a loop of length 4 (the last element change closes the loop).
    * We can derive all coordinates of 4 changed elements from the first element's coordinates.
    * Matrices' "center" are never changed (i.e., for matrices with an odd n).

    Complexity:
    * Time: O(n**2)
    * Space: O(1)
    """
    assert (len(x.shape) == 2) and (x.shape[0] == x.shape[1]), f"Expect square matrix of size nxn -- Received array shape: {x.shape} (array: {x})"
    n = x.shape[0]

    for i in range(0, n//2):  # Note: we only have n//2 rings
        for j in range(i, n-1-i):  # Note: we don't go to the last column of the ring, since it's been changed already
            # print(f"({i}, {j})")
            # Loop of 4 changes
            x[i, j], x[n-1-j, i], x[n-1-i, n-1-j], x[j, n-1-i] = x[j, n-1-i], x[i, j], x[n-1-j, i], x[n-1-i, n-1-j]

    return x


# -----------------------------------------------------------------------------

from ctci.__util__ import run_test_cases


_TEST_FROM_TO_N = (0, 20)

TEST_CASES = list(
     map(lambda x: ((x, ), np.copy(np.rot90(x))),  # Copy/clone the expected output given by numpy's rot90, since it returns a view, which is the difficult to use when testing the mutable version
                      (np.arange(1, n**2 + 1).reshape(n, n) for n in range(_TEST_FROM_TO_N[0], _TEST_FROM_TO_N[1]+1))))


def test():
    run_test_cases(TEST_CASES,
                   rotate_matrix_1,
                   rotate_matrix_2,
                   # Provide specific `equal`` function for array/matrix (numpy's equal implementation creates a new element-wise boolean matrix)
                   equal = lambda x, y: np.array_equal(x, y))
