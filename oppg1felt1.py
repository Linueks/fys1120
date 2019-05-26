from __future__ import division, print_function
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('fivethirtyeight')


electron_mass = 9.11e-31 # [kg]
electron_charge = -1.60e-19 # [C]
electric_field = np.array([-5, 0, 0]) # [N/C]


total_time = 1.0 * 10**-6 # [s]
dt = np.array([1.0 * 10**-9, 1.0 * 10**-7]) # JEG HATER TALL
total_time_steps = total_time / dt


def initialize_arrays(i):
    position = np.zeros((3, int(total_time_steps[i])))
    velocity = np.zeros((3, int(total_time_steps[i])))
    acceleration = np.zeros((3, int(total_time_steps[i])))
    #time = np.arange(0, total_time, dt[i])
    time = np.linspace(0, total_time-dt[i], int(total_time_steps[i]))

    return position, velocity, acceleration, time


def euler_cromer(position, velocity, acceleration, i):
    for t in xrange(int(total_time_steps[i])- 1):
        force = electric_field * electron_charge
        acceleration[:, t] = force / electron_mass
        velocity[:, t+1] = velocity[:, t] + acceleration[:, t] * dt[i]
        position[:, t+1] = position[:, t] + velocity[:, t+1] * dt[i]

    return position


def plot3d(position1, position2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_zlabel('z [m]')
    plt.show()


def plot2d(position, acceleration, time):
    x, y, z = position[0, :], position[1, :], position[2, :]

    plt.plot(time, x,
             time, 0.5 * acceleration[0, 0] * time**2)
    plt.legend(['Numerical x', 'Analytical x'])
    plt.show()

position1, velocity1, acceleration1, time1 = initialize_arrays(0)
position2, velocity2, acceleration2, time2 = initialize_arrays(1)

integrated_position1 = euler_cromer(position1, velocity1, acceleration1, 0)
integrated_position2 = euler_cromer(position2, velocity2, acceleration2, 1)

#plot2d(integrated_position1, acceleration1, time1)
plot2d(integrated_position2, acceleration2, time2)
