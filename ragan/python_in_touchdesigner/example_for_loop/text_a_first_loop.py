# lets first make a simple list so we have something to work with
simple_list	= [ 'apple', 'kiwi', 'orange', 'grape', 'pineapple' ]

# the anatomy of our for loop can be a little confusing at first
# but once we get the hang of it, they're very powerful.

# okay, so what does that syntax look like

# for stand_in_variable in a_list_or_range:
#	do each of these operations

# let's first imagine that we want to print out each
# of the items in our list

for item in simple_list:
	print( item )

# here we can see that 'item' is our stand in
# variable. For reach positial item in our
# simple_list, we print out that item.