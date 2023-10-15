from sys import argv

script,file_name = argv

def print_all(file):
    print file.read()

def rewind(file):
    file.seek(0)

def print_a_line(current_line,file):
    print current_line,file.readline(),

current_file = open(file_name)

print "prnt all data"

print_all(current_file)

print "let us rewind"

rewind(current_file)

print "let's print these lines"

current_line = 1

print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
