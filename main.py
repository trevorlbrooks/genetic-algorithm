# Trevor Brooks - tbrooks
# File: main.py
# Description: Main handler for program. Read in file, run generations.
# Call structure: python3 main.py <filename> <number of generations>
# Warning: Testing with deer hunter can take some time. It will print status as it goes. 

import csv
import random
import math
from gene import *
from chromosome import *
from individual import *
from population import *
import sys

random.seed()

#Default test file
filename = 'class.csv'
generations = 10

def is_int(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

#Read in data and remove top lines if needed.
def read_and_format(filename):
    with open(filename) as f:
        data = list(csv.reader(f))
        header = data[0];
        data = data[2:]
    if(is_int(data[0][0]) and data[0][0] == '0' and  not is_int(data[1][0])):
        data = data[1:]
    return data, header

#Splites data half and half between training and test data.
def split_test_data(data):
    #split_point = min(len(data)//2, 50)
    split_point = len(data)//2
    training = data[:split_point]
    test = data[split_point:]
    return training, test

#Read command line arguments.
if len(sys.argv) > 1:
    filename = sys.argv[1]
if len(sys.argv) > 2:
    generations = int(sys.argv[2])

#Retrieve data.
data, header = read_and_format(filename)
test_data, data = split_test_data(data)

#Set up data structuring.
discrete_values = dict()
for col in header:
    discrete_values[col] = set()

for i in range(len(test_data)):
    for j in range(len(header)):
        discrete_values[header[j]].add(test_data[i][j])

for col in header:
    discrete_values[col] = list(discrete_values[col])

#Build the chromosome for the population models.
chromosome = Chromosome()
chromosome.generate_chromosome_lengths(discrete_values)

#normalize data if needed.
was_normalized = False
if chromosome.is_normalized == False:
    for row in data:
        for gene in range(0, len(row)):
            row[gene] = chromosome.get_normalized(gene, row[gene])
    for row in test_data:
        for gene in range(0, len(row)):
            row[gene] = chromosome.get_normalized(gene, row[gene])
    was_normalized = True
    chromosome.is_normalized = True

#Generate first generation population.
population = Population()
population.initialize(chromosome, 250)
population.run_fitnesses(test_data, header)

print(
        'avg: ', population.get_average_fitness(),
        '  min: ', population.get_minimum_fitness(),
        '  max: ', population.get_maximum_fitness())

# Run generations across training data.
for i in range(0, generations):
    next_gen = population.generate_next_gen()
    next_gen.run_fitnesses(test_data, header)
    print(
        'avg: ', next_gen.get_average_fitness(),
        '  min: ', next_gen.get_minimum_fitness(),
        '  max: ', next_gen.get_maximum_fitness() )
    population = next_gen

#Try to predict answers.
correct = 0
for row in data:
    if row[len(row)-1] == population.get_prediction(header, row[0:len(row)-1]):
        correct += 1

# Output results.
print('Num correct: ', correct, '\nPercentage: ', correct/len(data) * 100)
