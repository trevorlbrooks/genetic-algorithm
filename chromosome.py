# Trevor Brooks - tbrooks
# File: chromosome.py
# Description: Represent a series of genes into a single string. Handle creation and managment of genes.

from gene import *

class Chromosome:
    def __init__(self):
        self.__genes = list()
        self.is_normalized = True
        self.discrete_values = None

    #Generates the length of the chromosome given needed data values to be represented.
    def generate_chromosome_lengths(self, discrete_values):
        self.discrete_values = discrete_values
        total_bits = 0
        for value in discrete_values:
            gene = Gene()
            total_bits += gene.set(total_bits, len(discrete_values[value]))
            self.__genes.append(gene)
            gene.values = discrete_values[value]
        try:
            float(self.__genes[0].values[0])
            self.is_normalized = False
        except ValueError:
            self.is_normalized = True

    def get_gene(self, index):
        if 0 <= index < self.get_num_genes():
            return self.__genes[index]
        else:
            raise IndexError('Index must be between 0 and ' + self.get_num_genes())

    def get_num_genes(self):
        return len(self.__genes)

    # Retrieves the normalized gene value for a non-normalized data value.
    def get_normalized(self, index, value):
        if self.is_normalized:
            return value
        else:
            sorted_gene = sorted(self.get_gene(index).values)
            for gene_value in sorted_gene:
                if value <= gene_value:
                    return gene_value
            return sorted_gene[len(sorted_gene)-1]

    def __str__(self):
        stmt = 'Start Chromosome: (' + str(len(self.__genes)) + ' genes)\n'
        for gene in self.__genes:
            stmt += str(gene) +'\n'
        stmt += '\n'
        return stmt
