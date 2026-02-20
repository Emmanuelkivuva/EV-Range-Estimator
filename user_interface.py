"""User Interface function for Ev Range Estimator.
This module handles all user interactions including input collection and result display.
"""


def display_welcome() -> None:
    """Display welcome message and program description."""

    print("=" * 50)
    print("EV Range Estimator v1.0")
    print("=" * 50)
    print()
    print("This program estimates electric vehicle range based on:")
    print("- Vehicle specifications (mass, aerodynamics)")
    print("- Driving conditions (speed, road slope)")
    print("- Battery capacity and efficiency")
    print()
    print("Let's gather the necessary information...")
    print()

def get_user_input(prompt:str, min_value:float=None, max_value:float=None, default_value:float=None) -> float:
    """Get validated numeric input from user.
    Args:
        prompt: message to display to user
        min_value: Minimum acceptable value (optional)
        max_value: Maximum acceptable value (optional)
        default_value: Default if user presses 'enter' (optional)

    Returns:
        valid float number from the user
    """

    while True:
        user_input = input(prompt)
        if user_input == "" and default_value is not None:
            return default_value
        try:
            value = float(user_input)
            if min_value is not None and value < min_value:
                print(f"Error: Value must be at least {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Error: Value must be at most {max_value}")
                continue

            return value
        except ValueError:
            print("Error: Please enter a numeric value")


def get_vehicle_parameters() -> dict:
   """Collect Vehicle specifications from user.

    User can choose between predefined vehicle profiles or enter custom specifications.

    Returns:
        Dictionary with keys: battery_capacity, mass, drag_coefficient, frontal_area,
        rolling resistance
   """
   print("--- Vehicle Specifications ---")
   print()
   print("Choose vehicle specification method")
   print(" 1. Use preset vehicle profile")
   print(" 2. Enter custom specifications")
   print()

   while True:
       choice = input("Enter choice 1 or 2 ")

       if choice == "1":
           return _get_preset_vehicle()
       elif choice == "2":
           return _get_custom_vehicle()
       else:
           print("Error: Please enter 1 or 2")

def _get_preset_vehicle() -> dict:
    """Let user select form predefined vehicle profiles.

    Returns:
        Dictionary wih vehicle specification from preset
    """
    from vehicle_data import COMPACT_EV, SUV_EV, SPORTS_EV

    print()
    print("Available vehicle presets:")
    print(f" 1. {COMPACT_EV['name']}")
    print(f" 2. {SUV_EV['name']}")
    print(f" 3. {SPORTS_EV['name']}")
    print()

    while True:
        choice = input("Select vehicle (1-3) ")

        if choice == "1":
            selected = COMPACT_EV
            break
        elif choice == "2":
            selected = SUV_EV
            break
        elif choice == "3":
            selected = SPORTS_EV
            break
        else:
            print("Error: Please enter 1, 2 or 3")

    print()
    print(f"Selected: {selected['name']}")
    print(f" Mass: {selected['mass']} kg")
    print(f" Battery: {selected['battery_capacity']} kWh")
    print()

    return selected

def _get_custom_vehicle() -> dict:
    """Get custom vehicle specification from user input.

    Returns:
        Dictionary with vehicle specifications
    """
    print()
    print("Enter custom vehicle specification")
    print()

    battery = get_user_input("Enter battery capacity (kWh): ", min_value=10, max_value=200)
    mass = get_user_input("Enter vehicle mass (kg): ", min_value=800, max_value=3000)
    cd = get_user_input("Enter drag coefficient (Cd): ", min_value=0.15, max_value=0.50, default_value=0.28)
    area = get_user_input("Enter frontal area (m²): ", min_value=1.5, max_value=4.0, default_value=2.2)
    crr = get_user_input("Enter rolling resistance (Crr): ", min_value=0.005, max_value=0.020, default_value=0.010)

    print()

    return {
        'battery_capacity': battery,
        'mass': mass,
        'drag_coefficient': cd,
        'frontal_area': area,
        'rolling_resistance': crr
    }

def get_driving_conditions() -> dict:
    """Collect driving scenario information from user.

    Returns:
        Dictionary with keys: speed_kmh, slope_percent
    """

    print("--- Driving Conditions ---")
    print()

    speed_kmh = get_user_input("Enter speed (km/h): ", min_value=10, max_value=200)

    print("Road slope options:")
    print(" - Enter 0 for flat road")
    print(" - Enter a positive number for uphill (e.g., 5 for 5%)")
    print(" - Enter a negative number for downhill (e.g., -3 for -3% )")

    slope_percent = get_user_input("Enter slope percentage (%): ", min_value=-15, max_value=15, default_value=0)

    print()

    return {
        'speed_kmh': speed_kmh,
        'slope_percent': slope_percent,
    }

def get_system_parameters() -> dict:
    """Get efficiency and battery usage settings.
    Returns:
        Dictionary with keys: drivetrain_efficiency, battery_usable_percent
        (values as decimals, not percentages)
    """

    print("--- System Efficiency Settings ---")
    print("Press Enter to use the default values")
    print()

    efficiency = get_user_input("Enter drivetrain efficiency (%, default 88): ", min_value=70, max_value=98, default_value=88)
    usable = get_user_input("Enter battery usable percentage (%): ", min_value=70, max_value=100, default_value=90)

    print()

    return {
        'drivetrain_efficiency': efficiency / 100,
        'battery_usable_percent': usable / 100,
    }

def display_results(range_km: float, energy_per_km: float, speed_kmh: float) -> None :
    """Display calculation results to user.

    Args:
        range_km: Estimated range in kilometers (km)
        energy_per_km: Energy consumption in kWh/km
        speed_kmh: Driving speed in km/h
    """

    print()
    print("=" * 50)
    print("RESULTS")
    print("=" * 50)
    print()
    print(f"Estimated range: {range_km:.2f} km")
    print(f"Energy consumption: {energy_per_km:.3f} kWh/km")
    print(f"Driving speed: {speed_kmh:.0f} km/h")
    print()
    print("=" * 50)
    print()

def ask_continue() -> bool:
    """Ask user if they want to continue calculation.

    Returns:
        True if user wants to continue, False otherwise
    """

    while True:
        response = input("Do you want to run another calculation (yes/no): ")
        response_lower = response.lower()

        if response_lower in ["yes", "y"]:
            return True

        if response_lower in ["no", "n"]:
            return False

        print("Please enter yes or no.")

if __name__ == "__main__":
    display_welcome()
