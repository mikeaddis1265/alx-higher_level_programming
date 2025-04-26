#!/usr/bin/env python3
"""
Test script that will deliberately fail so we can test our bug reporting
Run this script with: python test_bug_report.py
"""

import os
import subprocess

# Get the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
bug_report_script = os.path.join(script_dir, "scripts", "report_bug.py")

def test_fail():
    """This test will fail on purpose to trigger bug reporting"""
    assert False, "This test is designed to fail to test bug reporting"

def run_bug_report():
    """Run the bug report script manually to test it"""
    subprocess.run([
        "python", 
        bug_report_script, 
        "--dir", ".", 
        "--repo", "alx-higher_level_programming",
        "--commit", "manual-test",
        "--force-report"
    ])
    
if __name__ == "__main__":
    # Run the bug report script to test it
    print("Running bug report test...")
    run_bug_report() 