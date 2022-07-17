# import pytest

# Function: Runs once per test.
# Class:    Runs once per class of tests.
# Module:   Runs once per module.
# Session:  Runs once per session.

# Testing using fixtures

# @pytest.fixture(scope="session")
# def fixture_1():
#     print('Fixture 1 running...')
#     return 2

# def test_example2(fixture_1):
#     print('Example 2 running...')
#     number = fixture_1
#     assert number == 2

# def test_example3(fixture_1):
#     print('Example 2 running...')
#     number = fixture_1
#     assert number == 2


# @pytest.fixture
# def yield_fixture():
#     print("Start of the test phase")
#     yield 5
#     print("End of the test phase")

# def test_example(yield_fixture):
#     print("Test example running...")
#     assert yield_fixture == 5


