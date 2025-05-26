"""
Let's talk about measuring distance. A hand is a unit of distance equal to four inches, 
and is commonly used to measure the height of horses in English-speaking countries. 
A light year is another unit of distance equal to the distance a particle (or is it wave?) of light travels in a certain number of seconds, 
equal roughly to one Earth year. On the face of it, these two units have little to do with one another beyond being used to measure distance, 
but it turns out that Google can convert between them pretty easily.

Given a list of conversion rates (formatted in the language of your choice) as a collection of origin unit, 
destination unit, and multiplier, for example:

foot inch 12

foot yard 0.3333333

yard inch 36

M -> inch 

inch -> foot 

foot -> yard 

yard -> M 

etc…

Such that ORIGIN * MULTIPLIER = DESTINATION, design an algorithm that takes two arbitrary unit values and returns the conversion rate between them.

Answer:
https://alexgolec.medium.com/google-interview-problems-ratio-finder-d7aa8bf201e3
"""


# In progress

# Design a conversion class
# Convert function - polymorphism depending on the inputs
# TODO design an algorithm that takes two arbitrary unit values and returns the conversion rate between them.
# use a adj graph inch -> foot 1/12 and foot -> inch 12
# Meters -> foot , foot -> inch = 1/12

class Conversions:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.multiplier = None
        

    def getDesiredUnit(self, origin, multiplier, value) -> int:
        return value * self.multiplier


