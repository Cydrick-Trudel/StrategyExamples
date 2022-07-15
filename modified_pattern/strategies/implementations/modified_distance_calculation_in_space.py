import sys
from modified_pattern.modified_projectile import ModifiedProjectile
from modified_pattern.strategies.modified_distance_strategy import ModifiedDistanceStrategy

class ModifiedDistanceCalculationInSpace(ModifiedDistanceStrategy):

    # Essentiallyt the same code as the base pattern.
    def get_distance(self, projectile: ModifiedProjectile) -> float:
        return sys.float_info.max