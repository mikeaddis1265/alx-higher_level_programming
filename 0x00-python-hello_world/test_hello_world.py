import pytest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout

# Import the module to test
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import 0-hello_world

@pytest.mark.alx
@pytest.mark.mandatory
def test_hello_world_output():
    """Test that the hello world script prints the correct output"""
    expected_output = "Hello, World!\n"
    
    # Capture stdout
    with StringIO() as buf, redirect_stdout(buf):
        # Import and run the module
        importlib.reload(0-hello_world)
        output = buf.getvalue()
    
    assert output == expected_output, f"Expected '{expected_output}', got '{output}'"

@pytest.mark.alx
@pytest.mark.mandatory
def test_pep8_compliance():
    """Test that the script follows PEP 8 style guidelines"""
    # This will be checked by pycodestyle in the workflow
    pass 