import numpy as np
import matplotlib.pyplot as plt
import math


pi_A = 0.04
M = 10000
N = 10000
num_of_epsilon = 9
epsilon = np.linspace(0.2, 1,num_of_epsilon)
exp_of_epsilon = np.exp(epsilon)

'''
Improved Christofides, L=3, theoretical analysis
'''
L = 3
opt_epsilon = [0] * num_of_epsilon
var_IC_Theory_Analysis_L3 = [0] * num_of_epsilon
bound_of_rate = np.exp(epsilon)
p2 = 0.36
p1 = bound_of_rate / (bound_of_rate + 1) * (1 - p2)
p3 = 1 / (bound_of_rate + 1) * (1 - p2)
for i in range(num_of_epsilon):
    print(i)

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
            var_epsilon[a,b] = (4 * pi_A * (1 - pi_A) * DY[a, b] / (L + 1 - 2 * EY[a, b]) / (L + 1 - 2 * EY[a, b]) / (N-1)) * epsilon_ab
    var_epsilon[var_epsilon == 0] = 9999
    [A,B] = np.unravel_index(np.argmin(var_epsilon), var_epsilon.shape)
    opt_epsilon[i] = np.log(np.max([card1[A]/card3[B],card3[B]/card1[A]]))
    var_IC_Theory_Analysis_L3[i] = 4 * pi_A * (1 - pi_A) * DY[A, B] / (L + 1 - 2 * EY[A, B]) / (L + 1 - 2 * EY[A, B]) / (N-1)
plt.plot(opt_epsilon, var_IC_Theory_Analysis_L3, color='r', marker ='*', linewidth=1, markerfacecolor='r', markersize=8, linestyle='--', label='improved Christofides(L=3, thepretical analysis)')

'''
Improved Christofides, L=3, numerical simulation
'''
input_list = np.zeros(N)
input_list[:round(pi_A*N)] = 1
REPEAT_TIMES = 10000
var_IC_Numerical_Simulation_L3 = [0] * num_of_epsilon
mean_proportion = [0] * REPEAT_TIMES
q = np.zeros((len(epsilon), L + 1))
bound_of_rate = np.exp(epsilon)
p2 = 0.36
p1 = bound_of_rate / (bound_of_rate + 1) * (1 - p2)
p3 = 1 / (bound_of_rate + 1) * (1 - p2)
p = np.vstack((p1, 1 - p1 - p3, p3)).T
for i in range(len(epsilon)):
    for l in range(1, L + 1):
        q[i, l] = np.sum(p[i, :l])
for i in range(num_of_epsilon):
    print(i)

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
            var_epsilon[a,b] = (4 * pi_A * (1 - pi_A) * DY[a, b] / (L + 1 - 2 * EY[a, b]) / (L + 1 - 2 * EY[a, b]) / (N-1)) * epsilon_ab
    var_epsilon[var_epsilon == 0] = 9999
    [A,B] = np.unravel_index(np.argmin(var_epsilon), var_epsilon.shape)
    opt_epsilon[i] = np.log(np.max([card1[A] / card3[B], card3[B] / card1[A]]))
    cards = [1] * int(card1[A]) + [2] * int(card2[A,B]) + [3] * int(card3[B])
    cards = np.array(cards)
    for epoch in range(REPEAT_TIMES):
        if epoch % 1000 == 0:
            print(epoch)
        card_draw = cards[np.random.permutation(len(input_list))]
        answer = (L + 1 - card_draw) * input_list + card_draw * (1 - input_list)
        mean_proportion[epoch] = (np.mean(answer) - EY[A, B]) / (L + 1 - 2 * EY[A, B])

    var_IC_Numerical_Simulation_L3[i] = np.var(mean_proportion)
plt.plot(opt_epsilon, var_IC_Numerical_Simulation_L3, color='r', marker ='o', linewidth=1, markerfacecolor='none', markersize=10, linestyle='dashed', label='improved Christofides(L=3, numerical simulation)')

plt.xlim(0.2, 1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.xlabel('privacy budget $(\epsilon)$')
plt.ylabel('variance')
plt.title('Experimental verification of theory')
plt.legend()
plt.show()

with open('Experimental_IC_L=3.txt', 'w') as file:
    for i in range(len(opt_epsilon)):
        line = f"{opt_epsilon[i]}\t{var_IC_Theory_Analysis_L3[i]}\t{var_IC_Numerical_Simulation_L3[i]}\n"  
        file.write(line)

