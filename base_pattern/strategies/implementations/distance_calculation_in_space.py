import sys
from base_pattern.strategies.base_distance_strategy import BaseDistanceStrategy

class DistanceCalculationInSpace(BaseDistanceStrategy):

    def get_distance(self, initial_velocity: float, angle: float) -> float:
        return sys.float_info.max