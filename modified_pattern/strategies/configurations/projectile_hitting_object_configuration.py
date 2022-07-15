from modified_pattern.strategies.configurations.configuration import Configuration


class ProjectileHittingObjectConfiguration(Configuration):
    # Configuration object for the strategy that hits an object. Note that it implements Configuration, and does not contain any logic.
    def __init__(self, object_distance: float) -> None:
        self.object_distance = object_distance
