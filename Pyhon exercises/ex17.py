#you need two text documents created before running this program

from sys import argv
from os.path import exists 

script, from_file, to_file = argv

print("Copying the %s to %s "% (from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long "% len(indata))

print("Does the output file exists? %r"% exists(to_file))
print("Ready, hit enter to continue, CTRL-c to exit")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()