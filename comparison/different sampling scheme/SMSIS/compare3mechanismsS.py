import matplotlib.pyplot as plt
import numpy as np

'''
S
'''
data = np.loadtxt('Experimental_of_S.txt')

epsilon = data[:, 0]  
numericalsimulation = data[:, 1]

# plt.figure(figsize=(6,4))

plt.plot(epsilon, numericalsimulation, color='g', marker ='h', markerfacecolor='none', linewidth=1, markersize=10, linestyle='-', label='Simmons($\pi_B=0.5$)')


'''
MS
'''

data = np.loadtxt('Experimental_of_MS.txt')

epsilon = data[:, 0]  
numericalsimulation = data[:, 1]

plt.plot(epsilon, numericalsimulation, color='g', marker ='H', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Modified Simmons($\pi_B=0.5$)')


'''
IS
'''
data = np.loadtxt('Experimental_of_IS.txt')

epsilon = data[:, 0]  
numericalsimulation = data[:, 1]

plt.plot(epsilon, numericalsimulation, color='g', marker ='o', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Improved Simmons($\pi_B=0.5$)')


plt.xlim(0.2,1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.legend()
plt.xlabel('privacy budget($\epsilon$)')
plt.ylabel('variance')
plt.title('Comparison under different sampling schemes')
plt.savefig('SMSIS.pdf')

plt.show()
