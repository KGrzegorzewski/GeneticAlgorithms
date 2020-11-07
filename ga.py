import numpy as np
from random import randint

def calc_pop_fitness(equation_inputs, pop):
    #Fitness function calculates the sum of products between each input and its corresponding weight
    fitness = np.round(np.sum(pop * equation_inputs, axis = 1), decimals = 3)
    return fitness
    
    
def mutation(mutation_rate, pop):
    for chromosom in pop:
        for gen in range(len(chromosom)):
            if randint(0, mutation_rate) == 0:
                chromosom[gen] = np.round(np.random.uniform(-4.0, 4.0), decimals = 3)

    return pop
    
#Funkcja selection tournament dla walki 2 osobnikow  
def selection(population, fitness):
    pop_after_selection = []
    population_size = len(fitness)
    
    for i in range(int(population_size/2)):
        fighter_1 = randint(0, population_size - 1)
        fighter_2 = randint(0, population_size - 1)
    
        fighter_1_fitness = fitness[fighter_1]
        fighter_2_fitness = fitness[fighter_2]
    
        if fighter_1_fitness >= fighter_2_fitness:
            winner = fighter_1
        else:
            winner = fighter_2
    
        pop_after_selection.append(population[winner])
    
    pop_after_selection = np.array(pop_after_selection)
    
    return pop_after_selection
    
    
def evaluate(selection_pop, offspring_mutation):

    pop_after_selection = np.concatenate((selection_pop, offspring_mutation), axis = 0)
    
    return pop_after_selection