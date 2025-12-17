"""Validation helpers for DIRC inputs."""


def validate_positive(value: float, field_name: str | None = None) -> None:
    """Validate that a numeric value is strictly positive.

    Raises:
        ValueError: if value is not > 0
    """
    if value is None:
        raise ValueError(f"{field_name or 'Value'} is required")
    if value <= 0:
        label = field_name or "Value"
        raise ValueError(f"{label} must be greater than zero")


