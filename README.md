# EV-Range-Estimator
This project is designed to calculate the estimate range an Ev vehicle can reach based on various factors such as Aerodynamics, Rolling Resistance, Gradient resistance and drivetrain inefficiencies etc.
The project is made up of five modules:
a) main.py
This module orchesrates the other modules, meaning it is the brain that imports functions from other modules and tells them what to do and in what order.

b) physics_models.py
This is where the calculations actually happen, i.e. aerodynamic drag, rolling resistance, gradient resistance etc.

c) user_inteface.py
Here is where the user interacts with the program the user is allowed to give inputs or choose from the preset inputs already given. Moreover this module has error instructions in the case a user enters a wrong input.

d) utils.py
Repetitive calculations such as unit conversions are stored here and can be imported to other modules incase they are needed.

e) vehicle_data.py
Constant values are stored here which include gravitational force, and air density. Moreover there are stored vehicle data of different vehicles profiles a user can choose from instead of entering custom values.

