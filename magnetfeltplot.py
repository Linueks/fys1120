from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')


I = 10
mu = 4 * np.pi * 10**-7
r = np.linspace(0.02, 0.1, 100)
plt.plot(r, I*mu/(2*np.pi*r))
plt.xlim([0, 0.15])
plt.legend(['B-feltstyrke'])
plt.xlabel('radius [m]')
plt.ylabel('B-felt [T]')
#plt.savefig('B-feltstyrke.png')
