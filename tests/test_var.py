from pdl.pdl.pdl_ast import Program  # pyright: ignore
from pdl.pdl.pdl_interpreter import process_block  # pyright: ignore

var_data = {
    "title": "Hello world with variable use",
    "prompts": [
        "Hello,",
        {
            "assign": "NAME",
            "prompts": [
                {
                    "model": "ibm/granite-20b-code-instruct-v1",
                    "decoding": "argmax",
                    "stop_sequences": ["!"],
                }
            ],
        },
        "!\n",
        "Who is",
        {"var": "NAME"},
        "?\n",
    ],
}


def test_var():
    scope = {}
    log = []
    data = Program.model_validate(var_data)
    document = process_block(log, scope, [], data.root)
    assert document == ["Hello,", " world", "!\n", "Who is", " world", "?\n"]


code_var_data = {
    "title": "simple python",
    "prompts": [
        {
            "assign": "I",
            "prompts": [
                {
                    "lan": "python",
                    "code": ["result = 0"],
                }
            ],
            "show_result": True,
        },
    ],
}


def test_code_var():
    scope = {}
    log = []
    data = Program.model_validate(code_var_data)
    document = process_block(log, scope, [], data.root)
    assert scope == {"I": "0"}
    assert document == ["0"]