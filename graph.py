import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# define the function
def f(x):
    return x**3/(3*x**2+1)

x = np.linspace(-10, 10, 1000)
y = f(x)

# window principal
plt.plot(x, y)
plt.title('f(x) = x^3/(3x^2+1)')
plt.xlabel('x')
plt.ylabel('y')

# display the result in a graph
plt.show()