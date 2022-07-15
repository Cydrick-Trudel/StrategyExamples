from math import radians, sin, cos
from base_pattern.strategies.base_distance_strategy import BaseDistanceStrategy

class DistanceCalculationHittingObject(BaseDistanceStrategy):
    # There's an object at 25m. If the projectile lands short of 25m, we use that distance. Otherwise, it's max is 25m.
    # Note that it's a bit problematic in this particular case. What if we have an object at 26m? We create another strategy? 
    # We'll address this issue in the modified pattern section.
    object_distance: int = 25.0

    # There's an object at 25m. If the projectile lands short of 25m, we use that distance. Otherwise, it's max is 25m.
    def get_distance(self, initial_velocity: float, angle: float) -> float:
        angle_in_radians: float = radians(angle)
        time_of_flight: float = (2 * initial_velocity * sin(angle_in_radians) ) / 9.8
        horizontal_velocity = initial_velocity * cos(angle_in_radians)
        true_distance = time_of_flight * horizontal_velocity

        if true_distance > DistanceCalculationHittingObject.object_distance:
            return DistanceCalculationHittingObject.object_distance
        else:
            return true_distance