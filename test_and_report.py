#!/usr/bin/env python3
"""
This script runs our always-failing test and then reports a bug.
"""

import os
import sys
import subprocess
from scripts.report_bug import report_bug

def main():
    """Run the always-failing test and report a bug"""
    print("Running test that will always fail...")
    
    # Run the test
    test_result = subprocess.run(
        ["python", "always_fail_test.py"],
        capture_output=True,
        text=True
    )
    
    # Print the test output
    print(test_result.stdout)
    if test_result.stderr:
        print(test_result.stderr)
    
    # Report a bug
    print("Reporting bug...")
    success = report_bug(
        test_output=test_result.stdout + "\n" + test_result.stderr,
        repo_name="alx-higher_level_programming",
        commit_hash="test-run"
    )
    
    if success:
        print("Bug reported successfully!")
    else:
        print("Failed to report bug.")
        sys.exit(1)

if __name__ == "__main__":
    main() 