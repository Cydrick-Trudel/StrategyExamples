from math import radians, sin, cos
from modified_pattern.modified_projectile import ModifiedProjectile
from modified_pattern.strategies.configurations.projectile_hitting_object_configuration import ProjectileHittingObjectConfiguration
from modified_pattern.strategies.modified_distance_strategy import ModifiedDistanceStrategy

class ModifiedDistanceCalculationHittingObject(ModifiedDistanceStrategy):

    def get_distance(self, projectile: ModifiedProjectile) -> float:
        configuration: ProjectileHittingObjectConfiguration = self.get_configuration()
        angle_in_radians: float = radians(projectile.angle)
        time_of_flight: float = (2 * projectile.initial_velocity * sin(angle_in_radians) ) / 9.8
        horizontal_velocity: float = projectile.initial_velocity * cos(angle_in_radians)
        true_distance: float = time_of_flight * horizontal_velocity

        # Don't need to rely on a hard-coded variable set to 25m anymore. We can get the distance of the object from the configuration.
        if true_distance > configuration.object_distance:
            return configuration.object_distance
        else:
            return true_distance