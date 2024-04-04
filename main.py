import punctuation_parser as p_parser

from case_converter import (
    convert_to_camel_case,
    convert_to_pascal_case,
    convert_to_snake_case,
)


def __convert(word: str, to_case) -> str:
    word = word.replace("    ", "\t")
    result: str = ""
    separator = ""
    for w in word.split(" "):
        root = p_parser.parse(w)
        result = result + separator + p_parser.resolve(root, to_case)
        separator = " "
    return result


def to_camel_case(word: str) -> str:
    return __convert(word, convert_to_camel_case)


def to_snake_case(word: str) -> str:
    return __convert(word, convert_to_snake_case)


def to_pascal_case(word: str) -> str:
    return __convert(word, convert_to_pascal_case)


