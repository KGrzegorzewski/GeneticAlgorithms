import numpy as np
import ga
import matplotlib.pyplot as plt

#Program ma obliczyc wartosci wag (niewiadomych) dla ktorych wartosci
#funkcji bedzie mozliwe jak najwieksza 
#Y = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6

#Wartosci x - ow (dane wejsciowe)
equation_inupts = [4, -2, 3.5, 5, -11, -4.7]
num_weights = 6
sol_per_pop = 20 #ilosc osobnikow w populacji
pop_size = (sol_per_pop, num_weights) #wymiary populacji

#Ograniczenie (dziedzina) genów wylosowanej populacji
lower_limit = -3.0
upper_limit = 5.0
new_population = np.round(np.random.uniform(low = lower_limit, high = upper_limit, size = pop_size), decimals = 3)

#Ograniczenie ilosc iteracji
num_generations = 2000

#Wspolczynnik mutacji 1/mutation_rate - prawdopodobienstwo mutacji
mutation_rate = 20

#Testowe wywolania zeby obczaic co sie dzieje po kolei
print("Nowa populacja osobnikow")
print(new_population)

#Tablica najlepszych wynikow oraz najlepsze znalezione wagi
best_score_progress = []
best_weights = []

#Jedno wywołanie
new_population = np.random.uniform(low = lower_limit, high = upper_limit, size = pop_size)
for generation in range(num_generations):
    fitness = ga.calc_pop_fitness(equation_inupts, new_population)
    
    best_score = max(fitness)
    best_index = np.where(fitness == best_score)
    best_weights = new_population[best_index][0]
    
    best_score_progress.append(best_score)
    print("Najlepszy wynik w {:d} generacji wynosi {:.3f}".format(generation, best_score))
    
    selection_pop = ga.selection(new_population, fitness)
    offspring_mutation = ga.mutation(mutation_rate, selection_pop)
    new_population = ga.evaluate(selection_pop, offspring_mutation)
    # 

print("Po ostatniej generacji otrzymany wynik występuje dla wag: ", best_weights)

plt.plot(best_score_progress)
plt.xlabel("Generation [n]")
plt.ylabel("Best score [value of the function]")
plt.show()






