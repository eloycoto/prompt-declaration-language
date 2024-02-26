from pdl.pdl.pdl_ast import Program  # pyright: ignore
from pdl.pdl.pdl_interpreter import empty_scope  # pyright: ignore
from pdl.pdl.pdl_interpreter import process_block  # pyright: ignore

defs_data = {
    "description": "Hello world with variable use",
    "defs": {
        "HELLO": "Hello,",
        "NAME": {
            "prompts": [
                {
                    "model": "ibm/granite-20b-code-instruct-v1",
                    "input": {"get": "HELLO"},
                    "decoding": "argmax",
                    "stop_sequences": ["!"],
                }
            ]
        },
    },
    "prompts": [
        {"get": "HELLO"},
        {"get": "NAME"},
        "!\n",
    ],
}


def test_defs():
    log = []
    data = Program.model_validate(defs_data)
    _, document, _, _ = process_block(log, empty_scope, data.root)
    assert document == "Hello, world!\n"


defs_chain_data = {
    "description": "Hello world with variable use",
    "defs": {
        "X": {"value": "a"},
        "Y": {"value": "b"},
        "Z": {"prompts": [{"get": "X"}, {"get": "Y"}, "c"]},
    },
    "prompts": [{"get": "X"}, {"get": "Y"}, {"get": "Z"}],
}


def test_defs_chain():
    log = []
    data = Program.model_validate(defs_chain_data)
    _, document, _, _ = process_block(log, empty_scope, data.root)
    assert document == "abc"