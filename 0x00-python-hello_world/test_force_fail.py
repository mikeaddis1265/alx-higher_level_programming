def test_force_fail():
    """Test that will fail to demonstrate automated bug reporting."""
    expected = "Hello, World!"
    actual = "Goodbye, World!"
    assert expected == actual, f"Expected '{expected}' but got '{actual}' - Testing automated bug reporting" 