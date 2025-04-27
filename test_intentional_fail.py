#!/usr/bin/python3
"""
Intentionally failing test to test bug reporting integration
"""
import unittest


class TestIntentionalFailure(unittest.TestCase):
    """Test class with intentionally failing tests"""

    def test_will_fail(self):
        """This test will fail on purpose to test bug reporting"""
        self.assertEqual(True, False, "Intentional failure to test bug reporting")

    def test_another_failure(self):
        """Another test that will fail with a different message"""
        self.assertEqual("working", "failing", "Another intentional failure")


if __name__ == "__main__":
    unittest.main() 