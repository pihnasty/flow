import pytest

# Test class with a setup_class method
class TestClass:

    @classmethod
    def setup_class(cls):
        print("\nSetup code before all tests in the class")

    def test_example_one(self):
        assert 1 + 1 == 2

    def test_example_two(self):
        assert 2 * 2 == 4