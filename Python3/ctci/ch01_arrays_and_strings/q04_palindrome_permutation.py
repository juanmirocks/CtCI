from collections import Counter


def is_permutation_of_palindrome_1(x: str) -> bool:
    """
    Notes:
    * Observation: A palindrome must be a string where each character is repeated an even number of times (even sequence), or, in addition, has a single character repeated 1 time (odd sequence).
    * Spaces are to be ignored (as per the question definition). That is: "tact coa" is equivalent to "tactcoa".
    * Case is ignored (as per the question assumptions).

    Complexity:
    * Time: O(n)
    * Space: O(n)
    """
    # Add all string's characters to a hash-table-based counter -> time & space: O(n)
    counter = Counter(x)

    one_char_is_odd = False

    # Iterate sorted by counts (DESC). In that way, we can easily
    for elem, count in counter.items():
        if elem == " ":
            # ignore spaces
            continue
        else:
            if (count % 2 == 1):
                if one_char_is_odd:
                    # at least two chars are repeated an odd number of times, so it's not a palindrome
                    return False
                else:
                    one_char_is_odd = True

    return True


# -----------------------------------------------------------------------------

from ctci.__util__ import run_test_cases


TEST_CASES = [
    (("", ), True),
    (("a", ), True),
    (("aa", ), True),
    (("a a", ), True),
    (("a b", ), False),
    (("aaa", ), True),
    (("aab", ), True),
    (("aaaa", ), True),
    (("aaab", ), False),
    (("tact coa", ), True),
    (("tactcoapapa", ), True)
]

def test():
    run_test_cases(TEST_CASES, is_permutation_of_palindrome_1)
