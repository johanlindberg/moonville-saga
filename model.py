## Moonville

import random

## Objects
class Robonaut(object):
    pass

class Solar_Cell(object):
    pass

class Processor(object):
    pass

class Digger(object):
    pass

## Raw Material
class Regolith(object):
    """Because the concentration of helium-3 is extremely low, it would be
    necessary to process large amounts of rock and soil to isolate the material.
    Digging a patch of lunar surface roughly three-quarters of a square mile to
    a depth of about 9 feet should yield about 220 pounds of helium-3, enough
    to power a city the size of Dallas or Detroit for a year. [1]

    [1] http://www.popularmechanics.com/science/space/moon-mars/1283056"""

    def __init__(self):
        self.variation = [90, 115] # upper and lower bounds, in %

        # There's roughly 0.000035 kg He-3 per cubic meter. To get the 100 kg
        # (220 pounds) described above we would have to dig up and process
        # 3 000 000 cubic meters.
        self.concentration = 0.000035

    def process(self, amount = 1, concentration = None, variation = None):
        """Returns the amount (in kg) of He-3 that can be processed.

        >>> r = Regolith()
        >>> r.process(1000000) >= 31.5
        True
        >>> r.process(1000000) <= 40.25
        True
        """

        # Concentration of He-3 in this sample
        c = self.concentration
        if concentration:
            c = concentration
            
        # Variation of concentration in this sample
        v = self.variation
        if variation:
            v = variation

        r = random.randrange(v[0], v[1])
        a = c * r / 100
        
        # Amount of He-3 in this sample
        return a * amount
        
        
## External events
class External_Event(object):
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
