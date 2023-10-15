from sys import argv
script,filename = argv

print "we are going to erase the %r" %filename
print "if you dont want that,hit ctr + c"
print "if you want that,hit return"
raw_input('?')

file = open(filename,'w')

print "truncate the file"
file.truncate()

print "now, i am going to ask you for three lines"
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "i am goning to write these lines to file"
file.write(line1+'\n'+line2+'\n'+line3)

print "done"
file.close()