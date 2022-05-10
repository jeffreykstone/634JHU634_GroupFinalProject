#!/usr/bin/env python
# coding: utf-8

import re


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
    print(seq_dict)
    return seq_dict


def get_reverse_complement(sequence):
    """Function that returns the reverse complement of given DNA sequence."""
    rev_seq = sequence[::-1]  # reverse the given sequence
    # dictionary containing complementary bases
    complementary_bases = {"G": "C", "C": "G", "A": "T", "T": "A"}
    # return reverse complementary sequence
    return "".join([complementary_bases[base] for base in rev_seq])


def get_open_reading_frames(sequence, length):
    """Function that returns list of all possible open reading frames of the min
    length in the given DNA sequences (or reverse complement of each).
    """
    all_orfs_list = []
    # regular expression identifying ORFs
    orf_regex = "(ATG(([AGCT]){3})*?(TAG|TGA|TAA))"
    # use the above regular expression to identify ORFs in the given DNA sequence
    all_orfs_list.extend(re.findall("(?=%s)" % orf_regex, sequence))
    # use the above regular expression to identify ORFs in the reverse complement sequence
    all_orfs_list.extend(re.findall("(?=%s)" % orf_regex, get_reverse_complement(sequence)))
    # Keep the orfs longer than the min length
    orfs_of_min_length_list = []
    # iterate through all extracted ORFs
    for (frame, a, b, c) in all_orfs_list:
        if len(frame) >= length:
            orfs_of_min_length_list.append(frame)
    # return the ORFs of specified number of bases
    return orfs_of_min_length_list


# ask user to enter FASTA file_path or path
file_path = input("Enter FASTA file_path: ")
min_length = int(input("Enter the minimum length of ORF to search for (greater than 50): "))
if min_length < 50:
    print("The minimum length will be set to 50.")
    min_length = 50

# read and process the FASTA file
seq_dict = process_fasta_file(file_path)

# iterate through all sequences
for header, seq in seq_dict.items():
    # get ORFs
    orfs = get_open_reading_frames(seq, min_length)
    # print all obtained ORFs
    for i, orf in enumerate(orfs):
        print(">", header)
        print("ORF %d: %s" % (i + 1, orf))
    print(end="\n\n")
