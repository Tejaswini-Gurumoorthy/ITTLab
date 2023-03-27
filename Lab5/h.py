# function to perform set operations
def set_operations(set1, set2):
    # union of sets
    union = set1 | set2
    # intersection of sets
    intersection = set1 & set2
    # difference of sets
    diff1 = set1 - set2
    diff2 = set2 - set1
    # symmetric difference of sets
    # display the results
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Union of sets:", union)
    print("Intersection of sets:", intersection)
    print("Difference of sets (Set 1 - Set 2):", diff1)
    print("Difference of sets (Set 2 - Set 1):", diff2)

# take input from user for set 1
set1 = set(input("Enter elements of set 1 separated by spaces: ").split())

# take input from user for set 2
set2 = set(input("Enter elements of set 2 separated by spaces: ").split())

# perform set operations
set_operations(set1, set2)
