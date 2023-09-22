from sympy import *
import numpy as np
N = symbols('N')
epsilon = 0.2
x = np.exp(epsilon)
Var = 0.001
print(solve(x/(x-1)/(x-1)/N-Var, N))
print(solve(1/(4*N)*((x+1)*(x+1)/(x-1)/(x-1)/(1-0.5)-1)-Var, N))
print(solve(4*0.5*0.5/(N-1)*(x/(x-1)/(x-1))-Var, N))
print(solve(0.1*0.9/(N-1)*((x+1)*(x+1)/(x-1)/(x-1)/(1-0.5)-1)-Var, N))
