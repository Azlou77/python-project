""" Write a Python program to get the number of occurrences of a specified element in an array.
Sample Output: """
from array import *
array_num = array('i', [1, 3, 5, 7, 9])

print ("Original array: "+str(array_num))
print ("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))