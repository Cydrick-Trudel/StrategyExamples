from modified_pattern.strategies.configurations.configuration import Configuration
from marshmallow import Schema, fields, post_load

class ProjectileHittingObjectConfiguration(Configuration):
    # Configuration object for the strategy that hits an object. Note that it implements Configuration, and does not contain any logic.
    def __init__(self, object_distance: float) -> None:
        self.object_distance = object_distance

# See comment in `standard_projectile_configuration.py`
class ProjectileHittingObjectConfigurationSchema(Schema):
    object_distance = fields.Float()

    @post_load
    def make_obj(self, data, **kwargs):  # note: method name is arbitrary
        return ProjectileHittingObjectConfiguration(**data)