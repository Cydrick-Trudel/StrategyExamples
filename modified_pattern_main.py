


from base_pattern.strategies.implementations.distance_calculation_hitting_object import DistanceCalculationHittingObject
from modified_pattern.modified_projectile import ModifiedProjectile
from modified_pattern.strategies.configurations.projectile_hitting_object_configuration import ProjectileHittingObjectConfiguration
from modified_pattern.strategies.configurations.standard_projectile_configuration import StandardProjectileConfiguration
from modified_pattern.strategies.implementations.modified_distance_calculation import ModifiedDistanceCalculation
from modified_pattern.strategies.implementations.modified_distance_calculation_hitting_object import ModifiedDistanceCalculationHittingObject
from modified_pattern.strategies.implementations.modified_distance_calculation_in_space import ModifiedDistanceCalculationInSpace


p: ModifiedProjectile = ModifiedProjectile(10, 45)

earth_configuration: StandardProjectileConfiguration = StandardProjectileConfiguration(9.8)
earth_strategy = ModifiedDistanceCalculation()
earth_strategy.set_configuration(earth_configuration)
basic_distance: float = earth_strategy.get_distance(p)  #Also note the reversal of objects here.
print(f"Distance on earth: {basic_distance}m")

moon_configuration: StandardProjectileConfiguration = StandardProjectileConfiguration(1.62)
moon_strategy = ModifiedDistanceCalculation()
moon_strategy.set_configuration(moon_configuration)
distance_on_moon: float = moon_strategy.get_distance(p)
print(f"Distance on moon: {distance_on_moon}m")

mars_configuration: StandardProjectileConfiguration = StandardProjectileConfiguration(3.721)
mars_strategy = ModifiedDistanceCalculation()
mars_strategy.set_configuration(moon_configuration)
distace_on_mars: float = mars_strategy.get_distance(p)
print(f"Distance on mars : {distace_on_mars}m")

space_strategy: ModifiedDistanceCalculationInSpace = ModifiedDistanceCalculationInSpace()
distace_in_space: float = space_strategy.get_distance(p)
print(f"Distance in space : {distace_in_space}m")

hitting_object_configuration: ProjectileHittingObjectConfiguration = ProjectileHittingObjectConfiguration(25.0)
hitting_object_strategy : ModifiedDistanceCalculationHittingObject = ModifiedDistanceCalculationHittingObject()
hitting_object_strategy.set_configuration(hitting_object_configuration)
distance_hitting_object: float = hitting_object_strategy.get_distance(p)
print(f"Distance while hitting object : {distance_hitting_object}m")