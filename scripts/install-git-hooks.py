#!/usr/bin/python3
"""
Script to install git hooks for the project
"""
import os
import shutil
import subprocess
import sys

def install_hook():
    """Install the pre-push hook to the git hooks directory"""
    # Get the git hooks directory
    try:
        git_dir = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"],
            text=True
        ).strip()
    except subprocess.CalledProcessError:
        print("Error: Not a git repository")
        return False

    # Create the hooks directory if it doesn't exist
    hooks_dir = os.path.join(git_dir, "hooks")
    os.makedirs(hooks_dir, exist_ok=True)

    # Source and destination paths for the pre-push hook
    source_path = os.path.join("scripts", "pre-push-hook.sh")
    dest_path = os.path.join(hooks_dir, "pre-push")

    # Copy the hook script
    try:
        shutil.copy2(source_path, dest_path)
        print(f"Copied pre-push hook from {source_path} to {dest_path}")
    except Exception as e:
        print(f"Error copying hook: {str(e)}")
        return False

    # Make the hook executable
    try:
        if sys.platform != "win32":
            # On Unix-like systems, make the script executable
            os.chmod(dest_path, 0o755)
        else:
            # On Windows, we may need another approach
            pass
        print("Made pre-push hook executable")
    except Exception as e:
        print(f"Error making hook executable: {str(e)}")
        return False

    # Install required packages
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("Installed required packages")
    except subprocess.CalledProcessError as e:
        print(f"Error installing required packages: {str(e)}")
        # Continue anyway as packages might already be installed

    print("\nGit pre-push hook installed successfully!")
    print("The hook will run tests before each push and report any failures to the bug tracking system.")
    return True

if __name__ == "__main__":
    if install_hook():
        print("Done! Your git pre-push hook is now installed.")
    else:
        print("Failed to install git pre-push hook. Please check the errors above.")
        sys.exit(1) 