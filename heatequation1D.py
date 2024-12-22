import numpy as np
import matplotlib.pyplot as plt

#defining our problem

a = 110 #mm²/s
length = 50 #mm
time = 8 #seconds
nodes = 30

#initialisation

dx = length / nodes
dt = 0.5 * dx**2 / a
t_nodes= int(time / dt)

u = np.zeros(nodes) + 20 #we define a plate initially at 20 celcius 

#Boundary conditions

u[0] = 100
u[-1] = 100

#Visualizing
fig, axis = plt.subplots()
pcm = axis.pcolormesh([u], cmap = plt.cm.jet, vmin=0, vmax= 100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2, 3])

#Simulating

counter = 0 

while counter < time :
    w = u.copy()

    for i in range(1 , nodes -1):

        u[i] = dt * a * (w[i - 1 ] -2 * w[i] + w[i + 1]) / dx ** 2 + w[i]
    
    counter += dt

    print("t: {:.3f} [s], Average Temperature: {:.2f} Celcius" .format(counter, np.average(u)))

    #Updating the ploot:
    pcm.set_array([u])
    axis.set_title("Distribution at t : {:.3f} [s].".format(counter))
    plt.pause(0.01)

plt.show()