import numpy as np
import matplotlib.pyplot as plt
import math
import random

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
Christofides, L=3, theorical analysis
'''

L = 3
opt_epsilon = [0] * num_of_epsilon
var_C_Theory_Analysis_L3 = [0] * num_of_epsilon
for i in range(num_of_epsilon):
    print(i)
    bound_of_rate = np.exp(epsilon)
    p2 = 0.5
    p1 = bound_of_rate / (bound_of_rate + 1) * (1 - p2)
    p3 = 1 / (bound_of_rate + 1) * (1 - p2)

    card11 = [round(p1[i] * M)]
    card12 = [math.ceil(p1[i] * M)]
    card13 = [math.floor(p1[i] * M)]
    card31 = [round(p3[i] * M)]
    card32 = [math.ceil(p3[i] * M)]
    card33 = [math.floor(p3[i] * M)]

    card1 = card11+card12+card13
    card3 = card31+card32+card33
    shape = (3,3)
    card2 = np.zeros(shape)
    EY = np.zeros(shape)
    DY = np.zeros(shape)
    var_epsilon = np.zeros(shape)
    for a in range(3):
        for b in range(3):
            epsilon_ab = 0
            card2[a,b] = M - card1[a] - card3[b]
            if card2[a,b] > 0 and card1[a] > 0 and card3[b] > 0 and (np.max([card1[a]/card3[b],card3[b]/card1[a]])) <= bound_of_rate[i]:
                EY[a,b] = (card1[a] + 2 * card2[a,b] + 3 * card3[b]) / M
                DY[a,b] = (card1[a] + 4 * card2[a,b] + 9 * card3[b]) / M - EY[a, b] * EY[a, b]
                epsilon_ab = np.log(np.max([card1[a]/card3[b],card3[b]/card1[a]]))
            var_epsilon[a,b] = (DY[a, b] / (L + 1 - 2 * EY[a, b]) / (L + 1 - 2 * EY[a, b]) / N) * epsilon_ab
    var_epsilon[var_epsilon == 0] = 9999
    [A,B] = np.unravel_index(np.argmin(var_epsilon), var_epsilon.shape)
    opt_epsilon[i] = np.log(np.max([card1[A]/card3[B],card3[B]/card1[A]]))
    var_C_Theory_Analysis_L3[i] = DY[A, B] / (L + 1 - 2 * EY[A, B]) / (L + 1 - 2 * EY[A, B]) / M
plt.plot(opt_epsilon, var_C_Theory_Analysis_L3, color='g', marker ='*', linewidth=1, markerfacecolor='g', markersize=8, linestyle='--', label='modified Christofides(L=3, theoretical analysis)')

'''
Christofides, L=3, numerical simulation
'''
input_list = np.zeros(N)
input_list[:round(pi_A*N)] = 1
REPEAT_TIMES = 10000
var_C_numerical_simulation_L3 = [0] * num_of_epsilon
mean_proportion = [0] * REPEAT_TIMES
for i in range(num_of_epsilon):
    print(i)
    bound_of_rate = np.exp(epsilon)
    p2 = 0.5
    p1 = bound_of_rate / (bound_of_rate + 1) * (1 - p2)
    p3 = 1 / (bound_of_rate + 1) * (1 - p2)

    card11 = [round(p1[i] * M)]
    card12 = [math.ceil(p1[i] * M)]
    card13 = [math.floor(p1[i] * M)]
    card31 = [round(p3[i] * M)]
    card32 = [math.ceil(p3[i] * M)]
    card33 = [math.floor(p3[i] * M)]

    card1 = card11+card12+card13
    card3 = card31+card32+card33
    shape = (3,3)
    card2 = np.zeros(shape)
    EY = np.zeros(shape)
    DY = np.zeros(shape)
    var_epsilon = np.zeros(shape)
    for a in range(3):
        for b in range(3):
            epsilon_ab = 0
            card2[a,b] = M - card1[a] - card3[b]
            if card2[a,b] > 0 and card1[a] > 0 and card3[b] > 0 and (np.max([card1[a]/card3[b],card3[b]/card1[a]])) <= bound_of_rate[i]:
                EY[a,b] = (card1[a] + 2 * card2[a,b] + 3 * card3[b]) / M
                DY[a,b] = (card1[a] + 4 * card2[a,b] + 9 * card3[b]) / M - EY[a, b] * EY[a, b]
                epsilon_ab = np.log(np.max([card1[a]/card3[b],card3[b]/card1[a]]))
            var_epsilon[a,b] = (DY[a, b] / (L + 1 - 2 * EY[a, b]) / (L + 1 - 2 * EY[a, b]) / N) * epsilon_ab
    var_epsilon[var_epsilon == 0] = 9999
    [A,B] = np.unravel_index(np.argmin(var_epsilon), var_epsilon.shape)
    opt_epsilon[i] = np.log(np.max([card1[A] / card3[B], card3[B] / card1[A]]))
    for epoch in range(REPEAT_TIMES):
        if epoch % 100 == 0:
            print(epoch)
        np.random.shuffle(input_list)
        card_draw = np.zeros((N))
        rand1 = np.random.rand(N)
        card_draw[rand1 < card1[A] / N] = 1
        card_draw[(rand1 >= card1[A] / N) & (rand1 < (card1[A] + card2[A,B]) / N)] = 2
        card_draw[rand1 > (card1[A] + card2[A,B]) / N] = 3

        answer = (L + 1 - card_draw) * input_list + card_draw * (1 - input_list)
        mean_proportion[epoch] = (np.mean(answer) - EY[A, B]) / (L + 1 - 2 * EY[A, B])

    var_C_numerical_simulation_L3[i] = np.var(mean_proportion)
plt.plot(opt_epsilon, var_C_numerical_simulation_L3, color='g', marker ='^', linewidth=1, markerfacecolor='none', markersize=10, linestyle='dashed', label='modified Christofides(L=3, numerical simulation)')

plt.xlim(0.2, 1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.xlabel('privacy budget $(\epsilon)$')
plt.ylabel('variance')
plt.title('Experimental verification of theory')
plt.legend()
plt.show()


with open('Experimental_verification_of_theory_C_L=3.txt', 'w') as file:
    for i in range(len(opt_epsilon)):
        line = f"{opt_epsilon[i]}\t{var_C_Theory_Analysis_L3[i]}\t{var_C_numerical_simulation_L3[i]}\n"  
        file.write(line)

