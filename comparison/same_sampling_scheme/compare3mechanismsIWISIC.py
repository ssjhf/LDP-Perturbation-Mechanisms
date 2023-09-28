import matplotlib.pyplot as plt
import numpy as np

'''
IW
'''
# 从txt文件中读取数据
data = np.loadtxt('Experimental_IW.txt')  # 跳过第一行表头

# 分离列数据
epsilon = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# plt.figure(figsize=(6,4))

# 绘制图表
plt.plot(epsilon, numericalsimulation, color='g', marker ='^', markerfacecolor='none', linewidth=1, markersize=10, linestyle=':', label='Improved Warner/Simmons_($\pi_B=1/2$)(numerical simulation)')


# '''
# IS
# '''
#
# # 从txt文件中读取数据
# data = np.loadtxt('Experimental_S_pi_B=0.25.txt')  # 跳过第一行表头
#
# # 分离列数据
# epsilon = data[:, 0]  # 第一列作为横坐标
# theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
# numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标
#
# # 绘制图表
# plt.plot(epsilon, numericalsimulation, color='b', marker ='h', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Improved Simmons($\pi_B=1/2$)($\pi_B$=0.25, numerical simulation)')

'''
IC
'''
# 从txt文件中读取数据
data = np.loadtxt('Experimental_IC_L=3_p2=0.25.txt')  # 跳过第一行表头

# 分离列数据
epsilon = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# 绘制图表
plt.plot(epsilon, numericalsimulation, color='k', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Improved Christofides($p_2$=0.25, numerical simulation)')

# 从txt文件中读取数据
data = np.loadtxt('Experimental_IC_L=3_p2=0.5.txt')  # 跳过第一行表头

# 分离列数据
epsilon = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# 绘制图表
plt.plot(epsilon, numericalsimulation, color='k', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='Improved Christofides($p_2$=0.50, numerical simulation)')

# 从txt文件中读取数据
data = np.loadtxt('Experimental_IC_L=3_p2=0.75.txt')  # 跳过第一行表头

# 分离列数据
epsilon = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# 绘制图表
plt.plot(epsilon, numericalsimulation, color='k', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Improved Christofides($p_2$=0.75, numerical simulation)')


plt.xlim(0.2,1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.legend()
plt.xlabel('privacy budget($\epsilon$)')
plt.ylabel('variance')
plt.title('Comparison under the same sampling scheme')
plt.savefig('IWISIC.pdf')

plt.show()
