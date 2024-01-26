from pdl.pdl.pdl_ast import Program  # pyright: ignore
from pdl.pdl.pdl_interpreter import process_block  # pyright: ignore

hello = {
    "title": "Hello world!",
    "prompts": ["Hello, world!\n", "This is your first prompt descriptor!\n"],
}


def repeat_data(n):
    return {
        "title": "Hello world with a nested block",
        "prompts": [
            "Hello, world!\n",
            "This is your first prompt descriptor!\n",
        ],
        "repeats": n,
    }


def nested_repeat_data(n):
    return {
        "title": "Hello world with a nested block",
        "prompts": [
            "Hello, world!\n",
            "This is your first prompt descriptor!\n",
            {"prompts": ["This sentence repeats!\n"], "repeats": n},
        ],
    }


def test_hello():
    scope = {}
    log = []
    data = Program.model_validate(hello)
    document = process_block(log, scope, [], data.root)
    assert document == ["Hello, world!\n", "This is your first prompt descriptor!\n"]


def repeat(n):
    scope = {}
    log = []
    data = Program.model_validate(repeat_data(n))
    document = process_block(log, scope, [], data.root)
    assert_string = []
    for _ in range(0, n):
        assert_string.append("Hello, world!\n")
        assert_string.append("This is your first prompt descriptor!\n")
    assert document == assert_string


def test_repeat_neg():
    repeat(-1)


def test_repeat0():
    repeat(0)


def test_repeat1():
    repeat(1)


def test_repeat2():
    repeat(2)


def test_repeat3():
    repeat(3)


def repeat_nested(n):
    scope = {}
    log = []
    data = Program.model_validate(nested_repeat_data(n))
    document = process_block(log, scope, [], data.root)
    assert_string = ["Hello, world!\n", "This is your first prompt descriptor!\n"]
    for _ in range(0, n):
        assert_string.append("This sentence repeats!\n")
    assert document == assert_string


def test_repeat_nested0():
    repeat_nested(0)


def test_repeat_nested1():
    repeat_nested(1)


def test_repeat_nested2():
    repeat_nested(2)


def test_repeat_nested3():
    repeat_nested(3)