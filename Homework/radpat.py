import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

# Read data file and plot
df = pd.read_csv('EIRP_Data.csv')  # henter data fra Excel

theta1d = df['Theta']
theta1d = np.array(theta1d)
# "Theta" kolonen blir hentet ut, satt i numpy array og gjort om til 2d array
theta2d = theta1d.reshape([37, 73])

phi1d = df['Phi']
phi1d = np.array(phi1d)
# "Phi" kolonen blir hentet ut, satt i numpy array og gjort om til 2d Array
phi2d = phi1d.reshape([37, 73])

power1d = df['Power']
power1d = np.array(power1d)
# "Power" kolonen blir hentet ut, satt i numpy array og gjort om til 2d array
power2d = power1d.reshape([37, 73])

THETA = np.deg2rad(theta2d)
PHI = np.deg2rad(phi2d)
R = power2d
Rmax = np.max(R)
Rmin = np.min(R)
N = R / Rmax

# Gjør om polar til kartesisk
X = R * np.sin(THETA) * np.cos(PHI)
Y = R * np.sin(THETA) * np.sin(PHI)
Z = R * np.cos(THETA)

fig = plt.figure()
