from math import radians, sin, cos
from modified_pattern.modified_projectile import ModifiedProjectile
from modified_pattern.strategies.configurations.standard_projectile_configuration import StandardProjectileConfiguration
from modified_pattern.strategies.modified_distance_strategy import ModifiedDistanceStrategy

class ModifiedDistanceCalculation(ModifiedDistanceStrategy):
    # Similarely to `base_distance_calculation.py` and other implementations of the base pattern, we're inheriting from the interface `ModifiedDistanceStrategy`.

    def get_distance(self, projectile: ModifiedProjectile) -> float:
        # This obtains the configuration given to this strategy.
        # There's implicit casting done here: `self.get_configuration()` returns an object of type `Configuration`, but we're casting it to `StandardProjectileConfiguration`, which is the right configuration type for this strategy.
        configuration: StandardProjectileConfiguration = self.get_configuration()
        angle_in_radians: float = radians(projectile.angle)
        # Note here that we don't hard-code 9.8 in the strategy. The gravitational acceleration is obtained from the configuration. We save two strategy implementations: one for mars and one for the moon
        time_of_flight: float = (2 * projectile.initial_velocity * sin(angle_in_radians) ) / configuration.gravitational_acceleration
        horizontal_velocity: float = projectile.initial_velocity * cos(angle_in_radians)
        return time_of_flight * horizontal_velocity