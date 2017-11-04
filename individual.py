import random

class Individual:
    def __init__(self):
        self.binary_chromosome = ''
        self.fitness = 0
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
    def randomize(self, chromosome):
        for i in range(0, chromosome.get_num_genes()):
            gene = chromosome.get_gene(i)
            self.binary_chromosome += gene.randomize(chromosome.is_normalized)
        return None
    def __str__(self):
        return 'Chromosome: ' + self.binary_chromosome + '   Fitness: ' +  str(self.fitness)
    def calc_fitness(self, test_data, chromosome, header):
        max = -1;
        if(chromosome.is_normalized):
            for data in test_data:
                current = 0
                for i in range(0, len(header)-1):
                    gene = chromosome.get_gene(i)
                    #switch binary to set value
                    gene_value = int(self.binary_chromosome[gene.start:gene.start+gene.length], 2)
                    if data[i] == chromosome.discrete_values[header[i]][gene_value]:
                        current += 1 / (chromosome.get_num_genes() -1)
                gene = chromosome.get_gene(len(data)-1)
                gene_value = int(self.binary_chromosome[gene.start:gene.start+gene.length], 2)
                if data[len(data)-1] != chromosome.discrete_values[header[len(data)-1]][gene_value]:
                    current *= -1
                #return if 1 or -1
                if current == 1 or current == -1:
                    self.fitness = current
                    return current
                #set max if better
                else:
                    # print(current, '\n')
                    max = max if max > current else current
        self.fitness = max
        return self.fitness
    def get_fitness(self):
        return self.fitness 
