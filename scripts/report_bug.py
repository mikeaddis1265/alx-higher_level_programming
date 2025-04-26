#!/usr/bin/env python3
"""
Script to run tests and report bugs to the BugTracker if tests fail.
This script is called from the terminal and runs tests in the current directory.
If tests fail, it sends a bug report to the BugTracker API.
"""

import os
import sys
import subprocess
import requests
import argparse
from datetime import datetime


def run_tests(directory):
    """Run pytest and pycodestyle in the specified directory"""
    test_output = ""
    
    # Change to the specified directory
    os.chdir(directory)
    
    # Run pytest
    try:
        pytest_result = subprocess.run(
            ["pytest", "--cov=.", "-v"],
            capture_output=True,
            text=True
        )
        test_output += f"Pytest Results:\n{pytest_result.stdout}\n{pytest_result.stderr}\n\n"
    except Exception as e:
        test_output += f"Error running pytest: {str(e)}\n\n"
    
    # Run pycodestyle
    try:
        style_result = subprocess.run(
            ["pycodestyle", "*.py"],
            capture_output=True,
            text=True
        )
        test_output += f"Style Check Results:\n{style_result.stdout}\n{style_result.stderr}\n\n"
    except Exception as e:
        test_output += f"Error running pycodestyle: {str(e)}\n\n"
    
    return test_output, pytest_result.returncode == 0 and style_result.returncode == 0


def report_bug(test_output, repo_name=None, commit_hash=None):
    """Report a bug to the BugTracker API"""
    # BugTracker API URL
    base_url = "https://c308-102-213-69-179.ngrok-free.app"
    api_url = f"{base_url}/api/bugs"
    
    # Get repository info from environment if not provided
    if not repo_name:
        repo_name = os.environ.get("GITHUB_REPOSITORY", "ALX Python Project")
    
    if not commit_hash:
        commit_hash = os.environ.get("GITHUB_SHA", "Unknown Commit")
    
    # Current datetime for the title
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create GitHub links for the commit
    github_url = f"https://github.com/{repo_name}"
    commit_url = f"{github_url}/commit/{commit_hash}"
    
    # Generate a better description with GitHub links
    description = f"""Tests failed in commit [{commit_hash}]({commit_url})

**Repository:** [{repo_name}]({github_url})
**Commit:** [{commit_hash}]({commit_url})
**Test Results:**

```
{test_output}
```
"""
    
    # Get a valid project ID from the URL
    print("Getting valid project IDs from BugTracker...")
    try:
        projects_response = requests.get(f"{base_url}/api/projects")
        projects = projects_response.json().get("projects", [])
        test_project = next((p for p in projects if "Test" in p.get("name", "")), None)
        
        if test_project:
            project_id = test_project.get("id")
            print(f"Found Test Project with ID: {project_id}")
        else:
            # Take the first project if no Test Project is found
            project_id = projects[0].get("id") if projects else "clm9x3cxh8000tirkwkxqjdd1"
            print(f"Using project ID: {project_id}")
    except Exception as e:
        print(f"Error getting projects: {str(e)}")
        # Fallback to a hardcoded project ID
        project_id = "clm9x3cxh8000tirkwkxqjdd1"
        print(f"Using fallback project ID: {project_id}")
    
    # Get a valid user ID from the URL
    print("Getting valid user IDs from BugTracker...")
    try:
        users_response = requests.get(f"{base_url}/api/users")
        users = users_response.json().get("users", [])
        # Use the first user as the reporter
        reporter_id = users[0].get("id") if users else "clm9x3c3c0000kytl24j0kp5qv"
        print(f"Using reporter ID: {reporter_id}")
    except Exception as e:
        print(f"Error getting users: {str(e)}")
        # Fallback to a hardcoded user ID
        reporter_id = "clm9x3c3c0000kytl24j0kp5qv"
        print(f"Using fallback reporter ID: {reporter_id}")
    
    # Bug data
    bug_data = {
        "title": f"Test Failure: {repo_name} at {current_time}",
        "description": description,
        "projectId": project_id,
        "reporterId": reporter_id,
        "priority": "HIGH",
        "severity": "MAJOR",
        "stepsToReproduce": f"1. Clone repo [{repo_name}]({github_url})\n2. Checkout commit [{commit_hash}]({commit_url})\n3. Run tests with 'pytest'",
        "source": "github",  # Set source to 'github' to indicate it's from GitHub CI
        "labels": "github,ci,test-failure",  # Add labels for better categorization
    }
    
    # Send the bug report
    try:
        print(f"Sending bug report to {api_url}...")
        response = requests.post(
            api_url,
            files={k: (None, v) for k, v in bug_data.items()},  # Convert to form data
        )
        
        if response.status_code == 201:
            bug_id = response.json().get("bug", {}).get("id")
            print(f"Bug reported successfully! Bug ID: {bug_id}")
            
            # The activity is automatically created when a bug is created
            # No need to create a separate activity record
            print("Activity record should be automatically created with the bug")
            
            # For good measure, let's add a comment to the bug with GitHub info
            comment_url = f"{base_url}/api/bugs/{bug_id}/comments"
            comment_data = {
                "content": f"This bug was automatically created from GitHub CI.\n\n**GitHub Repository:** [{repo_name}]({github_url})\n**Commit:** [{commit_hash}]({commit_url})",
                "userId": reporter_id,
                "bugId": bug_id
            }
            
            print(f"Adding a comment to the bug...")
            try:
                comment_response = requests.post(
                    comment_url,
                    json=comment_data
                )
                
                if comment_response.status_code in [200, 201]:
                    print(f"Comment added successfully!")
                else:
                    print(f"Failed to add comment. Status code: {comment_response.status_code}")
            except Exception as e:
                print(f"Error adding comment: {str(e)}")
            
            return True
        else:
            print(f"Failed to report bug. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"Error reporting bug: {str(e)}")
        return False


def main():
    """Main function to run tests and report bugs"""
    parser = argparse.ArgumentParser(description="Run tests and report bugs to BugTracker")
    parser.add_argument("--dir", default=".", help="Directory to run tests in")
    parser.add_argument("--repo", help="Repository name")
    parser.add_argument("--commit", help="Commit hash")
    parser.add_argument("--force-report", action="store_true", help="Report bug even if tests pass")
    
    args = parser.parse_args()
    
    print(f"Running tests in {args.dir}...")
    test_output, tests_passed = run_tests(args.dir)
    
    print(test_output)
    
    if not tests_passed or args.force_report:
        print("Tests failed. Reporting bug...")
        report_bug(test_output, args.repo, args.commit)
    else:
        print("All tests passed!")


if __name__ == "__main__":
    main() 