import wordninja


def convert_to_camel_case(word: str):
    if len(word.strip()) == 0:
        return ""

    words = wordninja.split(word)
    return words[0] + "".join([w.capitalize() for w in words[1:]])


def convert_to_snake_case(word: str):
    if len(word.strip()) == 0:
        return ""

    words = wordninja.split(word)
    return words[0] + "".join(["_" + w for w in words[1:]])


def convert_to_pascal_case(word: str):
    if len(word.strip()) == 0:
        return ""

    words = wordninja.split(word)
    return words[0].capitalize() + "".join([w.capitalize() for w in words[1:]])
