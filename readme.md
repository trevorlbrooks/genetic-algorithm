# Genetic Algorithms

This is a notebook for testing and annotating my work on a machine learning project using genetic algorithms as the learning element.
   
   
Formatting for text is done with Markdown.

## Sections
1. Read in file
1. Data structures
    1. Array, 0 index for rows. Column names inside rows
    1. Representing parameters as chromosomes
        1. Discretized Data
        1. Continuous Data
1. Find list of possible values
1. Configuration by command line
1. Test suite
1. Learning Element
    1. Mutation
    1. Crossover
    1. Fitness function
    1. Read / Write Learned data / populations for later use
1. Guesser
1. Test Runner (Test multiple variations, document and select best result)

## Steps 
1. Step 1:
    1. Represent the domain as a chromosome
    1. Choose population size N
    1. Choose crossover probability Pc
    1. Choose mutation probability Pm 
1. Step 2:
    1. Define fitness function to evaluate the “goodness” of a particular solution
1. Step 3:
    1. Randomly generate initial population of N chromosomes
1. Step 4:
    1. Calculate the fitness of each chromosome
1. Step 5:
    1. Select a pair of chromosomes for mating
    1. Base selection on both their fitness and a probability function
1. Step 6:
    1. Create offspring by applying crossover and mutation operators
1. Step 7:
    1. Put new offspring in the population
1. Step 8:
    1. Repeat. Go back to step 5 until new population is of size N
1. Step 9:
    1. Replace parent population with child population
1. Step 10:
    1. Go to step 4 and repeat process until termination criterion is reached
