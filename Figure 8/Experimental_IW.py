import numpy as np
import matplotlib.pyplot as plt
import math


health_insurance = np.loadtxt('health_insurance.dat')
health_insurance=2-health_insurance
input_list = health_insurance.T
pi_A = sum(input_list)/len(input_list)
M = len(input_list)
N = len(input_list)
num_of_epsilon = 9
epsilon = np.linspace(0.2, 1,num_of_epsilon)
exp_of_epsilon = np.exp(epsilon)

'''
Improved Warner, theorical analysis
'''
opt_epsilon = [0] * num_of_epsilon
var_IW_Theory_Analysis = [0] * num_of_epsilon
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
            var_epsilon[a] = (4 * pi_A * (1 - pi_A) * p_Warner[i]*(1-p_Warner[i])/((2*p_Warner[i]-1)**2)) * epsilon_a / (N - 1)
    var_epsilon[var_epsilon == 0] = 9999
    [A] = np.unravel_index(np.argmin(var_epsilon), var_epsilon.shape)
    opt_epsilon[i] = np.log(np.max([card1[A] / card2[A], card2[A] / card1[A]]))
    p_real_Warner[i] = card1[A] / M
    var_IW_Theory_Analysis[i] = 4 * pi_A * (1 - pi_A) * p_real_Warner[i]*(1-p_real_Warner[i])/((2*p_real_Warner[i]-1)**2) / (N-1)
plt.plot(opt_epsilon, var_IW_Theory_Analysis, color='r', marker ='*', linewidth=1, markerfacecolor='r', markersize=8, linestyle='--', label='improved Warner(thepretical analysis)')

'''
Improved Warner, numerical simulation
'''
input_list = np.zeros(N)
input_list[:round(pi_A*N)] = 1
REPEAT_TIMES = 10000
var_IW_Numerical_Simulation = [0] * num_of_epsilon
mean_proportion = [0] * REPEAT_TIMES
q = np.zeros((len(epsilon), 3))
bound_of_rate = np.exp(epsilon)
p_Warner = 1 / (bound_of_rate + 1)
p = np.vstack((p_Warner, 1- p_Warner)).T
for i in range(len(epsilon)):
    for l in range(1, 3):
        q[i, l] = np.sum(p[i, :l])
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
            var_epsilon[a] = (4 * pi_A * (1 - pi_A) * p_Warner[i]*(1-p_Warner[i])/((2*p_Warner[i]-1)**2)) * epsilon_a / (N - 1)
    var_epsilon[var_epsilon == 0] = 9999
    [A] = np.unravel_index(np.argmin(var_epsilon), var_epsilon.shape)
    opt_epsilon[i] = np.log(np.max([card1[A] / card2[A], card2[A] / card1[A]]))
    p_real_Warner[i] = card1[A] / M
    cards = [1] * int(card1[A]) + [2] * int(card2[A])
    cards = np.array(cards)
    for epoch in range(REPEAT_TIMES):
        if epoch % 1000 == 0:
            print(epoch)
        card_draw = cards[np.random.permutation(len(input_list))]
        answer = (3 - card_draw) * input_list + card_draw * (1 - input_list)
        mean_proportion[epoch] = (np.mean(answer) - 1 + p_real_Warner[i]) / (2*p_real_Warner[i] - 1)

    var_IW_Numerical_Simulation[i] = np.var(mean_proportion)
plt.plot(opt_epsilon, var_IW_Numerical_Simulation, color='r', marker ='o', linewidth=1, markerfacecolor='none', markersize=10, linestyle='dashed', label='improved Warner(numerical simulation)')

plt.xlim(0.2, 1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.xlabel('privacy budget $(\epsilon)$')
plt.ylabel('variance')
plt.title('Experimental verification of theory')
plt.legend()
plt.show()

with open('Experimental_IW.txt', 'w') as file:
    for i in range(len(opt_epsilon)):
        line = f"{opt_epsilon[i]}\t{var_IW_Theory_Analysis[i]}\t{var_IW_Numerical_Simulation[i]}\n"  

