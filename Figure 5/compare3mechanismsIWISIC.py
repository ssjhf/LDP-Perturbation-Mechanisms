import matplotlib.pyplot as plt
import numpy as np

'''
IW
'''
data = np.loadtxt('Experimental_IW.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1] 
numericalsimulation = data[:, 2]  

# plt.figure(figsize=(6,4))

plt.plot(epsilon, numericalsimulation, color='g', marker ='^', markerfacecolor='none', linewidth=1, markersize=10, linestyle=':', label='Improved Warner/Simmons_($\pi_B=1/2$)(numerical simulation)')


# '''
# IS
# '''
#
# data = np.loadtxt('Experimental_S_pi_B=0.25.txt')  
#
# epsilon = data[:, 0]  
# theoryanalysis = data[:, 1]  
# numericalsimulation = data[:, 2]
#
# plt.plot(epsilon, numericalsimulation, color='b', marker ='h', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Improved Simmons($\pi_B=1/2$)($\pi_B$=0.25, numerical simulation)')

'''
IC
'''
data = np.loadtxt('Experimental_IC_L=3_p2=0.25.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon, numericalsimulation, color='k', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Improved Christofides($p_2$=0.25, numerical simulation)')

data = np.loadtxt('Experimental_IC_L=3_p2=0.5.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon, numericalsimulation, color='k', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='Improved Christofides($p_2$=0.50, numerical simulation)')

data = np.loadtxt('Experimental_IC_L=3_p2=0.75.txt')  
epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon, numericalsimulation, color='k', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Improved Christofides($p_2$=0.75, numerical simulation)')


plt.xlim(0.2,1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.legend()
plt.xlabel('privacy budget($\epsilon$)')
plt.ylabel('variance')
plt.title('Comparison under the same sampling scheme')
plt.savefig('IWISIC.pdf')

plt.show()
