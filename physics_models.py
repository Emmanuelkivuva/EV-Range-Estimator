"""Physics calculations for EV range estimation.
This module provides functions for calculating forces, power, energy, and range  used in Ev Range Estimator calculations.


"""

import math
from utils import convert_ms_to_kmh, convert_watts_to_kwh


def calculate_rolling_resistance(mass: float, Crr: float, g: float = 9.81) -> float:
    """Calculate rolling resistance force.

    Args:
        mass: Vehicle mass in kg
        Crr: Rolling resistance coefficient (dimensionless)
        g: gravitational acceleration in m/s² (default: 9.81)

    Returns:
        rolling resistance force in Newtons
    """
    return mass * Crr  * g


def calculate_drag_force(speed_ms: float, Cd: float, frontal_area: float, air_density: float = 1.225) -> float:
    """Calculate Aerodynamic drag force.

    Args:
        speed_ms: Vehicle speed m/s
        Cd: Drag coefficient (dimensionless)
        frontal_area: Frontal_area in m²
        air_density: Air density kg/m³ (default: 1.225)

    Returns:
        Aerodynamic drag force in Newtons
    """

    return  0.5 * Cd * frontal_area * air_density * speed_ms ** 2


def calculate_gradient_force(mass: float, slope_angle_rad: float, g: float = 9.81) -> float:
    """Calculate gradient/ slope resistance force.

    Args:
        mass: Vehicle mass in kg
        slope_angle_rad: Slope angle in radians
        g: Gravitational acceleration in m/s² (default: 9.81)

    Returns:
        gradient force in Newtons (Positive = Uphill , Negative = Downhill)
    """

    return mass * g * math.sin(slope_angle_rad)

def calculate_total_resistance(rolling_force: float, drag_force: float, gradient_force: float) -> float:
    """Calculate total resistive forces acting on the vehicle.

    Args:
        rolling_force: Rolling force in Newtons
        drag_force: Drag force in Newtons
        gradient_force: Gradient force in Newtons

    Returns:
        Total resistive force in Newtons
    """

    return rolling_force + drag_force + gradient_force


def calculate_power_at_wheels(total_force: float, speed_ms: float) -> float:
    """Calculate Mechanical power needed at  wheels.
    Args:
        total_force: Total resistive force in Newtons
        speed_ms: Vehicle speed (m/s)

    Returns:
        Mechanical power in Watts (W)
    """

    return total_force * speed_ms


def calculate_power_from_battery(power_at_wheels: float, drivetrain_efficiency: float) -> float:
    """Calculate power needed from the battery (Accounting for losses)

    Args:
        power_at_wheels: Mechanical power in Watts (W)
        drivetrain_efficiency: Overall efficiency (eg 0.88 / 88%)

    Returns:
        Battery power in Watts (W)
    """
    return power_at_wheels / drivetrain_efficiency


def calculate_energy_per_km(power_battery_watts: float, speed_ms: float) -> float:
    """Calculate energy consumption per kilometer (kWh)

    Args:
        power_battery_watts: Battery power in Watts (W)
        speed_ms: Vehicle speed (m/s)

    Returns:
        Energy consumption in kWh/km
    """
    power_kwh = convert_watts_to_kwh(power_battery_watts)
    speed_km = convert_ms_to_kmh(speed_ms)

    return power_kwh / speed_km


def calculate_usable_battery_energy(battery_capacity_kwh: float, usable_percent: float) -> float:
    """Calculate usable battery energy (kWh)

    Args:
        battery_capacity_kwh: Battery capacity in kWh
        usable_percent: Usable percent ( e.g. 0.90 , 90%)

    Returns:
        usable energy in kWh
    """

    return battery_capacity_kwh * usable_percent


def calculate_range(usable_energy_kwh: float, energy_per_km: float) -> float:
    """Calculate the estimated vehicle range.
    Args:
        usable_energy_kwh: Available battery energy in kWh
        energy_per_km: Energy consumption in kWh/km

    Returns:
        Estimated range in Kilometers
    """
    return usable_energy_kwh / energy_per_km


