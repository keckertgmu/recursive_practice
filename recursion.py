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
    
	
# Fibonacci Sequence
# Calculate the nth element of the fibonacci sequence. 
# 0, 1, 1, 2, 3, 5, 8, 13 etc. Each number is the same as the two before it.
# In this example, I use three base cases to account for the initial 0, 1, and 1. Hence n-3 in the final elif (and the fourth base case)
# Note that the operations in this version of the Fibonacci sequences are all simple (if/else and addition).
# Accordingly, the time complexity of this version should be lower (potentially much lower) than the "canonical" example (shown below). 
def fibonacci(n, i, a, b):
	if n==1: return a
	elif n==2: return b
	elif n==3: return a+b
	elif i==n-3: return (a+b)
	return fibonacci(n, i+1, b, a+b) # this is where the magic happens. The important calculcations are done here in the arguments of the function call (b, a+b)
	
# Here is another version
# This version is more elegant than the above version. It takes a subtractive approach, with the iterative portion iterating backwords from n until it can find something to add.
# This contrasts with the above version, which iterates from 0 to n-3.  
# However, there is a subtle issue with the below implementation: For n=1 the function returns 1. However, the first element of the fibonnaci sequence is 0
# Recall that normally, when discussing a set, we don't refer to the zeroeth element. Typically, an index of 0 corresponds to the first element of a set. 
# However, in this implementation, n refers to the index of the set. Accordingly, for a user interested in the 10th element of the fibonacci sequence, n-1 should be input instead.
def fibonacci2(n):
	if n<2 : return n
	return fibonacci2(n-1) + fibonacci2(n-2)

# This function uses the above fibonacci function and corrects the index issue. 
def fixedonacci(n):
	return fibonacci2(n-1)


# Permutator
# For a given string, print out all permutations of that string (or, if you prefer, for an array, print out each possible arrangement of elements in that array)
# For example, ABC -> ABC, ACB, BAC, BCA, CAB, CBA
# This is an example of array slicing. We want to take parts of the array and recombine them using concatonation
def permutations(array):
	output = []
	if len(array) <= 1: 
		output.append(array)
		return output # or simply return array
	for i,element in enumerate(array):
		for permutation in permutations(array[:i] + array[i+1:]): # this is where the magic happens. 
			output.append(element + permutation) # or output += [element + permutation]
	return output

# Here is a version using a for-loop instead of enumerate, to help make what's going on a touch clearer. 
def perm2(arr):
	output = []
	if len(arr) < 2:
		return arr
	else:
		i = 0
		for element in arr: # This could be a while loop. while i<len(arr), and element becomes arr[i] below. 
			for permutation in perm2(arr[:i] + arr[i+1:]):
				output += [element + permutation]
			i+=1
	return output
	
# The line "for permutation in perm2(arr[:i] + arr[i+1:])" is critical. 
# The argument for perm2() is capturing all of the string characters not corresponding to the current index (i) of the input array. 
# The highest level call of perm2() will execute len(arr) times. The first recursion will execute the for-loop len(array)-1 times, and so forth.
# This continues until we reach the base case and simply return the relevant character of the input string (or array). 
# Also note that "for permutation in perm2(arr[:i] + arr[i+1:])" is using the call stack. The recursive calls to perm2() are evaluated before 
# higher level calls of the function, and the highest level call of the function is evaluated last. This means that the recursive function calls 
# have returned an array with a knowable length before the higher level calls are evaluated. This is how that line knows to loop for a finite number 
# of times. It is roughly equivalent to replacing "for permutation in perm2(arr[:i] + arr[i+1:])" with a while loop that would look something like:
#	while x < len(perm2()):
#		output += []
#		x++
# You can replace the for loops with while loops if you wish. 
# Note, for an input with repeat values ("aabc") these permutation functions do not "clean" the resulting array to remove duplicates that will occur. 
# To remove duplicates is trivial and left as an exercise for the reader. 
