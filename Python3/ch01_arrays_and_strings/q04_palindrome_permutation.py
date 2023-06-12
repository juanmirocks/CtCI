

def is_permutation_of_palindrome_1(x: str) -> bool:
    """
    Notes:
    * Observation: A palindrome must be a string where each character is repeated exactly 2 times (even sequence), or each character is repeated 2 times and one character is repeated only 1 time (odd sequence).
    * Spaces are to be ignored (as per the question definition). That is: "tact coa" is equivalent to "tactcoa".
    * Case is ignored (as per the question assumptions).
    """
    return False


TEST_CASES = [
    ("", True),
    ("a", True),
    ("aa", True),
    ("a a", True),
    ("a b", False),
    ("tact coa", True)
]

def test():
    fun = is_permutation_of_palindrome_1

    for input, expected in TEST_CASES:
        output = fun(input)
        assert expected == output, f"in[{input}] -> expected[{expected}] vs. output[{output}]"
