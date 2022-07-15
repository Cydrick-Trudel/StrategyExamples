from base_pattern.strategies.base_distance_strategy import BaseDistanceStrategy

class BaseProjectile:
    def __init__(self, initial_velocity: float, angle: float):
        '''
        initial_velocity: velocity in m/s
        angle: angle in degrees
        '''
        self.initial_velocity = initial_velocity
        self.angle = angle

    # That's the strategy pattern in all its glory. The distance returned by the BaseProjectile depends on the strategy given.
    # We just give all the relevant info to the strategy instance, and it gives out a distance.
    # Note that this method accepts the interface `BaseDistanceStrategy`, which is implemented by all the strategies implementations.
    def get_distance(self, distance_strategy: BaseDistanceStrategy) -> float:
        return distance_strategy.get_distance(self.initial_velocity, self.angle)
    