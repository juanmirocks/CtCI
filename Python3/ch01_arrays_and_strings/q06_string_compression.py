from io import StringIO
import random
import string


def compress_string_1(x: str) -> str:
    """
    Complexity:
    * Time: O(n) -- we iterate once over all x's elements/chars.
    * Space: O(n) -- we create an in-memory string buffer (StringIO) with a worst-case length of 2 * n (if no chars are repeated contiguously).
    """
    if x == "":
        return x  # return early for empty string

    elem = x[0]
    count = 1

    with StringIO() as buffer:
        for i in range(1, len(x)):
            if x[i] != elem:
                buffer.write(elem)
                buffer.write(str(count))

                elem = x[i]
                count = 1
            else:
                count += 1

        # Write the last repeated char
        buffer.write(elem)
        buffer.write(str(count))

        ret = buffer.getvalue()

    # Confirm the compression is actually smaller than the original string
    if len(ret) < len(x):
        return ret
    else:
        return x


# -----------------------------------------------------------------------------

from Python3.__util__ import run_test_cases


TEST_CASES = [
    (("aabcccccaaa", ), "a2b1c5a3"),
    #
    (("", ), ""),
    (("a", ), "a"),
    (("aa", ), "aa"),
    (("aaa", ), "a3")
]


FUNS = [
    compress_string_1
]


def test_arbitrary():
    run_test_cases(TEST_CASES, *FUNS)


def test_the_output_is_always_smaller_or_equals_the_input():
    for fun in FUNS:
        for i in range(0, 1000):
            input_random_string = "".join(random.choices(string.ascii_letters, k=random.randint(1, 100)))

            output = fun(input_random_string)
            assert (len(output) < len(input_random_string)) or output == input_random_string, f"in[{input_random_string}] vs. out[{output}]"
