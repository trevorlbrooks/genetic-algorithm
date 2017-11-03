from individual import *

class Population:
    chromosome = None
    population_max = 100
    mutation_probability = 0.001
    preserve_fittest = False
    __members = list()
    def add_member(self):
        return None
    def initialize(self, chromosome, population_max):
        self.chromosome = chromosome
        self.population_max = population_max
        for i in range(0, population_max):
            individual = Individual()
            individual.randomize(chromosome)
            self.__members.append(individual)
    def selection(self, population):
        return None
    def reproduce(self, population):
        
        if(random.random() < mutation_probability):
            mutate(individual1)
        if(random.random() < mutation_probability):
            mutate(individual2)
        return None
    def crossover(self, individual1, individual2):
        return None
    def mutate(self, individual):
        
        return None
    def get_average_fitness(self):
        return sum(self.__members)/len(self.__members)
    def get_minimum_fitness(self):
        minimum = sys.maxint
        for member in self.__members:
            if member.fitness < minimum:
                minimum = member.fitness
        return minimum
    def get_maximum_fitness(self):
        maximum = -sys.maxint -1
        for member in __members:
            if member.fitness > maximum:
                maximum = member.fitness
        return maximum
    def run_fitnesses(self, test_data, header):
        for individual in self.__members:
            individual.calc_fitness(test_data, self.chromosome, header)
    def __str__(self):
        stmt = ''
        for member in self.__members:
            stmt += str(member) + '\n'
        return stmt
