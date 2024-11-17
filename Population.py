from Chromosome import Chromosome
from Knight import Knight
import random
import cProfile
class Population:
    def __init__(self,population_size):
        self.population_size=population_size
        self.generation=1
        self.knights=[]
        for _ in range(self.population_size):
            self.knights.append(Knight())
    
    def check_population(self):
        for knight in self.knights:
            knight.check_moves()
    
    def evaluate(self):
        best_knight=None
        best_fitness=-1
        for knight in self.knights:
            knight.evaluate_fitness()
            if knight.fitness>best_fitness:
                best_knight=knight
                best_fitness=knight.fitness
        return best_fitness,best_knight
    
    def tournament_selection(self,size=3):
        tournament_sample = random.sample(self.knights, size)
        tournament_sample.sort(key=lambda x: x.fitness, reverse=True)
        parent1 = tournament_sample[0]
        parent2 = tournament_sample[1]
        
        return parent1, parent2
    
    def create_new_generation(self):
        new_knights=[]
        while len(new_knights)<self.population_size:
            parent1,parent2=self.tournament_selection(size=3)
            offspring1 = parent1.chromosome.crossover(parent2.chromosome)
            offspring2 = parent2.chromosome.crossover(parent1.chromosome)
            offspring1.mutate()
            offspring2.mutate()
            new_knights.append(Knight(chromosome=offspring1))
            new_knights.append(Knight(chromosome=offspring2))
        self.knights = new_knights
        self.generation += 1 
def main():
    population_size = 50
    population = Population(population_size)
    while True:
        population.check_population()
        maxFit, bestSolution = population.evaluate ()
        # print("Final Path:", bestSolution.path)
        # print("Fitness:", maxFit)
        if maxFit == 63:
            print("Final Path:", bestSolution.path)
            print("Fitness:", maxFit)
            break
        #Generate the new population
        population.create_new_generation ()
if __name__ == "__main__":
    cProfile.run('main()')

        