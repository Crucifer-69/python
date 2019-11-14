from sys import argv

script, filename = argv

print("We're going to erase %r."% filename)
print("If you do not want that, hit CTRL-C")
print("If you do want it hit return ")
input("? ")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file.")
target.truncate()

print("Now input 3 lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Now I'm  going to write these lines to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it")
target.close()
