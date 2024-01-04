from levenshtein_distance import levenshtein_distance

# sequences: ensemble de mots
# mots ou sequence: ADN

def find(table, value):
    for Row in table:
        for Column in Row:
            if value == Column:
                return { 'row': table.index(Row), 'col': Row.index(value)}
    return { 'row': -1, 'col': -1 }

def get_minimum_in_distance_table(DistanceTable):
    DistancesWithoutZero = []
    for Row in DistanceTable:
        for item in Row:
            if isinstance(item, int) and item > 0:
                DistancesWithoutZero.append(item)
    minimum = min(DistancesWithoutZero)
    return minimum

def get_sequences_by_distance(table, distance_value):
    Position = find(table, distance_value)
    ColumnOfTheDistance = Position['col']
    FirstSequence = table[0][ColumnOfTheDistance]
    RowOfTheDistance = Position['row']
    SecondSequence = table[RowOfTheDistance][0]
    return { 'first_sequence': FirstSequence, 'second_sequence': SecondSequence }

def is_finished(table, sequences_table):
    InSequencesTable = 0
    for item in table:
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
    Merge = []
    for sequence in firstClassTable:
        Merge.append(sequence)
    for sequence in secondClassTable:
        Merge.append(sequence)
    return Merge

def create_new_table(sequences):
    DistanceTable = []
    FirstRow = []
    FirstRow.append("")
    for sequence in sequences:
        FirstRow.append(sequence)
    DistanceTable.append(FirstRow)
    # add rows width distance in distance table
    for sequence in sequences:
        NewRow = []
        NewRow.append(sequence)
        for item in sequences:
            distance = 0
            if is_class(item) and is_class(sequence):
                distance = distance_between_classes(item, sequence)
            elif is_class(item):
                distance = distance_between_class_and_sequence(item, sequence)
            elif is_class(sequence):
                distance = (distance_between_class_and_sequence(sequence, item))
            else:
                distance = levenshtein_distance(item, sequence)
            NewRow.append(distance)
        DistanceTable.append(NewRow)
    return DistanceTable

def create_sequences(LastSequences, NewClass):
    NewSequences = []
    for item in LastSequences:
        if is_class(item):
            count = 0
            for sequence in NewClass:
                for i in item:
                    if i == sequence:
                        count += 1
            if(count == 0):
                NewSequences.append(item)    
        else:
            InNewClass = False
            for sequence in NewClass:
                if sequence == item:
                    InNewClass = True
            if InNewClass == False:
                NewSequences.append(item)
    NewSequences.append(NewClass)
    return NewSequences


def main():
    NumberOfSequences = int(input("Enter the number of sequences: "))
    Sequences = []
    for i in range(NumberOfSequences):
        sequence = input("Entrer the ADN sequence " + str(i+1) + ": ")
        Sequences.append(sequence)

    print("All sequences you entered: ", Sequences)

    Classes = []
    LastSequences = Sequences
    while True:
        DistancesTable = create_new_table(LastSequences)
        MinimumDistance = get_minimum_in_distance_table(DistancesTable)
        SequecenesPositions = get_sequences_by_distance(DistancesTable, MinimumDistance)
        FirstSequence = SequecenesPositions['first_sequence']
        SecondSequence = SequecenesPositions['second_sequence']        
        # create new class
        NewClasses = []
        if is_class(FirstSequence) and is_class(SecondSequence):
            NewClasses = merge_classes(FirstSequence, SecondSequence)
        elif is_class(FirstSequence):
            for sequence in FirstSequence:
                NewClasses.append(sequence)
            NewClasses.append(SecondSequence)
        elif is_class(SecondSequence):
            for sequence in SecondSequence:
                NewClasses.append(sequence)
            NewClasses.append(SecondSequence)
        else:
            NewClasses = [FirstSequence, SecondSequence]
        Classes.append(NewClasses)
        print("new class", NewClasses)
        LastSequences = create_sequences(LastSequences, NewClasses)
        LastClass = Classes[len(Classes)-1]
        if is_finished(LastClass, Sequences):
            break
    for classe in reversed(Classes):
        print("classe niveau:", classe)
    LastLevel = "classe niveau: "
    for sequence in Sequences:
        a = [sequence]
        LastLevel += str(a) + ", "
    print(LastLevel)



main()