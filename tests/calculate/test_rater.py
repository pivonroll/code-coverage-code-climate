from code_coverage.calculator.rater import name


def test_name() -> None:
    """Test the name function."""
    assert name() == "Calculator"
