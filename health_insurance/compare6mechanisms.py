import matplotlib.pyplot as plt
import numpy as np

# '''
# Warner
# '''
# # 从txt文件中读取数据
# data = np.loadtxt('Experimental_verification_of_theory_W.txt')  # 跳过第一行表头
#
# # 分离列数据
# epsilon_Warner = data[:, 0]  # 第一列作为横坐标
# theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
# numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标
#
# # plt.figure(figsize=(6,8))
#
# # 绘制图表
# plt.plot(epsilon_Warner, theoryanalysis, color='b', marker ='*', markerfacecolor='b', linewidth=1, markersize=8, linestyle=':', label='Warner/Simmons_($\pi_B=1/2$)(Theory)')
# plt.plot(epsilon_Warner, numericalsimulation, color='b', marker ='o', markerfacecolor='none', linewidth=1, markersize=10, linestyle=':', label='Warner/Simmons_($\pi_B=1/2$)(Numerical)')

# '''
# Simmons_($\pi_B=1/2$)
# '''
# # 从txt文件中读取数据
# data = np.loadtxt('Experimental_verification_of_theory_MS.txt')  # 跳过第一行表头
#
# # 分离列数据
# epsilon_S = data[:, 0]  # 第一列作为横坐标
# theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
# numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标
#
# # plt.figure(figsize=(6,8))
#
# # 绘制图表
# plt.plot(epsilon_S, theoryanalysis, color='b', marker ='*', markerfacecolor='b', linewidth=1, markersize=8, linestyle=':', label='Simmons_($\pi_B=1/2$)(Theory)')
# plt.plot(epsilon_S, numericalsimulation, color='b', marker ='h', markerfacecolor='none', linewidth=1, markersize=10, linestyle=':', label='Simmons_($\pi_B=1/2$)(Numerical)')


# '''
# C
# '''
# # 从txt文件中读取数据
# data = np.loadtxt('Experimental_verification_of_theory_C_L=3.txt')  # 跳过第一行表头
#
# # 分离列数据
# epsilon_MC_L3 = data[:, 0]  # 第一列作为横坐标
# theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
# numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标
#
# # 绘制图表
# plt.plot(epsilon_MC_L3, theoryanalysis, color='b', marker ='*', linewidth=1, markerfacecolor='b', markersize=8, linestyle=':', label='Christofides(L=3, Theory)')
# plt.plot(epsilon_MC_L3, numericalsimulation, color='b', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle=':', label='Christofides(L=3, Numerical)')





'''
MW
'''
# 从txt文件中读取数据
data = np.loadtxt('Experimental_MW.txt')  # 跳过第一行表头

# 分离列数据
epsilon_Warner = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# plt.figure(figsize=(6,4))

# 绘制图表
plt.plot(epsilon_Warner, numericalsimulation, color='b', marker ='^', markerfacecolor='none', linewidth=1, markersize=10, linestyle='--', label='modified Warner/Simmons_($\pi_B=1/2$)(Numerical)')


'''
MC
'''
# 从txt文件中读取数据
data = np.loadtxt('Experimental_MC_L=3.txt')  # 跳过第一行表头

# 分离列数据
epsilon_MC_L3 = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# 绘制图表
plt.plot(epsilon_MC_L3, numericalsimulation, color='r', marker ='o', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='modified Christofides(L=3, Numerical)')



'''
IW
'''
# 从txt文件中读取数据
data = np.loadtxt('Experimental_IW.txt')  # 跳过第一行表头

# 分离列数据
epsilon_IW = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# 绘制图表
plt.plot(epsilon_IW, numericalsimulation, color='g', marker ='D', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='improved Warner/Simmons_($\pi_B=1/2$)(Numerical)')

# '''
# MS
# '''
# # 从txt文件中读取数据
# data = np.loadtxt('Experimental_verification_of_theory_MS.txt')  # 跳过第一行表头
#
# # 分离列数据
# epsilon_MS = data[:, 0]  # 第一列作为横坐标
# theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
# numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标
#
# # plt.figure(figsize=(6,8))
#
# # 绘制图表
# plt.plot(epsilon_MS, theoryanalysis, color='g', marker ='*', markerfacecolor='g', linewidth=1, markersize=8, linestyle='--', label='modified Simmons_($\pi_B=1/2$)(Theory)')
# plt.plot(epsilon_MS, numericalsimulation, color='g', marker ='o', markerfacecolor='none', linewidth=1, markersize=10, linestyle='--', label='modified Simmons_($\pi_B=1/2$)(Numerical)')





'''
IC
'''
# 从txt文件中读取数据
data = np.loadtxt('Experimental_IC_L=3.txt')  # 跳过第一行表头

# 分离列数据
epsilon_IC_L3 = data[:, 0]  # 第一列作为横坐标
theoryanalysis = data[:, 1]  # 第二列作为第一条曲线的纵坐标
numericalsimulation = data[:, 2]  # 第三列作为第二条曲线的纵坐标

# 绘制图表
plt.plot(epsilon_IC_L3, numericalsimulation, color='k', marker ='s', linewidth=1, markerfacecolor='none', markersize=10, linestyle='--', label='improved Christofides(L=3, Numerical)')

# Adjust the legend display
plt.legend(ncol=1)

# Set the x and y axis limits and ticks
plt.xlim(0.2, 1)
plt.ylim(0, 0.00002)
plt.xticks(np.linspace(0.2, 1, num=len(epsilon_IC_L3)))
plt.yticks(np.linspace(0, 0.00002, num=6))

# Set the axis labels and title
plt.xlabel('Privacy Budget ($\epsilon$)')
plt.ylabel('Variance')
plt.title('Comparison of mechanisms')
plt.savefig('compare6mechanisms.pdf', dpi=100)

# Display the plot
plt.show()
