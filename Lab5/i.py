def is_palindrome(lst):
    # get the length of the list
    n = len(lst)
    # loop through the first half of the list and check if the corresponding element in the second half is the same
    for i in range(n//2):
        if lst[i] != lst[n-i-1]:
            return False
    return True

# take input from user for the list
lst = input("Enter elements of the list separated by spaces: ").split()

# check if the list is palindrome
if is_palindrome(lst):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
