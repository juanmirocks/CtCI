import urllib.parse
from typing import Callable, MutableSequence

# -----------------------------------------------------------------------------

signature = Callable[[str, int], str]

REPL_IN = " "
REPL_OUT = "%20"
REPL_OUT_LEN = len(REPL_OUT)
REPL_OUT_LEN_MINUS_1 = len(REPL_OUT) - 1


def urlify_1(x: str, l: int) -> str:
   return urlify_1_pure(x[0:l])

def urlify_1_pure(x: str) -> str:
    """Pythonic way to escape/encode a string to form a URL."""
    return urllib.parse.quote(x)


def urlify_2(x: str, l: int) -> str:
    return urlify_2_pure(x[0:l])

def urlify_2_pure(x: str) -> str:
    return x.replace(REPL_IN, REPL_OUT)


def urlify_3(x: str, l: int) -> str:
    tmp = urlify_3_raw(list(x), l)
    return "".join(tmp)

def urlify_3_raw(x: MutableSequence[str], l: int) -> MutableSequence[str]:
    """
    Replace spaces with "%20" (URL-escape) in a mutable sequence in place.

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
        if x[before_idx] == REPL_IN:
            for i in range(REPL_OUT_LEN_MINUS_1, -1, -1):
                x[after_idx] = REPL_OUT[i]
                after_idx -= 1
        else:
            x[after_idx] = x[before_idx]
            after_idx -= 1

        before_idx -= 1


    return x

# -----------------------------------------------------------------------------

from typing import NamedTuple

class Input(NamedTuple):
    x: str
    l: int

class Case(NamedTuple):
    input: Input
    expected: str

SAMPLE_TEST_CASE = Case(
    Input("Mr John Smith    ", 13),
    "Mr%20John%20Smith")

TEST_CASES = [
  Case(Input("", 0), ""),
  Case(Input("   ", 1), "%20"),
  SAMPLE_TEST_CASE
]

def _test(fun: signature):
    for input, expected in TEST_CASES:
        out = fun(*input)
        assert out == expected, f"in[{input}] -> expected: [{expected}] vs. out[{out}]"


def test_urlify_1():
    _test(urlify_1)

def test_urlify_2():
    _test(urlify_2)

def test_urlify_3():
    _test(urlify_3)
