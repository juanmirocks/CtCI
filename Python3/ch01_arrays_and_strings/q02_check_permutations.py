from typing import Sequence, Any

# -----------------------------------------------------------------------------

# Q: Given two strings, write a method to decide if one is a permutation of the other.

def are_mutual_permutations(a: Sequence[Any], b: Sequence[Any]) -> bool:
    """
    Note:
    * If string `a` is a permutation `b`, then `b` is also a permutation of `a`.

    Improvements:
    * Generalize for any sequence type.

    Complexity:
    * Assumption: len(Sequence[Any]) has O(1)

    * Time: O(a + b) ~ O(max(a, b)) -> O(2*a) ~> O(a)
    * Space: O(a + b) ~ O(2*a) ~> O(a)
    """
    if len(a) != len(b): # exit early if this
        return False
    else:
        return set(a) == set(b)

# -----------------------------------------------------------------------------

from itertools import permutations

def test_are_mutual_permutations():
    fun = are_mutual_permutations

    assert True == fun("", "")
    assert True == fun("a", "a")
    assert False == fun("a", "b")

    arbitrary_string = "abc"

    for permutation in (''.join(p) for p in permutations(arbitrary_string)):
        assert True == fun(permutation, arbitrary_string), f"{permutation} vs. {arbitrary_string}"
