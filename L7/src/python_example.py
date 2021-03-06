%matplotlib inline
import matplotlib.ticker
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np
import pylab as pl

def gain_dip(theta, phi):
    return 1.641*(np.cos(np.pi/2*np.cos(theta))/np.sin(theta))**2

theta = np.arange(-np.pi, np.pi,0.01)
# plot
ax = plt.subplot(111, polar=True)
# set zero west
ax.set_theta_zero_location('W')
ax.set_theta_direction('clockwise')
# let set an azimuth for example, pi
plt.plot(theta, gain_dip(theta, np.pi))