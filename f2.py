import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-2*math.pi,2*math.pi,100)
z = np.zeros_like(x)
for i in range(1,10):
    val = (4/(i*math.pi))*((-1)**(i+1))*np.sin((i*math.pi*x)/2)
    z += val

plt.plot(x,z)

plt.show()