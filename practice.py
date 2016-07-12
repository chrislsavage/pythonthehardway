





##########################   DICTIONAIRES (AKA OBJECTS)   ########################

# create a mapping of state to abbreviation
# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }

# # create a basic set of states and some cities in them
# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }

# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'

# # print out some cities
# # print '-' * 10
# # print "NY State has: ", cities['NY']
# # print "OR State has: ", cities['OR']

# # print some states
# # print '-' * 10
# # print "Michigan's abbreviation is: ", states['Michigan']
# # print "Florida's abbreviation is: ", states['Florida']

# # do it by using the state then cities dict
# # print '-' * 10
# # print "Michigan has: ", cities[states['Michigan']]
# # print "Florida has: ", cities[states['Florida']]

# # print every state abbreviation
# print '-' * 10
# for state, abbrev in states.items():

#     print "%s is abbreviated %s" % (state, abbrev)

# # print every city in state
# print '-' * 10
# for abbrev, city in cities.items():
#     print "%s has the city %s" % (abbrev, city)

# # now do both at the same time
# print '-' * 10
# for state, abbrev in states.items():
#     print "%s state is abbreviated %s and has city %s" % (
#         state, abbrev, cities[abbrev])

# print '-' * 10
# # safely get a abbreviation by state that might not be there
# state = states.get('Texas')

# if not state:
#     print "Sorry, no Texas."

# # get a city with a default value
# city = cities.get('TX', 'Does Not Exist')
# print "The city for the state 'TX' is: %s" % city



# >>> del stuff['city']
# >>> del stuff[1]
# >>> del stuff[2]
# >>> stuff
# {'name': 'Zed', 'age': 39, 'height': 74}


##########################   splitting and such with arrays   ########################

# ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print "Wait there are not 10 things in that list. Let's fix that."

# stuff = ten_things.split(' ')
# more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print "Adding: ", next_one
#     stuff.append(next_one)
#     print "There are %d items now." % len(stuff)

# print "There we go: ", stuff

# print "Let's do some things with stuff."

# print stuff[1]
# print stuff[-1] # whoa! fancy
# print stuff.pop()
# print ' '.join(stuff) # what? cool!
# print '#'.join(stuff[3:5]) # This is a slice 

##########################   SYMBOL REVIEW  ########################

# KEYWORD	DESCRIPTION	EXAMPLE
# and	Logical and.	True and False == False
# as	Part of the with-as statement.	with X as Y: pass
# assert	Assert (ensure) that something is true.	assert False, "Error!"
# break	Stop this loop right now.	while True: break
# class	Define a class.	class Person(object)
# continue	Don't process more of the loop, do it again.	while True: continue
# def	Define a function.	def X(): pass
# del	Delete from dictionary.	del X[Y]
# elif	Else if condition.	if: X; elif: Y; else: J
# else	Else condition.	if: X; elif: Y; else: J
# except	If an exception happens, do this.	except ValueError, e: print e
# exec	Run a string as Python.	exec 'print "hello"'
# finally	Exceptions or not, finally do this no matter what.	finally: pass
# for	Loop over a collection of things.	for X in Y: pass
# from	Importing specific parts of a module.	from x import Y
# global	Declare that you want a global variable.	global X
# if	If condition.	if: X; elif: Y; else: J
# import	Import a module into this one to use.	import os
# in	Part of for-loops. Also a test of X in Y.	for X in Y: pass also 1 in [1] == True
# is	Like == to test equality.	1 is 1 == True
# lambda	Create a short anonymous function.	s = lambda y: y ** y; s(3)
# not	Logical not.	not True == False
# or	Logical or.	True or False == True
# pass	This block is empty.	def empty(): pass
# print	Print this string.	print 'this string'
# raise	Raise an exception when things go wrong.	raise ValueError("No")
# return	Exit the function with a return value.	def X(): return Y
# try	Try this block, and if exception, go to except.	try: pass
# while	While loop.	while X: pass
# with	With an expression as a variable do.	with X as Y: pass
# yield	Pause here and return to caller.	def X(): yield Y; X().next()
# Data Types
# For data types, write out what makes up each one. For example, with strings write out how you create a string. For numbers write out a few numbers.

# TYPE	DESCRIPTION	EXAMPLE
# True	True boolean value.	True or False == True
# False	False boolean value.	False and True == False
# None	Represents "nothing" or "no value".	x = None
# strings	Stores textual information.	x = "hello"
# numbers	Stores integers.	i = 100
# floats	Stores decimals.	i = 10.389
# lists	Stores a list of things.	j = [1,2,3,4]
# dicts	Stores a key=value mapping of things.	e = {'x': 1, 'y': 2}
# String Escape Sequences
# For string escape sequences, use them in strings to make sure they do what you think they do.

# ESCAPE	DESCRIPTION
# \\	Backslash
# \'	Single-quote
# \"	Double-quote
# \a	Bell
# \b	Backspace
# \f	Formfeed
# \n	Newline
# \r	Carriage
# \t	Tab
# \v	Vertical tab
# String Formats
# Same thing for string formats: use them in some strings to know what they do.

# ESCAPE	DESCRIPTION	EXAMPLE
# %d	Decimal integers (not floating point).	"%d" % 45 == '45'
# %i	Same as %d.	"%i" % 45 == '45'
# %o	Octal number.	"%o" % 1000 == '1750'
# %u	Unsigned decimal.	"%u" % -1000 == '-1000'
# %x	Hexadecimal lowercase.	"%x" % 1000 == '3e8'
# %X	Hexadecimal uppercase.	"%X" % 1000 == '3E8'
# %e	Exponential notation, lowercase 'e'.	"%e" % 1000 == '1.000000e+03'
# %E	Exponential notation, uppercase 'E'.	"%E" % 1000 == '1.000000E+03'
# %f	Floating point real number.	"%f" % 10.34 == '10.340000'
# %F	Same as %f.	"%F" % 10.34 == '10.340000'
# %g	Either %f or %e, whichever is shorter.	"%g" % 10.34 == '10.34'
# %G	Same as %g but uppercase.	"%G" % 10.34 == '10.34'
# %c	Character format.	"%c" % 34 == '"'
# %r	Repr format (debugging format).	"%r" % int == "<type 'int'>"
# %s	String format.	"%s there" % 'hi' == 'hi there'
# %%	A percent sign.	"%g%%" % 10.34 == '10.34%'
# Operators
# Some of these may be unfamiliar to you, but look them up anyway. Find out what they do, and if you still can't figure it out, save it for later.

# OPERATOR	DESCRIPTION	EXAMPLE
# +	Addition	2 + 4 == 6
# -	Subtraction	2 - 4 == -2
# *	Multiplication	2 * 4 == 8
# **	Power of	2 ** 4 == 16
# /	Division	2 / 4.0 == 0.5
# //	Floor division	2 // 4.0 == 0.0
# %	String interpolate or modulus	2 % 4 == 2
# <	Less than	4 < 4 == False
# >	Greater than	4 > 4 == False
# <=	Less than equal	4 <= 4 == True
# >=	Greater than equal	4 >= 4 == True
# ==	Equal	4 == 5 == False
# !=	Not equal	4 != 5 == True
# <>	Not equal	4 <> 5 == True
# ( )	Parenthesis	len('hi') == 2
# [ ]	List brackets	[1,3,4]
# { }	Dict curly braces	{'x': 5, 'y': 10}
# @	At (decorators)	@classmethod
# ,	Comma	range(0, 10)
# :	Colon	def X():
# .	Dot	self.x = 10
# =	Assign equal	x = 10
# ;	semi-colon	print "hi"; print "there"
# +=	Add and assign	x = 1; x += 2
# -=	Subtract and assign	x = 1; x -= 2
# *=	Multiply and assign	x = 1; x *= 2
# /=	Divide and assign	x = 1; x /= 2
# //=	Floor divide and assign	x = 1; x //= 2
# %=	Modulus assign	x = 1; x %= 2
# **=	Power assign	x = 1; x **= 2

###########  EXAMPLE PROGRAM  #################

# from sys import exit

# def gold_room():
#     print "This room is full of gold.  How much do you take?"

#     choice = raw_input("> ")
#     if "0" in choice or "1" in choice:
#         how_much = int(choice)
#     else:
#         dead("Man, learn to type a number.")

#     if how_much < 50:
#         print "Nice, you're not greedy, you win!"
#         exit(0)
#     else:
#         dead("You greedy bastard!")


# def bear_room():
#     print "There is a bear here."
#     print "The bear has a bunch of honey."
#     print "The fat bear is in front of another door."
#     print "How are you going to move the bear?"
#     bear_moved = False

#     while True:
#         choice = raw_input("> ")

#         if choice == "take honey":
#             dead("The bear looks at you then slaps your face off.")
#         elif choice == "taunt bear" and not bear_moved:
#             print "The bear has moved from the door. You can go through it now."
#             bear_moved = True
#         elif choice == "taunt bear" and bear_moved:
#             dead("The bear gets pissed off and chews your leg off.")
#         elif choice == "open door" and bear_moved:
#             gold_room()
#         else:
#             print "I got no idea what that means."


# def cthulhu_room():
#     print "Here you see the great evil Cthulhu."
#     print "He, it, whatever stares at you and you go insane."
#     print "Do you flee for your life or eat your head?"

#     choice = raw_input("> ")

#     if "flee" in choice:
#         start()
#     elif "head" in choice:
#         dead("Well that was tasty!")
#     else:
#         cthulhu_room()


# def dead(why):
#     print why, "Good job!"
#     exit(0)

# def start():
#     print "You are in a dark room."
#     print "There is a door to your right and left."
#     print "Which one do you take?"

#     choice = raw_input("> ")

#     if choice == "left":
#         bear_room()
#     elif choice == "right":
#         cthulhu_room()
#     else:
#         dead("You stumble around the room until you starve.")


# start()


####################  WHILE LOOPS ################

# i = 0
# numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i = i + 1
#     print "Nusmbers now: ", numbers
#     print "At the bottom i is %d" % i


# print "The numbers: "

# for num in numbers:
#     print num

####################  FOR LOOPS ################

# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# # this first kind of for-loop goes through a list
# for number in the_count:
#     print "This is count %d" % number

# # same as above
# for fruit in fruits:
#     print "A fruit of type: %s" % fruit

# # also we can go through mixed lists too
# # notice we have to use %r since we don't know what's in it
# for i in change:
#     print "I got %r" % i

# # we can also build lists, first start with an empty one
# elements = []

# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print "Adding %d to the list." % i
#     # append is a function that lists understand
#     elements.append(i)

# # now we can print them out too
# for i in elements:
#     print "Element was: %d" % i

####################   INPUT WITH CONTROL FLOW ##########################

# print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

# door = raw_input("> ")

# if door == "1":
#     print "There's a giant bear here eating a cheese cake.  What do you do?"
#     print "1. Take the cake."
#     print "2. Scream at the bear."

#     bear = raw_input("> ")

#     if bear == "1":
#         print "The bear eats your face off.  Good job!"
#     elif bear == "2":
#         print "The bear eats your legs off.  Good job!"
#     else:
#         print "Well, doing %s is probably better.  Bear runs away." % bear

# elif door == "2":
#     print "You stare into the endless abyss at Cthulhu's retina."
#     print "1. Blueberries."
#     print "2. Yellow jacket clothespins."
#     print "3. Understanding revolvers yelling melodies."

#     insanity = raw_input("> ")

#     if insanity == "1" or insanity == "2":
#         print "Your body survives powered by a mind of jello.  Good job!"
#     else:
#         print "The insanity rots your eyes into a pool of muck.  Good job!"

# else:
#     print "You stumble around and fall on a knife and die.  Good job!"


################# elif ########################

# people = 30
# cars = 40
# trucks = 15


# if cars > people:
#     print "We should take the cars."
# elif cars < people:
#     print "We should not take the cars."
# else:
#     print "We can't decide."

# if trucks > cars:
#     print "That's too many trucks."
# elif trucks < cars:
#     print "Maybe we could take the trucks."
# else:
#     print "We still can't decide."

# if people > trucks:
#     print "Alright, let's just take the trucks."
# else:
#     print "Fine, let's stay home then."

################### IF STATEMENTS ###################

# people = 20
# cats = 30
# dogs = 15


# if people < cats:
#     print "Too many cats! The world is doomed!"

# if people > cats:
#     print "Not many cats! The world is saved!"

# if people < dogs:
#     print "The world is drooled on!"

# if people > dogs:
#     print "The world is dry!"


# dogs += 5

# if people >= dogs:
#     print "People are greater than or equal to dogs."

# if people <= dogs:
#     print "People are less than or equal to dogs."


# if people == dogs:
#     print "People are dogs."



#################  TRUTH TABLES  ####################

# True and True  #true
# False and True #false
# 1 == 1 and 2 == 1 #false
# "test" == "test" #true
# 1 == 1 or 2 != 1 #True
# True and 1 == 1 #true
# False and 0 != 0 #False
# True or 1 == 1#true
# "test" == "testing" #false
# 1 != 0 and 2 == 1 #false
# "test" != "testing" #true
# "test" == 1 #false
# not (True and False) #true
# not (1 == 1 and 0 != 1) #false
# not (10 == 1 or 1000 == 1000) #False
# not (1 != 10 or 3 == 4) #flase
# not ("testing" == "testing" and "Zed" == "Cool Guy") #true
# 1 == 1 and (not ("testing" == 1 or 1 == 0)) #true
# "chunky" == "bacon" and (not (3 == 4 or 3 == 3))  #flase
# 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) #flase

# NOT	TRUE?
# not False	True
# not True	False
# OR	TRUE?
# True or False	True
# True or True	True
# False or True	True
# False or False	False
# AND	TRUE?
# True and False	False
# True and True	True
# False and True	False
# False and False	False
# NOT OR	TRUE?
# not (True or False)	False
# not (True or True)	False
# not (False or True)	False
# not (False or False)	True
# NOT AND	TRUE?
# not (True and False)	True
# not (True and True)	   False
# not (False and True)	True
# not (False and False)	True
# !=	TRUE?
# 1 != 0	True
# 1 != 1	False
# 0 != 1	True
# 0 != 0	False
# ==	TRUE?
# 1 == 0	False
# 1 == 1	True
# 0 == 1	False
# 0 == 0	True
###################  MATH FUNCTIONS ##########################

# def add(a, b):
#     print "ADDING %d + %d" % (a, b)
#     return a + b

# def subtract(a, b):
#     print "SUBTRACTING %d - %d" % (a, b)
#     return a - b

# def multiply(a, b):
#     print "MULTIPLYING %d * %d" % (a, b)
#     return a * b

# def divide(a, b):
#     print "DIVIDING %d / %d" % (a, b)
#     return a / b


# print "Let's do some math with just functions!"

# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)

# print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# # A puzzle for the extra credit, type it in anyway.
# print "Here is a puzzle."

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print "That becomes: ", what, "Can you do it by hand?"

### Reading from a file  ##  Use myfile.txt as file to read from ##################

# from sys import argv

# script, input_file = argv

# def print_all(f):
#     print f.read()

# def rewind(f):
#     f.seek(0)

# def print_a_line(line_count, f):
#     print line_count, f.readline()

# current_file = open(input_file)

# print "First let's print the whole file:\n"

# print_all(current_file)

# print "Now let's rewind, kind of like a tape."

# rewind(current_file)

# print "Let's print three lines:"

# current_line = 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)


#####################  FUNCTIONS  ##########################

# def print_two(*args):
#     arg1, arg2 = args
#     print "arg1: %r, arg2: %r" % (arg1, arg2)

# def print_two_again(arg1, arg2):
#     print "arg1: %r, arg2: %r" % (arg1, arg2)

# # this just takes one argument
# def print_one(arg1):
#     print "arg1: %r" % arg1

# # this one takes no arguments
# def print_none():
#     print "I got nothin'."


# print_two("Zed","Shaw")
# print_two_again("Zed","Shaw")
# print_one("First!")
# print_none()


#######################   ARGV  ##########################

# from sys import argv
# #passing argv
# script, first, second, third = argv
# print "The script is called:", script
# print "first var is:", first
# print "second var is:", second
# print "third var is:", third

############# STRING INTERPOLATION #########################
# x = "There are %d types of people." % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." % (binary, do_not)

# print x
# print y

# print "I said: %r." % x  # %r is more of a literal interpretation
# print "I also said: '%s'." % y

# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation % hilarious

# w = "This is the left side of..."
# e = "a string with a right side."

# print w + e


# print "Mary had a little lamb."
# print "It's fleece was white as %s." % 'snow'  /string interpolation
# print "And everywhere that Mary went."
# print '.' * 10

# end1 = "Ch"
# end2 = "h"
# end3 = 'e'
# end4 = "burger"

# print end1 + end2
# print end3 + end4


# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74 # inches
# my_weight = 180 # lbs
# my_eyes = 'Blue' 
# my_teeth = 'White'
# my_hair = 'Brown'

# print "Let's talk about %s." % my_name  # %s is for string
# print "He's %d inches tall." % my_height # %d is for digit
# print "He's %d pounds heavy." % my_weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# print "His teeth are usually %s depending on the coffee." % my_teeth

# # this line is tricky, try to get it exactly right
# print "If I add %d, %d, and %d I get %d." % (
#     my_age, my_height, my_weight, my_age + my_height + my_weight)