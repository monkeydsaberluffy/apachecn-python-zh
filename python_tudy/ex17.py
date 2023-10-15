from sys import argv
from os.path import exists
script,from_file,to_file = argv

in_file = open(from_file)

file_date = in_file.read()

out_file = open(to_file,'w')
out_file.write(file_date)

in_file.close()
out_file.close()
