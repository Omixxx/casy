from binarytree import Node

TRAILING_CHARACTERS = set('\t".,;:()[]{}<>!@#$%^&*-_+=|\\/?><\n')


def parse(word: str):
    root = Node(word)
    word_list = list(word)
    for char in word_list:
        if char in TRAILING_CHARACTERS:
            index = word_list.index(char)
            root.value = char
            root.left = Node("".join(word_list[:index]))
            root.right = parse("".join(word_list[index + 1 :]))
            break

    return root


def resolve(root: Node | None, to_case) -> str:
    if root is None:
        return ""

    left = to_case(root.left.value) if root.left else ""
    middle = (
        to_case(root.value) if root.value not in TRAILING_CHARACTERS else root.value
    )

    right = resolve(root.right, to_case)
    return "".join(left + middle + right)
