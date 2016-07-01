# define our variables
# using modules means that we can use our dot notation to
# access an object inside of our text DAT
inventory = mod( 'text_test_dictionary' ).inventory

# loop through the dictionary and print out contents
for dictionary_key , dictionary_value in inventory.items():
	# print out the first key depth in the dictionary	
	print( "- " * 10 )
	print( "this dictionary key is: " , dictionary_key )
	print( "in this dictionary we have:" )
	
	# loop through second dictionary layer
	for inventory_key , inventory_quantity in dictionary_value.items():
		# print out the key and value pairs from the second level
		print( '\t' , inventory_key , inventory_quantity )