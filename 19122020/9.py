from operator import add
in_list1 = [11, 21, 34, 12, 31]
in_list2 = [23, 25, 54, 24, 20, 27]
print ("\nTest Input: **********\n Input List (1) : " + str(in_list1))
print (" Input List (2) : " + str(in_list2))
final_list = list(map(add, in_list1, in_list2))
print ("\nTest Result: **********\n Resultant list is : " + str(final_list))
