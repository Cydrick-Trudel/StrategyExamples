from base_pattern.strategies.base_distance_strategy import BaseDistanceStrategy

class BaseProjectile:
    def __init__(self, initial_velocity: float, angle: float):
        '''
        initial_velocity: velocity in m/s
        angle: angle in degrees
        '''
        self.initial_velocity = initial_velocity
        self.angle = angle

    def get_distance(self, distance_strategy: BaseDistanceStrategy) -> float:
        return distance_strategy.get_distance(self.initial_velocity, self.angle)
    