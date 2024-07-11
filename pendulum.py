import numpy as np
import matplotlib.pyplot as plt

g = 9.8
L = 11      #pendulum length
mu = 0.1    #resistance e.g air 

THETA_0 = np.pi / 3 #initial position
THETA_DOT_0 = 0     #no initial velocity

def getThetaDoubleDot(thetaRad, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(thetaRad)

def theta(t):
    theta = THETA_0
    theta_dot = THETA_DOT_0
    delta_t = 0.01
    
    for time in np.arange(0, t, delta_t):
        theta_double_dot = getThetaDoubleDot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
    
    return theta

rads = []

x_plot = []
y_plot = []

for i in np.arange(0, 50, 0.1):
    x_plot.append(i)
    y_plot.append(theta(i))

plt.plot(x_plot, y_plot)

plt.axis([-1, 51, -2, 2])
plt.xlabel("time(s)")
plt.ylabel("degree(rad)")
plt.title("Grafik Fungsi Pendulum")

plt.show()