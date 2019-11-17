def add (a, b):
	print("Adding two numbers %d and %d"% (a, b))
	return a+b

def subtract(a, b):
	print("Subtracting two numbers %d and %d"% (a, b))
	return a-b

def multply(a, b):
	print("multipying two numbers %d and %d"% (a, b))
	return a*b

def divide(a, b):
	print("Dividing two numbers %d and %d"% (a, b))
	return a/b

print("Lte's do some math with same functions: ")

age = add(30,5)
height = subtract(78,4)
weight = multply(90, 2)
iq = divide(100, 2)

print("Age = %d\nHeight = %d\nWeight = %d\nIQ = %d"% (age, height, weight, iq))

print("\nHere is a puzzle\n")
what = add(age, subtract(height, multply(weight, divide(iq, 2))))
print("\nThat becomes ", what)