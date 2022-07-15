import sys
from base_pattern.strategies.base_distance_strategy import BaseDistanceStrategy

class DistanceCalculationInSpace(BaseDistanceStrategy):

    # No gravitational acceleration in space: we go to infinity.
    # Don't need the initial velocity or the angle.
    def get_distance(self, initial_velocity: float, angle: float) -> float:
        return sys.float_info.max