from levenshtein_distance import levenshtein_distance

NumberOfSequences = int(input("Enter the number of ADN sequences or genes: "))

Sequences = []
for _ in range(NumberOfSequences):
    Sequence = input("Enter the ADN sequence " + str(_+1) + ": ")
    Sequences.append(Sequence)

print("All sequences you entered:", Sequences)

DoorStep = int(input("Enter the doorstep: "))
Classes = []
Classe1 = []
Classe1.append(Sequences[0])
Classes.append(Classe1)
j = 1
m = 1
while j < len(Sequences):
    Distances = []   
    for classe in Classes:
        DistanceBetweenSequences = []
        for sequence in classe:
            distance = levenshtein_distance(sequence, Sequences[j])
            DistanceBetweenSequences.append(distance)
        DistanceBetweenClassAndGene = min(DistanceBetweenSequences)
        Distances.append(DistanceBetweenClassAndGene)
    MinimumDistance = min(Distances)
    PositionOfTheMinimumDistance = Distances.index(MinimumDistance)
    if MinimumDistance <= DoorStep:
        ClassOfTheGene = Classes[PositionOfTheMinimumDistance]
        ClassOfTheGene.append(Sequences[j])
    else:
        Classes.append([]) # nouvelle classe pour Sequences[j]
        Classes[m].append(Sequences[j]) # insertion de la sequence dans la nouvelle classe
        m += 1
    j += 1

# display
print()
for classe in Classes:
    GroupeClass = "Classe " + str(Classes.index(classe)+1) + ":"
    for sequence in classe:
        GroupeClass += " " + sequence + ", "
    print(GroupeClass)
print()
