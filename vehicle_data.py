"""Physical Constants and Vehicle Profile data.
   This module contains constant physics values and predefined vehicle specifications
   used in the EV Range Estimator Calculations.
"""

# =============================================================================================
# PHYSICAL CONSTANTS
# =============================================================================================


GRAVITY = 9.81  # m/s² - Earth's gravitational acceleration
AIR_DENSITY = 1.225  # kg/m³ - Standard air density at sea level, 15°C


# =============================================================================================
#   SYSTEM EFFICIENCY DEFAULTS
# =============================================================================================


EFFICIENCY_DRIVETRAIN = 0.88  # 88% - Overall motor/inverter/transmission efficiency
EFFICIENCY_REGEN = 0.65  # 65% - Regenerative braking recovery efficiency
BATTERY_USABLE_PERCENT = 0.90  # 90% - Usable battery capacity (protects battery health)


# =============================================================================================
#   VEHICLE PROFILES
# =============================================================================================


COMPACT_EV = {
    'name': 'Nissan Leaf',
    'mass': 1500,  # kg
    'drag_coefficient': 0.28,  # Cd
    'frontal_area': 2.2,  # m²
    'rolling_resistance': 0.010,  # Crr
    'battery_capacity': 50  # kWh
}

SUV_EV = {
    'name': 'Volvo EX90',
    'mass': 2200,  # kg
    'drag_coefficient': 0.32,  # Cd
    'frontal_area': 2.8,  # m²
    'rolling_resistance': 0.012,   # Crr
    'battery_capacity': 80  # kWh
}

SPORTS_EV = {
    'name': 'Tesla Roadster',
    'mass': 1800,  # kg
    'drag_coefficient': 0.24,  # Cd
    'frontal_area': 2.0,  # m²
    'rolling_resistance': 0.009,   # Crr
    'battery_capacity': 75  # kWh
}




