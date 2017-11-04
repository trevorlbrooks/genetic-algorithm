import random
from individual import *
import sys
class Population:
    mutation_probability = 0.001
    preserve_fittest = True
    def __init__(self):
        self.__members = list()
        self.population_max = 100
        self.chromosome = ''
    def add_member(self, individual):
        self.__members.append(individual)
    def initialize(self, chromosome, population_max):
        self.chromosome = chromosome
        self.population_max = population_max
        for i in range(0, population_max):
            individual = Individual()
            individual.randomize(chromosome)
            self.__members.append(individual)
    def selection(self, population):
        totalFitness = population.get_average_fitness() * len(population.__members)
        selectCnt = random.random() * totalFitness
        individual = None
        for member in self.__members:
            individual = member
            selectCnt -= member.get_fitness()
            if selectCnt <= 0:
                break
        return individual
    def reproduce(self, population):
        individual1 = population.selection(population)
        individual2 = population.selection(population)
        crossover_point = random.randrange(0, self.chromosome.get_num_genes())
        crossover_index = self.chromosome.get_gene(crossover_point).start
        child1 = Individual()
        child2 = Individual()
        child1.binary_chromosome = individual1.binary_chromosome[0:crossover_index] + individual2.binary_chromosome[crossover_index:]
        child2.binary_chromosome = individual2.binary_chromosome[0:crossover_index] + individual1.binary_chromosome[crossover_index:]
        if(random.random() < self.mutation_probability):
            child1 = self.mutate(child1)
        if(random.random() < self.mutation_probability):
            child2 = self.mutate(child2)
        return child1, child2
    def mutate(self, individual):
        individual = individual.mutate(self.chromosome) 
        return individual
    def generate_next_gen(self):
        next_gen  = Population()
        population = self
        if self.preserve_fittest == True:
            population = Population()
            for i in range(0, self.population_max // 2):
                fittest = self.pop_fittest_individual()
                population.add_member(fittest)
                next_gen.add_member(fittest)
        next_gen.chromosome = self.chromosome
        while next_gen.get_num_members() < self.population_max:
            child1, child2 = next_gen.reproduce(population)
            next_gen.add_member(child1)
            next_gen.add_member(child2)
        return next_gen
    def get_prediction(self, header, data):
        ans = ''
        best_data_fitness = -1
        best_test_fitness = -1
        for member in self.__members:
            current = 0
            for i in range(0, len(header)-1):
                gene = self.chromosome.get_gene(i)
                #switch binary to set value
                gene_value = int(member.binary_chromosome[gene.start:gene.start+gene.length], 2)
                if self.chromosome.get_normalized(i, data[i]) == gene.values[gene_value]:
                    current += 1 / (self.chromosome.get_num_genes() -1)
            if current > best_data_fitness and member.get_fitness() != -1: # and  member.get_fitness() > best_test_fitness:
                gene = self.chromosome.get_gene(len(header)-1)
                gene_value = int(member.binary_chromosome[gene.start:gene.start+gene.length], 2)
                ans = gene.values[gene_value]
                best_data_fitness = current
                best_test_fitness = member.get_fitness()
        return ans
    def get_num_members(self):
        return len(self.__members)
    def get_average_fitness(self):
        sum = 0
        for individual in self.__members:
            sum += individual.get_fitness()
        return sum/len(self.__members)
    def get_minimum_fitness(self):
        minimum = sys.maxsize
        for member in self.__members:
            if member.get_fitness() < minimum:
                minimum = member.get_fitness()
        return minimum
    def pop_fittest_individual(self):
        maximum = -sys.maxsize -1
        fittest = None
        for member in self.__members:
            if member.get_fitness() > maximum:
                maximum = member.get_fitness()
                fittest = member
                if(maximum == 1):
                    break
        self.__members.remove(fittest)
        return fittest
    def get_maximum_fitness(self):
        maximum = -sys.maxsize -1
        for member in self.__members:
            if member.get_fitness() > maximum:
                maximum = member.get_fitness()
        return maximum
    def run_fitnesses(self, test_data, header):
        for individual in self.__members:
            individual.calc_fitness(test_data, self.chromosome, header)
    def __str__(self):
        stmt = ''
        for member in self.__members:
            stmt += str(member) + '\n'
        return stmt
