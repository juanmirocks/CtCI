from typing import Callable, TypeVar, Sequence


Output = TypeVar("Output")


def run_test_cases(test_cases: Sequence[tuple[tuple, Output]], *funs: Callable[..., Output], **kwargs) -> None:
    equal = kwargs.get("equal", lambda x, y: x == y)

    for fun in funs:
        for input, expected_output in test_cases:
            output = fun(*input)
            assert equal(expected_output, output), f"in[{input}] -> expected_out[{expected_output}] vs. out[{output}]"
