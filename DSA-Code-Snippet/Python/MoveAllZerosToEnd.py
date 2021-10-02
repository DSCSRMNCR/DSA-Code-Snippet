#CODE

list_input = list(map(int, input().split(" ")))             #Taking input                  
list_filtered=list(filter(lambda a: a != 0, list_input))    #filtering the orignal list to remove zeros
list_filtered.extend([0]*list_input.count(0))               #adding the zero's list to the filtered list
print(*list_filtered)


"""
SAMPLE

INPUT:
0 1 2 30 0 1

#OUTPUT:
1 2 30 1 0 0  
"""


"""
Contributed by:
Name: Sanmay Paniker
Github Username: Soupierbucket 
"""
