# The following function should NOT be modified!!
def read_one_seq_fasta(file):
    """Read a FASTA file that contains one sequence."""

    seq = ''
    with open(file, 'r') as f:
        f.readline()  # bypass description in first line of data file
        for line in f.readlines():
            seq = seq + line[:-1]
        print(seq)
        return seq


# The above function should NOT be modified!!!

def gc_content(seq):
    """determine gc content"""

    count_G = 0
    count_C = 0
    for itr in seq:
        if itr == 'G':
            count_G += 1
        elif itr == 'C':
            count_C += 1
    return float((count_C + count_G)) / float(len(seq))


# Tests for gc_content function. Should print True in all cases.
print('\ngc_content Tests')
print(gc_content('ATGTGAA') == 0.2857142857142857)
print(gc_content('ATGAGATAAG') == 0.3)


def get_orf(seq):
    ''' describe function here '''

    stop_codons = ['TAG', 'TAA', 'TGA']
    itr = 0
    while itr < len(seq):
        if seq[itr:itr + 3] in stop_codons:
            return seq[0:itr]
    else:
        itr += 3
    return seq


# Tests for get_orf function. Should print True in all cases.
print('\nget_orf Tests')
print(get_orf('ATGTGAA') == 'ATG')
print(get_orf('ATGAGATAAG') == 'ATGAGA')
print(get_orf('ATGAGATAGG') == 'ATGAGA')
print(get_orf('ATGAGATGAGGGTAA') == 'ATGAGA')
print(get_orf('ATGAAATT') == 'ATGAAATT')


def one_frame(seq):
    ''' describe function here '''

    start_codon = 'ATG'
    orf = []
    itr = 0
    while itr < len(seq):
        if seq[itr:itr + 3] == start_codon:
            orf.append(get_orf(seq[itr:len(seq)]))
    itr += 3
    return orf


# Tests for one_frame function. Should print True in all cases.
print('\none_frame')
print(one_frame('ATGTGAA') == ['ATG'])
print(one_frame('ATGAGATAAG') == ['ATGAGA'])
print(one_frame('ATGAGATAGG') == ['ATGAGA'])
print(one_frame('ATGAGATGAGGGTAA') == ['ATGAGA'])
print(one_frame('ATGAAATT') == ['ATGAAATT'])
print(one_frame('ATGAGATGAACCATGGGGTAA') == ['ATGAGA', 'ATGGGG'])


def forward_frames(seq):
    ''' describe function here '''

    orf = []
    orf += one_frame(seq[0:])
    orf += one_frame(seq[1:])
    orf += one_frame(seq[2:])
    return orf


# Tests for forward_frames function. Should print True in all cases.
print('\nforward_frames')
print(forward_frames('ATGAGATAAG') == ['ATGAGA'])
print(forward_frames('ATGAGATGAGGGTAA') == ['ATGAGA', 'ATGAGGGTAA'])
print(forward_frames('ATGAAATT') == ['ATGAAATT'])
print(forward_frames('ATGAGATGACACCATGGGGTAA') == ['ATGAGA', 'ATGGGG', 'ATGACACCATGGGGTAA'])


def gene_finder(fasta_file, min_len, min_gc):
    ''' describe function here '''

    file_dna = read_one_seq_fasta(fasta_file)
    ff = forward_frames(file_dna)
    result = []
    for itr in ff:
        gc = gc_content(itr)
    if len(itr) >= min_len and gc >= min_gc:
        result.append([len(itr), gc, itr])
    return result


# Tests for gene_finder function. Should print True.
print('\ngene_finder')
calculated_result = gene_finder('gene_finder_test.fasta', 6, 0.45)
desired_result = [[6, 0.6666666666666666, 'ATGCCC'], [9, 0.7777777777777778, 'ATGCCCCGG']]
print(calculated_result == desired_result)

orf_list = gene_finder('human_chr9_segment.fasta', 550, 0.45)
print(len(orf_list) == 6)

# viewing the results of the gene_finder( ) calculations
orf_list = gene_finder('gene_finder_test.fasta', 6, 0.45)
print(orf_list)


def main():
    file = 'gene.fna'
    seq = read_one_seq_fasta(file)
    print(seq)


if __name__ == '__main__':
    main()
