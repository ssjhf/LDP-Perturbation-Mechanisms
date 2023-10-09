import matplotlib.pyplot as plt
import numpy as np

'''
W
'''
data = np.loadtxt('Experimental_W.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

# plt.figure(figsize=(6,4))

plt.plot(epsilon, numericalsimulation, color='#FF8C00', marker ='.', markerfacecolor='#FF8C00', linewidth=1, markersize=10, linestyle=':', label='Warner/Simmons_($\pi_B=1/2$)(numerical simulation)')


# '''
# S
# '''
#
# data = np.loadtxt('Experimental_S_pi_B=0.25.txt')  
#
# epsilon = data[:, 0]  
# theoryanalysis = data[:, 1]  
# numericalsimulation = data[:, 2]  
#
# plt.plot(epsilon, numericalsimulation, color='b', marker ='h', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Simmons($\pi_B=1/2$)($\pi_B$=0.25, numerical simulation)')

'''
C
'''
data = np.loadtxt('Experimental_C_L=3_p2=0.25.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon, numericalsimulation, color='b', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Christofides($p_2$=0.25, numerical simulation)')

data = np.loadtxt('Experimental_C_L=3_p2=0.5.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2] 

plt.plot(epsilon, numericalsimulation, color='b', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='Christofides($p_2$=0.50, numerical simulation)')

data = np.loadtxt('Experimental_C_L=3_p2=0.75.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon, numericalsimulation, color='b', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Christofides($p_2$=0.75, numerical simulation)')


plt.xlim(0.2,1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.legend()
plt.xlabel('privacy budget($\epsilon$)')
plt.ylabel('variance')
plt.title('Comparison under the same sampling scheme')
plt.savefig('WSC.pdf')

plt.show()
