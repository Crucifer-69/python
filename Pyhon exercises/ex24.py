print("let's practice everithing.")
print('you\'d need to know \'bout escapes with \\ that do \n newline anf \t tabs.')

poem = """
\tThe lovely world
with logic so firmly panted 
cannot discern \n the needs of love
 nor comprenhed passion from intituton
 and requires an explanation
 \n\t\twhere there id none.
"""

print("------------------")
print(poem)
print("------------------")

five = 10-2+3-6
print("This should be five:{}".format(five))

def secret_formula(started):
	jelly_beans=started*100
	jars = jelly_beans / 1000
	crates = jars /100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {} ".format(start_point))
print("we'd have {} beans, {} jars and {} crates. ".format(beans , jars, crates))

start_point = start_point/10

print("we can also do that this way:")
print("we'd have %d beans, %d jars and %d crates. "% secret_formula(start_point))