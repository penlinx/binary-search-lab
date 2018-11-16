#================================================================================================= 
# Implementation of Binary Search Algorithm
#=================================================================================================

class binarySearch(list):
    '''
    Implementation of the Binary Search algorithm. It has been extended with a search function that returns the index of the number searched for in the array and the number of iterations needed to find it.
    '''
    def __init__(self,length, step):
	self.length = length
	self.step = step
	for element in range(1, self.length + 1):
	    self.append(element * self.step)
    

    def search(self, value): 
	# Initialize leftmost and rightmost values
	left = 0
	right = len(self) - 1
	key = 0
	found = False

	# Initialize counter
	counter = 0

	# check if value is the first or last element
        if value == self[left]:
            key = left
            found = True
        elif value == self[right]:
            key = right
            found = True

	#Terminate if value not in list
	if value not in self: 
	    key = -1 
	    found = True	
 
	# Iterative binary search
        while (left <= right) and not found: 
	    middle = left + (right - left) / 2   # Get the middle of the list
            if self[middle] == value:    # Check if the middle is our key 
                key = middle
		found = True
		print middle, key
	    else:  
                counter += 1 
                if (self[middle] < value): # Our key might be in the right half 
                    left = middle + 1 
		    print middle, key
                else:			 # Our key might be in the left half  
                    right = middle - 1
		    print middle, key

	return {'count': counter, 'index': key}

class Array:
    '''
    toTwenty() returns [1, 2, 3 . . . 20]

    toForty() returns [2, 4, 6 . . . 40]

    toOneThousand() returns [10, 20, 30 . . . 1000]
    '''
    def __init__(self):
	pass	
    
    def toTwenty(self):
 	return binarySearch(20, 1)

    def toForty(self):
	return binarySearch(20, 2)

    def toOneThousand(self):
	return binarySearch(100, 10)

