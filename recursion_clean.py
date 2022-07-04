# These are some of my solutions to the recursive programming challenge found here: 
# https://betterprogramming.pub/practicing-recursion-with-7-algorithm-challenges-7ffdd634557

# Recursively reverse string
def reverse_string(string, index):
    if index+1 >= len(string):
        return string[index]
    return reverse_string(string, index+1) + string[index]
    
def reverse_string_OLD(string, index):
    rstring = string[0]
    if index+1 >= len(string):
        return string[index] 
    rstring = reverse_string(string, index+1) + rstring
    return rstring

# Recursively add
def recursive_adder(array, i): 
    if i == 0: return array[i]
    return array[i] + recursive_adder(array, i-1)

# Helper Function
def max(x, y):
	if x >= y: return x
	else: return y

# Find largest element in an array
def find_largest(array, i):
	if i+1 >= len(array): return array[i]
	return max(array[i], find_largest(array, i+1))
	
# Search an array to see if it contains a specific element. Assumes an integer array.
def id_element(array, element, i):
	if array[i] == element: return True
	elif i+1 >= len(array): return False
	return id_element(array, element, i+1)
	
# Palindrome detector
def is_palindrome(array, i):
	if i >= len(array)//2:
		if array[i] == array[len(array)-(1+i)]: 
			return True
	if array[i] != array[len(array)-(1+i)]: 
		return False
	return is_palindrome(array, i+1)	
    
# Fibonacci Sequence
def fibonacci(n, i, a, b):
	if n==1: return a
	elif n==2: return b
	elif n==3: return a+b
	elif i==n-3: return (a+b)
	return fibonacci(n, i+1, b, a+b) 
	
# Here is another version
def fibonacci2(n):
	if n<2 : return n
	return fibonacci2(n-1) + fibonacci2(n-2)

# This function uses the above fibonacci function and corrects the index issue. 
def fixedonacci(n):
	return fibonacci2(n-1)

# Permutator
def permutations(array):
	output = []
	if len(array) <= 1: 
		output.append(array)
		return output
	for i,element in enumerate(array):
		for permutation in permutations(array[:i] + array[i+1:]):
			output.append(element + permutation) 
	return output

# Here is a version using a for-loop instead of enumerate, to help make what's going on a touch clearer. 
def perm2(arr):
	output = []
	if len(arr) < 2:
		return arr
	else:
		i = 0
		for element in arr:
			for permutation in perm2(arr[:i] + arr[i+1:]):
				output += [element + permutation]
			i+=1
	return output
