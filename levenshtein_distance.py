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
    Rows, Cols = (len(firstSequence), len(secondSequence))
    Distance = [[0] * Cols] * Rows
    print(Distance)

levenshtein_distance(FirstSequence, SecondSequence)