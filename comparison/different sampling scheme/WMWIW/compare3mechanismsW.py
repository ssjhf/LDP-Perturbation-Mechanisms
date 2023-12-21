import matplotlib.pyplot as plt
import numpy as np

'''
C
'''
data = np.loadtxt('Experimental_W.txt')

epsilon = data[:, 0]  
numericalsimulation = data[:, 1]

# plt.figure(figsize=(6,4))

plt.plot(epsilon, numericalsimulation, color='b', marker ='v', markerfacecolor='none', linewidth=1, markersize=10, linestyle='-', label='Warner')


'''
MC
'''

data = np.loadtxt('Experimental_MW.txt')

epsilon = data[:, 0]  
numericalsimulation = data[:, 1]

plt.plot(epsilon, numericalsimulation, color='b', marker ='>', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Modified Warner')


'''
IC
'''
data = np.loadtxt('Experimental_IW.txt')

epsilon = data[:, 0]  
numericalsimulation = data[:, 1]

plt.plot(epsilon, numericalsimulation, color='b', marker ='^', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Improved Warner')


plt.xlim(0.2,1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.legend()
plt.xlabel('privacy budget($\epsilon$)')
plt.ylabel('variance')
plt.title('Comparison under different sampling schemes')
plt.savefig('WMWIW.pdf')

plt.show()
