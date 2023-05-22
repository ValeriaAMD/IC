
import numpy as np
import time 
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
nc = ctrl.Antecedent(np.arange(0, 10, 1), 'nc')
tespera = ctrl.Antecedent(np.arange(0, 10, 1), 'tespera')
color = ctrl.Consequent(np.arange(0, 10, 1), 'color')

# Auto-membership function population is possible with .automf(3, 5, or 7)
nc.automf(3)
tespera.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
color['low'] = fuzz.trimf(color.universe, [0, 2, 4])
color['medium'] = fuzz.trimf(color.universe, [2, 3, 4])
color['high'] = fuzz.trimf(color.universe, [2, 3, 5])

"""
To help understand what the membership looks like, use the ``view`` methods.
"""

# You can see how these look with .view()
nc['average'].view()

"""
.. image:: PLOT2RST.current_figure
"""
tespera.view()
"""
.. image:: PLOT2RST.current_figure
"""
color.view()
time.sleep(10)
