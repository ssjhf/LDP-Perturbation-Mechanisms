import numpy as np
import matplotlib.pyplot as plt
import math

pi_A = 0.05
M = 10000
N = 10000
num_of_epsilon = 9
epsilon = np.linspace(0.2, 1,num_of_epsilon)
exp_of_epsilon = np.exp(epsilon)

'''
Warner, theoretical analysis
'''
opt_epsilon = [0] * num_of_epsilon
var_W_Theory_Analysis = [0] * num_of_epsilon
bound_of_rate = np.exp(epsilon)
p_Warner = 1 / (bound_of_rate + 1)
p_real_Warner = [0] * num_of_epsilon
for i in range(num_of_epsilon):
    print(i)

    card11 = [round(p_Warner[i] * M)]
    card12 = [math.ceil(p_Warner[i] * M)]
    card13 = [math.floor(p_Warner[i] * M)]

    card1 = card11+card12+card13
    shape = (3)
    card2 = np.zeros(shape)
    var_epsilon = np.zeros(shape)
    for a in range(3):
        for b in range(3):
            epsilon_a = 0
            card2[a] = M - card1[a]
            if card1[a] > 0 and card2[a] >0 and (np.max([card1[a]/card2[a],card2[a]/card1[a]])) <= bound_of_rate[i]:
                epsilon_a = np.log(np.max([card1[a] / card2[a], card2[a] / card1[a]]))
            var_epsilon[a] = (p_Warner[i]*(1-p_Warner[i])/((2*p_Warner[i]-1)**2)) * epsilon_a / N
    var_epsilon[var_epsilon == 0] = 9999
    [A] = np.unravel_index(np.argmin(var_epsilon), var_epsilon.shape)
    opt_epsilon[i] = np.log(np.max([card1[A] / card2[A], card2[A] / card1[A]]))
    p_real_Warner[i] = card1[A] / M
    var_W_Theory_Analysis[i] = pi_A * (1 - pi_A) / N + p_real_Warner[i] * (1 - p_real_Warner[i]) / ((2 * p_real_Warner[i] - 1) ** 2) / N
plt.plot(opt_epsilon, var_W_Theory_Analysis, color='b', marker ='*', linewidth=1, markerfacecolor='b', markersize=8, linestyle='--', label='improved Warner(thepretical analysis)')

'''
Warner, numerical simulation
'''
'''
numerical simulation
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

