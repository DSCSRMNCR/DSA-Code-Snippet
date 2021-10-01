#CODE

list1 = list(map(int, input().split(" ")))      #Taking input
list2 = [0]*list1.count(0)                      #To make a list of zeros
list3=list(filter(lambda a: a != 0, list1))     #filtering the orignal list to remove zeros
list3.extend(list2)                             #adding the zero's list to the filtered list
print(*list3)


"""
#SAMPLE

0 1 2 30 0 1  #input

1 2 30 1 0 0  #output

"""


"""
Contributed by:
Sanmay Paniker
Github Username: Soupierbucket 
"""

