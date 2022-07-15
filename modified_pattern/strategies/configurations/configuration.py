from abc import ABC


class Configuration(ABC):
    # This is an interface to simply signal that an object is a configuration that can be accepted by `modified_distance_strategy.py`. All specific configuration objects must implement it.

    # Configuration objects should never contain logic or states. Only constants that can be used by strategies. This allows the object to be persistent (ie: configured by the user, then saved in the database and retrieved when calling the strategy)
    pass