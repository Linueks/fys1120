from numpy import *
from matplotlib.pyplot import *
from scipy import *

# opg5
# t = array([1.05, 0.63, 0.65, 1.02, 0.63, 0.63, 0.64, 0.60, 0.63, 0.57])
#
# e0 = array([15, 18, 17, 18, 21, 22, 21, 23, 21, 20])*1e-3/9
#
#
# b = e0*t/(11*pi)
# print(b)
# print(average(b))





# opg4
# v1 = array([9, 6, 4.5, 5, 1, 12])*1e-5
# v2 = array([7, 5, 4.5, 3, 2, 1])*1e-5
# v3 = array([1.7, 1.45, 1.25, 0.94, 0.73, 0.38, 0.10])*1e-3
# v4 = array([4.16, 3.66, 3.04, 2.22, 1.83, 0.97, 0.38])*1e-3
# a4 = array([2.014, 1.779, 1.482, 1.082, 0.893, 0.473, 0.186])
# a3 = array([2.007, 1.757, 1.517, 1.140, 0.885, 0.467, 0.118])
# a2 = array([2.01, 1.512, 1.263, 0.755, 0.51, 0.258])
# a1 = array([1.514, 1.013, 0.759, 0.507, 0.159, 2.01])
#
# R1 = v1/a1
# print('alum', R1)
# print(average(R1))
#
# R2 = v2/a2
# print('cobber', R2)
# print(average(R2))
#
# R3 = v3/a3
# print('cobber topunkt', R3)
# print(average(R3))
#
# R4 = v4/a4
# print('alum topiunkt', R4)
# print(average(R4))
#
# print(average(R3)/average(R2))
#
# print(average(R4)/average(R1))



# opg 1

v = array([8.911, 6.227, 4.442, 3.115, 2.12, 1.516, 1.1041, 0.7663])
t = array([0, 30, 60, 90, 120, 150, 180, 210])
ddd = polyfit(t, log(v), 1)
scatter(t, log(v))
print 1. / ddd[0]
xxx = linspace(0, 210, 1000)
xlabel('time [s]')
ylabel('log(voltage) [V]')
plot(xxx, ddd[0]*xxx+ddd[1])
show()





# opg 2
# i = array([17.3, 12.37, 8.736, 7.302, 5.862])*1e-3
# u = array([273, 197, 138.8, 116, 93.11])*1e-3
# print(polyfit(i,u,1))
#
# scatter(i,u)
# show()






#opg 3
v = array([158, 200, 275, 350, 510])*1e-3
r = array([1, 1.5, 2.5, 4, 10])
xlabel('voltage [V]')
ylabel('current [A]')
scatter(v/r, v)
print(polyfit(v/r, v, 1))
show()
