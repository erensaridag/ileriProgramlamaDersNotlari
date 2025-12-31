import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example DataFrame
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 20, 30, 40, 50],
    'Z': [100, 200, 300, 400, 500]
}
plotdata = pd.DataFrame(data)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(plotdata['X'], plotdata['Y'], plotdata['Z'])

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()