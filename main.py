"""Main program for EV Range Estimator.

This module orchestrates the entire calculation flow by connecting
user interface, physics calculation, and utility functions.
"""

import physics_models
import utils
import vehicle_data
import user_interface

def main():
    """Run the EV Range Estimator main program."""

    user_interface.display_welcome()

    continue_flag = True

    while continue_flag:
        # GET ALL INPUTS FROM THE USER

        vehicle_params=user_interface.get_vehicle_parameters()
        driving_conditions=user_interface.get_driving_conditions()
        system_params=user_interface.get_system_parameters()

        # CONVERT SI UNITS (m/s, radians)
        speed_ms=utils.convert_kmh_to_ms(driving_conditions['speed_kmh'])
        slope_rad=utils.convert_slope_percent_to_radians(driving_conditions['slope_percent'])

        # CALCULATE RESISTIVE FORCES
        rolling = physics_models.calculate_rolling_resistance(
            mass=vehicle_params['mass'],
            Crr=vehicle_params['rolling_resistance'],
            g=vehicle_data.GRAVITY,
        )

        drag = physics_models.calculate_drag_force(
            speed_ms=speed_ms,
            Cd=vehicle_params['drag_coefficient'],
            frontal_area=vehicle_params['frontal_area'],
            air_density=vehicle_data.AIR_DENSITY
        )

        gradient=physics_models.calculate_gradient_force(
            mass=vehicle_params['mass'],
            slope_angle_rad= slope_rad,
            g=vehicle_data.GRAVITY,
        )

        total_force=physics_models.calculate_total_resistance(
            rolling_force=rolling,
            drag_force=drag,
            gradient_force=gradient,
        )

        # CALCULATE POWER AND ENERGY CONSUMPTION
        power_wheels=physics_models.calculate_power_at_wheels(
            total_force=total_force,
            speed_ms=speed_ms,
        )

        power_battery=physics_models.calculate_power_from_battery(
            power_at_wheels=power_wheels,
            drivetrain_efficiency=system_params['drivetrain_efficiency'],
        )

        energy_per_km=physics_models.calculate_energy_per_km(
            power_battery_watts=power_battery,
            speed_ms=speed_ms,
        )

        # CALCULATE ESTIMATED RANGE
        usable_energy=physics_models.calculate_usable_battery_energy(
            battery_capacity_kwh=vehicle_params['battery_capacity'],
            usable_percent=system_params['battery_usable_percent'],
        )

        range_km=physics_models.calculate_range(
            usable_energy_kwh=usable_energy,
            energy_per_km=energy_per_km,
        )

        # DISPLAY RESULTS
        user_interface.display_results(
            range_km=range_km,
            energy_per_km=energy_per_km,
            speed_kmh=driving_conditions['speed_kmh'],
        )

        # ASK TO CONTINUE
        continue_flag=user_interface.ask_continue()

        # EXIT MESSAGE
    print()
    print("Thank you for using EV Range Estimator!")
    print("Drive efficiently!")
    print()

if __name__ == "__main__":
    main()





