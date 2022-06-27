from abc import ABC

class BaseDistanceStrategy(ABC):
    

    def get_distance(self, initial_velocity: float, angle: float) -> float:
        raise NotImplementedError()