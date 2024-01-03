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

for Row in DistancesBetweenSequences:
    for Column in Row:
        print(Column, end=" ")
    print()