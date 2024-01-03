def minimum(arg1, arg2, arg3):
    if arg1 < arg2:
        if arg1 < arg3:
            return arg1
        else: return arg3
    elif arg2 < arg3:
        return arg2
    else: return arg3

def levenshtein_distance(firstSequence, secondSequence):
    RowNumberToStop = len(secondSequence) + 1
    ColumnNumberToStop = len(firstSequence)+1
    Distance = [[] for _ in range(RowNumberToStop)]    
    Distance[0].append(0)
    for RowIndex in range(1, RowNumberToStop):
        Distance[RowIndex].append(Distance[RowIndex-1][0] + 1)
    for ColumnIndex in range(1, ColumnNumberToStop):
        Distance[0].append(Distance[0][ColumnIndex-1]+1)
    for RowIndex in range(1, len(Distance)):
        for ColumnIndex in range(1, ColumnNumberToStop):
            if firstSequence[ColumnIndex-1] != secondSequence[RowIndex-1]:
                dist1 = Distance[RowIndex-1][ColumnIndex-1] + 1
            else:
                dist1 = Distance[RowIndex-1][ColumnIndex-1]
            dist2 = Distance[RowIndex-1][ColumnIndex] + 1
            dist3 = Distance[RowIndex][ColumnIndex-1] + 1
            Distance[RowIndex].append(minimum(dist1, dist2, dist3))
    LevenshteinDistanceBetweenTheTwoSequences = Distance[len(secondSequence)][len(firstSequence)]
    print("The levenshtein distance between '" + firstSequence + "' and '" + secondSequence + "' is:")
    print("Dl(" + firstSequence + "," + secondSequence + ") =", LevenshteinDistanceBetweenTheTwoSequences)
    return LevenshteinDistanceBetweenTheTwoSequences