# Strategy Examples

## Introduction
This is a study of the [strategy design pattern](https://en.wikipedia.org/wiki/Strategy_pattern) applied to a projectile distance calculation under various circumstances (ie: different planets in the solar system, in space or hitting an object during it's flight). 

The `base_pattern` folder is the "pure" version of the pattern as seen on Wikipedia. Various strategies shows the distance of a projectile under different circumstances

The `modified_pattern` shows a structure that is similar to the first, but with two main changes:

- The base pattern gives the strategy instance to the context, whereas the modified pattern gives the context to the strategy.
- The base pattern has no configuration, whereas the modified pattern allows to have a configuration that's provided to the strategy. The configuration is also saved on the filesystem.

It's recommended to fully understand the base pattern before moving onto the modified pattern. The file names and structure is similar, so it will be easier to understand the differences between the base and modified pattern if you understand the base pattern.

## Purpose

This shows the power of the strategy pattern. The `base_pattern` is useful for understanding the basic of the pattern, whereas the `modified_pattern` shows something that is closer to what you can expect in enterprise software.

Here are the advantages of the `modified_pattern` version compared to the `base_pattern`:

### Ease of expanding features 

The reversed flow between the strategy and the context means that it's cleaner to have strategies to control multiple facets of the software. 
  
For instance, if we needed to obtain the maximum height of the projectile with the `base_pattern`, we would need to add a method to the projectile class to accept strategies that obtains the height of the projectile. This can lead to clutter if we need to add a lot of methods, on an object that is otherwise clean (the projectile object). 

With the `modified_pattern`, it's the caller's responsability to handle the multiple cases.

### Removing similar strategies

In the `base_pattern` variant, the algorithms to calculate the for earth, the moon and Mars are very similar: Only the gravitational acceleration (a constant that varies from planet to planet) changes. This leads to code duplication and general clutter of strategy implementations.

With the `modified_pattern` variant, configuration objects are introduced. Properties that varies can be put into these configuration object, and the strategy's algorithm can refer to the values saved in these configuration objects. This leads to having a single strategy implementation that's acceptable to every planet, and just takes the gravitational acceleration.



## How to run

The softwares can be executed as follows:
```
cd <project root>

pip install -r requirements.txt

# Base Pattern
python3 base_pattern_main.py

# Modified Pattern
python3 modified_pattern_create_fake_db.py  # You may run this only once if you want
python3 modified_pattern_main.py

```
