import csv
import random
import math
from gene import *
from chromosome import *
from individual import *
from population import *
import sys

random.seed()

filename = 'class.csv'
generations = 10

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

if len(sys.argv) > 1:
    filename = sys.argv[1]
if len(sys.argv) > 2:
    generations = int(sys.argv[2])

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

print(
        'avg: ', population.get_average_fitness(), 
        '  min: ', population.get_minimum_fitness(), 
        '  max: ', population.get_maximum_fitness())

for i in range(0, generations):
    next_gen = population.generate_next_gen()
    next_gen.run_fitnesses(test_data, header)
    print(
        'avg: ', next_gen.get_average_fitness(), 
        '  min: ', next_gen.get_minimum_fitness(), 
        '  max: ', next_gen.get_maximum_fitness() )
    population = next_gen

correct = 0
for row in data:
    if row[len(row)-1] == population.get_prediction(header, row[0:len(row)-1]):
        correct += 1

print('Num correct: ', correct, '\nPercentage: ', correct/len(data))
