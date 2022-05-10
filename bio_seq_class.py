# seq = 'ATGCTAATGTACCATTTTCCATAG'


class BioSeq:
    def __init__(self, seq="ATCG", seq_type="DNA", label="No Label"):
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Input data does not seem to be a correct {self.seq_type} sequence."

    def __validate(self):
        dna_nucs = ['A', 'T', 'C', 'G']
        return set(dna_nucs).issuperset(self.seq)
