from math import radians, sin, cos
from modified_pattern.modified_projectile import ModifiedProjectile
from modified_pattern.strategies.configurations.standard_projectile_configuration import StandardProjectileConfiguration
from modified_pattern.strategies.modified_distance_strategy import ModifiedDistanceStrategy

class ModifiedDistanceCalculation(ModifiedDistanceStrategy):

    def get_distance(self, projectile: ModifiedProjectile) -> float:
        configuration: StandardProjectileConfiguration = self.get_configuration()
        angle_in_radians: float = radians(projectile.angle)
        time_of_flight: float = (2 * projectile.initial_velocity * sin(angle_in_radians) ) / configuration.gravitational_acceleration
        horizontal_velocity = projectile.initial_velocity * cos(angle_in_radians)
        return time_of_flight * horizontal_velocity