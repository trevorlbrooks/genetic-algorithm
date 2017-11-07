# Trevor Brooks - tbrooks
# File: individual.py
# Description: Represents an individual of a population. This can be randomized or mutated. Also fitness is calculated here.

import random

class Individual:
    def __init__(self):
        self.binary_chromosome = ''
        self.fitness = 0

    # Perform mutation on individual. Called from population.
    def mutate(self, chromosome):
        mutated_gene = chromosome.get_gene(random.randrange(0, chromosome.get_num_genes()))
        start = mutated_gene.start
        end = mutated_gene.length + start
        size = mutated_gene.size
        gene_value = self.binary_chromosome[start:end]

        if int(gene_value, 2) + 1 < size:
            new_gene = (str(bin(int(gene_value, 2) + 1))[2:]).zfill(end-start)
        else:
            new_gene = (str(bin(int(gene_value, 2) - 1))[2:]).zfill(end-start)
        self.binary_chromosome = self.binary_chromosome[0:start] + new_gene + self.binary_chromosome[end:]
        return self

    #Randomize a new individual.
    def randomize(self, chromosome):
        for i in range(0, chromosome.get_num_genes()):
            gene = chromosome.get_gene(i)
            self.binary_chromosome += gene.randomize()
        return None

    #Return a string representation of the individual.
    def __str__(self):
        return 'Chromosome: ' + self.binary_chromosome + '   Fitness: ' +  str(self.fitness)

    #Calculate the fitness of the individual given the training data.
    def calc_fitness(self, test_data, chromosome, header):
        max = -1;
        for data in test_data:
            current = 0
            for i in range(0, len(header)):
                gene = chromosome.get_gene(i)
                #switch binary to set value
                gene_value = int(self.binary_chromosome[gene.start:gene.start+gene.length], 2)
                if chromosome.get_normalized(i, data[i]) == gene.values[gene_value]:
                    current += 1 / (chromosome.get_num_genes())

            if current == 1:
                self.fitness = current
                return current
            #set max if better
            else:
                max = max if max > current else current
        self.fitness = max
        return self.fitness
    def get_fitness(self):
        return self.fitness
