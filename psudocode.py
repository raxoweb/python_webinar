# One Liners,  Super powerful code 


# Palindrome check 

def palindrome():
	word = "wow"
	p = bool(word.find(word[::-1])+1)
	print(p)

	"""
		How the code works
		1. word[::-1] inverts the input.
		2. word.find(char) return either the index of char inside word or -1 if word does not contain that char. 
		Since we use the entire input , we get either  0 or -1.
		3. since bool(0) = False and bool(1) = True we simply add 1 to the result before we convert it to its bool values
	"""
# Sum of even number up to n

def sum_of_even():
	n = 20
	s = sum((range(n+1))[::2])
	print(s)

	"""
		1. With range(n+1) we create a range containing all the numbers from 0 to n.
		2. Using slicing we cut out each second element from the range, this is done by the operator[::2]
		3. The build-in function sum sums up all elements in the range.
	"""

# Read Lines of file into a list

def read_file():
	f = "myfile.txt"
	lines = [line.strip() for line in open(f)]

	"""
		How the code works
		1. The build-in function open(filename) opens the file
		2. Using a list comprehension we remove all leading and trailing white-spaces from each line.
		3. Better use two lines:
			with open("filename.txt") as file:
				lines = [line.strip() for line in f]
		what if file not closed?
	"""

# Factorial

def factorial():
	from functools import reduce
	n = 5 
	factorial = reduce(lambda x, y: x*y, range(1, n+1))

	"""
		How the code work
		1. with the range function we create a range from 1 to n
		2. Then we apply the reduce function on this range, this multiple together all elements in the range: 1*2*3..*n
	"""

# Fibonacci number

def fibonacci():
	fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
	result = fib(10)

	"""
		How the code works
		1. The lambda expression returns 0 if n == 0 and 1 if n == 1
		2. if n > 1 the lambda returns fib(n-1) + fib(n-2) which is a recursive call.

		Note: In terms of execution time, the recursive computation of fibonacci number is rather slow.
	"""

# Get first and last element of list

def first_last():
	l = [1, 2, 3, 4, 5]
	first, *x, last = l

	"""
		How the code works
		1. you can write as many variables as there are elements in the list on the left side.
		2. if you put less variables then there are elements in the list one variable has to marked with the asterisk.
		this means that "all the rest" goes to variable.
		3. At max one variable can have an asterisk. The variable with the asterisk will point to a list with all the values
		which  were not assigned to a variable.
		4. In the code first = 1, x = [2,3,4], last = 5
	"""