import numpy as np
health_insurance = np.loadtxt('health_insurance.dat')
health_insurance=2-health_insurance
input_list = health_insurance.T
pi_A = sum(input_list)/len(input_list)
print(pi_A)
y = pi_A*(1-pi_A)
print(np.log((1+4*y)/(1-4*y)))


x = np.exp(0.2)
N = len(health_insurance)
print(N*(x-1)*(1+4*y)/2/(N-1)/x)