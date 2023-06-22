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
    return ret if (len(ret) < len(x)) else x


def compress_string_2(x: str) -> str:
    """
    Alternative: look-ahead elements to avoid special conditions and simplify code.

    Complexity: same (asymptotically).
    """
    count = 0

    with StringIO() as buffer:
        for i in range(0, len(x)):
            count += 1

            if (i+1 == len(x)) or (x[i] != x[i+1]):
                buffer.write(x[i])
                buffer.write(str(count))
                count = 0

        ret = buffer.getvalue()

    # Confirm the compression is actually smaller than the original string
    return ret if (len(ret) < len(x)) else x


def compress_string_3(x: str) -> str:
    """
    Alternative: return the original string as soon as the internal buffer's length equals the input's.
    Note: in such a case, this implementation avoids calculating the buffer's value;
    ref: [StringIO.getvalue()](https://github.com/python/cpython/blob/3.10/Modules/_io/stringio.c#L277)

    Complexity: same (asymptotically)


    Note:
        the book discusses another alternative wherein the compression size is calculated first (without calculating the buffer) with the loop code,
        then, if it's smaller than the original input's, repeats the loop code to do calculate the buffer.
        I find that solution rather ugly. Either way, one would need to check with real data how often that case happens, then benchmark, and then decide.
    """
    count = 0

    with StringIO() as buffer:
        for i in range(0, len(x)):
            count += 1

            if (i+1 == len(x)) or (x[i] != x[i+1]):
                buffer.write(x[i])
                buffer.write(str(count))

                # Confirm the compression is STILL smaller than the original string
                if buffer.tell() >= len(x):
                    return x

                count = 0

        return buffer.getvalue()


# -----------------------------------------------------------------------------

from ctci.__util__ import run_test_cases


TEST_CASES = [
    (("aabcccccaaa", ), "a2b1c5a3"),
    #
    (("", ), ""),
    (("a", ), "a"),
    (("aa", ), "aa"),
    (("aaa", ), "a3")
]


FUNS = [
    compress_string_1,
    compress_string_2,
    compress_string_3
]


def test_arbitrary():
    run_test_cases(TEST_CASES, *FUNS)


def test_the_output_is_always_smaller_or_equals_the_input():
    for fun in FUNS:
        for i in range(0, 1000):
            input_random_string = "".join(random.choices(string.ascii_letters, k=random.randint(1, 100)))

            output = fun(input_random_string)
            assert (len(output) < len(input_random_string)) or output == input_random_string, f"in[{input_random_string}] vs. out[{output}]"
