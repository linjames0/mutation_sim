import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def evolve_virus(population_size, initial_state, target_state, mutation_rate, num_generations):
    ''' Evolve a virus from an initial to target genetic state

    -----------
    Parameters:
        population_size: number of viruses in the population
        initial_state: list of initial base pairs
        target_state: list of target base pairs
        mutation_rate: probability of any base pair mutating in generation
        num_generations: number of generations to run simulation

    -----------
    Returns:
        correct_base_pairs: list of percentages representing the number of correct base pairs over time
    '''

    # Initialize the population
    population = [initial_state.copy() for _ in range(population_size)]
    correct_base_pairs = np.zeros((population_size, num_generations), dtype=np.float32)

    for generation in range(num_generations):
        for i in range(population_size):
            # Mutate the virus
            population[i] = [np.random.choice(['A', 'T', 'G', 'C']) if np.random.rand() < mutation_rate else curr for curr in population[i]]
            
            # Count the number of correct evolved base pairs
            correct_count = sum(curr == target for curr, target in zip(population[i], target_state))
            correct_base_pairs[i][generation] = correct_count / len(target_state)

            # If all base pairs are correct, the virus can infect the cell
            if np.max(correct_base_pairs[i][generation]) == 1:
                print(np.max(correct_base_pairs[i][generation]))
                print(f'Virus has infected the cell at generation {generation}')
                break

            # Count the number of correct evolved base pairs
            correct_count = sum(curr == target for curr, target in zip(population[i], target_state))
            correct_base_pairs[i][generation] = correct_count / len(target_state)
    
    return correct_base_pairs

# Define parameters
population_size = 20
initial_state = ['A'] * 100
target_state = ['G'] * 50 + ['C'] * 50
mutation_rate = 0.01
num_generations = 1000

''' In reality, different base pairs have different mutations rates
    e.g. A -> T has a different mutation rate than A -> G, etc.'''

correct_base_pairs = evolve_virus(population_size, initial_state, target_state, mutation_rate, num_generations)

fig, axs = plt.subplots(1, 2, figsize=(14, 6))
plt.suptitle("Stochastic Genome Evolution")

# Plot the heatmap
cax = axs[0].imshow(correct_base_pairs, cmap='inferno', aspect='auto', interpolation='none', origin='lower', extent=[0, num_generations, 0, population_size])        # Plot the evolved base pairs over time
axs[0].set_xlabel('Generation')
axs[0].set_ylabel('Individual Cells')
fig.colorbar(cax, ax=axs[0], label='Percent Evolved Base Pairs')
axs[0].yaxis.set_major_locator(MaxNLocator(integer=True))

# Plot the line graph of 5 random individuals over time, including the best individual
for i in range(3    ):
    axs[1].plot(correct_base_pairs[i], label=f'Cell {i + 1}')
    axs[1].set_xlabel('Generation')
    axs[1].set_ylabel('Percent Evolved Base Pairs')

axs[1].plot(np.max(correct_base_pairs, axis=0), label='Greatest Resistance', color='black')
axs[1].set_xlabel('Generation')
axs[1].set_ylabel('Percent Evolved Base Pairs')

plt.legend()
plt.show()
