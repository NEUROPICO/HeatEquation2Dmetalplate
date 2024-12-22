import numpy as np
import matplotlib.pyplot as plt

#defining our problem

a = 110 #mm²/s
length = 50 #mm
time = 4 
nodes = 40

#initialisation

dx = length / nodes
dy = length / nodes
dt = min ( dx**2 / (4 * a), dy**2 / (4 * a))
t_nodes= int(time / dt)

u = np.zeros((nodes, nodes)) + 20 #we define a plate initially at 20 celcius 

#Boundary conditions

u[0, :] = 100
u[-1, :] = 100
u[:, 0] = 100
u[:, -1] = 100
#Visualizing
fig, axis = plt.subplots()
pcm = axis.pcolormesh(u, cmap = plt.cm.jet, vmin=0, vmax= 100)
plt.colorbar(pcm, ax=axis)

#Simulating

counter = 0 

while counter < time :
    w = u.copy()

    for i in range(1 , nodes -1):
        for j in range(1, nodes -1):
            
            dd_ux= (w[i- 1, j]- 2 * w[i,j]+ w[i+ 1, j]) /dx**2
            dd_uy= (w[i, j-1]- 2 * w[i,j]+ w[i, j +1]) /dy**2
            u[i,j] = dt * a * (dd_ux + dd_uy) + w[i, j]
    
    counter += dt

    print("t: {:.3f} [s], Average Temperature: {:.2f} Celcius" .format(counter, np.average(u)))

    #Updating the ploot:
    pcm.set_array(u)
    axis.set_title("Distribution at t : {:.3f} ".format(counter))
    plt.pause(0.01)

plt.show()