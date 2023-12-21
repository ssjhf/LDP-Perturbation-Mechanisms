import numpy as np
import matplotlib.pyplot as plt
import math


pi_A = 0.05
N = 10000
num_of_epsilon = 9
epsilon = np.linspace(0.2, 1,num_of_epsilon)
exp_of_epsilon = np.exp(epsilon)

'''
IKUK, theoretical analysis
'''
var_IKUK_Theory_Analysis = [0] * num_of_epsilon
for i in range(num_of_epsilon):
    print(i)
    var_IKUK_Theory_Analysis[i] = pi_A * (1 - pi_A)*(-exp_of_epsilon**2+2*exp_of_epsilon+1)/(2*exp_of_epsilon - 1)/(N-1)
plt.plot(epsilon, var_IKUK_Theory_Analysis, color='b', marker ='*', linewidth=1, markerfacecolor='b', markersize=8, linestyle='--', label='improved Warner(thepretical analysis)')

'''
IKUK, numerical simulation
'''
input_list = np.zeros(N)
input_list[:round(pi_A*N)] = 1
REPEAT_TIMES = 10000
p_Warner = 1 / (np.exp(epsilon) + 1)
var_MW_Numerical_Simulation = np.zeros(len(epsilon))

for j in range(len(epsilon)):
    print(j)
    mean_proportion = np.zeros(REPEAT_TIMES)
    for times in range(REPEAT_TIMES):
        if (times%100==0):
            print(times)
        np.random.shuffle(input_list)
        rand_num = np.random.rand(N)
        output_list = np.where(rand_num < p_real_Warner[j], input_list, 1 - input_list)
        lambda_val = np.mean(output_list)
        mean_proportion[times] = (lambda_val - (1 - p_real_Warner[j])) / (2 * p_real_Warner[j] - 1)
    var_MW_Numerical_Simulation[j] = np.var(mean_proportion)
plt.plot(opt_epsilon, var_MW_Numerical_Simulation, color='b', marker ='o', markerfacecolor='none', linewidth=1, markersize=10, linestyle='--', label='modified Warner(numerical simulation)')
plt.xlim(0.2,1)
plt.xticks(np.linspace(0.2,1, num=num_of_epsilon))
plt.xlabel('privacy budget $(\epsilon)$')
plt.ylabel('variance')
plt.legend()
plt.show()

with open('Experimental_verification_of_theory_W.txt', 'w') as file:
    for i in range(len(epsilon)):
        line = f"{epsilon[i]}\t{var_W_Theory_Analysis[i]}\t{var_MW_Numerical_Simulation[i]}\n"
        file.write(line)

