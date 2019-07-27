import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera
from matplotlib.pyplot import figure
fig = plt.figure()
ax = fig.add_subplot(111)

fig.set_size_inches(10, 10)
ax.set_aspect(aspect=1)

camera = Camera(fig)
t = np.linspace(0, 2 * np.pi, 16, endpoint=False)
t= np.append(t[:-1], t[:0:-1])
print(t)
for i in t:
    # if i != 0 and i
    print(i, i-1)
    semn = 1
    # a = plt.scatter(i-1, np.sin(i-1)*3, color='blue')
    a = plt.scatter(i, np.sin(i)*3*semn, color='blue')
    camera.snap()

animation = camera.animate()
animation.save('sdf.gif', writer = 'imagemagick')
