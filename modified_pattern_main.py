
import json
from modified_pattern.modified_projectile import ModifiedProjectile
from modified_pattern.strategies.configurations.configuration import Configuration
from modified_pattern.strategies.configurations.projectile_hitting_object_configuration import ProjectileHittingObjectConfiguration, ProjectileHittingObjectConfigurationSchema
from modified_pattern.strategies.configurations.standard_projectile_configuration import StandardProjectileConfiguration, StandardProjectileConfigurationSchema
from modified_pattern.strategies.implementations.modified_distance_calculation import ModifiedDistanceCalculation
from modified_pattern.strategies.implementations.modified_distance_calculation_hitting_object import ModifiedDistanceCalculationHittingObject
from modified_pattern.strategies.implementations.modified_distance_calculation_in_space import ModifiedDistanceCalculationInSpace
from marshmallow import Schema

# This is the modified pattern. There's a couple of key differences compared to `base_pattern_main.py`:
#
# ============== 1- Reversal of flow between strategy and context ==============  
# There's a bit of reversal between the projectile and its strategies. In the base pattern, we give the strategy to the projectile, and it returns a different distance. In this modified pattern, we give the projectile to the strategy, and it returns a distance. It's a small difference, but it will be easier to implement it this way for the future.
# 
# ============== 2- Configurable strategies ==============
# We give a configuration object to the strategy instance when there's a need. The configuration object is tailored to the strategy (ie: StandardProjectileConfiguration is for ModifiedDistanceCalculation only)
#
# These configuration objects were saved in JSON files located in `<project_root>/modified_pattern/db` when you executed `modified_pattern_create_fake_db.py`. We then use Marshmallow to take the JSON saved in those files and put them back into the objects, with the right values as if they were instantiated here. But as you may see, we're not defining any gravitational acceleration values anywhere. 
#  
# This simplifies two things:
# 1. We don't have to create a strategy per planet. We just load the gravitational acceleration (ie: earth=9.8, moon=1.62, mars=3.721) from the configuration, we give it to the strategy, and the strategy's implementation can use it.
# 2. The hard-coded 25m in the previous `distance_calculation_hitting_object.py` is now configurable. 


'''
This method reads a Configuration object from a json file using Marshmallow's Schemas.
'''
def load_object_from_file(schema: Schema, file_name: str) -> Configuration:
    file_path: str = configuration_folder + file_name
    f = open(file_path, "r")
    configuration_as_string: str = f.read()
    configuration_as_dictionary: dict = json.loads(configuration_as_string)
    configuration_as_object: Configuration = schema.load(configuration_as_dictionary)

    print(f"Retrieved the following configuration from {file_path}: ")
    print(configuration_as_dictionary)

    return configuration_as_object


configuration_folder: str = "modified_pattern/db/"

# The only difference with this projectile is that the projectile does not have a `get_distance` method because of the reversal as seen in point 1. described above.
# Besides that, again it's the same projectile given to all the strategies.
p: ModifiedProjectile = ModifiedProjectile(100, 45)


earth_configuration: StandardProjectileConfiguration = load_object_from_file(StandardProjectileConfigurationSchema(), "earth_configuration.json") #This is the configuration for earth, with a gravitational acceleration of 9.8 m/s
earth_strategy = ModifiedDistanceCalculation()
earth_strategy.set_configuration(earth_configuration) #We give that configuration to the strategy. The strategy will then use the 9.8 m/s saved within the configuration
basic_distance: float = earth_strategy.get_distance(p)  #Note the reversal of objects here. We give the projectile to the strategy.
print(f"Distance on earth: {basic_distance}m")

# Same exact code as earth, with one difference: the gravitational acceleration is adjusted to the moon. But we don't have a different strategy or configuration. So we don't have a specific strategy for earth, moon or mars now. Nice!
moon_configuration: StandardProjectileConfiguration = load_object_from_file(StandardProjectileConfigurationSchema(), "moon_configuration.json") #There is implicit casting done here: `load_object_from_file` returns `Configuration`, but we're casting it to `StandardProjectileConfiguration`
str = StandardProjectileConfigurationSchema().dump(moon_configuration)
moon_strategy = ModifiedDistanceCalculation()
moon_strategy.set_configuration(moon_configuration)
distance_on_moon: float = moon_strategy.get_distance(p)
print(f"Distance on moon: {distance_on_moon}m")

# Same comment as above.
mars_configuration: StandardProjectileConfiguration = load_object_from_file(StandardProjectileConfigurationSchema(), "mars_configuration.json")
mars_strategy = ModifiedDistanceCalculation()
mars_strategy.set_configuration(mars_configuration)
distace_on_mars: float = mars_strategy.get_distance(p)
print(f"Distance on mars : {distace_on_mars}m")

# No real change here compared to the base pattern, but no need to provide a configuration object in this case: There's nothing that can change.
space_strategy: ModifiedDistanceCalculationInSpace = ModifiedDistanceCalculationInSpace()
distace_in_space: float = space_strategy.get_distance(p)
print(f"Distance in space : {distace_in_space}m")

# Again, another cool thing here is that the distance where the object is located is configurable.
hitting_object_configuration: ProjectileHittingObjectConfiguration = load_object_from_file(ProjectileHittingObjectConfigurationSchema(), "hitting_object.json")
hitting_object_strategy : ModifiedDistanceCalculationHittingObject = ModifiedDistanceCalculationHittingObject()
hitting_object_strategy.set_configuration(hitting_object_configuration)
distance_hitting_object: float = hitting_object_strategy.get_distance(p)
print(f"Distance while hitting object : {distance_hitting_object}m")