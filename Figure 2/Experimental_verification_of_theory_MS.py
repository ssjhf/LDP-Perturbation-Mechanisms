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
Modified Simmons, theoretical analysis
'''
pi_B = 0.5
opt_epsilon = [0] * num_of_epsilon
var_MS_Theory_Analysis = [0] * num_of_epsilon
bound_of_rate = np.exp(epsilon)
p_Simmons = (np.exp(epsilon) - 1)*pi_B / ((np.exp(epsilon) - 1)*pi_B + 1)
# p_Simmons = (np.exp(epsilon) - 1)*(1-pi_B) / ((np.exp(epsilon) - 1)*(1-pi_B) + 1)
p_real_Simmons = [0] * num_of_epsilon
for i in range(num_of_epsilon):
    print(i)

    card11 = [round(p_Simmons[i] * M)]
    card12 = [math.ceil(p_Simmons[i] * M)]
    card13 = [math.floor(p_Simmons[i] * M)]

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
            var_epsilon[a] = ((pi_B*(1-p_Simmons[i])-pi_B*(1-p_Simmons[i])*pi_B*(1-p_Simmons[i])) /p_Simmons[i]/p_Simmons[i]/ N) * epsilon_a
    var_epsilon[var_epsilon == 0] = 9999
    [A] = np.unravel_index(np.argmin(var_epsilon), var_epsilon.shape)
    p_real_Simmons[i] = card1[A] / M
    opt_epsilon[i] = np.log(p_real_Simmons[i]/(1-p_real_Simmons[i])/pi_B+1)
    # opt_epsilon[i] = np.log(p_real_Simmons[i]/(1-p_real_Simmons[i])/(1-pi_B)+1)
    var_MS_Theory_Analysis[i] = (pi_B * (1 - p_Simmons[i]) - pi_B * (1 - p_Simmons[i]) * pi_B * (1 - p_Simmons[i])) / p_Simmons[i] / p_Simmons[i] / N
plt.plot(opt_epsilon, var_MS_Theory_Analysis, color='b', marker ='*', linewidth=1, markerfacecolor='b', markersize=8, linestyle='--', label='modified Simmons(thepretical analysis)')

'''
Modified Simmons, numerical simulation
'''
'''
numerical simulation
'''
input_list = np.zeros(N)
input_list[:round(pi_A*N)] = 1
REPEAT_TIMES = 10000
p_Simmons = (np.exp(epsilon) - 1)*pi_B / ((np.exp(epsilon) - 1)*pi_B + 1)
# p_Simmons = (np.exp(epsilon) - 1)*(1-pi_B) / ((np.exp(epsilon) - 1)*(1-pi_B) + 1)
var_MS_Numerical_Simulation = np.zeros(len(epsilon))

for j in range(len(epsilon)):
    print(j)
    mean_proportion = np.zeros(REPEAT_TIMES)
    for times in range(REPEAT_TIMES):
        if (times%1000==0):
            print(times)
        rand_num = np.random.rand(N)
        u_vector = np.random.random(len(input_list))
        v_vector = np.random.random(len(input_list))
        output_list = np.where(u_vector < p_real_Simmons[j], input_list, np.where(v_vector < pi_B, 1, 0))
        lambda_val = np.mean(output_list)
        mean_proportion[times] = (lambda_val - (1 - p_real_Simmons[j])*pi_B) / p_real_Simmons[j]
    var_MS_Numerical_Simulation[j] = np.var(mean_proportion)

plt.plot(opt_epsilon, var_MS_Numerical_Simulation, color='b', marker ='o', markerfacecolor='none', linewidth=1, markersize=10, linestyle='--', label='modified Simmons(numerical simulation)')
plt.xlim(0.2,1)
plt.xticks(np.linspace(0.2,1, num=num_of_epsilon))
plt.xlabel('privacy budget $(\epsilon)$')
plt.ylabel('variance')
plt.legend()
plt.show()


with open('Experimental_verification_of_theory_MS.txt', 'w') as file:
    for i in range(len(epsilon)):
        line = f"{epsilon[i]}\t{var_MS_Theory_Analysis[i]}\t{var_MS_Numerical_Simulation[i]}\n"  
        file.write(line)

