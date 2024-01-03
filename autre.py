from levenshtein_distance import levenshtein_distance

NumberOfSequences = int(input("Enter the number of ADN sequences: "))

Sequences = []
for _ in range(NumberOfSequences):
    Sequence = input("Enter the ADN sequence " + str(_+1) + ": ")
    Sequences.append(Sequence)

print("All sequences you'd enter:", Sequences)

DistancesBetweenSequences = []
for rowSequence in Sequences:
    CurrentRow = []
    for colSequence in Sequences:
        distance = levenshtein_distance(rowSequence, colSequence)
        CurrentRow.append(distance)
    DistancesBetweenSequences.append(CurrentRow)

Blank = " "
FirstRow = []
DistancesBetweenSequencesLength = len(DistancesBetweenSequences)
charLength = len(str(DistancesBetweenSequencesLength+1))
FirstColFirstRow = ""
for _ in range(charLength+1):
    FirstColFirstRow += Blank
FirstColFirstRow += "|"
FirstRow.append(FirstColFirstRow)
for sequence in range(len(Sequences)):    
    ColumnValue = " x" + str(sequence+1) + "|"
    FirstRow.append(ColumnValue)
FirstRowToPrint = ""
for _ in FirstRow:
    FirstRowToPrint += _
print()
print(FirstRowToPrint)
for Row in DistancesBetweenSequences:
    CurrentRow = "x" + str(DistancesBetweenSequences.index(Row)+1) + "|"
    for Column in Row:
        CurrentRow += "  " + str(Column) + "|"
    print(CurrentRow)