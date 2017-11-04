import csv
import random
import math
from gene import *
from chromosome import *
from individual import *
from population import *


random.seed()

filename = 'weather.csv'

def is_int(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

def read_and_format(filename):
    with open(filename) as f:
        data = list(csv.reader(f))
        header = data[0];
        data = data[2:]
    if(is_int(data[0][0]) and data[0][0] == '0' and  not is_int(data[1][0])):
        data = data[1:]
    return data, header

def split_test_data(data):
    test = data[:len(data)//2]
    data = data[len(data)//2:]
    return test, data

data, header = read_and_format(filename)
test_data, data = split_test_data(data)

discrete_values = dict()
for col in header:
    discrete_values[col] = set()

for i in range(len(test_data)):
    for j in range(len(header)):
        discrete_values[header[j]].add(test_data[i][j])

for col in header:
    discrete_values[col] = list(discrete_values[col])

chromosome = Chromosome()
chromosome.generate_chromosome_lengths(discrete_values)
print(chromosome)

population = Population()
population.initialize(chromosome, 100)
population.run_fitnesses(test_data, header)
#print(population)

print(
        'avg: ', population.get_average_fitness(), 
        '  min: ', population.get_minimum_fitness(), 
        '  max: ', population.get_maximum_fitness() ,'\n')

next_gen = population.generate_next_gen()
next_gen.run_fitnesses(test_data, header)
print(
        'avg: ', next_gen.get_average_fitness(), 
        '  min: ', next_gen.get_minimum_fitness(), 
        '  max: ', next_gen.get_maximum_fitness() ,'\n')


