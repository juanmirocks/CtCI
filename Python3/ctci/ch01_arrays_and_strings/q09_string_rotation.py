# Name the "is_substring" function for clarity
def is_substring(x: str, y: str) -> bool:
    return x in y


def is_rotation_1(s1: str, s2: str) -> bool:
    return False


# -----------------------------------------------------------------------------

from ctci.__util__ import run_test_cases


TEST_CASES = [
    (("", ""), True),
    (("a", "a"), True),
    (("a", "b"), False),
    (("ab", "ba"), True),
    (("ba", "ab", True)),  # The order does not matter
    (("erbottlewat", "waterbottle"), True)
]


run_test_cases(
    TEST_CASES,
    is_rotation_1
)
