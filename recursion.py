# These are some of my solutions to the recursive programming challenge found here: 
# https://betterprogramming.pub/practicing-recursion-with-7-algorithm-challenges-7ffdd634557
# These are pretty simple challenges. I recommend doing them without looking at the solutions posted below or the solutions posted on the page. 
# I chose python for implementation, but these code snippets are easy to implement in C and other languages with relatively minor changes. 

# Because I did this for fun/learning, some of my comments may be a bit extensive

# Simple recursive string reversal
# Given a string, right a recursive function to reverse the string. 
# Example: "Hello world" -> "dlrow olleH"
def reverse_string(string, index):
    if index+1 >= len(string):
        return string[index]
    return reverse_string(string, index+1) + string[index]
    
# Here is another, less elegant iterative solution.
# Without rstring = string[0], this function would not include the 0th element. I.e., "hello world" would become "dlrow olle" and would miss the "h".
# The "h" is dropped because the line "rstrin = reverse_string() + rstring" does not include a case for when the index is 0. Thus, if rstring were initialized 
# to an empty string, "rstring=''", the function would not capture the zeroeth element of the array. 
def reverse_string_OLD(string, index):
    rstring = string[0] # it may be easier to understand the issues with this function by moving this line to be directly above the iterative part of the function
    if index+1 >= len(string):
        return string[index] 
    rstring = reverse_string(string, index+1) + rstring # iterative part
    return rstring
    

# Simple recursive adder for an index and an array of numbers. 
# The goal is to add each number up to the number at the relevant index. Assume the index is less than the array length.
# If you want to add the entire array, you can simply pass len(array)-1 as the value of i.
# 
# It is helpful to think of the below as fundamentally saying two things. 
# First, the statement "array[i] + recursive_adder(array, i-1)" says that we want to add the highest index to the next highest index. 
# the if-return statement says that if we are at the lowest index (i=0), we should simlpy return array[0], and array[0] becomes the value we substitute into "recursive_adder(array, i-1)" for the final recursion. 
#
# To put this another way, the "base case" (or termination case) is just a case that tells us what to plug into the recursive function call during the last recursion. 
def recursive_adder(array, i): 
    if i == 0: return array[i]
    return array[i] + recursive_adder(array, i-1)
    

# Given an array, recursively find the largest value in the array
# We can implement this without the max function if we want. Such an implementation would clutter find_largest(). 
# As a a result, I think the below implementation is clearer.  
#
# Note that the function should work fine even if x >= y is substituted with x > y. The case where x = y is dealt with correctly either way.
def max(x, y):
	if x >= y: return x
	else: return y

def find_largest(array, i):
	if i+1 >= len(array): return array[i]
	return max(array[i], find_largest(array, i+1))
	
	
# Search an array to see if it contains a specific element. Assumes an integer array.
# This is identical to the string search, except we now have two base cases (i.e. termination conditions)
# The first is for when we find what we're looking for and the second is for if we don't find what we're looking for. 
#
# If we wanted the index of the first identical element, we could return a tuple or array instead (index, True/False), or just return the index value.
# For example, "return True" could become "return i", such that we return the index when we find the element, and otherwise return False. 
def id_element(array, element, i):
	if array[i] == element: return True
	elif i+1 >= len(array): return False
	return id_element(array, element, i+1)
	

# Palindrome detector
# Since strings are arrays, you can do this with any array of even or odd size 
# Note, for odd-size arrays we can ignore the middle element, hence the integer division
# This is another example of two base cases. The first if statement accounts for if we 
# recursively reach the center of the array. If we do, and the array is palindrome, we can return True and be done. 
# On the other hand, if at any time in the recursion we reach a state where the array isn't a palindrome, we terminate immediately by returning False.
def is_palindrome(array, i):
	if i >= len(array)//2:
		if array[i] == array[len(array)-(1+i)]: 
			return True
	if array[i] != array[len(array)-(1+i)]: 
		return False
	return is_palindrome(array, i+1)	
    
