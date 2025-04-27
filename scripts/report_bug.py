#!/usr/bin/python3
"""
Script to report test failures as bugs to the bug tracking system
"""
import sys
import os
import json
import subprocess
import requests
import re

# Get command line arguments
commit_hash = sys.argv[1] if len(sys.argv) > 1 else 'unknown'
commit_msg = sys.argv[2] if len(sys.argv) > 2 else 'unknown'
branch = sys.argv[3] if len(sys.argv) > 3 else 'unknown'

# Configuration - Update these values
BUG_API_URL = "http://localhost:3000/api/bugs"  # Change if using ngrok
PROJECT_ID = "proj-1"  # Your project ID in the bug tracking system
REPORTER_ID = "user-1"  # Your user ID in the bug tracking system

def get_test_output():
    """Capture test output by running the tests"""
    try:
        # Run tests again to capture output
        result = subprocess.run(
            ["python", "-m", "unittest", "discover"],
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout + result.stderr
    except Exception as e:
        return f"Failed to capture test output: {str(e)}"

def extract_failing_tests(output):
    """Extract failing test information from output"""
    # Look for lines with "FAIL:" or "ERROR:" pattern in unittest output
    failures = re.findall(r'(FAIL|ERROR): ([^\n]+)', output)
    failure_details = [f"{status}: {test}" for status, test in failures]
    
    if not failure_details:
        return ["Test suite failed without specific test failures"]
    
    return failure_details

def report_bug():
    """Report bug to the tracking system"""
    test_output = get_test_output()
    failing_tests = extract_failing_tests(test_output)
    
    # Create bug report data
    data = {
        "title": f"Test Failure: {failing_tests[0] if failing_tests else 'Unknown failure'}",
        "description": f"""Tests failed during pre-push hook execution on branch {branch}.

**Commit Details**
- Hash: {commit_hash}
- Message: {commit_msg}
- Branch: {branch}

**Failing Tests**
{chr(10).join(failing_tests)}

**Test Output**
```
{test_output[:2000]}{"..." if len(test_output) > 2000 else ""}
```
""",
        "stepsToReproduce": f"""1. Checkout commit {commit_hash} on branch {branch}
2. Run `python -m unittest discover`
3. Observe test failures""",
        "priority": "HIGH",
        "severity": "MAJOR",
        "projectId": PROJECT_ID,
        "reporterId": REPORTER_ID,
        "source": "CI",
    }
    
    # Send the bug report
    try:
        response = requests.post(BUG_API_URL, json=data)
        if response.status_code >= 200 and response.status_code < 300:
            print(f"Bug reported successfully: {response.json()}")
            return True
        else:
            print(f"Failed to report bug. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"Error reporting bug: {str(e)}")
        return False

if __name__ == "__main__":
    # Verify configuration
    if not PROJECT_ID or not REPORTER_ID:
        print("Missing required configuration: PROJECT_ID and/or REPORTER_ID")
        sys.exit(1)
    
    print("Reporting test failures as bugs...")
    if report_bug():
        print("Bug reported successfully!")
    else:
        print("Failed to report bug")
        sys.exit(1) 