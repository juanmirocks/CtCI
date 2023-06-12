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

from typing import Callable

TEST_CASES = [
    (True, ""),
    (True, "a"),
    (False, "aa"),
    (True, "".join(str(i) for i in range(10))),
    (False, "".join(str(i) for i in range(10)) + "0")
]

def _test(fun: Callable[[Sequence[Any]], bool]):
    for expected, test_case in TEST_CASES:
      assert expected == fun(test_case), f"case: {test_case}"


def test_are_all_unique_elements_1():
    _test(are_all_unique_elements_1)

def test_are_all_unique_elements_2():
    _test(are_all_unique_elements_2)

def test_are_all_unique_elements_3():
    _test(are_all_unique_elements_3)
