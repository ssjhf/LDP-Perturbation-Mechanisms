import matplotlib.pyplot as plt
import numpy as np

'''
MS
'''
data = np.loadtxt('Experimental_of_MS_N=1000_pi_A=0.04.txt')

epsilon = data[:, 0]  
numericalsimulation = data[:, 1]

# plt.figure(figsize=(6,4))

plt.plot(epsilon, numericalsimulation, color='g', marker ='.', markerfacecolor='none', linewidth=1, markersize=10, linestyle=':', label='mofidied Simmons($\pi_B=0.5,\pi_A=0.04$)')

'''
IS
'''
data = np.loadtxt('Experimental_of_IS_N=1000_pi_A=0.04.txt')

epsilon = data[:, 0]
numericalsimulation = data[:, 1]

# plt.figure(figsize=(6,4))

plt.plot(epsilon, numericalsimulation, color='g', marker ='.', markerfacecolor='none', linewidth=1, markersize=10, linestyle='-.', label='improved Simmons($\pi_B=0.5,\pi_A=0.04$)')
#
#
# '''
# IS
# '''
#
# data = np.loadtxt('Experimental_of_IS_N=1000_pi_A=0.1.txt')
#
# epsilon = data[:, 0]
# numericalsimulation = data[:, 1]
#
# plt.plot(epsilon, numericalsimulation, color='g', marker ='none', linewidth=1, markerfacecolor='g', markersize=10, linestyle='--', label='improved Simmons($\pi_B=0.5,\pi_A=0.1$)')
#

'''
IS
'''
data = np.loadtxt('Experimental_of_MS_N=1000_pi_A=0.5.txt')

epsilon = data[:, 0]
numericalsimulation = data[:, 1]

plt.plot(epsilon, numericalsimulation, color='g', marker ='none', linewidth=1, markerfacecolor='r', markersize=10, linestyle='--', label='modified Simmons($\pi_B=0.5,\pi_A=0.05$)')

'''
IS
'''
data = np.loadtxt('Experimental_of_IS_N=1000_pi_A=0.5.txt')

epsilon = data[:, 0]
numericalsimulation = data[:, 1]

plt.plot(epsilon, numericalsimulation, color='g', marker ='none', linewidth=1, markerfacecolor='k', markersize=10, linestyle='-', label='improved Simmons($\pi_B=0.5,\pi_A=0.5$)')


plt.xlim(5, 10)
plt.ylim(0, 0.000005)
plt.xticks(np.linspace(5, 10, num=10))
plt.legend()
plt.xlabel('privacy budget($\epsilon$)')
plt.ylabel('variance')
plt.title('Comparison under different sampling schemes')
plt.savefig('MSIS.pdf')

plt.show()
