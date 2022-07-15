


from base_pattern.strategies.implementations.distance_calculation_hitting_object import DistanceCalculationHittingObject
from modified_pattern.modified_projectile import ModifiedProjectile
from modified_pattern.strategies.configurations.projectile_hitting_object_configuration import ProjectileHittingObjectConfiguration
from modified_pattern.strategies.configurations.standard_projectile_configuration import StandardProjectileConfiguration
from modified_pattern.strategies.implementations.modified_distance_calculation import ModifiedDistanceCalculation
from modified_pattern.strategies.implementations.modified_distance_calculation_hitting_object import ModifiedDistanceCalculationHittingObject
from modified_pattern.strategies.implementations.modified_distance_calculation_in_space import ModifiedDistanceCalculationInSpace

# This is the modified pattern. There's a couple of key differences:
# 
# 1- There's a bit of reversal between the projectile and its strategies. In the base pattern, we give the strategy to the projectile, and it returns a different distance. In this modified pattern, we give the projectile to the strategy, and it returns a distance. It's a small difference, but it will be easier to implement it this way for the future.
# 
# 2- We give a configuration object to the strategy instance when there's a need. The configuration object is tailored to the strategy (ie: StandardProjectileConfiguration is for ModifiedDistanceCalculation only)
# This simplifies two things:
# 2.1- We don't have to create a strategy per planet. We just give the gravitational acceleration (ie: earth=9.8, moon=1.62, mars=3.721) to the configuration, and the strategy can use it.
# 2.2- The hard-coded 25m in the previous `distance_calculation_hitting_object.py` is now configurable.


# The only difference with this projectile is that the projectile does not have a `get_distance` method because of the reversal as seen in point 1. described above.
# Besides that, again it's the same projectile given to all the strategies.
p: ModifiedProjectile = ModifiedProjectile(100, 45)

earth_configuration: StandardProjectileConfiguration = StandardProjectileConfiguration(9.8) #This is the configuration for earth, with a gravitational acceleration of 9.8 m/s
earth_strategy = ModifiedDistanceCalculation()
earth_strategy.set_configuration(earth_configuration) #We give that configuration to the strategy. The strategy will then use the 9.8 m/s saved within the configuration
basic_distance: float = earth_strategy.get_distance(p)  #Note the reversal of objects here. We give the projectile to the strategy.
print(f"Distance on earth: {basic_distance}m")

# Same exact code as earth, with one difference: the gravitational acceleration is adjusted to the moon. But we don't have a different strategy or configuration. So we don't have a specific strategy for earth, moon or mars now. Nice!
moon_configuration: StandardProjectileConfiguration = StandardProjectileConfiguration(1.62)
moon_strategy = ModifiedDistanceCalculation()
moon_strategy.set_configuration(moon_configuration)
distance_on_moon: float = moon_strategy.get_distance(p)
print(f"Distance on moon: {distance_on_moon}m")

# Same comment as above.
mars_configuration: StandardProjectileConfiguration = StandardProjectileConfiguration(3.721)
mars_strategy = ModifiedDistanceCalculation()
mars_strategy.set_configuration(moon_configuration)
distace_on_mars: float = mars_strategy.get_distance(p)
print(f"Distance on mars : {distace_on_mars}m")

# No real change here compared to the base pattern, but no need to provide a configuration object in this case: There's nothing that can change.
space_strategy: ModifiedDistanceCalculationInSpace = ModifiedDistanceCalculationInSpace()
distace_in_space: float = space_strategy.get_distance(p)
print(f"Distance in space : {distace_in_space}m")

# Again, another cool thing here is that the distance where the object is located is configurable.
hitting_object_configuration: ProjectileHittingObjectConfiguration = ProjectileHittingObjectConfiguration(25.0)
hitting_object_strategy : ModifiedDistanceCalculationHittingObject = ModifiedDistanceCalculationHittingObject()
hitting_object_strategy.set_configuration(hitting_object_configuration)
distance_hitting_object: float = hitting_object_strategy.get_distance(p)
print(f"Distance while hitting object : {distance_hitting_object}m")