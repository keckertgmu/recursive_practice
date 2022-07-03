# Simple recursive string reversal
# Given a string, right a recursive function to reverse the string. 
# Example: "Hello world" -> "dlrow olleH"

def reverse_string(string, index):
    # stop condition is if we reach end of string. 
    if index+1 >= len(string):
        return string[index]
    
    # If we aren't at end of string, we must continue until we are. 
    return reverse_string(string, index+1) + string[index]
    
# Here is another, less elegant iterative solution. 
# Without assigning rstring = string[0] at the beginning, 
# we would drop string[0] from the reversal process and lose it. 
# The reason is because nothing in the function as written gets us
# to index 0 in the iterative part of the function
# compare to the better version above, and you'll see I concatonate
# string[index] thus ensuring I reach index = 0 at some point, 
# whereas, below, I do no such thing. 
def reverse_string_OLD(string, index):
    rstring = string[0]
    if index+1 >= len(string):
        return string[index] 
    rstring = reverse_string(string, index+1) + rstring # iterative part
    return rstring
    

# Simple recursive adder for an index and an array of numbers. The goal is to add 
# each number up to the number at the relevant index. 
# assume the index is less than the array length (i.e., don't sanitize inputs).
# 
# It is helpful to think of the below as fundamentally saying two things. 
# First, the statement "array[i] + recursive_adder(array, i-1)" says that
# we want to add the highest index to the next highest index. 
# the if-return statement says that if we are at the lowest index (i=0), we 
# should simlpy return array[0], and array[0] becomes the value we substitute into 
# "recursive_adder(array, i-1)" for the final recursion. 
#
# To put this another way, the "base case" (or termination case) is just a case 
# that tells us what to plug into the recursive function call during the last recursion. 
def recursive_adder(array, i): 
    if i == 0:
        return array[i]
    
    return array[i] + recursive_adder(array, i-1)
    

# Given an array, recursively find the largest function in the array
# We can implement this without the max function if we want. Such an implementation 
# would require more sophisticated looping in find_largest(). As a a result, I think 
# the below implementation is clearer.  
def max(x, y):
	if x >= y:
		return x
	else: return y

def find_largest(array, i):
	if i+1 >= len(array):
		return array[i]
	
	return max(array[i], find_largest(array, i+1))
	
	
# Search an array to see if it contains a specific element
# assume integer array.
# This is identical to the string search, except we now have two base cases (i.e. termination conditions)
# The first is for when we find what we're looking for and the second is for if we don't find what we're looking for. 
def id_element(array, element, i):
	if array[i] == element: return True
	elif i+1 >= len(array): return False
	return id_element(array, element, i+1)
	

	
    