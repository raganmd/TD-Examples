# our simple list
simple_list	= [ 'apple', 'kiwi', 'orange', 'grape', 'pineapple' ]

# sometimes we want to use the contents of a list
# but we also need to know the position of the item
# in the list. For that we can use the enumerate method
# that's built into python.

# let's see it in action to better understand
# what we're getting when we use enumerate

print( "Here's our enumerated list" )
for item in enumerate( simple_list ):
	print( item )

# alright, that's great, we can see here that we
# get a tuple of our list position, and our list item.
# that's great, but how can we use that?

print( '\n' )
print( "Here's our enumerated list broken up a bit" )
for item in enumerate( simple_list ):
	print( item[ 0 ], item[ 1 ] )

# let's imagine that we want to fill in something
# like a sentance with the information from
# our list.

message = "Item list position {}, actual item {}"

print( '\n' )
print( "Here's our enumerated list used with format" )
for item in enumerate( simple_list ):
	print( message.format( item[ 0 ], item[ 1 ] ) )