#these are 3 lists
the_count = [1,2,3,4,5]
fruits = ['apples','orangs','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

print("\n")

#this loop only traves through the first list
for number in the_count:
	print("this is count {}".format(number))
print("\n")

#this loop only traves through the second list
for fruit in fruits:
	print("A fruit of type: {}".format(fruit))
print("\n")

#this loop only traves through the third mixed list
for i in change:
	print("I got {}".format(i))
print("\n")

elements = []

#here range function is used which takes 6 elements. so in acctuality it goes from 0 to 5 ie. 6 elements
for i in range(0,6):
	print("Adding {} to the list.".format(i))
	elements.append(i)
print("\n")

#this loop only traves through element list
for i in elements:
	print("Element was: {}".format(i))
print("\n")
