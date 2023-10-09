import matplotlib.pyplot as plt
import numpy as np

# '''
# Warner
# '''
# data = np.loadtxt('Experimental_verification_of_theory_W.txt')  
#
# epsilon_Warner = data[:, 0]  
# theoryanalysis = data[:, 1]  
# numericalsimulation = data[:, 2]  
#
# # plt.figure(figsize=(6,8))
#

# plt.plot(epsilon_Warner, theoryanalysis, color='b', marker ='*', markerfacecolor='b', linewidth=1, markersize=8, linestyle=':', label='Warner/Simmons_($\pi_B=1/2$)(Theory)')
# plt.plot(epsilon_Warner, numericalsimulation, color='b', marker ='o', markerfacecolor='none', linewidth=1, markersize=10, linestyle=':', label='Warner/Simmons_($\pi_B=1/2$)(Numerical)')

# '''
# Simmons_($\pi_B=1/2$)
# '''

# data = np.loadtxt('Experimental_verification_of_theory_MS.txt')  

#
# epsilon_S = data[:, 0]  
# theoryanalysis = data[:, 1]  
# numericalsimulation = data[:, 2]  
#
# # plt.figure(figsize=(6,8))
#

# plt.plot(epsilon_S, theoryanalysis, color='b', marker ='*', markerfacecolor='b', linewidth=1, markersize=8, linestyle=':', label='Simmons_($\pi_B=1/2$)(Theory)')
# plt.plot(epsilon_S, numericalsimulation, color='b', marker ='h', markerfacecolor='none', linewidth=1, markersize=10, linestyle=':', label='Simmons_($\pi_B=1/2$)(Numerical)')


# '''
# C
# '''

# data = np.loadtxt('Experimental_verification_of_theory_C_L=3.txt')  

#
# epsilon_MC_L3 = data[:, 0]  
# theoryanalysis = data[:, 1]  
# numericalsimulation = data[:, 2]  
#

# plt.plot(epsilon_MC_L3, theoryanalysis, color='b', marker ='*', linewidth=1, markerfacecolor='b', markersize=8, linestyle=':', label='Christofides(L=3, Theory)')
# plt.plot(epsilon_MC_L3, numericalsimulation, color='b', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Christofides(L=3, Numerical)')





'''
MW
'''

data = np.loadtxt('Experimental_MW.txt')  

epsilon_Warner = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

# plt.figure(figsize=(6,4))

plt.plot(epsilon_Warner, numericalsimulation, color='b', marker ='^', markerfacecolor='none', linewidth=1, markersize=10, linestyle='--', label='modified Warner/Simmons_($\pi_B=1/2$)(Numerical)')


'''
MC
'''
data = np.loadtxt('Experimental_MC_L=3.txt')  


epsilon_MC_L3 = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon_MC_L3, numericalsimulation, color='r', marker ='o', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='modified Christofides(L=3, Numerical)')



'''
IW
'''
data = np.loadtxt('Experimental_IW.txt')  

epsilon_IW = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon_IW, numericalsimulation, color='g', marker ='D', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='improved Warner/Simmons_($\pi_B=1/2$)(Numerical)')

# '''
# MS
# '''
# data = np.loadtxt('Experimental_verification_of_theory_MS.txt')  
#
# epsilon_MS = data[:, 0]  
# theoryanalysis = data[:, 1]  
# numericalsimulation = data[:, 2]  
#
# # plt.figure(figsize=(6,8))
#
# plt.plot(epsilon_MS, theoryanalysis, color='g', marker ='*', markerfacecolor='g', linewidth=1, markersize=8, linestyle='--', label='modified Simmons_($\pi_B=1/2$)(Theory)')
# plt.plot(epsilon_MS, numericalsimulation, color='g', marker ='o', markerfacecolor='none', linewidth=1, markersize=10, linestyle='--', label='modified Simmons_($\pi_B=1/2$)(Numerical)')





'''
IC
'''
data = np.loadtxt('Experimental_IC_L=3.txt')  

epsilon_IC_L3 = data[:, 0]  
theoryanalysis = data[:, 1]  
numericalsimulation = data[:, 2]  

plt.plot(epsilon_IC_L3, numericalsimulation, color='k', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='improved Christofides(L=3, Numerical)')

# Adjust the legend display
plt.legend(ncol=1)

# Set the x and y axis limits and ticks
plt.xlim(0.2, 1)
plt.ylim(0, 0.00002)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon_IC_L3)))
plt.yticks(np.linspace(0, 0.00002, num=6))

# Set the axis labels and title
plt.xlabel('Privacy Budget ($\epsilon$)')
plt.ylabel('Variance')
plt.title('Comparison of mechanisms')
plt.savefig('compare6mechanisms.pdf', dpi=100)

# Display the plot
plt.show()
