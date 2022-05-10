def start_stop_codon(frame, pos, orflen, dna):
    dna = dna.upper()
    for i in range(frame, len(dna), 3):
        codon1 = dna[i: i + 3]
        if codon1 == 'ATG':
            position1 = i
            for j in range(position1, len(dna), 3):
                codon2 = dna[j: j + 3]
                if codon2 in ['TAA', 'TAG', 'TGA']:
                    position2 = j
                    orflen = position2 - position1 + 3
                    yield (frame + 1, position1 + 1, orflen, dna[position1:position2 + 3])
                    break


def main():
    dna = 'ATGTGGATTATGGCTGGGGAGTAG'
    frame = 0
    pos = 0
    orflen = 0
    results = print(list(start_stop_codon(frame, pos, orflen, dna)))

    for frame, pos, orflen, orf in start_stop_codon(frame, pos, orflen, dna):
        return results


if __name__ == '__main__':
    main()