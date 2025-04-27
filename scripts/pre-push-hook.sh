#!/bin/sh
# Pre-push hook to run tests before pushing

# Get the current branch name
branch="$(git symbolic-ref --short HEAD)"

echo "Running tests before pushing to $branch..."

# Run Python tests
python -m unittest discover

# Save the exit code 
exit_code=$?

if [ $exit_code -ne 0 ]; then
  echo "Tests failed! Reporting bug to the tracking system..."
  
  # Get the last commit message and hash
  commit_hash=$(git rev-parse HEAD)
  commit_msg=$(git log -1 --pretty=%B)
  
  # Report the bug using Python script
  python scripts/report_bug.py "$commit_hash" "$commit_msg" "$branch"
  
  # Ask the user if they want to proceed with the push despite test failures
  exec < /dev/tty
  echo "Tests failed. Do you want to push anyway? (y/n)"
  read answer
  if [ "$answer" != "y" ]; then
    echo "Push aborted."
    exit 1
  fi
  echo "Proceeding with push despite test failures."
  exec <&-
fi

exit 0 