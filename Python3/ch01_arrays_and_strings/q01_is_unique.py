from typing import Sequence, Any

# -----------------------------------------------------------------------------

# Q: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def are_all_unique_elements_1(x: Sequence[Any]) -> bool:
    """
    Improvements:
    * Generalize for any sequence type.

    Complexity:
      * n == len(x)
      * Assumption: len() has time O(1) for both lists & sets

      * Time: O(n)
      * Space: O(n)
    """
    return len(x) == len(set(x))

def are_all_unique_elements_2(x: Sequence[Any]) -> bool:
    """
    Improve base implementation. It exists early as soon as a repeated element is found.
    It does, however, more `__contains__` (`in`) operations, which nonetheless have time O(1).

    Complexity:
      * n == len(x)

      * Time: O(n) -- worst case scenario
      * Space: O(n) -- worst case scenario
    """
    tmp = set()
    for elem in x:
        if elem in tmp:
            return False
        else:
            tmp.add(elem)

    return True

def are_all_unique_elements_3(x: Sequence[Any]) -> bool:
    """
    Without using additional data structures.

    Complexity:
      * n == len(x)

      * Time: O(n^2)
      * Space: O(1)
    """
    for i in range(0, len(x)-1):
        for j in range(i+1, len(x)):
            if x[i] == x[j]:
                return False

    return True


# -----------------------------------------------------------------------------

from Python3.__util__ import run_test_cases


TEST_CASES: list[tuple[tuple[str], bool]] = [
    (("", ), True),
    (("a", ), True),
    (("aa", ), False),
    (("".join(str(i) for i in range(10)), ), True),
    (("".join(str(i) for i in range(10)) + "0", ), False)
]


def test_1():
    run_test_cases(are_all_unique_elements_1, TEST_CASES)

def test_2():
    run_test_cases(are_all_unique_elements_2, TEST_CASES)

def test_3():
    run_test_cases(are_all_unique_elements_3, TEST_CASES)
