import numpy as np
import random
import matplotlib.pyplot as plt

n = int(input('Motion number: '))

x, y = 0, 0

history = [(x, y)]

for i in range(0, n):
    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)
    y = y + np.sin(rad)

    history.append((x, y))

print(history)

xs = list(map(lambda point: point[0], history))
ys = list(map(lambda point: point[1], history))
plt.plot(xs, ys, 'o:', color='green', linewidth=2, alpha=0.5, label='history')
plt.plot([xs[0], xs[-1]], [ys[0], ys[-1]], color='blue', linewidth=2, alpha=1, label='diff')
plt.legend(loc="upper left")

plt.xlabel('X')
plt.ylabel('Y')

plt.title('Brownian motion')
plt.grid(True)
plt.show()