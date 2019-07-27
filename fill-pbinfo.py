import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def mod(l, c):
    mapa[l][c] = 0
    if l > 0 and mapa[l-1][c] == 1:
      mod(l-1, c)
    if l < n-1 and mapa[l+1][c] == 1:
      mod(l+1, c)
    if c > 0 and mapa[l][c-1] == 1:
      mod(l, c-1)
    if c < m-1 and mapa[l][c+1] == 1:
      mod(l, c+1)

  
f=open("fill.in", "r")
if f.mode == 'r': 
    line = f.readline()
    mapa = f.read()
    n, m = map(int, (line.split()))
      mapa = mapa.split()
      mapa = list(map(int, mapa))
    mapa = np.reshape(mapa, (n,m))

cmap = colors.ListedColormap(['green', 'blue'])
bounds = [-0.5,0.5,1.5]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(mapa, cmap=cmap, norm=norm)

ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, m, 1))
ax.set_yticks(np.arange(-.5, n, 1))
ax.tick_params(labelbottom = False)   
ax.tick_params(labelleft = False)    

plt.show()
plt.savefig('foo.png')

contor = 0
for i in range(n):
  for j in range(m):
    if mapa[i][j] == 1:
      contor += 1
      mod(i, j)


print(contor)


