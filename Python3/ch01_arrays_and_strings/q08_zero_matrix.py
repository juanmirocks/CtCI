import numpy as np
import numpy.typing as npt
from typing import Any


# Q: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

# Note: the question does not specify whether we should do the operation in-place or not.
# My solution's functions are pure (i.e., not in-place)
# Since the 2 alternatives are the same algorithmically, I disregard the space complexity of creating a copy of the input matrix.


_ZERO: Any = 0


def zero_matrix_1(x: npt.NDArray, zero: Any = _ZERO) -> npt.NDArray:
    """
    Algorithm:
    * First, we collect the rows & columns we need to zero. Second, we zero those rows & columns.

    Optimizations:
    * As soon as we find that a row/column has a zero value, we stop searching for that row/column.
    * An optional `zero` parameter (defaults to `0`/ZERO) can be given.

    Complexity:
    * Time: O(n*m)
    * Space: O(n + m)
    """
    assert len(x.shape) == 2, f"Expect a matrix (i.e. 2 dimensions) -- Received array shape: {x.shape} (array: {x})"

    y = np.copy(x)  # Return a modified copy

    nullify_rows: set[int] = set()
    nullify_cols: set[int] = set()

    for row in range(0, x.shape[0]):
      for col in range(0, x.shape[1]):
         if y[row, col] == zero:
            nullify_rows.add(row)
            nullify_cols.add(col)
            break  # no need to iterate further in the row

    # print(f"{nullify_rows} - {nullify_cols}")

    for row in nullify_rows:
        y[row, :] = zero
        # Alternative:
        #  for col in range(0, x.shape[1]):
        #     y[row, col] = zero

    for col in nullify_cols:
        y[:, col] = zero
        # Alternative:
        # for row in range(0, x.shape[0]):
        #     y[row, col] = zero

    return y


def zero_matrix_2(x: npt.NDArray, zero: Any = _ZERO) -> npt.NDArray:
    """
    Algorithm:
    * As soon as we find a zero element, we zero its entire row to zero and collect the column to zero later. Second, we zero the collected columns.

    Optimizations:
    * As soon as we find that a row/column has a zero value, we stop searching for that row/column.
    * An optional `zero` parameter (defaults to `0`) can be given.

    Complexity:
    * Time: O(n*m)
    * Space: O(m)
    """
    assert len(x.shape) == 2, f"Expect a matrix (i.e. 2 dimensions) -- Received array shape: {x.shape} (array: {x})"

    y = np.copy(x)  # Return a modified copy

    nullify_cols: set[int] = set()

    for row in range(0, x.shape[0]):
      for col in range(0, x.shape[1]):
         if y[row, col] == zero:
            y[row, :] = zero
            nullify_cols.add(col)
            break  # no need to iterate further in the row

    for col in nullify_cols:
        y[:, col] = zero
        # Alternative:
        # for row in range(0, x.shape[0]):
        #     y[row, col] = zero

    return y


# -----------------------------------------------------------------------------

from Python3.__util__ import run_test_cases


TEST_CASES: list[tuple[tuple[npt.NDArray], npt.NDArray]] = [
    # edge case, empty matrix
    ((np.ndarray((0, 0)), ), np.ndarray((0, 0))),
    # basic case, matrix of size 1x1 with cell value 0
    ((np.arange(0, 0 + 1).reshape(1, 1), ), np.arange(0, 0 + 1).reshape(1, 1)),
    # basic case, matrix of size 1x1 with cell value != 0 (e.g., 1)
    ((np.arange(1, 1 + 1).reshape(1, 1), ), np.arange(1, 1 + 1).reshape(1, 1)),
    # Arbitrary case
    ((
      np.array([
      [1, 0, 1],
      [1, 0, 1],
      [1, 1, 1]
      ]), ),
      np.array([
      [0, 0, 0],
      [0, 0, 0],
      [1, 0, 1]
      ])),
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
                   zero_matrix_2,
                   # Provide specific `equal`` function for array/matrix (numpy's equal implementation creates a new element-wise boolean matrix)
                   equal = lambda x, y: np.array_equal(x, y))
