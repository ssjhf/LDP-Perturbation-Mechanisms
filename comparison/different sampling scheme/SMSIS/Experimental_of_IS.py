import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

## improved Simmons, numerical simulication
def simulate_cheating_survey(cheating_status, p, N,first_group_cards):

    # 第二组卡片（红色和蓝色，红色为1，蓝色为0）
    second_group_cards = np.array([1] * int(N*p) + [0] * (N - int(N*p)))
    np.random.shuffle(second_group_cards)
    # 学生的回答
    responses = np.zeros(N)
    for i in range(N):
        if second_group_cards[i] == 1:  # 如果抽到红色卡片
            responses[i] = cheating_status[i]
        else:  # 如果抽到蓝色卡片
            responses[i] = first_group_cards[i]

    # 计算回答中1的比例
    proportion_of_ones = np.mean(responses)

    # 根据比例估计作弊的比例
    estimated_cheating_ratio = (proportion_of_ones - 0.5 * (1 - p)) / p

    return estimated_cheating_ratio


pi_A = 0.04
pi_B = 0.5
N = 1000
num_of_epsilon = 20
epsilon = np.linspace(0.5, 10, num_of_epsilon)
var_IS_numerical_simulation =np.zeros(num_of_epsilon)
for i in range(num_of_epsilon):
    p_Simmons = (np.exp(epsilon[i])-1)/(np.exp(epsilon[i])+1)
    EPOCH = 10000
    # 创建学生作弊情况的数组（1表示作弊，0表示未作弊）
    cheating_status = np.zeros(N)
    cheating_status[:int(pi_A * N)] = 1
    np.random.shuffle(cheating_status)
    estimated_cheating_ratio = np.zeros(EPOCH)
    # 第一组卡片（黑色和白色，黑色为1，白色为0）
    first_group_cards = np.array([1] * int(N * 0.5) + [0] * (N - int(N * 0.5)))
    np.random.shuffle(first_group_cards)
    for epoch in range(EPOCH):
        print(epoch)

        # 运行模拟并输出估计的作弊比例
        estimated_cheating_ratio[epoch] = simulate_cheating_survey(cheating_status, p_Simmons, N, first_group_cards)
    var_IS_numerical_simulation[i] = np.var(estimated_cheating_ratio)

plt.plot(epsilon, var_IS_numerical_simulation, color='g', marker ='^', linewidth=1, markerfacecolor='none', markersize=10, linestyle='dashed', label='improved Simmons$_{\pi_B=0.50}$')

plt.xlim(0.5, 10)
plt.xticks(np.linspace(0.5, 10, num=len(epsilon)))
plt.xlabel('privacy budget $(\epsilon)$')
plt.ylabel('variance')
plt.title('Experimental verification of theory')
plt.legend()
plt.show()


with open('Experimental_of_IS_N=1000_pi_A=0.04.txt', 'w') as file:
    for i in range(len(epsilon)):
        line = f"{epsilon[i]}\t{var_IS_numerical_simulation[i]}\n"
        file.write(line)
