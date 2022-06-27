from modified_pattern.modified_projectile import ModifiedProjectile
from modified_pattern.strategies.configurations.projectile_hitting_object_configuration import ProjectileHittingObjectConfiguration
from modified_pattern.strategies.modified_distance_strategy import ModifiedDistanceStrategy

class ModifiedDistanceCalculationHittingObject(ModifiedDistanceStrategy):

    def get_distance(self, projectile: ModifiedProjectile) -> float:
        configuration: ProjectileHittingObjectConfiguration = self.get_configuration()
        return configuration.object_distance