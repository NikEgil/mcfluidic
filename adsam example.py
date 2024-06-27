import os, shutil
import numpy as np
from minlpe import minlpe, nextPoint


debug = False
folder = 'tmp'+os.sep+'minlpe'


# Example 4
# get next points for the given initial sample
if os.path.exists(folder+'3'): shutil.rmtree(folder+'3')
samplerParams = dict(seed=0, samplerTimeConstraint=None, debug=debug)
X = [[0, 15.0], [20.0, 30.0]]
Y = [150.0, -100.0]
newX1 = nextPoint(X, Y, bounds=[[0, 60], [0, 60]], **samplerParams)
# if we can calculate multiple point in parallel, we can generate multiple new X. Set Y=None for not yet calculated points
X.append(newX1)
Y.append(None)
newX2 = nextPoint(X, Y, bounds=[[0, 60], [0, 30]], **samplerParams)
X.append(newX2)
Y.append(None)
newX3 = nextPoint(X, Y, bounds=[[0, 60], [0, 30]], **samplerParams)
print('Get next points for the given initial sample')
print('newX1 =', newX1)
print('newX2 =', newX2)
print('newX2 =', newX3)
