sequences = []
descr = None
# here is the path of multi-fasta file
with open('gene.fna') as file:
    line = file.readline()[:-1]  # always trim newline
    while line:
        if line[0] == '>':
            if descr:  # any sequence found yet?
                sequences.append((descr, seq))
            descr = str(line[1:].split('>'))
            seq = ''  # start a new sequence
        else:
            seq += line
        line = file.readline()[:-1]
    sequences.append((descr, seq))
print(sequences)

list_of_orf = list()
for index, value in enumerate(sequences):  # looping over the fragments extracted
    frames = []  # storing the six frame translation that should be extracted from the fragments
    dna = value[1]  # extract the fragment
    description = value[0]  # extract the description
    reverse_cdna = []  # storing the reverse complements
    # create the positive frames
    # split the frames into codons for better performance
    frames.append([dna[i:i + 3] for i in range(0, len(dna), 3)])
    frames.append([dna[i:i + 3] for i in range(1, len(dna), 3)])
    frames.append([dna[i:i + 3] for i in range(2, len(dna), 3)])
    # reverse complement of the fragment
    reverse = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for i in range(len(dna)):
        reverse_cdna.append(reverse[dna[-i - 1]]) if dna[-i - 1] in reverse.keys() else reverse_cdna.append(
            dna[-i - 1])  # if any contamination found we keep it for further check
    reverse_cdna = ''.join(reverse_cdna)  # joining
    # create the negative frames
    frames.append([reverse_cdna[i:i + 3] for i in range(0, len(reverse_cdna), 3)])
    frames.append([reverse_cdna[i:i + 3] for i in range(1, len(reverse_cdna), 3)])
    frames.append([reverse_cdna[i:i + 3] for i in range(2, len(reverse_cdna), 3)])

for i in range(0, len(frames), 1):  # looping all the frames
    start = 0
    while start < len(frames[i]):  # looping each frame for start and stop codons
        if frames[i][start] == "ATG":
            for stop in range(start + 1, len(frames[i]), 1):
                if frames[i][stop] == "TAA" or frames[i][stop] == "TAG" or frames[i][stop] == "TGA":
                    list_of_orf.append(frames[i][start:stop])  # retrieve the orf
                    start = stop + 1  # avoiding multiple start codons
                    break
        start += 1

print(list_of_orf)