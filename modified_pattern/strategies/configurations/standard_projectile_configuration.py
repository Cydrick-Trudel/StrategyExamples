from modified_pattern.strategies.configurations.configuration import Configuration


class StandardProjectileConfiguration(Configuration):
    def __init__(self, gravitational_acceleration: float) -> None:
        self.gravitational_acceleration = gravitational_acceleration
