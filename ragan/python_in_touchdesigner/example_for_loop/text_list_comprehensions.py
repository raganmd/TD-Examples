# List comprehensions are a powerful means of constructing lists
# quickly. These might feel familar from math courses you've taken
# or they may feel totally unfamiliar. In either case, they're 
# a wonderful tool to be able to use, and can make fast work
# for building or changing lists.

# Let's make a fast list so we can see the initial mechaics of list 
# comprehensions
my_list = [ 5, 10 , 4 , 6 , 20, 13, 7, 31 ]

# First let's look at how we can print the contents of a list
# from inside the list
print( "Let's start by just printing out the contents of the list" )
print( "- - - - - - - - - -" )
new_list1 = [ print( item ) for item in my_list ]

# We can also print out the index of our item as we go
print( "\n" )
print( "Now lets look at how we can see the index of the items in our list" )
print( "- - - - - - - - - -" )
new_list2 = [ print( my_list.index( item ) ) for item in my_list ]

# With a little bit of careful writing we can do both at the same time
print( "\n" )
print( "Now let's print both together" )
print( "- - - - - - - - - -" )
new_list3 = [ 
				print( 'the index of this item is: ' + str( my_list.index( item ) ) , 
						'the acutal list item is: ' + str( item ) ) for item in my_list 
			]

# We can also construct a list from scratch, in this case we'll 
# make a list of each number in the list * 2 for the range of 10
# If we write that out by hand we can see what we'll expect from 
# our comprehension:
# 0 * 2 = 0
# 1 * 2 = 2
# 2 * 2 = 4
# 3 * 2 = 6
# 4 * 2 = 8
# 5 * 2 = 10
# 6 * 2 = 12
# 7 * 2 = 14
# 8 * 2 = 16
# 9 * 2 = 18

# now that we know what we're expecting to see, let's see if it
# works the way we want
print( "\n" )
print( """Let's see how we can construct a list 
from scratch with a list comprehension""" )
print( "- - - - - - - - - -" )
list_from_scratch = [ item * 2 for item in range( 10 )  ]
print( list_from_scratch )

# We can also construct a new list from a previous one. In this case
# Let's see if we can construct a list that's only the even nubmers 
# from our first list.
print( "\n" )
print( "Let's see how we can construct a new list from an old one" )
print( "In this case, let's see if we can build one that's only even numbers" )
print( "- - - - - - - - - -" )
evens_only = [ item for item in my_list if item % 2 == 0 ]
print( evens_only )