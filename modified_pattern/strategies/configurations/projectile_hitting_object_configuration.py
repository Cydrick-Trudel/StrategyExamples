from modified_pattern.strategies.configurations.configuration import Configuration


class ProjectileHittingObjectConfiguration(Configuration):
    def __init__(self, object_distance: float) -> None:
        self.object_distance = object_distance
