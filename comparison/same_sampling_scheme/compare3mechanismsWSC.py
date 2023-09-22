import matplotlib.pyplot as plt
import numpy as np

'''
W
'''
# 从txt文件中读取数据
data = np.loadtxt('Experimental_W.txt')  # 跳过第一行表头

# 分离列数据
epsilon = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# plt.figure(figsize=(6,4))

# 绘制图表
plt.plot(epsilon, numericalsimulation, color='#FF8C00', marker ='.', markerfacecolor='#FF8C00', linewidth=1, markersize=10, linestyle=':', label='Warner/Simmons_($\pi_B=1/2$)(numerical simulation)')


# '''
# S
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
# plt.plot(epsilon, numericalsimulation, color='b', marker ='h', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Simmons($\pi_B=1/2$)($\pi_B$=0.25, numerical simulation)')

'''
C
'''
# 从txt文件中读取数据
data = np.loadtxt('Experimental_C_L=3_p2=0.25.txt')  # 跳过第一行表头

# 分离列数据
epsilon = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# 绘制图表
plt.plot(epsilon, numericalsimulation, color='b', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Christofides($p_2$=0.25, numerical simulation)')

# 从txt文件中读取数据
data = np.loadtxt('Experimental_C_L=3_p2=0.5.txt')  # 跳过第一行表头

# 分离列数据
epsilon = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# 绘制图表
plt.plot(epsilon, numericalsimulation, color='b', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='Christofides($p_2$=0.50, numerical simulation)')

# 从txt文件中读取数据
data = np.loadtxt('Experimental_C_L=3_p2=0.75.txt')  # 跳过第一行表头

# 分离列数据
epsilon = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# 绘制图表
plt.plot(epsilon, numericalsimulation, color='b', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='-', label='Christofides($p_2$=0.75, numerical simulation)')


plt.xlim(0.2,1)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon)))
plt.legend()
plt.xlabel('privacy budget($\epsilon$)')
plt.ylabel('variance')
plt.title('Comparison under the same sampling scheme')
plt.savefig('WSC.pdf')

plt.show()
