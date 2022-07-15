from math import radians, sin, cos
from base_pattern.strategies.base_distance_strategy import BaseDistanceStrategy

class DistanceCalculationOnMars(BaseDistanceStrategy):

    # See comment in `basic_distance_calculation.py`
    def get_distance(self, initial_velocity: float, angle: float) -> float:
        angle_in_radians: float = radians(angle)
        time_of_flight: float = (2 * initial_velocity * sin(angle_in_radians) ) / 3.721
        horizontal_velocity = initial_velocity * cos(angle_in_radians)
        return time_of_flight * horizontal_velocity