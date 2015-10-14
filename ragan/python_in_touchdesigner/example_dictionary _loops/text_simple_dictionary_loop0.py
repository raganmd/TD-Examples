# define our variables
# using modues means that we can use our dot notation to
# access an object inside of our text DAT
inventory = mod( 'text_test_dictionary' ).inventory

# list of dictionary keys and their position
dictionary_keys = list( enumerate( inventory ) )

# let's get a feeling for how this works before we
# write a sentance
for item in dictionary_keys:
	print( item[ 0 ] , item[ 1 ] )

# loop through list and print the key and its
# list position
for item in dictionary_keys:
	print( "The key %r is in the %r position of the list" % ( item[ 1 ] , item[ 0 ] ) )