from base_pattern.base_projectile import BaseProjectile
from base_pattern.strategies.implementations.basic_distance_calculation import BasicDistanceCalculation
from base_pattern.strategies.implementations.distance_calculation_hitting_object import DistanceCalculationHittingObject
from base_pattern.strategies.implementations.distance_calculation_in_space import DistanceCalculationInSpace
from base_pattern.strategies.implementations.distance_calculation_on_mars import DistanceCalculationOnMars
from base_pattern.strategies.implementations.distance_calculation_on_moon import DistanceCalculationOnMoon

# This is the first main we'll start with. This is the 'pure' form of the Strategy pattern as seen in https://en.wikipedia.org/wiki/Strategy_pattern and the easiest to understand.

# We start with the same projectile. Regardless of if we're on earth, the moon, mars or space, we have a projectile that travels with an initial velocity of 100 m/s at a 45° angle.
p: BaseProjectile = BaseProjectile(100, 45)

# Here's the magic. When we want to get the distance, we give a different type of strategy depending on the conditions. The returned distance will change, despite using the same projectile.
basic_distance: float = p.get_distance(BasicDistanceCalculation())
print(f"Distance on earth: {basic_distance}m")

distance_on_moon: float = p.get_distance(DistanceCalculationOnMoon())
print(f"Distance on moon: {distance_on_moon}m")

distace_on_mars: float = p.get_distance(DistanceCalculationOnMars())
print(f"Distance on mars : {distace_on_mars}m")

distace_in_space: float = p.get_distance(DistanceCalculationInSpace())
print(f"Distance in space : {distace_in_space}m")

distance_hitting_object: float = p.get_distance(DistanceCalculationHittingObject())
print(f"Distance while hitting object : {distance_hitting_object}m")