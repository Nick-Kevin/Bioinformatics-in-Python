from levenshtein_distance import levenshtein_distance

def find(table, value):
    for Row in table:
        for Column in Row:
            if value == Column:
                return { 'row': table.index(Row), 'col': Row.index(value)}
    return { 'row': -1, 'col': -1 }

def get_sequences_by_distance(table, distance_value):
    Position = find(table, distance_value)
    ColumnOfTheDistance = Position['col']
    FirstSequence = table[0][ColumnOfTheDistance]
    RowOfTheDistance = Position['row']
    SecondSequence = table[RowOfTheDistance][0]
    return { 'first_sequence': FirstSequence, 'second_sequence': SecondSequence }

def is_finished(table, sequences_table):
    LastTable = table[len(table)-1]
    InSequencesTable = 0
    for item in LastTable:
        for sequence in sequences_table:
            if item == sequence:
                InSequencesTable += 1
    if InSequencesTable != len(sequences_table):
        return False
    return True

def is_class(value):
    if isinstance(value, list) == False:
        return False
    return True

def distance_between_class_and_sequence(classTable, sequence):
    Distance = []
    for item in classTable:
        dist = levenshtein_distance(item, sequence)
        Distance.append(dist)
    minimum = min(Distance)
    return minimum

def distance_between_classes(firstClassTable, secondClassTable):
    Distance = []
    for sequence in secondClassTable:
        dist = distance_between_class_and_sequence(firstClassTable, sequence)
        Distance.append(dist)
    minimum = min(Distance)
    return minimum

def merge_classes(firstClassTable, secondClassTable):
    for sequence in secondClassTable:
        firstClassTable.append(sequence)
    return firstClassTable

def main():
    NumberOfSequences = int(input("Enter the number of sequences: "))
    Sequences = []
    for i in range(NumberOfSequences):
        sequence = input("Entrer the ADN sequence " + str(i+1) + ": ")
        Sequences.append(sequence)

    print("All sequences you entered: ", Sequences)

    DistanceTable = []
    Classes = []
    FirstRow = []
    FirstRow.append("")
    for sequence in Sequences:
        FirstRow.append(sequence)
    print(FirstRow  )
    DistanceTable.append(FirstRow)

    for sequence in Sequences:
        NewRow = []
        NewRow.append(sequence)
        for other_sequence in Sequences:
            Distance = levenshtein_distance(sequence, other_sequence)
            NewRow.append(Distance)
        DistanceTable.append(NewRow)

    for Row in DistanceTable:
        print(Row)

    Value = int(input("Enter the distance between the two sequence: "))

    SequencesOfTheValue = get_sequences_by_distance(DistanceTable, Value)
    print('First sequence: ', SequencesOfTheValue['first_sequence'])
    print('Second sequence: ', SequencesOfTheValue['second_sequence'])

#main()
tab = ["aa","bb", "cc"]
checkTab = is_class(['a'])
if checkTab:
    print("it's an array")
else:
    print("it's not array")