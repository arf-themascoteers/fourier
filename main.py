import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-2*math.pi,2*math.pi,100)
y = list()
z = np.zeros_like(x)
k = 3
growth = k*2
for i in range(0,3):
    n = k + (growth*i)
    print(n)
    val = (1/n*np.sin(n*x))
    plt.plot(x, val)
    y.append(val)
    z += val

plt.plot(x,z)

plt.show()