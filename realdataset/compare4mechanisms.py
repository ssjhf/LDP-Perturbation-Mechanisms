import matplotlib.pyplot as plt
import numpy as np

'''
MW
'''

data = np.loadtxt('Experimental_MW.txt')  

epsilon_Warner = data[:, 0]  
numericalsimulation = data[:, 2]

plt.plot(epsilon_Warner, numericalsimulation, color='b', marker ='>', markerfacecolor='none', linewidth=1, markersize=10, linestyle='--', label='modified Warner')

'''
MS
'''

data = np.loadtxt('Experimental_MS.txt')

epsilon_Warner = data[:, 0]
numericalsimulation = data[:, 2]

plt.plot(epsilon_Warner, numericalsimulation, color='g', marker ='H', markerfacecolor='none', linewidth=1, markersize=10, linestyle='--', label='modified Simmons$(\pi_B=1/2)$')


# '''
# MC
# '''
# data = np.loadtxt('Experimental_MC_L=3.txt')
#
#
# epsilon_MC_L3 = data[:, 0]
# numericalsimulation = data[:, 2]
#
# plt.plot(epsilon_MC_L3, numericalsimulation, color='r', marker ='o', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='modified Christofides(L=3)')



'''
IW
'''
data = np.loadtxt('Experimental_IW.txt')  

epsilon_IW = data[:, 0]  
numericalsimulation = data[:, 2]

plt.plot(epsilon_IW, numericalsimulation, color='b', marker ='^', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='improved Warner')

'''
IS
'''
data = np.loadtxt('Experimental_IS.txt')

epsilon_IS = data[:, 0]
numericalsimulation = data[:, 1]

# plt.figure(figsize=(6,8))

plt.plot(epsilon_IS, numericalsimulation, color='g', marker ='o', markerfacecolor='none', linewidth=1, markersize=10, linestyle='--', label='improved Simmons($\pi_B=1/2$)')

# '''
# IC
# '''
# data = np.loadtxt('Experimental_IC_L=3.txt')
#
# epsilon_IC_L3 = data[:, 0]
# numericalsimulation = data[:, 2]
#
# plt.plot(epsilon_IC_L3, numericalsimulation, color='k', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='improved Christofides(L=3)')

# Adjust the legend display
plt.legend(ncol=1)

# Set the x and y axis limits and ticks
plt.xlim(0.2, 1)
# plt.ylim(0, 0.00002)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon_IS)))
plt.yticks(np.linspace(0, 0.00001, num=6))

# Set the axis labels and title
plt.xlabel('Privacy Budget ($\epsilon$)')
plt.ylabel('Variance')
plt.title('Comparison of mechanisms')
plt.savefig('compare4mechanisms.pdf', dpi=100)

# Display the plot
plt.show()
