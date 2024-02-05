import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2
# View given x,y,z coordinates
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

# 3
# Create a figure
fig = plt.figure()
# Add your subplot
ax = fig.add_subplot(1, 1, 1)

ax.scatter(x, y, color='white')
ax.set_facecolor('black')
plt.title("2D scatterplot")
plt.show()


fig_3d = plt.figure()


ax= fig_3d.add_subplot(1, 1, 1, projection="3d")
ax.scatter(x,y,z, color='white')
ax.set_facecolor('black')
plt.title("3D scatterplot")
plt.show()