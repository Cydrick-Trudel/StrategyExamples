from math import radians, sin, cos
from base_pattern.strategies.base_distance_strategy import BaseDistanceStrategy

class BasicDistanceCalculation(BaseDistanceStrategy):
    # Note that we're inheriting from the interface `BaseDistanceStrategy`. All other implementations inherits from it.

    # Notice that the code of this method is very similar to the code of `distance_calculation_on_mars.py` and `distance_calculation_in_space.py`.
    # Only the gravitational acceleration (earth's gravitational acceleration is 9.8 m/s) changes between them. So essentially, we have mostly duplicated code, which is bad.
    # We'll address this issue in the modified pattern version.
    def get_distance(self, initial_velocity: float, angle: float) -> float:
        angle_in_radians: float = radians(angle)
        time_of_flight: float = (2 * initial_velocity * sin(angle_in_radians) ) / 9.8
        horizontal_velocity = initial_velocity * cos(angle_in_radians)
        return time_of_flight * horizontal_velocity