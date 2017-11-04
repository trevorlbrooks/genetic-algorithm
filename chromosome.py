from gene import *

class Chromosome:
    def __init__(self):
        self.__genes = list()
        self.is_normalized = True
        self.discrete_values = None
    
    def generate_chromosome_lengths(self, discrete_values):
        self.discrete_values = discrete_values
        total_bits = 0
        for value in discrete_values:
            gene = Gene()
            total_bits += gene.set(total_bits, len(discrete_values[value]))
            self.__genes.append(gene)
    def get_gene(self, index):
        if 0 <= index < self.get_num_genes():
            return self.__genes[index]
        else:
            raise IndexError('Index must be between 0 and ' + self.get_num_genes())
    def get_num_genes(self):
        return len(self.__genes)
    def __str__(self):
        stmt = 'Start Chromosome: (' + str(len(self.__genes)) + ' genes)\n'
        for gene in self.__genes:
            stmt += str(gene) +'\n'
        stmt += '\n'
        return stmt
 
