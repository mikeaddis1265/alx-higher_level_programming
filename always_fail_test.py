#!/usr/bin/env python3
"""
This file contains a test that will always fail.
It's used to test the bug reporting system.
"""

def test_always_fail():
    """This test will always fail"""
    assert False, "This test is designed to fail to test bug reporting"

if __name__ == "__main__":
    print("Running test that will always fail...")
    try:
        test_always_fail()
        print("Test passed (this should never happen)")
    except AssertionError as e:
        print(f"Test failed as expected: {e}")
        exit(1)  # Exit with error code 