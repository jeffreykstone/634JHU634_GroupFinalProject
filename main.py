#!/usr/bin/env python
# coding: utf-8
'''
def process_fasta_file(file_path):
    """Function that process the given FASTA file (file_path) and returns
    dictionary with key as sequence ID and value as sequence.
    """

    # open the file
    with open(file_path, "r") as f:
        seq_dict = {}  # dictionary for storing all sequences read from the file
        header = 0  # sequence ID
        seq = ""  # concatenate sequences
        # iterate through lines of FASTA file
        for line in f:
            # remove white spaces and convert to uppercase
            line = line.replace(" ", "").upper()
            # if first character of the line is ">" => header (seqID)
            if line.startswith(">"):
                if header != 0:
                    # store in seq_dict dictionary
                    seq_dict[header] = seq
                header = line[1:-1]
                seq = ""
            else:
                # concatenate to seq
                seq += line[:-1]
        # for last sequence
        seq_dict[header] = seq
    # return the dictionary containing all sequences
    print(f"seq_dict: {seq_dict}")
    return seq_dict
'''


def get_reverse_complement(seq):
    """Function returns the reverse complement of given DNA sequence."""
    rev_seq = seq[::-1]  # reverse the given sequence
    # dictionary containing complementary bases
    complementary_bases = {"G": "C", "C": "G", "A": "T", "T": "A"}
    # return reverse complementary sequence
    return "".join([complementary_bases[base] for base in rev_seq])


def start_stop_codon(frame, pos, orf_len, seq):
    """Generator function returns FRAME, POS, LEN, SEQ of ORFs"""
    seq = seq.upper()
    for i in range(frame, len(seq), 3):
        codon1 = seq[i: i + 3]
        if codon1 == 'ATG ':
            position1 = i
            for j in range(position1, len(seq), 3):
                codon2 = seq[j: j + 3]
                if codon2 in ['TAA', 'TAG', 'TGA']:
                    position2 = j
                    orf_len = position2 - position1 + 3
                    yield frame + 1, position1 + 1, orf_len, seq[position1:position2 + 3]
                    break


def main():
    '''
    # ask user to enter FASTA file_path or path
    file_path = input("Enter FASTA file_path: ")
    min_length = int(input("Enter the minimum length of ORF to search for (greater than 50): "))
    if min_length < 50:
        print("The minimum length will be set to 50.")
        min_length = 50

    # read and process the FASTA file
    seq = process_fasta_file(file_path)
    '''

    seq = 'ATGTGGATTATGGCTGGGGAGTAG'
    frame = 0
    pos = 0
    orf_len = 0
    results = list(start_stop_codon(frame, pos, orf_len, seq))

    for index, tup in enumerate(results):
        frame_element = tup[0]
        pos_element = tup[1]
        orf_len_element = tup[2]
        seq_element = tup[3]
        print(f"> **Insert Header Here|FRAME = {frame_element} POS = {pos_element} \
LEN = {orf_len_element}\n{seq_element}")
    # for frame, pos, orflen, orf in start_stop_codon(frame, pos, orflen, seq):


if __name__ == '__main__':
    main()

'''




'''
