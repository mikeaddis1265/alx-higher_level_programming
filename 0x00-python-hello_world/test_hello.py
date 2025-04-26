import pytest
import sys
import os
import subprocess
from io import StringIO
from contextlib import redirect_stdout

# Import the module to test
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    import hello_world
except ImportError:
    print("Could not import hello_world module")
    sys.exit(1)

@pytest.mark.alx
@pytest.mark.mandatory
def test_hello_world_output():
    """Test that the hello world script prints the correct output"""
    expected_output = "Hello, World!\n"
    
    # Get the path to the hello world script
    script_path = os.path.join(os.path.dirname(__file__), "0-hello_world.py")
    
    # Run the script and capture its output
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True
    )
    
    assert result.stdout == expected_output, f"Expected '{expected_output}', got '{result.stdout}'"
    assert result.stderr == "", f"Expected no stderr, got '{result.stderr}'"
    assert result.returncode == 0, f"Expected return code 0, got {result.returncode}"

@pytest.mark.alx
@pytest.mark.mandatory
def test_pep8_compliance():
    """Test that the script follows PEP 8 style guidelines"""
    # This will be checked by pycodestyle in the workflow
    pass 