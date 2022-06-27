from math import radians, sin, cos
from base_pattern.strategies.base_distance_strategy import BaseDistanceStrategy

class DistanceCalculationHittingObject(BaseDistanceStrategy):

    def get_distance(self, initial_velocity: float, angle: float) -> float:
        return 25.0