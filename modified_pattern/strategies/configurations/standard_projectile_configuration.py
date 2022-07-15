from modified_pattern.strategies.configurations.configuration import Configuration
from marshmallow import Schema, fields, post_load

class StandardProjectileConfiguration(Configuration):
    # Configuration object for the strategy that calculates the distance of a projectile on a planet. Note that it implements Configuration, and does not contain any logic.
    def __init__(self, gravitational_acceleration: float) -> None:
        self.gravitational_acceleration = gravitational_acceleration

class StandardProjectileConfigurationSchema(Schema):
    gravitational_acceleration = fields.Float()

    @post_load
    def make_obj(self, data, **kwargs):  # note: method name is arbitrary
        return StandardProjectileConfiguration(**data)