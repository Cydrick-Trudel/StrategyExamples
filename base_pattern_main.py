from base_pattern.base_projectile import BaseProjectile
from base_pattern.strategies.implementations.basic_distance_calculation import BasicDistanceCalculation
from base_pattern.strategies.implementations.distance_calculation_hitting_object import DistanceCalculationHittingObject
from base_pattern.strategies.implementations.distance_calculation_in_space import DistanceCalculationInSpace
from base_pattern.strategies.implementations.distance_calculation_on_mars import DistanceCalculationOnMars
from base_pattern.strategies.implementations.distance_calculation_on_moon import DistanceCalculationOnMoon


p: BaseProjectile = BaseProjectile(10, 45)
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