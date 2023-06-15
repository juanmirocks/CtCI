from collections import Counter
from typing import Any, List, Sequence, Tuple


def is_one_edit_away(a: Sequence[Any], b: Sequence[Any]) -> bool:
    """
    Complexity:

    * Time: O(min(a, b))
    * Space: O(1) - no extra data structures needed
    """
    if a == b:
        # Return early for trivial case of zero edits, thus equal
        return True

    a_len = len(a)
    b_len = len(b)
    diff_len = a_len - b_len

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
    (("aa", ""), False),
    (("", "aa"), False),
    (("aab", "baa"), False)
]


def test():
    fun = is_one_edit_away

    for input, expected_output in TEST_CASES:
        output = fun(*input)
        assert expected_output == output, f"in[{input}] -> expected_output[{expected_output}] vs. output[{output}]"
