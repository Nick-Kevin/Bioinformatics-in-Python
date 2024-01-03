print("\nThis module calculate the Levenshtein distance between two ADN sequences\n")

FirstSequence = input("Enter the first sequence: ")
SecondSequence = input("Enter the second sequence: ")

def minimum(arg1, arg2, arg3):
    if arg1 < arg2:
        if arg1 < arg3:
            return arg1
        else: return arg3
    elif arg2 < arg3:
        return arg2
    else: return arg3

def levenshtein_distance(firstSequence, secondSequence):
    Distance = [[] for _ in range(len(secondSequence)+1)]
    Distance[0].append(0)
    for RowIndex in range(1, len(secondSequence), 1):
        Distance[RowIndex].append(Distance[RowIndex-1][0] + 1)
    for ColumnIndex in range(1, len(firstSequence), 1):
        Distance[0].append(Distance[0][ColumnIndex-1]+1)    
    """for row in Distance:
        for column in row:
            if firstSequence[column] != secondSequence[Distance.index(row)]:
                dist1 = Distance[Distance.index(row)-1][column-1] + 1
            else:
                dist1 = Distance[Distance.index(row)-1][column-1]
            dist2 = Distance[Distance.index(row)-1][column] + 1
            dist3 = Distance[Distance.index(row)][column-1] + 1
            Distance[Distance.index(row)].append(minimum(dist1, dist2, dist3))"""
    for RowIndex in range(1, len(Distance)-1):
        for ColumnIndex in range(1, len(firstSequence)):
            if firstSequence[ColumnIndex] != secondSequence[RowIndex]:
                dist1 = Distance[RowIndex-1][ColumnIndex-1] + 1
            else:
                dist1 = Distance[RowIndex-1][ColumnIndex-1]
            dist2 = Distance[RowIndex-1][ColumnIndex] + 1
            dist3 = Distance[RowIndex][ColumnIndex-1] + 1
            Distance[RowIndex].append(minimum(dist1, dist2, dist3))
    for row in Distance:
        for column in row:
            print(column, end=" ")
        print()
    

levenshtein_distance(FirstSequence, SecondSequence)