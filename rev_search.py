import re


def revSearch(seq, length):
    # Dictionary to return output, in format key = frame pos length, value = sequence
    revDict = {}

    # Pull variables from input
    revSeq = seq.replace(" ", "").replace("/n", "")
    length = length

    # Create two additional sequences for other two frames
    revSeq5 = revSeq[1:]
    revSeq6 = revSeq[2:]

    # Format sequences to add a space allowing for regex
    revSeq4String = ""
    revSeq5String = ""
    revSeq6String = ""

    while len(revSeq) >= 3:
        tempCodon = revSeq[0:3]
        revSeq4String += tempCodon + " "
        revSeq = revSeq[3:]

    while len(revSeq5) >= 3:
        tempCodon = revSeq5[0:3]
        revSeq5String += tempCodon + " "
        revSeq5 = revSeq5[3:]

    while len(revSeq6) >= 3:
        tempCodon = revSeq6[0:3]
        revSeq6String += tempCodon + " "
        revSeq6 = revSeq6[3:]

    # Search Frame 4 with regex
    frame = 4
    firstMatch = re.search("ATG", revSeq4String)
    if firstMatch != None:
        # Set negative for Frames 4-6
        POS = firstMatch.start() + 1
        # Negative pos variables
        negativePOS = 0 - POS

        # Length will be found using replace()
        firstEnd = re.search("TAA|TAG|TGA", revSeq4String)
        if firstEnd != None:
            tempValue = revSeq4String[firstMatch.start():firstEnd.end()]
            stringStripped = tempValue.replace(" ", "").replace("\n", "")
            tempLength = len(stringStripped)
            # Ensures only proper length sequences are added to dictionary
            if tempLength > length:
                # Add back spaces and newline character for output
                codonCounter = 1
                dictValue = ""
                while len(stringStripped) > 3:
                    codon = stringStripped[0:3]
                    stringStripped = stringStripped[3:]
                    if codonCounter == 15:
                        dictValue += codon + "\n"
                        codonCounter = 1
                    else:
                        dictValue += codon + " "
                        codonCounter += 1
                keyString = str(frame) + " " + str(negativePOS) + " " + str(tempLength)
                revDict[keyString] = dictValue

            # Gets ready for loop, plus 1 accounts for extra space
            revSeq4String = revSeq4String[firstEnd.end() + 1:]
            nextMatch = re.search("ATG", revSeq4String)

            while nextMatch != None:
                POS = nextMatch.start() + POS + tempLength
                negativePOS = 0 - POS
                nextEnd = re.search("TAA|TAG|TGA", revSeq4String)
                if nextEnd != None:
                    tempValue = revSeq4String[nextMatch.start():nextEnd.end()]
                    stringStripped = tempValue.replace(" ", "").replace("\n", "")
                    tempLength = len(stringStripped)

                    if tempLength > length:
                        # Add back spaces and newline character for output
                        codonCounter = 1
                        dictValue = ""
                        while len(stringStripped) > 3:
                            codon = stringStripped[0:3]
                            stringStripped = stringStripped[3:]
                            if codonCounter == 15:
                                dictValue += codon + "\n"
                                codonCounter = 1
                            else:
                                dictValue += codon + " "
                                codonCounter += 1
                        keyString = str(frame) + " " + str(negativePOS) + " " + str(tempLength)
                        revDict[keyString] = dictValue

                    revSeq4String = revSeq4String[nextEnd.end():]
                    nextMatch = re.search("ATG", revSeq4String)
                else:
                    nextMatch = None

                    # Search Frame 5 with regex (Copied from Frame 4)
    frame = 5
    firstMatch = re.search("ATG", revSeq5String)
    if firstMatch != None:
        # Set negative for Frames 4-6
        POS = firstMatch.start() + 2
        # Negative pos variables
        negativePOS = 0 - POS

        # Length will be found using replace()
        firstEnd = re.search("TAA|TAG|TGA", revSeq5String)
        if firstEnd != None:
            tempValue = revSeq5String[firstMatch.start():firstEnd.end()]
            stringStripped = tempValue.replace(" ", "").replace("\n", "")
            tempLength = len(stringStripped)
            # Ensures only proper length sequences are added to dictionary
            if tempLength > length:
                # Add back spaces and newline character for output
                codonCounter = 1
                dictValue = ""
                while len(stringStripped) > 3:
                    codon = stringStripped[0:3]
                    stringStripped = stringStripped[3:]
                    if codonCounter == 15:
                        dictValue += codon + "\n"
                        codonCounter = 1
                    else:
                        dictValue += codon + " "
                        codonCounter += 1
                keyString = str(frame) + " " + str(negativePOS) + " " + str(tempLength)
                revDict[keyString] = dictValue

            # Gets ready for loop, plus 1 accounts for extra space
            revSeq5String = revSeq5String[firstEnd.end() + 1:]
            nextMatch = re.search("ATG", revSeq5String)

            while nextMatch != None:
                POS = nextMatch.start() + POS + tempLength
                negativePOS = 0 - POS
                nextEnd = re.search("TAA|TAG|TGA", revSeq5String)
                if nextEnd != None:
                    tempValue = revSeq5String[nextMatch.start():nextEnd.end()]
                    stringStripped = tempValue.replace(" ", "").replace("\n", "")
                    tempLength = len(stringStripped)

                    if tempLength > length:
                        # Add back spaces and newline character for output
                        codonCounter = 1
                        dictValue = ""
                        while len(stringStripped) > 3:
                            codon = stringStripped[0:3]
                            stringStripped = stringStripped[3:]
                            if codonCounter == 15:
                                dictValue += codon + "\n"
                                codonCounter = 1
                            else:
                                dictValue += codon + " "
                                codonCounter += 1
                        keyString = str(frame) + " " + str(negativePOS) + " " + str(tempLength)
                        revDict[keyString] = dictValue

                    revSeq5String = revSeq5String[nextEnd.end():]
                    nextMatch = re.search("ATG", revSeq5String)
                else:
                    nextMatch = None

                    # Search Frame 6 with regex
    frame = 6
    firstMatch = re.search("ATG", revSeq6String)
    if firstMatch != None:
        # Set negative for Frames 4-6
        POS = firstMatch.start() + 3
        # Negative pos variables
        negativePOS = 0 - POS

        # Length will be found using replace()
        firstEnd = re.search("TAA|TAG|TGA", revSeq6String)
        if firstEnd != None:
            tempValue = revSeq6String[firstMatch.start():firstEnd.end()]
            stringStripped = tempValue.replace(" ", "").replace("\n", "")
            tempLength = len(stringStripped)
            # Ensures only proper length sequences are added to dictionary
            if tempLength > length:
                # Add back spaces and newline character for output
                codonCounter = 1
                dictValue = ""
                while len(stringStripped) > 3:
                    codon = stringStripped[0:3]
                    stringStripped = stringStripped[3:]
                    if codonCounter == 15:
                        dictValue += codon + "\n"
                        codonCounter = 1
                    else:
                        dictValue += codon + " "
                        codonCounter += 1
                keyString = str(frame) + " " + str(negativePOS) + " " + str(tempLength)
                revDict[keyString] = dictValue

            # Gets ready for loop, plus 1 accounts for extra space
            revSeq6String = revSeq6String[firstEnd.end() + 1:]
            nextMatch = re.search("ATG", revSeq6String)

            while nextMatch != None:
                POS = nextMatch.start() + POS + tempLength
                negativePOS = 0 - POS
                nextEnd = re.search("TAA|TAG|TGA", revSeq6String)
                if nextEnd != None:
                    tempValue = revSeq6String[nextMatch.start():nextEnd.end()]
                    stringStripped = tempValue.replace(" ", "").replace("\n", "")
                    tempLength = len(stringStripped)

                    if tempLength > length:
                        # Add back spaces and newline character for output
                        codonCounter = 1
                        dictValue = ""
                        while len(stringStripped) > 3:
                            codon = stringStripped[0:3]
                            stringStripped = stringStripped[3:]
                            if codonCounter == 15:
                                dictValue += codon + "\n"
                                codonCounter = 1
                            else:
                                dictValue += codon + " "
                                codonCounter += 1
                        keyString = str(frame) + " " + str(negativePOS) + " " + str(tempLength)
                        revDict[keyString] = dictValue

                    revSeq6String = revSeq6String[nextEnd.end():]
                    nextMatch = re.search("ATG", revSeq6String)
                else:
                    nextMatch = None

    return revDict


seq = "GTATGGTGTAGATGGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTTAAATGGTGTGTGTGTGTGTGTGTGTGTGTTTTGTGTGTTTATAA"

rev_dict = revSearch(seq, 10)
print(rev_dict)


def unwrap(rev_dict):
    for k, v in rev_dict.items():
        yield [(k2.strip(), v) for k2 in k.split(',')]


key_list = unwrap(rev_dict)

for i in key_list:
    print(key_list)
