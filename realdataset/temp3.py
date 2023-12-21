import numpy as np
import matplotlib.pyplot as plt

def simulate_cheating_survey(cheating_status, p, N, first_group_cards):
    second_group_cards = np.array([1] * int(N*p) + [0] * (N - int(N*p)))
    np.random.shuffle(second_group_cards)
    responses = np.where(second_group_cards == 1, cheating_status, first_group_cards)
    return (np.mean(responses) - 0.5 * (1 - p)) / p

# Parameters
health_insurance = np.loadtxt('health_insurance.dat')
health_insurance=2-health_insurance
input_list = health_insurance.T
pi_A = sum(input_list)/len(input_list)
pi_B = 0.5
N = len(input_list)
num_of_epsilon = 9
epsilon = np.linspace(0.2, 1, num_of_epsilon)
var_IS_numerical_simulation = np.zeros(num_of_epsilon)

# Simulation
for i in range(num_of_epsilon):
    print(i)
    p_Simmons = (np.exp(epsilon[i]) - 1) / (np.exp(epsilon[i]) + 1)
    cheating_status = np.random.choice([1, 0], size=N, p=[pi_A, 1 - pi_A])
    first_group_cards = np.random.choice([1, 0], size=N, p=[0.5, 0.5])
    estimated_ratios = [simulate_cheating_survey(cheating_status, p_Simmons, N, first_group_cards) for _ in range(10000)]
    var_IS_numerical_simulation[i] = np.var(estimated_ratios)

# Plotting
plt.plot(epsilon, var_IS_numerical_simulation, color='g', marker='^', linewidth=1, markerfacecolor='none', markersize=10, linestyle='dashed', label='improved Simmons ($\pi_B=0.50$)')
plt.xlim(0.2, 1)
plt.xticks(np.linspace(0.2, 1, num=num_of_epsilon))
plt.xlabel('privacy budget $(\epsilon)$')
plt.ylabel('variance')
plt.title('Experimental verification of theory')
plt.legend()
plt.show()

with open('Experimental_IS.txt', 'w') as file:
    for i in range(len(epsilon)):
        line = f"{epsilon[i]}\t{var_IS_numerical_simulation[i]}\n"
        file.write(line)