import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes()
xmin = 0
xmax = 5
ymin = 0
ymax = 5
ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin,ymax])
ax.arrow(0.5, 0, 0, np.pi, head_width=0.05, head_length=0.1, fc='k', ec='k')
plt.show()