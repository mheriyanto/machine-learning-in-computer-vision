# Links: https://github.com/mheriyanto/Data-Science
# Broadcasting in Practice
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10+y*x)*np.cos(x)
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar()
plt.show()
