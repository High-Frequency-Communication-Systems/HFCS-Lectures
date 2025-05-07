import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as Axes3D
from matplotlib import cm, colors


def interp_array(N1):  # add interpolated rows and columns to array
    # insert interpolated columns
    N2 = np.empty([int(N1.shape[0]), int(2*N1.shape[1] - 1)])
    N2[:, 0] = N1[:, 0]  # original column
    for k in range(N1.shape[1] - 1):  # loop through columns
        # interpolated column
        N2[:, 2*k+1] = np.mean(N1[:, [k, k + 1]], axis=1)
        N2[:, 2*k+2] = N1[:, k+1]  # original column
    # insert interpolated columns
    N3 = np.empty([int(2*N2.shape[0]-1), int(N2.shape[1])])
    N3[0] = N2[0]  # original row
    for k in range(N2.shape[0] - 1):  # loop through rows
        N3[2*k+1] = np.mean(N2[[k, k + 1]], axis=0)  # interpolated row
        N3[2*k+2] = N2[k+1]  # original row
    return N3


vals_theta = np.arange(0, 181, 5)
vals_phi = np.arange(0, 361, 5)

vals_phi, vals_theta = np.meshgrid(vals_phi, vals_theta)

THETA = np.deg2rad(vals_theta)
PHI = np.deg2rad(vals_phi)
Nsize = 3 # You can change N to get more lobes

# simulate the power data
R = abs(np.cos(Nsize*PHI)*np.sin(Nsize*THETA))  # 2 lobes (front and back)

interp_factor = 0  # 0 = no interpolation, 1 = 2x the points, 2 = 4x the points, 3 = 8x, etc

X = R * np.sin(THETA) * np.cos(PHI)
Y = R * np.sin(THETA) * np.sin(PHI)
Z = R * np.cos(THETA)

# # Interpolate between points to increase number of faces
# for counter in range(interp_factor):
#     X = interp_array(X)
#     Y = interp_array(Y)
#     Z = interp_array(Z)

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.grid(False)
ax.axis('off')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

N = np.sqrt(X**2 + Y**2 + Z**2)
Rmax = np.max(N)
N = N/Rmax

# axes_length = 1.5
# ax.plot([0, axes_length*Rmax], [0, 0], [0, 0], linewidth=2, color='red')
# ax.plot([0, 0], [0, axes_length*Rmax], [0, 0], linewidth=2, color='green')
# ax.plot([0, 0], [0, 0], [0, axes_length*Rmax], linewidth=2, color='blue')

# Find middle points between values for face colours
N = interp_array(N)[1::2, 1::2]

mycol = cm.jet(N)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=mycol,
                       linewidth=0.5, antialiased=True, shade=False)  # , alpha=0.5, zorder = 0.5)

# ax.set_xlim([-axes_length*Rmax, axes_length*Rmax])
# ax.set_ylim([-axes_length*Rmax, axes_length*Rmax])
# ax.set_zlim([-axes_length*Rmax, axes_length*Rmax])

m = cm.ScalarMappable(cmap=cm.jet)
# m.set_array(R)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# fig.colorbar(m, shrink=0.8)
ax.view_init(azim=300, elev=30)

plt.show()
