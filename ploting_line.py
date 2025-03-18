import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([1,8])
ypoint=np.array([3,10])

plt.plot(xpoint,ypoint)
plt.show()

#ploating without line

plt.plot(xpoint,ypoint,'o')
plt.show()

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()