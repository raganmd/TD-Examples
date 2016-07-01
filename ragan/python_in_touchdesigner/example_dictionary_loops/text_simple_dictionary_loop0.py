# define our variables
# using modules means that we can use our dot notation to
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
sentence = "The key {key} is in the {position} position of the list"

for item in dictionary_keys:
	print( sentence.format( key = item[ 1 ] , position = item[ 0 ] ) )