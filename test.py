from __future__ import division, print_function
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')


total_time = 300e-9
dt = 100e-15
total_time_steps = int(total_time / dt)
time = np.linspace(0, total_time-dt, total_time_steps)


proton_mass = 1.6726219e-27 # [kg]
proton_charge = 1.60e-19 # [C]


magnetic_field = np.array([0, 0, 2]) # [T]
cyclotron_frequency = proton_charge * np.linalg.norm(magnetic_field) / proton_mass



acceleration = np.load('acceleration.npy')
position = np.load('integrated_position.npy')





valley_gap = 9.0e-5


plt.axvline(x=valley_gap/2, ymin=0, ymax = 1, linewidth=2, color='k')
plt.axvline(x=-valley_gap/2, ymin=0, ymax = 1, linewidth=2, color='k')
plt.axis('equal')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.plot(position[0, :], position[1, :])
plt.show()
