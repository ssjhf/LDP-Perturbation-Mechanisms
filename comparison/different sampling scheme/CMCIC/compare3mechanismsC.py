import matplotlib.pyplot as plt
import numpy as np

'''
C
'''
data = np.loadtxt('Experimental_C_L=3.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

# plt.figure(figsize=(6,4))

plt.plot(epsilon, numericalsimulation, color='r', marker ='d', markerfacecolor='none', linewidth=1, markersize=10, linestyle='-', label='Christofides(L=3)')


'''
MC
'''

data = np.loadtxt('Experimental_MC_L=3.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon, numericalsimulation, color='r', marker ='D', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Modified Christofides(L=3)')


'''
IC
'''
data = np.loadtxt('Experimental_IC_L=3.txt')  

epsilon = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon, numericalsimulation, color='r', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Improved Christofides(L=3)')


plt.xlim(0.2,1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.legend()
plt.xlabel('privacy budget($\epsilon$)')
plt.ylabel('variance')
plt.title('Comparison under different sampling schemes')
plt.savefig('CMCIC.pdf')

plt.show()
