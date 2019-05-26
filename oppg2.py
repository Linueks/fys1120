from __future__ import division, print_function
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

electron_mass = 9.11e-31 # [kg]
electron_charge = -1.60e-19 # [C]
magnetic_field = np.array([0, 0, 2]) # [T]


total_time = 30e-12
dt = 1e-15
total_time_steps = total_time/dt


def initialize_arrays():
    position = np.zeros((3, int(total_time_steps)))
    velocity = np.zeros((3, int(total_time_steps)))
    acceleration = np.zeros((3, int(total_time_steps)))
    time = np.linspace(0, total_time, int(total_time_steps))

    velocity[:, 0] = np.array([5000, 0, 2000])

    return position, velocity, acceleration, time


def euler_cromer(position, velocity, acceleration):
    for t in xrange(int(total_time_steps)- 1):
        force = electron_charge * np.cross(velocity[:, t], magnetic_field)
        acceleration[:, t+1] = force / electron_mass
        velocity[:, t+1] = velocity[:, t] + acceleration[:, t] * dt
        position[:, t+1] = position[:, t] + velocity[:, t+1] * dt

    return position, velocity


def plot3d(position, filename=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_zlabel('z [m]')
    ax.plot(position[0, :], position[1, :], position[2, :])
    plt.savefig(filename)
    #plt.show()


def plot2d(position, time, filename=None):
    x, y, z = position[0, :], position[1, :], position[2, :]

    plt.plot(time, x,
             time, y,
             time, z)
    plt.legend(['vx(t)', 'vy(t)', 'vz(t)'], loc='best')
    plt.xlabel('time [s]')
    plt.ylabel('velocity [m/s]')
    #plt.savefig(filename)
    #plt.show()


def measure_period(position):
    for t in xrange(int(total_time_steps)-1):
        if np.sign(position[0, t+1]) + np.sign(position[0, t]) == 0 and position[1, t] <= 4e-11:
            period = (t+ 1 + t) / 2 * dt
            return period



position, velocity, acceleration, time = initialize_arrays()
integrated_position, integrated_velocity = euler_cromer(position, velocity, acceleration)
#plot2d(integrated_position, time, 'velocity_components.png')
plot3d(integrated_position, 'particle_path_new_conditions.png')
#print(measure_period(integrated_position))
