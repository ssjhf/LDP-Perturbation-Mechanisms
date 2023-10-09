from sympy import *
import numpy as np
N = symbols('N')
epsilon = 1
x = np.exp(epsilon)
Var = 0.001
pi_A = 0.1
print(solve(pi_A*(1-pi_A)/N + x/(x-1)/(x-1)/N-Var, N))
print(solve(pi_A*(1-pi_A)/N + 1/(4*N)*((x+1)*(x+1)/(x-1)/(x-1)/(1-0.5)-1)-Var, N))
print(solve(x/(x-1)/(x-1)/N-Var, N))
print(solve(1/(4*N)*((x+1)*(x+1)/(x-1)/(x-1)/(1-0.5)-1)-Var, N))
print(solve(4*0.5*0.5/(N-1)*(x/(x-1)/(x-1))-Var, N))
print(solve(0.1*0.9/(N-1)*((x+1)*(x+1)/(x-1)/(x-1)/(1-0.5)-1)-Var, N))
