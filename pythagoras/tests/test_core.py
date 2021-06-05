import os
from unittest import TestCase

from pythagoras import python_to_go

# Change directories to the location of the test for consistency between testing environments
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def assert_examples_match(test_case: TestCase, example: str):
    with open(f"examples/{example}.py") as a, \
            open(f"examples/{example}.go") as b:
        test_case.assertEqual(python_to_go(a.read()), b.read())


class Test(TestCase):
    def test_hello_world(self):
        assert_examples_match(self, "helloworld")

    def test_add(self):
        assert_examples_match(self, "add")
