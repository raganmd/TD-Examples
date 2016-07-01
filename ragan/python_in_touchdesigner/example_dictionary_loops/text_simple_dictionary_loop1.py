# define our variables
# using modules means that we can use our dot notation to
# access an object inside of our text DAT
inventory = mod( 'text_test_dictionary' ).inventory

for dictionary_key , dictionary_value in inventory.items():
	print( "this dictionary key is: " , dictionary_key )