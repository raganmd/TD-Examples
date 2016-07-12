def multi_by_two( value ):
	'''Multiplies input value by 2

	A simple example function to see how we can use modules on demand.
	This module takes a single arugment which is multplied by 2 and
	then returned from the function.
	
	Arguments
	---------------	
	value( int / float ) - numeric value to be multiplied by 2

	Returns
	---------------
	new_val( int / float ) - value * 2

	Notes
	---------------
	These are doc strings - they're a feature of the Python language
	and make documenting your code all easier. This format is based largly
	on Google's Python documentation format - though not exactly. It's 
	generally good practice to document your work, leaving notes both for 
	your future self, as well as for other programmers who might be using
	your code in the future.
	'''
	new_val				= value * 2
	
	return new_val

def logic_test( even_or_odd ):
	'''Tests if input value is even or odd

	This is a simple little function to test if an integer is even or odd.
	
	Arguments
	---------------	
	even_or_odd( int ) - an integer to be tested as even or odd

	Returns
	---------------
	test( str ) - string result of the even / odd test

	Notes
	---------------
	These are doc strings - they're a feature of the Python language
	and make documenting your code all easier. This format is based largly
	on Google's Python documentation format - though not exactly. It's 
	generally good practice to document your work, leaving notes both for 
	your future self, as well as for other programmers who might be using
	your code in the future.
	'''
	if even_or_odd % 2:
		test 				= "this value is odd"

	else:
		test 				= "this value is even"

	return test


def logic_test_two( value ):
	'''Silly logit test example

	Another simple function, this one to see another example of a 
	logic test working in a module on demand.
	
	Arguments
	---------------	
	value( int / float / str / bool ) - a value to be tested

	Returns
	---------------
	test( str ) - a string indicating the status of the test

	Notes
	---------------
	These are doc strings - they're a feature of the Python language
	and make documenting your code all easier. This format is based largly
	on Google's Python documentation format - though not exactly. It's 
	generally good practice to document your work, leaving notes both for 
	your future self, as well as for other programmers who might be using
	your code in the future.
	'''
	if value == "TouchDesigner":
		test 				= "Nice work"

	else:
		test 				= "Try again"

	return test