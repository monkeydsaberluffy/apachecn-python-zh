from sys import argv

script,user_name = argv
promot = '>>>'

print "HI %s,i am %s,do you like football?" %(user_name,script)
like = raw_input(promot)
print "HI %s,How old are you?" %user_name
age = raw_input(promot)

print """
your name is %s,your age is %s
""" %(user_name,age)

