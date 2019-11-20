numbers = []

def print_list(n, b):
	i=0
	while i < n:
		print("At the top i is {}".format(i))
		numbers.append(i)

		i=i+b
		print("Numbers now: ",numbers)
		print("At the bottom {}".format(i))

number = int(input("Enter the length of the list: "))
break_point = int(input("Enter the number you want to incrent the list by: "))
print_list(number, break_point)

print("The number: ")

for num in numbers :
	print(num)

