import random
from individual import *
import sys
class Population:
    population_max = 100
    mutation_probability = 0.001
    preserve_fittest = True
    def __init__(self):
        self.__members = list()
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
        #fit = Individual()
        #fit.binary_chromosome = fittest.binary_chromosome
        #fit.fitness = fittest.get_fitness()
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
