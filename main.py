import numpy as np
import matplotlib.pyplot as plt
import time

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
        evolve_state: list of percentages representing the number of correct base pairs over time
    '''

    population = [initial_state.copy() for _ in range(population_size)]
    evolved_base_pairs = np.zeros((population_size, num_generations), dtype=np.float32)
    start_time = time.time()

    for generation in range(num_generations):
        for i in range(population_size):
            # Mutate the virus
            population[i] = [np.random.choice(['A', 'T', 'G', 'C']) if np.random.rand() < mutation_rate else curr for curr in population[i]]
            
            # Count the number of correct evolved base pairs
            evolved_count = sum(curr == target for curr, target in zip(population[i], target_state))
            evolved_base_pairs[i][generation] = evolved_count / len(target_state)

            # If all base pairs are correct, the virus can infect the cell
            if np.max(evolved_base_pairs[i][generation]) == 1:
                print(np.max(evolved_base_pairs[i][generation]))
                print(f'Virus has infected the cell at generation {generation}')
                break

            # Count the number of correct evolved base pairs
            evolved_count = sum(curr == target for curr, target in zip(population[i], target_state))
            evolved_base_pairs[i][generation] = evolved_count / len(target_state)
    
    return evolved_base_pairs

# Define parameters
population_size = 30
initial_state = ['A'] * 100
target_state = ['G'] * 50 + ['C'] * 50
mutation_rate = 0.01
num_generations = 10000

''' In reality, different base pairs have different mutations rates
    e.g. A -> T has a different mutation rate than A -> G, etc.'''

evolved_base_pairs = evolve_virus(population_size, initial_state, target_state, mutation_rate, num_generations)

# print("Real Time: " num_generations * hours_per_generation)
plt.figure()                            # Create a new figure
plt.imshow(evolved_base_pairs, aspect='auto', interpolation='none', origin='lower', extent=[0, num_generations, 0, population_size])        # Plot the evolved base pairs over time
plt.colorbar(label="Number of Evolved Base Pairs") # Add a colorbar
# plt.plot(evolved_base_pairs)            # Plot the evolved base pairs over time
plt.xlabel('Generation')                # Label the x-axis Generation
plt.ylabel('Individual Viruses')        # Label the y-axis Evolved Base Pairs
plt.title("Evolution of Virus Genome")  # Title the plot
plt.show()



