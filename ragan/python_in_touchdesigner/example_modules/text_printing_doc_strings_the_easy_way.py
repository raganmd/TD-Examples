# first let's clear the text port to make sure we're starting fresh
clear()

# rather than wasting our time writing all the code in the other example, 
# instead let's write a for loop to automate that process.
# We'll start by first making a list of all of the methods we want to print 
# doc strings for
methods							= [
								"multi_by_two",
								"logic_test",
								"logic_test_two"
									]

# next we'll make a smiple placeholder expression that we can 
# pass each method into so we can print it out easily
doc_string_temp					= "mod( 'text_simple_reutrn' ).{target_function}.__doc__"

# finally we write a little for loop to go through all items in our list
# and pretty print their doc strings to the text port
for method in methods:
	print( "The Doc Strings for {} are:".format( method ) )
	temp_doc 					= doc_string_temp.format( target_function = method )
	print( eval( temp_doc ) )
	print( "= "  * 10 )
