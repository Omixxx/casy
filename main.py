from Case import Case
import punctuation_parser as p_parser
from case_converter import to_camel_case, to_pascal_case, to_snake_case


def __select_case(case: Case):
    if case == Case.CAMEL_CASE:
        return to_camel_case
    elif case == Case.SNAKE_CASE:
        return to_snake_case
    elif case == Case.PASCAL_CASE:
        return to_pascal_case
    else:
        return to_snake_case


def convert(word: str, case: Case) -> str:
    word = word.replace("    ", "\t")
    to_case = __select_case(case)
    result: str = ""
    separator = ""
    for w in word.split(" "):
        root = p_parser.parse(w)
        result = result + separator + p_parser.resolve(root, to_case)
        separator = " "
    return result


if __name__ == "__main__":

    word = """@Override 
    protected void generatenode(basenodemetamodel $string$, compilationunit nodecu, classorinterfacedeclaration "ciao") {
            nodecu.addimport(clonevisitor.class);
        }
        """

    word1 = "ialwayswonderedwhy i got a 100 on mytest"

    word2 = "dot.dot.dot who is there? Whatigot, is a lightinglobe!"

    print(convert(word, Case.PASCAL_CASE))
    print(convert(word1, Case.CAMEL_CASE))
    print(convert(word2, Case.SNAKE_CASE))
