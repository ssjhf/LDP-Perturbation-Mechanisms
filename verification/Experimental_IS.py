import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pi_A = 0.05
M = 10000
N = 10000
num_of_epsilon = 9
epsilon = np.linspace(0.2, 1, num_of_epsilon)
exp_of_epsilon = np.exp(epsilon)

# Improved Simmons, numerical simulation

def compare_arrays(u, b):
    return (np.array(u) < np.array(b)).astype(int)

pi_B = np.linspace(0.1, 0.9, 9)
input_list = np.zeros(N)
input_list[:round(pi_A * N)] = 1
np.random.shuffle(input_list)
REPEAT_TIMES = 1000

var_IS_Numerical_Simulation = np.zeros((len(epsilon),9))
for i in range(9):
    if pi_B[i] < 0.5:
        p_Simmons_initial = (np.exp(epsilon) - 1) * pi_B[i] / ((np.exp(epsilon) - 1) * pi_B[i] + 1)
    else:
        p_Simmons_initial = (np.exp(epsilon) - 1) * (1-pi_B[i]) / ((np.exp(epsilon) - 1) * (1-pi_B[i]) + 1)

    for j in range(len(epsilon)):
        Y_list = np.zeros(N)
        Y_list[:round(p_Simmons_initial[j] * N)] = 1
        np.random.shuffle(Y_list)
        print(j)
        mean_proportion = np.zeros(REPEAT_TIMES)
        for times in range(REPEAT_TIMES):
            if (times % 100 == 0):
                print(times)
            p_Simmons = p_Simmons_initial[j]
            np.random.shuffle(input_list)
            u_vector = np.random.random(N)
            output_list = Y_list * input_list + (1-Y_list) * input_list * compare_arrays(u_vector, pi_B[i]*np.ones(N)) + Y_list * (1 - input_list) * compare_arrays(u_vector, pi_B[i]*np.ones(N))
            lambda_val = np.mean(output_list)
            mean_proportion[times] = (lambda_val - (1 - p_Simmons_initial[j]) * pi_B[i]) / p_Simmons_initial[j]

        var_IS_Numerical_Simulation[i,j] = np.var(mean_proportion)


fig = plt.figure(figsize=(10,8))  # 设置为10x8英寸的图像
ax3 = plt.axes(projection='3d')

plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

#定义三维数据
epsilon = np.arange(0.2,1.01,0.1)
pi_B = np.arange(0.1,0.91,0.1)
X, Y = np.meshgrid(epsilon, pi_B)

#作图
ax3.plot_surface(X, Y, var_IS_Numerical_Simulation,cmap='rainbow')
# 改变cmap参数可以控制三维曲面的颜色组合, 一般我们见到的三维曲面就是 rainbow 的
plt.xlim(0.2, 1)
plt.ylim(0.1, 0.9)
plt.xticks(np.linspace(0.2, 1, num=num_of_epsilon))
plt.yticks(np.linspace(0.1, 0.9, num=9))
ax3.set_xlabel('privacy budget $(\epsilon)$') # 画出坐标轴
ax3.set_ylabel('$\pi_B$')
ax3.set_zlabel('variance')
plt.show()