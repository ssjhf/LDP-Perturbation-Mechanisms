import numpy as np
import logging

# Configure logging
logging.basicConfig(filename='simulation_log.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Your existing code
def simulate_cheating_survey(cheating_status, p, N, first_group_cards, pi_B):
    second_group_cards = np.random.choice([1, 0], size=N, p=[p, 1-p])
    responses = np.where(second_group_cards == 1, cheating_status, first_group_cards)
    proportion_of_ones = np.mean(responses)
    return (proportion_of_ones - pi_B * (1 - p)) / p


health_insurance = np.loadtxt('health_insurance.dat')
health_insurance = 2 - health_insurance
input_list = health_insurance.T
pi_A = sum(input_list)/len(input_list)
pi_B = 0.5
N = len(input_list)
num_of_epsilon = 9
epsilon = np.linspace(0.2, 1, num_of_epsilon)
var_IS_numerical_simulation = np.zeros(num_of_epsilon)

for i in range(num_of_epsilon):
    p_Simmons = (np.exp(epsilon[i])-1)/(np.exp(epsilon[i])+1)
    EPOCH = 1000
    cheating_status = np.zeros(N)
    cheating_status[:int(pi_A * N)] = 1
    np.random.shuffle(cheating_status)
    estimated_cheating_ratio = np.zeros(EPOCH)
    first_group_cards = np.array([1] * int(N * 0.5) + [0] * (N - int(N * 0.5)))
    np.random.shuffle(first_group_cards)
    for epoch in range(EPOCH):
        estimated_cheating_ratio[epoch] = simulate_cheating_survey(cheating_status, p_Simmons, N, first_group_cards, pi_B)
        logging.info(f'Iteration {i}, Epoch {epoch}')
    var_IS_numerical_simulation[i] = np.var(estimated_cheating_ratio)

# Save results to file
with open('Experimental_IS.txt', 'w') as file:
    for i in range(len(epsilon)):
        line = f"{epsilon[i]}\t{var_IS_numerical_simulation[i]}\n"
        file.write(line)
