from collections import Counter
from typing import Any, Callable, List, Sequence, Tuple


def is_one_edit_away_1(a: Sequence[Any], b: Sequence[Any]) -> bool:
    """
    Complexity:

    * Time: O(min(a, b))
    * Space: O(1) - ASSUMING THAT PYTHON SEQUENCE SLICING DOES NOT CREATE COPIES -- WARNING this might depends on the datastructures, specially for strings.
    """
    if a == b:
        # Return early for trivial case of zero edits, thus equal
        return True

    diff_len = len(a) - len(b)

    if diff_len < -1 or diff_len > 1:
        # Return early for trivial case of having a length different bigger than abs(1)
        return False

    if diff_len == 1:
        # swap to make sure a is the shortest sequence
        a, b = b, a

    for i in range(0, len(a)):
        if a[i] == b[i]:
            continue
        else:
            # We found the first different elem
            if diff_len == 0:
                # if same length, the rest of both sequences must be equal
                return a[i+1:] == b[i+1:]
            else:
                # else, the rest from the shortest sequence (including the current i elem ) must equal the rest of the longest sequence
                return a[i:] == b[i+1:]

    return True


def is_one_edit_away_2(a: Sequence[Any], b: Sequence[Any]) -> bool:
    """
    Alternative avoiding python sequence/string slicing altogether.

    Complexity:

    * Time: O(min(a, b))
    * Space: O(1)
    """
    if a == b:
        # Return early for trivial case of zero edits, thus equal
        return True

    diff_len = len(a) - len(b)

    if diff_len < -1 or diff_len > 1:
        # Return early for trivial case of having a length different bigger than abs(1)
        return False

    if diff_len == 1:
        # swap to make sure a is the shortest sequence
        a, b = b, a

    i, j = 0, 0
    found_diff_elem = False

    while i < len(a):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            if found_diff_elem:
                return False
            else:
                # We found the first different elem
                found_diff_elem = True

                if diff_len == 0:
                    # if same length, the rest of both sequences must be equal, i.e., a[i+1:] == b[i+1:], where j==i
                    i += 1
                    j += 1
                else:
                    # else, the rest from the shortest sequence (incl. the current i elem) must equal the rest of the longest sequence, i.e. a[i:] == b[i+1:], where j==i+1
                    j += 1

    return True


# -----------------------------------------------------------------------------


TEST_CASES: List[Tuple[Tuple[str, str], bool]] = [
    (("pale", "ple"), True),
    (("pales", "pale"), True),
    (("pale", "bale"), True),
    (("pale", "bake"), False),
    #
    (("", ""), True),
    (("a", ""), True),
    (("", "a"), True),
    (("a", "a"), True),
    (("aa", ""), False),
    (("", "aa"), False),
    (("aab", "baa"), False),
    (("pale", "pasle"), True),
    (("pale", "pales"), True)
]


def _test(fun: Callable[[Sequence[Any], Sequence[Any]], bool]):
    for input, expected_output in TEST_CASES:
        output = fun(*input)
        assert expected_output == output, f"in[{input}] -> expected_output[{expected_output}] vs. output[{output}]"


def test_1():
    _test(is_one_edit_away_1)


def test_2():
    _test(is_one_edit_away_2)
