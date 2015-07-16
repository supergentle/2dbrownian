from scipy.integrate import odeint
import time
import numpy as np

tinit = time.time()

def tdb(z, t):
	mu = 1
	r = 0
	phi = np.pi/2
	ex1 = 3
	ex2 = 0
	ey1 = 0
	ey2 = 3.5

	return np.array([z[1], (1/mu)*(-r*z[1] + np.sin(z[0])*(1+np.cos(z[2])) + ex1*np.sin(t) + ex2*np.sin(2*t+phi)), z[3], (1/mu)*(-r*z[3] + np.cos(z[0])*(2*np.sin(2*z[2])-1) +ey1*np.sin(t) + ey2*np.sin(2*t+phi))])

t = np.linspace(0.0, 1e4, 1e6)
zinit = np.array([0.0, 0.0, 0.0, 0.0])
sol = odeint(tdb, zinit, t)

size = len(sol[:,0])

data = open("tdb.dat", "w")

for i in range(0, size):
	data.write("%f %f %f %f %f\n" %(t[i], sol[i,0], sol[i,1], sol[i,2], sol[i,3]))

data.close()

tfinal = time.time()

print "The simulation time is %f" %(tfinal - tinit)




