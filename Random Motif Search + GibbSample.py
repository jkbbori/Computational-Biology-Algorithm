import random


def random_motif(dna_list, k):
    motifs = []
    for elem in dna_list:
        motif = random.randint(0, len(elem) - k)
        motifs.append(elem[motif:motif + k])
    return motifs


def Profile(alignment):
    profile = []
    length = len(alignment[0])
    profile_count = {'A': [1] * length, 'C': [1] * length, 'G': [1] * length, 'T': [1] * length}
    for elem in alignment:
        for i in range(length):
            profile_count[elem[i]][i] += 1
    for key in profile_count:
        profile.append([x / (len(alignment) + 1) for x in profile_count[key]])
    return profile


def Score(motifs):
    consensus = ''
    score = 0
    length = len(motifs[0])
    score_count = {'A': [1] * length, 'C': [1] * length, 'G': [1] * length, 'T': [1] * length}
    for elem in motifs:
        for i in range(length):
            score_count[elem[i]][i] += 1
    for i in range(length):
        n = 0
        symbol = ''
        for nuc in "ACGT":
            if score_count[nuc][i] > n:
                n = score_count[nuc][i]
                symbol = nuc
        consensus += symbol
    for elem in motifs:
        for i in range(length):
            if elem[i] != consensus[i]:
                score += 1
    return score


def most_probable_kmer(dna_list, k, profile):
    profile_most_probable_kmer = []
    length = len(dna_list)
    for i in range(length - k + 1):
        kmer = dna_list[i:i + k]
        motif_score = 1
        for j in range(k):
            motif_score *= profile['ACGT'.index(kmer[j])][j]
        profile_most_probable_kmer.append(motif_score)
    rand = random.uniform(0, sum(profile_most_probable_kmer))
    count = 0
    for i in range(length - k + 1):
        count += profile_most_probable_kmer[i]
        if count >= rand:
            return dna_list[i:i + k]


def Randomized_Motif_Search(dna_list, k, t):
    motif = random_motif(dna_list, k)
    best_motif = motif
    while True:
        profile = Profile(motif)
        motif = []
        for i in range(t):
            motif.append(most_probable_kmer(dna_list[i], k, profile))
        if Score(motif) < Score(best_motif):
            best_motif = motif
        else:
            return best_motif


def Rep_Rand_Mot_Searc(dna_list, k, t):
    Best_Score = float('inf')
    Best_Motif = []
    for i in range(1000):
        Motifs = Randomized_Motif_Search(dna_list, k, t)
        Current_Score = Score(Motifs)
        if Current_Score < Best_Score:
            Best_Score = Current_Score
            Best_Motif = Motifs
            print(Best_Score)
    return set(Best_Motif)


dna_list = [
    'CAGGGAAAACTCCTAAATAACGTAATCGGTCGTAATCCGGCATTATGGCGGTTCATGCAGGTTCCGGGCGGGGTCAGGGGTCTGAGTCGACTTCGATGGAAGGCGTACATAAAATGGAAGGGCTCGTACGACACTGAATGTTATTGCTTTGGTGGCCTCGGCACCTTAGCCCTGATCGCGCCAGGGAAAACTCCTA',
    'AATAACGTAATCGGTCGTAATCCGGCATTATGGCGGTTCATGCAGGTTCCGGGCGGGGTCAGGGGTCTGAGTCGACTGAGTTCGAGTTCGACTCGATGGAAGGCGTACATAAAATGGAAGGGCTCGTACGACACTGAATGTTATTGCTTTGGTGGCCTCGGCACCTTAGCCCTGATCGCGCCAGGGAAAACTCCTA',
    'TGCCAGTGCGGTACCGGTCGAGCCGAATCTCAAGGCTTACGGTTATGCTTAAGCCGGTGACGAAATGACCATTGTTATTATTGTAACCAGAACTACTCTAACAATCGTTCCTTGCCTTCCCATGCACTCTACACCTTGGCAAGCCACCGACTGAGAGGGAGAGTAAAACTTTCGATAAACCGCTTCTTTTTGTTGA',
    'CTACACCCATGCATCTGAGGTCATATTGCGAAACTGCGAACTCCATTGATTAGGAACAGTACAATGGACTAGACGGAATTCCGTGAGGGAGACGGCGACTTCAAATCGTTCGAATCGCATGCGCGCTGTACACTTATGTCTACTCAACGTTGACGCGTGAGGACGCCTGGAACGTGTTTAACGGTTTCAATGTATT',
    'AAAGTCCCCGTAAGGAACTCTTAATCCTTACGGATTTTGTGTCTGGATGGTCCGACGCATCGAGTATCCTGTTGTAAACGCGCCAGAGGGAGAGAGGGACAACGTAACCTCCGAGAAGCGGGGCTGATGGATTTGCTGTGGCGCTTTGGAGCGGGGAGTTACACGTGGTTTTTCAGCCAAAGCGCCTGCTTCAGAG',
    'TGGCTACAACAAAAGTACAATCCTGCGCTCATCGAGGGAGTAGTCGACTGGACTGACTTTCTAGCGTCGTATATAGGTCGCAGGTTGCTAAAATAACCCAACTCAACATTCACCTATCTCCTGTTTAGTCTTATTCGTAAAAATACGTCTCACCGACTTACACCTTAAAGAAGGCACAATGGCCGCAGGAAGGGCG',
    'CATACTTGACACAATCAGTGAATTCTGAGTGAGTACCGACCACTTTACCTCTGCCGCGAACCGTCGTCAAGGTGACAGACTACCGAGGTTAAGTTCGACAGAAGGTAGCTAGTGACGTGCACAGTCGACAGAGTCTAAATAGTGAAGCCTACCAGCTATTGGTTCTACATTATGTCGGTCTGTCGGAGTGTAGTTA',
    'AATCGTCTAAGCGTATGGTGCAATTCCAATGTCGTGACTCAACTCCTTCCTACCCAGATACACTATAACTGCACATTCCGAGACATGTGGTTCATAAACTTGACGCCACCAGTCGGGCCACTAGTCACTCCAGATGGCGGATCCGGGACTCACGAGGGAGAGTTGATCTGCAAACAAGATCAGTCCGGTGGCCTGA',
    'GGAGTTGGGTGCCTAAGCCGAAAAAGAGTTCGACCGACTGAAAAGTTCCCCCCTGACGCGGGAGGCTGACATACGCGCTCATTCCACGTTGTTCAGCAGGGTTGTACCTGATTTCGCTGAAGGAACGGACAGTATCCCCGCCCCTGGCGTACATTTGCGATCCACTGACAAGACAAAGAGACCACCCCAAAATTTC',
    'CGAGGGACGTTTCGACGACTGTAGAAGGTGGAATGGCTTATGACAAATTCGCTTGGCTGTGTTTTACCATCCTTTGTTATCCTGTCCTACTAGACAAAAGTTCAAGGCATCGTGCCGTTCTTATTTTCTTTCGGCACCATGAGGCTCAAGGGCAGTGAGTCTTTCCGAAAGCCGTTACATGGCAGGACTAGTGCCC',
    'GGCTATCCTCTTTGAAACTAGAACGCTGTCGATGGACAATGAGGTAACATCATAGTCCCGTGACGTAATTTAAAGCACTGCACCCTAGCGTATTGAGCTCCCCCGGGGACTTAACGATAAAGGATACCACGATAGAACGCGGGAATGGGGAGAGTTCGAGAATCAGACAGTGCACACAGACTGCAGTGAGGTTCTA',
    'CCAGGAGAGGGGAGGTTCGACGGCGCAGACTTTCGGCAAATGCGAAGTGACGTTGTGTTCTGACAGGCTCGGAAGCATAGTACATAACGAGTCCTATAAGGTACCCGACCGCTCTAGAGCCGGACCCAACATTGCCTGTTCTCGGTTCATGGTGGTAGCTCGGGTTTCCATGAGTCCAGGGTGTCCTCCTTACGCA',
    'ATATGAGACGGCCCTAAACTCGCTGGGAGGCACTTTCGACATTGTAAACTTCATTCGTGGCTGAACGGGGTCCTCAGTCCGTGGGTCCCGACGTGAGGTGTAGTTCGACCAACTTGGAAGGGGGCAAAGACCAGTCGGCCTACCTTAGTGCACTCCCTTTTACCAATAGACCTAGGTGCCCTTCGGTCCTAGCTAT',
    'TGGGGCATAGTTCCCCTGAGGAGGTCATTCGTAGATTGTTTGGAGAGTTCGACGCAAGTAGCTGTACGGCGCAAACCCGCTTATCTAATGCAAGTATGTTTTAGACCAGTGTCTACCACGGGGTCTCCGTGTCAACTCCATAGAAGGACAAAAGGCCCTACGCAGCAAGTATCCCACACTCAGGATTCGTTCTGTG',
    'AAACGGCCGGGGGGTAGATCAATCGCTCGAGATCTCTCTATGGGACTCGAGGGGTCGTTCGACCTATAGTTGAAGCCCGGAGTTGTTTGGACGGTAAAGCGGGGGAACTAGAACCAGCGTTTTGGAATGTTCCTTGTTCAAGCATAATTCCGTGGTGTGTCACTTTTAGGGAAACGGTCACATAGCGCATATTGCT',
    'TTACAATCCGAGGTTAGCGCAAAATCACTGATGCATGCACATAGACTTCTTTGGCCATCGGACCGATATGGAATCCAAGAGCATTATTCCCAATCTCCGCAAGTGACAGTCTTAACCGAAAGAGTAAAGGCAAAATTAGGCGAATACCGGAGGGATTATTCGACCACGGATCGCTTTCCTCATTCCGTTTTGGTGC',
    'GGGAGGGAGAGTTCTTAAAGTTGGAACAGTATACGCTAAGGCGCAAATTCCAGTTGCTACGGACAGGGTGCTGTTAGCTAGTCCGTTCTATATCGCGTGGCTATTTAATCTTTACCTGCCGATTGCACCGTTCAGCCCTCTCTGGAAGCATAGCCCTAATTTAGAGTGCACAACTATGGCCATTAAACACTAAGAG',
    'GGGCAACATCCGTCGGCGGCCAATCCAATGATCCCTCAACTCGCGATAATCGGCTTAATTCATAAACCTCAGTGATAGGTGGTTACTTTGGAGGAGCACGAGTTCGACCCTCCGAGCCTATTTGCTACATAATCTAATTATAGAGATGGGTGTATAGACGCCGAGTTTACCGCAGGGTTCATGCGGGACCCCGCCC',
    'TTATAGACAAACACAGTTGGTGTCCGCGATAGAGTTGGCCTCGTAGTGTAGTTTCGATAGTTTCAGAAACCACTCGACTACGTAACAAGGCAACACTGGTCTCGGGCATGGAGCAACGCGGGCGTGTTTTATGCACTGAATTTAAGCATCCAGGGAGAGTTCGTGCCATAGGGCGGCCTCCAAGTGTCCGGTTGGA',
    'ACCCACTATCGGGACCCGTACCCTTGGTTGTCGATAATTCAGGTAGCGTATCCTGCTCACTCGCCAACTACGAGTTAGTCAACCTGGTTGAGAGTTCGACTGCAAAGGCCTGAATGTATCCAGACCATGATCGGGCTAAATATCGCATAACCGTGAGGCATCATCGTCAGCCGTATGGGCTCCCAAGCTGAATCGG']


# print(Rep_Rand_Mot_Searc(dna_list, 15, 20))


def GibbsSampler(dna_list, k, t, N):
    motifs = random_motif(dna_list, k)
    best_motif = motifs
    for elem in range(N):
        profile = Profile(motifs)
        motifs = []
        for i in range(t):
            motifs.append(most_probable_kmer(dna_list[i], k, profile))
        if Score(motifs) < Score(best_motif):
            best_motif = motifs
        else:
            return best_motif


def Rep_Rand_Mot_Gibbs(dna_list, k, t, N):
    Best_Score = float('inf')
    Best_Motif = []
    for i in range(1000):
        Motifs = GibbsSampler(dna_list, k, t, N)
        Current_Score = Score(Motifs)
        if Current_Score < Best_Score:
            Best_Score = Current_Score
            Best_Motif = Motifs
            print(Best_Score)
    return set(Best_Motif)


k = 15
t = 20
N = 2000

Dna = [
    'GCTAACAGGGTTCGGACTCTCTCTTATGACATCCCGCCCTCGGAAAAGTTTACCCTATCGCCAGATGGGGCCTCTTACGGTCCTACTGGATGTACCCCTTGGACGCTCAAATTAACACGCGTATGACCCAACTATCTCGAGGGAAGGTATGTGAAGGTAGGTCTCCTACATTACTACGAAAGTTCAATTTGCCTGTGTACGAATTCGTACGACCGCATTCCCGCATGATTTCTGCTAGGGAGTGATAAAGTACGAGCGTGCTTGTGGGGCTGCCCGACTACTTTCTCGGAGCTTGGTGTTTTAACGAATACACCTACGTGCTAACAGGGTTCGG',
    'ACTCTCTCTTATGACATCCCGCCCTCGGAAAAGTTTACCCTATCGCCAGATGGGGCCTCTTACGGTCCTACTGGATGTACCCCTTGGACGCTCAAATTAACACGCGTATGACCCAACTATCTCGAGGGAAGGTATGTGAAGGTAGGTCTCCTACATTACTACGAAAGTTCAATTTGCCTGTGTACGAATTCGTACGACCGCATTCCCGCATGATTTCTGCTAGGGAGTGATAAAGTACGAGCGTGCTTGTGGGGCTGCCCGACTACTTTCTCGGAGCTTGGTGTTTTAACGAATACACCTACGTGACAGCGACGGCTAATCTAACAGGGTTCGG',
    'AACGTGATCCAAAGGGACTTCCGTATTCCTACAGGAGTAAATCATATCTAACAGCCAAGTTCGGAGCTTCCAGTCTCAACATGGATTCTCATCACGTATGAGCGATTGACCAGTAGGACGTCCGAAGCAAAACTGACCACATGCTCGGCTAATCACGGTTCAACCATACCCTCTTAGATGTAAAGAGATCCACAACAGCTAGTCGGACAGAGATACCTGGCGTATAGGTGCAAAAGTTGTATCCCCAGAGGAACGCGATCCCTACTTAACTTCACTCGTCTGCTAGGGAGTCCTATGAGGGACAACCGGAACCGGCTAAAGTCAGGCATTCACG',
    'ATGACCATCTGATACGGATTATTTGCGGACATCATACCCGTTAATGCTGCCGGTTTCTCTAACTTTATGGGCATGGGCGGGTCAGGCCGGCGATTCCAGGCCAACAATAATTGGAGGATTATCGTTGTCGGTTCGCTGACAACGTCCATATTGCCGACGTCACGTACCGTTTGGTTTACGGCTAATGGTTTACAAAACATGTATCACCTTATGCCCAGCTGTATCTTTCGGATAATGGTTGTAGTACTCCAACGAATCTGTTAACATGTGCCAACTTCATGCAGCCCAGGGACAGCGAAGCCCTGTTGAAGCTCGGCACATTCCGTCACAGGAT',
    'ACGAGATGATGGGCTGCTGTCTAACTGGCCGGTCAGCCAGTCTGAACGCGATAGTTTTGCTGTTGACACCCGTAGATATAGTTCAGAATGAGTTGAGCTTTTCACTTTCAGAGTGACTATAAAAAGCTTGCAAGACCCGTATGCTGAGGGTCCCAAGAAAGAGAGCCGCAGGTGCATTTACGGCTACCTTACTGCGTACCCACAATATGGGCGGAACTTATATCCTAAGAGGTATGGGCCGACATCACCTCGAAAGGCATCCAGTGGCACGACCTCAGACAACTTAGGCGTGCTCAGCCAATAATGGTTTCACCCGCATGCGTTACACCTTCAC',
    'GTGAGTTACAGCCCCGAGGCCGCGTCAGGACGACGCCCGCTTGAACCGTGTGCGTTAACTCGAAGAGCCGCCTCTTGTTTCGGCCGTCTCCAGAATCGGCGCTGACGGGACAGACTGGTTATTGAGGTATGGGCACCAATAATTCTTGTTCTACGAAGATGTCTCTATGTAGGCTCCCGCCCAAACGATAAGTATTATCCCGTGACGACGATCGCTCATCCCTCATGCCCGTGCGTCCAGTAAAAACTACTGCGAGCGCGAGTGCCCTGCATCAGTTTGTCGCGACATTCTGGGCTAATCATCAGGGTAGCAGTGCGATACCAGCGTGGTACAA',
    'ATACACAATCTCCAGTACTCGCACCTAACGGACCTGCCCGACCTAAACAGGGTAGGTTACTATCAGGCGTTGTGGAGTGCATCTGCTAAAAGTGGATGTCTACGAGACCATCGCGCCGAGACTAATACGGCTAATGCTGTCAGGTGAAGCTCTGGTCTTTTCGTTGGGAGTGTACCGTCGCCCCCGTGTAACCAGTCTTGCTCAACTCATTTAATACTTGACGAGGCCGTAGCCGTGCTATGTTCACTCCATATCAGAATTGGCATCTACCAGTCCCTGATTGTGGCCTCTTAGTAAATCATGGGCCTTGCGACGTTTTAATCCGCCCGGCAGC',
    'CCTGCAGGAGAGTAGACTGATTCAAGACAGTCTCTATCTCCCTGAATGCAAAGAATCGCTTTCGTAGTGACAAACATCCCAGTATTTACGGCTAACGGGTAATTATGGCGTGTCATCCATGACCCTATTCAATCGCTCGCCCTACAGCGTTTGGCTGACCGAGAATCCGTTGCCCTTGCGATCAGCGCCAATTTTAGGAGCAATACGGTTATTAACGGTCACGCACACAATTGGTTTGGTTATCGGTAGGTGAGGTATGCCGGGTGAATATACGTTGAAAATCTATCGCTGCCCAAAGCCAAAGCCCGGCAGGCGGCCTGGCTAGGGACCAACT',
    'CTATCGTATAGGAGCACACCAAAACTCGGTAGGAACATGTCGACTCCGAACTCCAAGGTAAATTCCTGGATCTAAGGTACGGTCTTACAAAGTGAGAAACGGGGTTTAGCGTTCTCCAGTAAATGCCGCGGAAACGTGGCCTTCTGTGCGGTAAAGGTCTACAGAACAACCACGGCTAATCAGCTGTCAGATGAAGGAGCGGTTCCCTTGCTTCCAAGGAAGATGGCTGCCTTGCTGCCGACCTCAGTCCTGAGTGGATTGAGAACGTGAAAACGACCAGTGCTTAGTCCGACCCCGTGTAACGCCGGATTCGAGTTCATACTCAATGCGTGAC',
    'AAATCTTTTGTGGAACAACCTCTCACCGTCGCCTTTTTTACCCACCTGCCAGGGTACTACGTAAATAAGGGCCCAGCAAGCCTGATTGCTCGATGAGCGGGATGTCAGTCTATTATTTATGAATACCTGGCCCTTAGGATTTCATTAGTCACGAAGACTTGGACACCCTCCTCATCGGACCAAGATTTTGACATTTACGGCTTGAATAGGGGAGACTTACTTACATTAATGTCTGTCTCGTGATTGGCCTTCGATCGCCCGAAACATTCGATGACTTCATAACAACCATTGCCTTGAGAGGCGGCTATCCAAAGACACATCAAGGGACTCTTAC',
    'ATGGAGCGGTTTAGACACGAGTTATCCCCTATGTTGACCAATGCGGTGATTATAACTCGGAGAAACGAGCTCCTAACAACACGATACTAGCGTACCAATACTAATGAAGGCAGTATAAAAGTATGCGACCTCAATAGTAAGTTGTCCTCATGGGTAAGAGAGATACGGCGCTAAGCGCGATTGGTGAATCCAGACATTTTAAGCTAATACAATCTACCTCCCGGATAAGATAGAGACAGCGTGTATTTTAACCCGGCGTGGCAAAGAGTCGGAGACCCATTGTAAACGACCAAGAAACTAAAACTGGTCAGATCGCGCGCAGAAATGGTGGATA',
    'AGGGAATTGCACTCCAACAATTTCCTAAGTAAGGTTAGTCCGGAAGCGACTGTTGCACCATGACCAACTAGGTACAGAGCCATCGATTTTGGATCGACGGCTCAAGCACCAGACCAGTTGAAACTGACCCATATAAAGACTGTATTGCTAACGCTAGATCGCCTCCCTACTCTCGCCCTCGTTCACCCTAGTGACGGATTGTAAGGAGAATCGTGAGCGAACATTTACTATTAATCTCAAGGTTTCTCGCAGGCCCCGGCTTCATGCACGTCTGCAACGCGCCCCATCAGAAGTCAATCCGTGATGACCTGGCAACCAGGTAAGCATTAAGAGT',
    'ACCGCGAATTTGGTCGTAATGCAACGTATCTGTTACAATTCACTATTGACTTACCCATATTAGGGCGAAACCGCCCCGTCGCAGCACCGAGTCTCTCTTCCCATACTATATGCTTTAAACGGGCTGCCTTGAGTGCAACCGTCGCACACATGCGCAGCTAGCCCGTCTCGGGCAATTAACGTGGGACTATTCGTGTAACCTACGGTAATAATCGGAGAAAAGTTAGGAGGCTCAAGTAGCTAACTTTTTGGTTATTCGCGACTGAGTTAGGAACAACCTCAGATCACATTGTGGGCTAATTGTCAGTCACAATACTGATCCGTAAACCTGTTCC',
    'CTGGGACTACGCTGTAAACTGCACATGATATATATGCCTAAACGTTCATTTCCGAATTGACGCACCACGCACTCACGAATCGTGGTATGAGCTGGACCGGGCTTAACTACACCTCGACGCAAGAAGCAAAACTGATGAGGGTCATTCCAGACTATTAAGTATGGTCTTGTTCCATGTGGCCTCCCGCAATTTCGCCCGTATGTGACGACTTGCTGTTTACAGCTAACAGGCTCGCATGCACGTCCGAAAATTTATGAAACATTATACCCTGAGACACATAGGGCTTGCGGATTCAGGAGAAAGTGTGCTTACATCCCCGGCTAATTGGTTACCT',
    'TATGGGTCATACCGTGGTTAGACTCTGATAGAAAGAGTCTAGACCCCAGACACCCTCAGCAAGAAGAGTAAGAGATCGGAGAAACAGGATCCTTACCCCCAGAACATTTACGTACAATATCGGGCGGCAGTGCTACATAAGAACGATGACTCTATCGTGGGGCACGCCTACATAATGCGTCGACATAAAGAGTAATACAAAGACCCACAGGGCAAAATTGCCCCTCCCACCGATGCTCACGGCCAGGGGGCCCACATCTGTGACAGCGCACGGTGCTTTGACTAGTAGACTAGGAATGGTCATGGCCGGTGTGGGCTGCGTGGCCCTTCATTAT',
    'GCAGCTTACACCGCGGAAGTTAGTAGCGCAGATTTAAGTCCCCCTGAAAGTGTGAATTCATTTAATTGGCCCCGGGTGCCTCATTAGAACCCTTGTGAAAGTAGAAGAGTGAGGGATCACTAACATTTAGTCCTAATTACGAATAGAAGCATAGACTGATTTGGCCATAATTCAGGCTTTGCATCGGGCTCGGATCGGTGCCCCAAATTGTCCCTAGCACGATGGTCCTAAGCATAGAACGCGCATGGTGAAACGGAAAGAGAGCTTCTATGCTTCGTGTGAGAAGCCCTAACGGAGTCCGATCTCGTGCGAGTAACCGCAATGAGTTTCTCGC',
    'TTAGGATATACTGAACGGTGGACCGCACTGCTAGACTGACGTAGTTCCCCACGTGCCTTTCCCAGATTAACTACTAACCAATTGGCGAAGGAAAGCTTGAATGGGCCTAAGCTGGAAGTGTTAAATTTATGGTACTTCTGTGAACGAGAATACTTGCTGCAAAGGGATCAAGTAGACGCTAGGTCTTGTGCAAACTTCTCTTCCGGGTGGTTATTTACACCGGTGACTGGTTTGGAGGACTACCACAATGCCATTGTGTATCGGGTTGGGGTCGGTCTTGCGACATTTACGGCCCGTCAGTTAGGTTCTCACGGACGTTCGGCAACTCCTGATC',
    'CGTGATGACCGGCGCAGTCTAACTTCCTACTGGGGATTACAGCAGCACCTGCTGATAACGAGCCTGCTTAGTGGTTTCTGTCGCTAATAGAGTGAAAGCAGGACTCTTCTCATCGCATCGCCCTGTGGACTATAGCAACTCTATCAGCCTGGATTAATCACCTCCGTCAAAGGGCTAGATAGCGCCGCCGTAGTTCATTAGCTTGCGGCCTGCAAATCTGCTCTCTTATTACCTAGAATCTATGGTGGATGGCAAAAAAGCGTCGCAAGCATTGTCACCCCTCAGATTCGCTGCTCGTCAAACGGTACATTTTTTGCTAATTTCCTGATCGCCG',
    'ATTAGCCAGGTTATGCCCATATCGTTACGGCTAATAAACTCTCTTAGCTCGTGCAGTATGATCAGCGAAGAAAGTCGTGTCTTTTATTGCAGTAGGTATACGAGCGTTTCCATTCATTCTCCACGCTAAACGGGTGGAGAGGCGTAATCTGTAGTGACGAACCTATGTTTGGCTCTACCGAGATTGGCCTCTAGGCAAGGCTCACGACTGAGCACCGCGGCTCCCAAACGCGACTAAGTGTGACACAAATTATCCTATTGAGTACACCAACGTGACGGCGATGGCCCTTACCAATCCTGCAAAAAGCAAATGCGGGCTTAGCGTGTCCTGGGGC',
    'TTATTCCGAACCGTAATTCATAATGCCGAGAACAGAATCCCGACGTTGACCTCTTACAAGCGTATCGTACTGCTTGAGAATGGCAAAACATTCGCTTTGACGAGGCCACCTAAGGAGAATTAACTAGAATAAATGAGAAGCCCTGGAGATCTGCACGACCGACAATCACCACTTATATCCTTCTAAGTGCGAAAGGTGCAAATACCTACATTTACGGACCATACACAGTTCCACAGTCCCCTGCTGCCCGGGCTATAAATTGTTTTGTGCTTTAGGAGAACGTTTCGTCTTAGTATCTAAAGCTCTAACGACACAAAAACGTCGGCGGTTGGTA'
    ]

print(Rep_Rand_Mot_Gibbs(Dna, k, t, N))
