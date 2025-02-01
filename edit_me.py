def monotonic(lst):
    #   """Return True if lst is monotonic; return False, otherwise."""
    #
    # YOUR IMPLEMENTATION GOES HERE
    #

    
    # Return true if the list contains one item or is an empty list
    if len(lst) <= 1:
        return True
    # Go through every item in the list, using all() to check the truth value of every item in the range
    ascend = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    descend = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    # If either is true, return true
    # If both are false, return false
    return ascend or descend


    # Check 10 lists to see if they return true/false correctly
    # (THEY DO, WOOHOO)

list1 = [1, 2, 3, 4, 5, 7, 8, 15]
list2 = [8, 5, 3, 2]
list3 = [2, 5, 1, 7, 6]
list4 = [15]
list5 = []
list6 = [7, 3, 1, 0, -4]
list7 = [5, 8, 2, 4, 1, 16, -55]
list8 = [62, 55, 99]
list9 = [44, 47, 72, 85, 146]
list0 = [56, 72]


    # Print that proof!

print(monotonic(list1))
print(monotonic(list2))
print(monotonic(list3))
print(monotonic(list4))
print(monotonic(list5))
print(monotonic(list6))
print(monotonic(list7))
print(monotonic(list8))
print(monotonic(list9))
print(monotonic(list0))