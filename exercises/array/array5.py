# Importing the library
from array import *
import psutil
array_num = array('i', [1, 3, 5, 7, 9])

# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(4))


# buffer in python is a temporary memory storage
# buffer_info() returns a tuple (address, length) giving the current memory address and the length in elements of the buffer used to hold array’s contents
print('The buffer info is: ', array_num.buffer_info())

# itemsize returns the length of one array item in bytes
print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))