from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')


def oppgave1():
    B_styrke = np.array([36, 63, 89, 115, 139])*1e-3
    hall_spenning = np.array([5.7, 9.2, 13.1, 17.1, 21.0])*1e-3

    polyfit = np.polyfit(B_styrke, hall_spenning, 1)

    xs = np.linspace(0, 200e-3, 400)


    plt.xlabel('B-feltstyrke [T]')
    plt.ylabel('Hall Spenning [V]')

    plt.plot(xs, xs * polyfit[0] + polyfit[1])
    plt.scatter(B_styrke, hall_spenning)
    plt.legend(['lin. tilpassing', 'datapunkter'])
    plt.show()


def oppgave3():
    B_styrke = np.array([0, 0.025, 0.052, 0.107, 0.206, 0.410])
    height = np.array([10, 8, 6, 4, 2, 0])*1e-2
    mu_0 = 4 * np.pi * 10**-7
    plt.xlabel('h fra detektor [m]')
    plt.ylabel('B-feltstyrke [T]')
    plt.scatter(height, B_styrke)
    hs = np.linspace(0, 15e-2, 200)
    N = 244
    I = 5
    L = 275e-3
    ######field_strength = (N*I / 0.017) * mu_0 / 2 * ((hs + 0.01) / (np.sqrt((hs + 0.01)**2+ 0.017**2) - (hs / (np.sqrt(hs**2 + 0.017**2)))))
    plt.plot(hs, field_strength)




    plt.show()













































def oppgave3_1():
    B_styrke = np.array([0, 0.025, 0.052, 0.107, 0.206, 0.410])
    height = np.array([10, 8, 6, 4, 2, 0])*1e-2

    mu_0 = 4 * np.pi * 10**-7
    plt.xlabel('h fra detektor [m]')
    plt.ylabel('B-feltstyrke [T]')
    plt.scatter(height, B_styrke)

    hs = np.linspace(0, 15e-2, 200)
    N = 244
    I = 5
    L = 275e-3
