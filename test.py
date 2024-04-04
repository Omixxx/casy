import unittest
from main import *


class Test(unittest.TestCase):

    def test_camel_case_on_a_single_string(self):
        input = "helloworld"
        output = "helloWorld"

        self.assertEqual(to_camel_case(input), output)

    def test_camel_case_on_a_java_method(self):
        input = """@Override 
                  protected void generatenode(basenodemetamodel $string$, compilationunit nodecu, classorinterfacedeclaration "ciao") {
                        nodecu.addimport(clonevisitor.class);
                    }"""

        output = """@Override 
                  protected void generateNode(baseNodeMetaModel $string$, compilationUnit nodeCu, classOrInterfaceDeclaration "ciao") {
                        nodeCu.addImport(cloneVisitor.class);
                    }"""
        self.assertEqual(to_camel_case(input), output)


if __name__ == "__main__":
    unittest.main()

# word1 = "ialwayswonderedwhy i got a 100 on mytest"
# word2 = "dot.dot.dot who is there? Whatigot, is a lightinglobe!"
