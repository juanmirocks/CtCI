def is_substring(x: str, y: str) -> bool:
    # Name the "is_substring" function for clarity
    return x in y


def is_rotation_1(s1: str, s2: str) -> bool:
    """
    Test if s2 is a rotation of s1 (or viceversa).

    Optimizations:
    * Two strings can only be a rotation of each other iff they have the same length -> we return early False for strings with diff. length and, accordingly, assume length n for both strings.

    Complexity:
    * Time: O(n) - assuming `is_substring` runs in time O(n) (i.e., O(len(y)))
    * Space: O(n)
    """
    if len(s1) != len(s2):
        return False

    tmp = s1 + s1  # space: 2*n -- A StringBuilder / io.StringIO should not be necessary for this
    return is_substring(s2, tmp)  # time: 2*n


# -----------------------------------------------------------------------------

from ctci.__util__ import run_test_cases

from collections import deque
import random
import string

def rotate(x: str, n: int|None = None) -> str:
    _n: int = random.randint(0, len(x)) if (n is None) else n

    items = deque(x)
    items.rotate(_n)

    return "".join(items)


TEST_CASES = [
    (("", ""), True),
    (("a", ""), False),
    (("a", "a"), True),
    (("a", "b"), False),
    (("ab", "ba"), True),
    (("ba", "ab"), True),  # The order does not matter
    (("erbottlewat", "waterbottle"), True),
    (("waterbottle", "erbottlewat"), True),  # The order does not matter
] + [
    # random generation of strings and its rotations --> they must all be tested to true
    ((x, rotate(x)), True)
    for x in ("".join(random.choices(string.ascii_letters, k=random.randint(10, 20))) for _ in range(100))
]


def test():
    run_test_cases(
        TEST_CASES,
        is_rotation_1
    )
