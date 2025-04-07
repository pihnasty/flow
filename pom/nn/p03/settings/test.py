import pytest

# Define a fixture with autouse=True to make it run automatically before each test
@pytest.fixture(autouse=True)
def setup_before_tests():
    # Code to run before each test
    print("\nSetup code before running the test")

# Your test functions go here
def test_example():
    assert 1 + 1 == 2

def test_another_example():
    assert 2 * 2 == 4