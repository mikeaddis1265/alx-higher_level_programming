#!/usr/bin/env python3
"""
Test for hello world module
"""
import os
import sys
import unittest
try:
    import hello_world
except ImportError:
    # This will fail the test but in a controlled way
    print("Could not import hello_world module")
    sys.exit(1)

class TestHelloWorld(unittest.TestCase):
    """Test cases for hello_world module"""
    
    def test_hello(self):
        """Test that hello() returns 'Hello, World!'"""
        self.assertEqual(hello_world.hello(), "Hello, World!")

if __name__ == "__main__":
    unittest.main() 