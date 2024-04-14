import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

x, y = np.meshgrid(x, y)
t = np.sqrt(x**2 + y**2)
z = np.sin(t) / t

surf = ax.plot_surface(x, y, z, cmap=cm.viridis, vmin=z.min() * 2)
ax.set_zlim(-0.2, 0.8)

fig.colorbar(surf)

plt.show()

