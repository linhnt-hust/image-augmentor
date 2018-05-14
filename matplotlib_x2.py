from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
X = np.array([[-3,-2,-1,0,1,2,3]]).T
# weight (kg)
y = np.array([[9,4,1,0,1,4,9]]).T
# Visualize data 
plt.plot(X, y, 'ro')
plt.axis([-3,3, 0,9])
plt.xlabel('x')

plt.ylabel('x^2')


plt.spines['left'].set_position(('axes', 0))
plt.spines['right'].set_color('none')
plt.spines['bottom'].set_position(('axes', 0))
plt.spines['top'].set_color('none')


plt.show()
