from abc import ABC

class BaseDistanceStrategy(ABC):
    
    # This is an interface that forces all strategy instances to implement this method.
    # The implementations may not necessary need the velocity and / or the angle (ie: `distance-calculation_in_space.py` does not need either),
    # but they are free to use it if they need.
    def get_distance(self, initial_velocity: float, angle: float) -> float:
        raise NotImplementedError()