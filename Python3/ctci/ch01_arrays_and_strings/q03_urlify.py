import urllib.parse
from typing import MutableSequence

# -----------------------------------------------------------------------------

#
# Define the replacements as constants to generalize the algorithm.
#
class Replacement:
    def __init__(self, old: str, new: str):
        assert len(old) == 1, f"Old must be a single character: {old}"

        self.old = old
        self.new = new
        self.new_len = len(self.new)
        self.new_len_minus_1 = self.new_len - 1


    def __repr__(self) -> str:
        return f"Replacement({self.old}->{self.new})--{self.new_len_minus_1}"


ORIGINAL_REPLACEMENT = Replacement(" ", "%20")

REPLACEMENTS = [
    ORIGINAL_REPLACEMENT,
    # ... can add more
]

REPLACEMENTS_DICT: dict[str, Replacement] = {repl.old: repl for repl in REPLACEMENTS}

# -----------------------------------------------------------------------------

def urlify_1(x: str, l: int) -> str:
   return urlify_1_pure(x[0:l])

def urlify_1_pure(x: str) -> str:
    """Pythonic way to escape/encode a string to form a URL."""
    return urllib.parse.quote(x)


def urlify_2(x: str, l: int) -> str:
    return urlify_2_pure(x[0:l])

def urlify_2_pure(x: str) -> str:
    # Here we only do one replacement (the one asked for originally).
    # Otherwise, we likely have to improve the algorithm, since Python always creates new (immutable) strings,
    # which would result in a practical time & space complexity of O(x * len(REPLACEMENTS)). Either way, that would be linear too.
    return x.replace(ORIGINAL_REPLACEMENT.old, ORIGINAL_REPLACEMENT.new)

# -----------------------------------------------------------------------------

def urlify_3(x: str, l: int) -> str:
    tmp = urlify_3_raw(list(x), l)
    return "".join(tmp)

def urlify_3_raw(x: MutableSequence[str], l: int) -> MutableSequence[str]:
    """
    Replace spaces with "%20" (and al other `REPLACEMENTS`) in a mutable sequence in place.

    Note:
    * Idea: Start indexing & setting characters backwards. We can do this without having to re-edit the sequence because we already have a buffer at the end.
    * In Python there is no char data type, so we use `str.

    Complexity:

    * Time: O(n)
    * Space: O(1) (in place)
    """
    before_idx = l - 1
    after_idx = len(x) - 1

    while before_idx > -1:
        replacement = REPLACEMENTS_DICT.get(x[before_idx])
        if replacement:
            for i in range(replacement.new_len_minus_1, -1, -1):
                x[after_idx] = replacement.new[i]
                after_idx -= 1

        else:
            x[after_idx] = x[before_idx]
            after_idx -= 1

        before_idx -= 1


    return x

# -----------------------------------------------------------------------------
# Testing
# -----------------------------------------------------------------------------

from ctci.__util__ import run_test_cases


SAMPLE_TEST_CASE = [
    (("Mr John Smith    ", 13), "Mr%20John%20Smith")
]

TEST_CASES = [
  (("", 0), ""),
  (("   ", 1), "%20"),
  *SAMPLE_TEST_CASE
]

def test():
    run_test_cases(TEST_CASES,
                   urlify_1,
                   urlify_2,
                   urlify_3)
