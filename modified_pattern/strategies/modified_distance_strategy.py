from abc import ABC
from modified_pattern.modified_projectile import ModifiedProjectile

from modified_pattern.strategies.configurations.configuration import Configuration

class ModifiedDistanceStrategy(ABC):

    def set_configuration(self, configuration: Configuration) -> None:
        self.configuration = configuration

    def get_configuration(self) -> None:
        return self.configuration
    
    def get_distance(self, projectile: ModifiedProjectile) -> float:
        raise NotImplementedError()