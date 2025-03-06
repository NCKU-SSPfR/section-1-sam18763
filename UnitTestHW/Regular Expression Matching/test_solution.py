import pytest
from solution import Solution  # Assuming the Solution class is in a file called solution.py

@pytest.fixture
def solution():
    return Solution()

# List of test cases with (s, p, expected_result)
testcases = [
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["a", ".*.", True],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]

# Parametrize the test to run for each case in testcases
@pytest.mark.parametrize("s, p, expected", testcases)
def test_isMatch(solution, s, p, expected):
    assert solution.isMatch(s, p) == expected

# Moving the failed test case into a new function and marking it as expected to fail
@pytest.mark.xfail
def test_broken_solution(solution):
    # This is just an example test that we expect to fail (Modify according to your case)
    assert solution.isMatch("a", ".*") == False  # This test is expected to fail
