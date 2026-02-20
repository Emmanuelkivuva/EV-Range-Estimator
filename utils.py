"""Utility functions for unit conversions.
This module provides conversion functions between different units used in the EV Range Estimator calculations
"""


import math


def convert_kmh_to_ms(speed_kmh: float) -> float:
    """Converts speed from kilometers per hour to meters per second.

    Args:
        speed_kmh: Speed in km/h

    Returns:
        Speed in meters per second
    """
    return speed_kmh / 3.6

def convert_ms_to_kmh(speed_ms: float) -> float:
    """Converts speed from meters per second to kilometers per hour.

    Args:
        speed_ms: Speed in meters per second

    Returns:
        Speed in kilometers per hour
    """
    return speed_ms * 3.6

def convert_degrees_to_radians(degrees: float) -> float:
    """Converts angle from degrees to radians.

    Args:
         degrees: Angle in degrees

    Returns:
        Angle in radians

    """
    return degrees * math.pi / 180

def convert_slope_percent_to_radians(slope_percent: float) -> float:
    """Converts slope percentage to angle in radians.

    Args:
        slope_percent: Road grade as a percentage (e.g., 5 for 5%)

    Returns:
        Slope angle in radians (for use in sin/cos functions)

    """
    return math.atan(slope_percent / 100)

def validate_positive_number(value: float, parameter_name: str) -> bool:
    """Check if a number is positive.

    Args:
        value: The number to validate
        parameter_name: The name of the parameter (for error messages)

    Returns:
        True if number > 0, False otherwise

    Examples:
        >>> validate_positive_number(50, "battery_capacity")
        True
        >>> validate_positive_number(-10, "mass")
        False

    """

    if not isinstance(value, (int, float)):
        print(f"Error: {parameter_name} must be a number")
        return False
    if value <= 0:
        print(f"Error: {parameter_name} must be a positive number (got {value})")
        return False
    return True

def convert_watts_to_kwh(power_watts: float) -> float:
    """Converts power from watt to kwh.

    Args:
        power_watts: Power in Watts

    Returns:
        Power in kwh
    """
    return power_watts / 1000

