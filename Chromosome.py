import random

class Chromosome:
    def __init__(self, genes=None):
        """
        Initializes a new Chromosome instance.
        Args:
        - genes (list): Optional. A predefined list of moves for the chromosome.
          If None, random moves are generated.
        """
        # The knight's tour requires 63 moves to cover all squares (64 squares total, starting square is given).
        self.num_moves = 63  
        self.num_possible_moves = 8  # The knight has 8 possible moves at each position.

        if genes:
            self.genes = genes  # Use the given genes
        else:
            # Generate random genes: Each gene is an integer between 0 and 7 representing a possible knight move.
            self.genes = [random.randint(0, self.num_possible_moves - 1) for _ in range(self.num_moves)]

    def crossover(self, partner):
        """
        Performs single-point crossover between this chromosome and a partner.
        Returns:
        - offspring (Chromosome): A new chromosome created by combining genes from both parents.
        """
        # Randomly choose a crossover point (from 1 to num_moves - 1 to ensure a split).
        crossover_point = random.randint(1, self.num_moves - 1)

        # Combine genes: Take the first part from this parent and the second part from the partner.
        new_genes = self.genes[:crossover_point] + partner.genes[crossover_point:]

        # Return the new Chromosome with the combined genes.
        return Chromosome(new_genes)

    def mutate(self, mutation_rate=0.05):
        """
       Mutation is the random modification of a gene (or genes) in a chromosome.
        """
        for i in range(self.num_moves):
            # Perform mutation with a probability equal to mutation_rate.
            if random.random() < mutation_rate:
                # Replace the current gene with a random move (0-7).
                self.genes[i] = random.randint(0, self.num_possible_moves - 1)

    def __repr__(self):
        """
        Returns a string representation of the Chromosome for debugging.
        """
        return f"Chromosome(genes={self.genes})"
    


#EXEMPLE
# Create two random parent chromosomes
parent1 = Chromosome()
parent2 = Chromosome()

print("Parent 1:", parent1)
print("Parent 2:", parent2)

# Perform crossover to create an offspring
offspring = parent1.crossover(parent2)
print("Offspring:", offspring)

# Mutate the offspring with a 5% mutation rate
offspring.mutate(mutation_rate=0.05)
print("Mutated Offspring:", offspring)
