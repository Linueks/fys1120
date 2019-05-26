from __future__ import division, print_function
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import matplotlib.patches as patch
style.use('ggplot')


total_time = 300e-9
dt = 100e-15
total_time_steps = int(total_time / dt)
time = np.linspace(0, total_time-dt, total_time_steps)


proton_mass = 1.6726219e-27 # [kg]
proton_charge = 1.60e-19 # [C]


magnetic_field = np.array([0, 0, 2]) # [T]
cyclotron_frequency = proton_charge * np.linalg.norm(magnetic_field) / proton_mass # [C * T / kg] = [s**-1]
valley_gap = 9e-5 # [m]
D_radius = 0.05 # [m]



def electric_field(x, t):
    if np.abs(x) <= valley_gap / 2:
        E_0 = 25000 / valley_gap                                                                    # [V]
        electric_field = E_0 * np.cos(cyclotron_frequency * t) * np.array([1, 0, 0])
        return electric_field

    else:
        electric_field = np.array([0, 0, 0])
        return electric_field


def initialize_arrays():
    position = np.zeros((3, int(total_time_steps)))
    velocity = np.zeros((3, int(total_time_steps)))
    acceleration = np.zeros((3, int(total_time_steps)))
    time = np.linspace(0, total_time-dt, int(total_time_steps))


    return position, velocity, acceleration, time


def euler_cromer(position, velocity, acceleration):
    for t in xrange(int(total_time_steps)- 1):
        force = proton_charge * (np.cross(velocity[:, t], magnetic_field) + electric_field(position[0, t], t*dt))
        acceleration[:, t] = force / proton_mass
        velocity[:, t+1] = velocity[:, t] + acceleration[:, t] * dt
        position[:, t+1] = position[:, t] + velocity[:, t+1] * dt

        if np.linalg.norm(position[:, t]) >= D_radius:
            velocity[:, t+1] = velocity[:, t]
            position[:, t+1] = position[:, t] + velocity[:, t+1] * dt

    return position


def plot2d(position, time, filename=False):
    x, y, z = position[0, :], position[1, :], position[2, :]

    ax = plt.gca()
    #half_circle1 = patch.Wedge((valley_gap/2, 0), D_radius, 270, 90, facecolor=(214/255, 230/255, 245/255), edgecolor=(30/255, 30/255, 47/255))
    #half_circle2 = patch.Wedge((-valley_gap/2, 0), D_radius, 90, 270, facecolor=(214/255, 230/255, 245/255), edgecolor=(30/255, 30/255, 47/255))

    half_circle1 = patch.Wedge((valley_gap/2, 0), D_radius - valley_gap/2, 270, 90, facecolor='#F6EDF6', edgecolor='#101212')
    half_circle2 = patch.Wedge((-valley_gap/2, 0), D_radius - valley_gap/2, 90, 270, facecolor='#F6EDF6', edgecolor='#101212')

    ax.add_artist(half_circle1)
    ax.add_artist(half_circle2)

    #plt.axvline(x=valley_gap/2, ymin=0, ymax = 1, linewidth=2, color='k')
    #plt.axvline(x=-valley_gap/2, ymin=0, ymax = 1, linewidth=2, color='k')
    plt.axis('equal')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.plot(x, y, color='#3E47F8')
    plt.legend(['proton path'])
    if filename:
        plt.savefig(filename)
    plt.show()

def plot2d_components(position, time, filename=False):
    x, y, z = position[0, :], position[1, :], position[2, :]

    plt.plot(time, x,
             time, y,
             time, z)
    plt.legend(['vx(t)', 'vy(t)', 'vz(t)'], loc='best')
    plt.xlabel('time [s]')
    plt.ylabel('velocity [m/s]')
    if filename:
        plt.savefig(filename)
    else:
        plt.show()


position, velocity, acceleration, time = initialize_arrays()
integrated_position = euler_cromer(position, velocity, acceleration)
#plot2d(integrated_position, time)
#plot2d_components(integrated_position, time, filename='3b_velocity_components.png')
#print(np.linalg.norm(integrated_position[:, -1]))


#np.save('acceleration.npy', acceleration)
#np.save('integrated_position', integrated_position)
