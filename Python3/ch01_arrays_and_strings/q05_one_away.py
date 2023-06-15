from collections import Counter
from typing import Any, List, Sequence, Tuple


def is_one_elem_away(a: Sequence[Any], b: Sequence[Any]) -> bool:
    """
    Complexity:

    * Time: O(a + b)
    * Space: O(a + b)
    """
    if a == b:
        # Return early for trivial case (zero edits, thus equal)
        return True

    a_counter = Counter(a) # linear time & space on a's length
    b_counter = Counter(b) # linear time & space on b's length

    is_one_count_away = False

    if len(b_counter) < len(a_counter):
        # Swap, so that we iterate only over the counter with the least number of keys, i.e., time O(min(a, b))
        a_counter, b_counter = b_counter, a_counter

    for a_elem, a_elem_count in a_counter.items():
        b_elem_count = b_counter.get(a_elem, None)
        if b_elem_count is None:
            if is_one_count_away or a_elem_count > 1:
                return False
            else:
                is_one_count_away = True
        else:
            diff = abs(a_elem_count - b_elem_count)
            match diff:
                case 0:
                    pass
                case 1:
                    if is_one_count_away:
                        return False
                    else:
                        is_one_count_away = True
                case _:
                    return False

            del b_counter[a_elem]

    # Now we need to verify that either b is empty or otherwise it contains a single element with a count of 1
    match len(b_counter):
        case 0:
            return True
        case 1:
            _, b_last_count = b_counter.popitem()
            return (b_last_count == 1)
        case _:
            return False


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
    (("", "aa"), False)
]


def test():
    fun = is_one_elem_away

    for input, expected_output in TEST_CASES:
        output = fun(*input)
        assert expected_output == output, f"in[{input}] -> expected_output[{expected_output}] vs. output[{output}]"
