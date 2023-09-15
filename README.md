# mutation_sim
# Evolutionary Simulation for Genomes

## Main
This is a program that simulates stochastic genome evolution over time, from an initial to a target genome. 
It assumes that you have a set of initial and final base pairs. Usually, transitioning from initial to final base pairs would encode some phenotypic change (e.g. antibiotic resistance).
This model essentially simulates the evolution of this genome over generations.

You can input factors relevant to your study:
1. Population Size
2. Initial Base Pairs
3. Final Base Pairs
4. Mutation Rate
5. Number of Generations

Population size is the number of organisms in your population.

Initial base pairs is the set of the base pairs that must change for the desired final outcome.

Final base pairs is the set of desired final base pairs.

Mutation rate is the mutation rate per bp of your organism (usually 1e-8 for viruses and 1e-10 for bacterial genes)

Number of generations is the expected number of replication cycles of your population.

## Misc
This is meant to be the backbone of many evolutionary simulation projects. The goal is for it to be as flexible as possible, while also being simple and easy to use.


