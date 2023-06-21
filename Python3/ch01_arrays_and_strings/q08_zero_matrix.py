import numpy as np
import numpy.typing as npt


# Q: Write an algorithm such tat if an element in an MxN matrix is 0, its entire row and column are set to 0.


def zero_matrix_1(x: npt.NDArray) -> npt.NDArray:
    return x


# -----------------------------------------------------------------------------

from Python3.__util__ import run_test_cases


TEST_CASES: list[tuple[tuple[npt.NDArray], npt.NDArray]] = [
    # edge case, empty matrix
    ((np.ndarray((0, 0)), ), np.ndarray((0, 0))),
    # basic case, matrix of size 1x1 with cell value 0
    ((np.arange(0, 0 + 1).reshape(1, 1), ), np.arange(0, 0 + 1).reshape(1, 1)),
    # basic case, matrix of size 1x1 with cell value != 0 (esp. 1)
    ((np.arange(1, 1 + 1).reshape(1, 1), ), np.arange(1, 1 + 1).reshape(1, 1)),
    # Arbitrary case
    ((
      np.array([
      [1, 1, 1, 1, 1],
      [1, 0, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 0]
      ]), ),
      np.array([
      [1, 0, 1, 1, 0],
      [0, 0, 0, 0, 0],
      [1, 0, 1, 1, 0],
      [0, 0, 0, 0, 0]
      ])),
    # Arbitrary case
    ((
      np.array([
      [0, 1, 1, 1, 1],
      [1, 0, 1, 1, 1],
      [1, 1, 0, 1, 1],
      [1, 1, 1, 0, 1],
      [1, 1, 1, 1, 1],
      ]), ),
      np.array([
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1]
      ])),
]


def test():
    run_test_cases(TEST_CASES,
                   zero_matrix_1,
                   # Provide specific `equal`` function for array/matrix (numpy's equal implementation creates a new element-wise boolean matrix)
                   equal = lambda x, y: np.array_equal(x, y))
