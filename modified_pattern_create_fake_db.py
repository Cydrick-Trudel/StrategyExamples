import os
from modified_pattern.strategies.configurations.projectile_hitting_object_configuration import ProjectileHittingObjectConfiguration, ProjectileHittingObjectConfigurationSchema
from modified_pattern.strategies.configurations.standard_projectile_configuration import StandardProjectileConfiguration, StandardProjectileConfigurationSchema
from modified_pattern.strategies.configurations.configuration import Configuration
from marshmallow import Schema
import json

# This file simulates a database by writing the configuration for the strategies into a JSON file. It should write it into the directory `<project_dir>/modified_pattern/db`. You can look at the files and even edit them if you want. This is to simulate a user configuring the strategies from an administration panel, then the strategies being applied when we run the software.

# We're using Marshmallow to convert the configuration objects into JSON and vice versa. This file does Object -> JSON though, whereas the `modified_pattern_main.py` does the opposite.

'''
This method writes a Configuration object into a json file using Marshmallow's Schemas.
'''
def write_object_to_file(configuration: Configuration, schema: Schema, file_name: str) -> None:
    file_path: str = configuration_folder + file_name
    configuration_as_dictionary: dict = schema.dump(configuration)  # Object to Dictionary using Marshmallow
    configuration_as_string: str = json.dumps(configuration_as_dictionary)  #Dictionary to String using json standard library
    f = open(file_path, "w")
    f.write(configuration_as_string)
    f.close()

    print(f"Here's the configuration saved to '{file_path}")
    print(configuration_as_string)

# We're saving the configuration instances to file:
configuration_folder: str = "modified_pattern/db/"
if os.path.isdir(configuration_folder) is False:
    os.makedirs(configuration_folder)

# Here, we have all the gravitational accelerations as we're used to. If you look in the files, you'll see that they are saved.
earth_configuration: Configuration = StandardProjectileConfiguration(9.8)
moon_configuration: Configuration = StandardProjectileConfiguration(1.62)
mars_configuration: Configuration = StandardProjectileConfiguration(3.721)
standard_projectile_configuration_schema : Schema = StandardProjectileConfigurationSchema() #This is a marshmallow schema that helps converting from object to JSON and vice versa.
write_object_to_file(earth_configuration, standard_projectile_configuration_schema, "earth_configuration.json")
write_object_to_file(moon_configuration, standard_projectile_configuration_schema, "moon_configuration.json")
write_object_to_file(mars_configuration, standard_projectile_configuration_schema, "mars_configuration.json")

# Same thing here, but with a different schema.
hitting_object_configuration: Configuration = ProjectileHittingObjectConfiguration(25.0)
hitting_object_configuration_schema: Schema = ProjectileHittingObjectConfigurationSchema()
write_object_to_file(hitting_object_configuration, hitting_object_configuration_schema, "hitting_object.json")
