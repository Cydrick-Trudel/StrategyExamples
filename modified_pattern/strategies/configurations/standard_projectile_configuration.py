from modified_pattern.strategies.configurations.configuration import Configuration


class StandardProjectileConfiguration(Configuration):
    # Configuration object for the strategy that calculates the distance of a projectile on a planet. Note that it implements Configuration, and does not contain any logic.
    def __init__(self, gravitational_acceleration: float) -> None:
        self.gravitational_acceleration = gravitational_acceleration
