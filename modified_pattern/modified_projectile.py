class ModifiedProjectile:

    # Not much different than the BaseProjectile, but note the removal of the method `get_distance`. This is because we're doing reversal in who's calling who between the strategy and the projectile.
    def __init__(self, initial_velocity: float, angle: float):
        '''
        initial_velocity: velocity in m/s
        angle: angle in degrees
        '''
        self.initial_velocity = initial_velocity
        self.angle = angle
    