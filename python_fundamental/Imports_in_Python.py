''' Importing Modules in Python: Modules and Packages
In Python, modules and packages help organize and reuse code.'''

import math
math.sqrt(16)

from math import sqrt,pi
print(sqrt(16))
print(sqrt(25))
print(pi)


import numpy as np
np.array([1,2,3,4])


from math import *
print(sqrt(16))
print(pi)

from package.maths import addition
addition(2,3)

from package import maths
maths.addition(2,3)
