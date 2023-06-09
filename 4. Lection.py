import requests


# Genome assembly

def String_Composition_Problem(k, genome):
    k_mers = set()
    for elem in range(len(genome) - k + 1):
        k_mer = genome[elem:elem + k]
        k_mers.add(k_mer)
    return k_mers


# print(String_Composition_Problem(100, 'CCTAGAAGACTTTGCTCGGTGTGTTCCTTGTTTGTCAAAATGACCAACCAAGCACTTTCCTGAACGCCAAACAGTACTTAGGCATAGCTCTCAAGAATGAAACACCTGGTTATCGTTCCGGGGGCATCGAAGCCGACTACCCGCAGCTTTGCGTATTTGGGACGAATACCATGTAGCAGTGATCCGCTTCTTTCAGGCTCCTTCCCAAGTGGATTCGCACGGGGCATAACCGTACAAAGGGGAAGCAGTGAGGTTTAAAAAGATATCCCGAGATTGTGCATAACGCTCAATACCAGACCTACTGGTCCTACTCAAAAGACTTTCATCTGATTTCACCGTCGCGCGTAACACAGCCTTTATTACCCCCGATGAGGGTTCTACGCGATACTACGTGTACTGGCTGCTTATAATGCAGCGGTTGTTATTTGAAATTGCGTGGTTCTTTGGACTTCCCAAAGAAGGTACAGGAAGGCTGGGCGTGTGGGGATAATTGTGAGCCGGTGCGGGATCGGCGGTTGGGAGTACGCGGGCGAGTCGGGATTCCACAGGACAAGTGTCCTGGCTGAGTAACCGTGAGAACTCTCATTCCACACATTCGTATTATGCGTAACTTGAGGCCCTGCCTCCTTAAAAAATATGGGTGGCCCCTTAGAGTTTTCTATACCATTATAGCGATTGTGCTCACATGTTGCGAGCACCTGCGGGACGGCGTAGCGAGCGGCGCTCTAATGGCTAGAAGGGCGTAAAATAGCTCGACCACCCGCGGCCTATTGACACCCTAATTTTCCCGTGGCCCCCCACAATCAGAGCACCGCGCTAACAGCGCAAAAGGCCATTTGAGATCACGTATTTATAAACTCCCCGGGACGCCATGCCTGCTAGGTCCCCTTGGGCCTCTATTTGTTGTTCACTCGTTGCACCCCCAAGTGAATTCGCCGGCAGACAGTTTACACTGCTCAAAGTCCCGAGGCAACCTGTGTTACATACTTGTAGACAACGATTGGTACAAGGCGACCTACTCGTGAGCCTCTCAGTGACAAGTTGCCCTCCCGAGTTGCTGGATAAGCCGTCGCATTCGTAATGCGGTTGGGGTGACGTTTGGACAATTCTGTGTAGAAGTACGGAAGACAGGATTCGCTAATGTGATAGTGTTAATGTGCACCGCAAGTAGCTAAAACCTTCATAGAGGTATAATTAGTCACGTGGGTTTGTTTTGCGCGCATTGGGTGCCTCTCTGACAGATCGGCCCACCTTTGCCCTTTAGGAGGTGGGTGCACTGGCGTAAAAAAGAGCCGGAATTAAATTATGTTGTATCGTCACTTCAGGCAGAATAGATCGATAGCGGACTATCACACTCCAGTTATAGGCACCAAGCTTCAAAACACCGTGACGGGCCACGACGACGTTTATCCCGATATACTTATGGGCCCCGTTACCATCGTACCGTTCGCAGTCGCACCGCGCAATGACACAAGACCAATGACCCTTACTTGCTTCGGGTGGGATATGGGTCTATACCAGAGCAGATCTAAACAGAGAGCGGATTGGAACCGCTACGGGACTGGAGAGGAGCCAAGAATCCTACGCCTTTGATTTAGCCTTGCATCCCTCGTTAAGCCCTGTCTACCCATAAGCGACTAGATTGTGCAGACTAGACCCATCGTGCTAAGGTTCTGGCTTAGGAGCGCAGACCCGATACGTCCTACATCTTCTCAGTTACAAGACTTCAGCTACGCTGATTAGACTCGTACCTCAAGTCCATACAGGTTAGAACGCACAACCACGGACCCCCGGTAGGGTACTGGCGAACCATTATGTTGTTATGGCGACACAACTTCTCCATGCAGTTCGAATTGCAACTAGCTCAAGCCCAATCTAATTCTGAGAGCCCTGGACGTCGGCAGGTGGACGGGGTGTGAGCCATTGGCACTCAGGTGGGGTACAGCGGGCTAACGGCCCAAATGCGTAGTCGAAAAATGTGAGGAATTGGGTCCATACGTCCCAGTGGCACCACGGACTCCTGGCAGTCGGTCCTTAGAGTATTAGTCTGTTAAGGTTCATTCAAAGCGCAAATCACCTTGATCCCGACAATGACGAGGGATACGATAAGAATAGCAGTAATAAAAACTGGGGGAGTCAGCAAAACAGGTATTCCCTCTGTTACGGTAGATCTGCCGTCGGAGGTTGGGTCGCAGTTTACGGCCCCTCCTTTGCGACGTAAATGGAAGCCAGACCAAGGGCAATAACGTCCCCAGGTGGGGCACACGACAAGACTATAAGCCCTCCCATATTAAGTTCACATTATTAAGTACATGGCTGATGTCAGTAATGTACAGAATCTGTTTCCGTTCAATCTCGCGACTCCAATGCATCATGGTTCCACATTAGGAAAAGGGCTATGTGCCGACGTCAGCTTAGGCCATGGATTGCGCGTCTCTATACACATGGCCGTGACTATTACTCATTCTCGCAATCAGGTCCACCGGCTGACTCTGGGTGTGGTGGTGCGACTATGCACACATGCGCGTCCGTCCTCCACTGGGAGGACTTGTAACTCGAGCCTACACAAGCCCCTAAAGGGCTCATGCCTCTAATAATAGGCTGGCTCGACACTCATGTCCCTGCTTCGGGCTGTTTACCGACCGAACGTTATTGCCGACCTGAGAGTAGGCTGCAAATTAGCTCAATTCTCAAGGGAATCTGGGATGTCTTGCAAGGCTTAGTTCCGGACGGGCTTACCCTTCTATTCGAGCTCTACGTACGGCGTTTGTCTACTGCCAACATAATGTCTGTATACGCCAGGATGCGCGCTCAGTCGCTATTGGCCCCTCATCCGGCTGCCAGGTCACTCTCTATTTGAATGAGTTACCACTGTTGGAGCCTGTCTGGCTTCGTGCTGAATTTCGCTTAACTCCCCACGTCACTCGTATCAACTCTATCGACGATATACGGACCCGGACCCCTGGCGCCCTCGTCGTCTACCCGCGATCGATTAGATAACCAAGGAGCGGCTCTCTAGGGTGTCAACTTATCGCTGACGAACCGTGGGAAATTAACCATGCTTTGGATGGTCAGTGAGTGTCTTGTATGCGCGATGACGACAAAATTCTGAGGATAGAGGAAGGGCTCTACCTTAGACTGGGCATTGACGGCGCTTCCGTTTAACAGAACGGCCACGGATGATATTCCCGCAGTGAACTCGTGCGCGTCGATGGTACATCGAGCATGGCCTTAAGATCCGCCAGCAGCTAATTGGAACACGAGTGTTACCCTCCACGGCCTAGCAGCCTACATTCAAGTTGGGTAATTAAAGTGACGCCGTGATATCTATGGTAGATGAAACGAAACTTGTGAAGTGCAAATTTACGATATATTAGTGGCCATACGTAAACCAACTACAAAGGAAGCACCTAATAGCAAACGGCCGTCTGCACTATCGAGACCCATCTTCGTAGTCACCGCTCAAGGGGAGCGTAGGTTCGGTCGGTAACTAGAAACATACAGACCCGACAGGCGTTGACGAGTGTAGCAACGGAAACTGACGTCCAGGCAGCTTTGTGTACGGGTACAACTAGGGACGCTCGCTCCTTAACCCAATCGGGCCGATGCTATCATGTAGGGCTCGCCAATGTAGAAGACGAAACGCCGCAGTGCGGCCAGACGTTTGCCACCTTGCCTGACCCCTGGACTAGGTAGGTCTCTAGTTGTTCTGCTATCGCAACGCCCACTTGACGCGCCAAAAGTAGATGACATGTTATATCGAGGGGACCACGACCTGGTAAAGCTACTTGGCCATGAAGTGAATCAACATTTAAGACATCGGACGGGTGTAGTTGTTCACCGTATAGTGAGGGCGGGAATTCTGCGAGGACTGCCCATGTCGCGTCCCGGAGGGGAAGGAGGGAGGACTAACAATCCTGAGACCACTGAACACATAGGATTTGTCAACCAGGGCAAAAACGTGTGTGGTTGTAGGTCTAGGATCGGTCTCTCTTGGGTACATCCACACATCTACTGCTAGGACATCATCATATATATGTGTGAGCCAAATGATCCTCGTGTGTTATTGCTACTGTCGGTTCTACGTTGTTCGATGCAGATCAGCTCATAAAGCACGTTTACTCCCTTAGCACACTATTCTACGGGAGTATCAACAGCCCCCAGGATGGCTTTTTCAGTGCGAAGTGTGGAACTTACGTAGTCACAAGTGACTGCTTGGTACCTCAGGATAGTAGCTACAATGCAAATAGTCGCTCTCCTGCGACCTTGATAACAGTATTGTTTACTGAAACGGCCTACAACCATGCACAATAGTGACCTTACAGTCTCATCCCGTTATACGGTTGATGTATAACGACGGCGTCCGCTGCAATTCGGGTTAGAATACACGCGCCACGGCTCGGCGCCATCGGTACTGTTTCACCGGGTTAACTATCGGTAGCAAACTTGCACAAGCTGGACGTCACACTAAAGGCTTGATATATCGCCAGTCAAAACGACAAGGAACTGCTACTAAGTACAACTAGAGGTATAGTTCAAAGAAATCGCTGTTTTACGGACATTTAATCAATCCTTACGCCTACCTCAAATGCTTGGATAACCCGAAGCCCCTTAGAAGCGCAAGATGTGCATTATTCTTCTCGATACAGTGAGGCGCGCATCTTAGGGATTTTCTCCGGGGATTCTTCTTTGGATATTGTAACGCAAGTCCCTGGACTGCAAGCTCCATGTCCTTAATAGTATCGCGTCGGTGTGGCCCAGGGTATTCACGCCTCGATCCGGATTGTAATGCACGAATAGCTAAAGGCCCCGGAGTATAGCAATATGAAGGTCGTTCCTAGGGCTTCCTGATAACCCAGAATAAGTATTTAATCGAGGGTGGCATTTAGTGTGGACACACCCCAGTCTTCGTACCTCGATTGCCAGCTTGCGGTCGGTCCAAAACCACGGCACGCATTGAATCTTCCCGGAATTGGCTTTGGGCACCCACAGACTAGCGT'))

response = requests.get(
    'https://gerdos.web.elte.hu/edu/bioinformatics_algorithms/data/week3/GenomPath/dataset_198_3%20(1).txt')
rep = response.text.splitlines()


def Genome_Path(kmers, last=True):
    genome = ''
    for kmer in kmers:
        genome += kmer[0]
    if last:
        genome += kmer[1:]
    return genome


# Gábor's solution

def genome_path(kmers):
    return kmers[0] + ''.join(x[-1] for x in kmers[1:])


# print(Genome_Path(rep))

# Define object

class Polygon:
    def __init__(self, list_of_side_length):
        self.list_of_side_length = list_of_side_length
        print(f"I have {list_of_side_length} sides")

    def number_of_sides(self):
        print(f"I have {len(self.list_of_side_length)} sides")

    def display_sides(self):
        for num, side in enumerate(self.list_of_side_length):
            print(f"Side {num} has length {side}")


class Triangle(Polygon):
    def __init__(self, list_of_sides):
        super().__init__(list_of_sides)

    def find_area(self):
        a, b, c = self.list_of_side_length
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"Triangle area is {area}")


class EqualTriangle(Triangle):
    def __init__(self, base, side):
        super().__init__([base, side, side])


# Graph Object

class Graph(dict):
    def __init__(self, dct):
        self.graph = dct
        super().__init__(dct)

    def __str__(self):
        return '\n'.join(['{} -> {}.'.format(node, edges) for node, edges in self.graph.items()])


my_new_grap_instance = Graph({'a': ['b', 'e'], 'b': ['c', 'd'], 'c': ['a'], 'd': ['a'], 'e': ['b', 'c', 'd']})


# print(my_new_grap_instance)

# Overlapping Graph Problem

class Graph(dict):
    def __init__(self, dct):
        super().__init__(dct)

    def __str__(self):
        return '\n'.join(['{} -> {}'.format(node, ','.join(edges)) for node, edges in self.items()])

    @classmethod
    def form_kmers(cls, kmers):
        asj_lst = {kmer: [] for kmer in kmers}
        for kmer1 in kmers:
            for kmer2 in kmers:
                if kmer1[1:] == kmer2[:-1] and kmer1 != kmer2:
                    asj_lst[kmer1].append(kmer2)
        return cls(asj_lst)

    @property
    def num_nodes(self):
        return len(self)


kmers = '''ATGCG
GCATG
CATGC
AGGCA
GGCAT
GGCAC'''

my_graph_object = Graph.form_kmers(kmers)
# print(my_graph_object.num_nodes)

rep = requests.get(
    'https://gerdos.web.elte.hu/edu/bioinformatics_algorithms/data/week3/OverlapGraph/dataset_198_10%20(1).txt')
rep = rep.text.splitlines()


def overlap_grap(kmers):
    asj_lst = {kmer: [] for kmer in kmers}
    for kmer1 in kmers:
        for kmer2 in kmers:
            if kmer1[1:] == kmer2[:-1]:
                asj_lst[kmer1].append(kmer2)
    return asj_lst


#print(overlap_grap(rep))

# de Bruijn graph what I found on the internet

def de_Bruijn_grap_from_string(k, string):
    kmer1 = []
    for elem in range(len(string) - k + 2):
        kmer1.append(string[elem:elem + k - 1])

    kmer1 = sorted(list(set(kmer1)))

    nodes = {}
    for i, v in enumerate(kmer1):
        nodes[i] = v
    invnodes = {v: i for i, v in nodes.items()}

    edges = {}
    for i in range(len(string) - k + 1):
        if invnodes[string[i:i + k - 1]] in edges:
            edges[invnodes[string[i:i + k - 1]]].append(invnodes[string[i + 1:i + k]])
        else:
            edges[invnodes[string[i:i + k - 1]]] = [invnodes[string[i + 1:i + k]]]

    temp = []
    for key, vals in edges.items():
        # print(nodes[key], '->', ','.join(sorted([nodes[val] for val in vals])))
        temp.append(nodes[key] + ' -> ' + ','.join(sorted([nodes[val] for val in vals])))
    return temp


# print(de_Bruijn_grap_from_string(4, 'AAGATTCTCTAAGA'))


def debruij_frem_text(k, genome):
    comp = String_Composition_Problem(k, genome)
    adj_list = {x[:-1]: [] for x in comp}
    for elem in comp:
        adj_list[elem[:-1]] += [elem[1:]] * genome.count(elem[:-1])
    return adj_list


# print(Graph(debruij_frem_text(12, 'GTCGTCGCCTCCACCGCGCTTGTGTTCGATGGCCAGGCAGGGGAAAGAAGCGAAGCAGACCGCCTCAGCGTCCTCACCGGCAGGTCAACAACAAAACGATCACTGCATAAACGACCCACTCGATTCCTCTGCCTCATGAAGGATTACGGCAGTTTGGCTTCGAGTGCCCGACGATCTCCATTGCGCCGATGGAGCCTGAGTCTGGAGGCCTTGTAGCCAGTTTAGCTTAACACAATTCTGAGTCCATTCAACCTCGGAATGCATTGCCTAGCCACCTTTCCTGTACTACGAGAGAGGATCTGTCGGTGCAGTTTGGCTCACGGGAGACACATGTTATGATCTTTATTATCAGTTGCAAGGAACATTTGCGGTATCTTAGACCATAAAGCAGTATGACGTCACCACGCTAATAAGGTCTGTGGAGGCCTCCACCCCCCGGTCTATATCCTACGAGGTTGCAACAGGGCCCGATAAAAAATCTTCCTAAAGCCATCCCGTTACTAGCACCCCCTCGTAAAACTGTCAGAGTACCCACCATGTTGCTATTTTACGATCTCAACTATTACTTGCTGGTAGTGAGCGCCCATGAATCGCTGCGTTAGCTTGTGACCAGACTAGAATTTTGTCCAATCCTGAAGACGTCGAGGAGATTAAGAAGGGGCAGCCCGTCGTCGTGGACGAAGCTATAGGGAGGATTCCGACGCTTGAGGATTAAGTCTCTGGAATGGGGCCGCTTAGATGGTAGCCGGCGTAGGGACCGGTCGGTATCCTCGTTCAGAATACAGTTATTTCTGCGTTTTATGTTTCTAGTGGTACGAACGTACTTAGGACTACTAGTAGGTACGGCCCGTGGCTTACGCTAAAGACTCTACGTCGGCTCTGGTCTATCGTCACACGATACACATGAACCGGGCTTCGCTTCCGTGCCTACTTCAAGGACCACTGGGTGATAGAATCAACGTCTATCCGTGCACAATGAATCTCTACCCGTGGTCATCCCGTGGAGATCATAAGGTTAAACTAACGTCGAGCTGCGGTGGGCCTGTTAGTAAATAGATTCTTCGAAGCGCCCCCCTGGAGTTGTTTTCGACCGCCAGCTGCCAAAGTACCGACCTTTCGCTCGTCCATGAGGAGACCGCCAAGGATAATCCCACCATCATTTCGCATGAGATGGTTGTAGAACCATTTGGCAATAGTCTGCTAAAGTTCGCCCGCAGCCGGAGTCCTGGAAGACGGACGGGGAACAGCGGAGACAACGCTGTATCAAGGGCAAACGTTAATTCCCTCTCTCGCTTCTTGGAGATGCCATGGCGACGTAGTGCAAAGGACTTCCTCAAGCCCAGCGCTCAGGAGACGGAGCTTATGTGATGGAAGTGCAGAGAATCGTATAGCTCTGCCAACGTAATAACCGCTCTATATACTTGAAGTGTCCTCCAGCGAGATCACTGAAACACGAGGAGATTACAACTACCAACTGTGCTCCAAGGCTCCGTGGTTAAGAGGGAAGCCTGTCTTAACTGCCCAGCTATATTTCTACCTGAGGAACAAGCACCACGGTACAGATCGGCCGCGAGCATTTGATGTCCCGAAAAGAAGTTTTGTTGGGGCGGGTCGGGAAGCAATCGTCAACTAACTCCGCTGGGGGTCGATGTTGACCGAAAACTCATGACGTGCTCCTAAGTAACTGACGCCCTATGCTCCCCCCCTATTGTGCTCGCGACCCAAGACCACGCGGGTCCAGGATAGTTCCTTCACGCTATACCGAATCGAACGTACTGACATTACCGTCGTTGCACGCGACTCCATTGCATCTGATCTATAGTTGACATATGCTTGTCCTAATCTCGGTATGTTCTAGGGTAACCAAATTGCGGTTGGCGCGAAGCCACACGATCTGCGAGGGAGTACTGTGCGTTATGCGAACCAGGGACCTCGTCGAGCTGACCTTAAAGAAAAGTCGAGAGCACAGGGTGGCCATTCTAGGCGAAACTCAGTTGCTG')))
