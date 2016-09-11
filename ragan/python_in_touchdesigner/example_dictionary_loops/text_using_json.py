# JSON, as a format is very similar to python dictionaries, 
# so similar in fact there's a very simple way to work with it. 

# If you're already working with dictionaries this will feel like an
# easy transition. There are, however, a few things you need to keep in mind.

# We need to make sure that our JSON is correctly formatted. If you compare
# the JSON to the right, with our first example you can see that we've 
# enclosed our entire dictionary in curly brackets {}. You can also see that
# we've replaced our first variable with a key-value pair.

# inventory = 

# became

# "inventory" :

# You can also check your JSON with some simple on line JSON validators. You
# might not need to do this with simple arrays, but with longer and more
# complicated sets it can be best to ensure that you have valid JSON before
# you start working in touch

# http://jsonlint.com/


# First we need to import the json module. 

import json

# next we're going to use just the text from our text dat
imported_dict		= op( 'text_simple_json' ).text

# next we'll use json.loads to import that as a python dictionary
dict_from_json		= json.loads( imported_dict )

# first let's just print the dictionary to make sure things worked out
print( "Here is our whole json object" )
print( imported_dict )

print( '_ ' * 10 )

# next we could print just the top tier keys
print( "Here are our top tier keys" )
for item in dict_from_json.keys():
	print( item )

print( '\n' )
print( '_ ' * 10 )
# next let's print the keys in our 'inventory' dictionary
print( "Here are the keys in inventory" )
for item in dict_from_json[ 'inventory' ].keys():
	print( item )
	
print( '\n' )
print( '_ ' * 10 )
# since we're on a roll, let's first print our keys, and
# then print their values
print( "Here are the keys and values in inventory" )
for key, value in dict_from_json[ 'inventory' ].items():
	print( key, 'contains', value )

print( '\n' )
print( '_ ' * 10 )
# That's still not very pretty, so let's see if we can make 
# something that's a little nicer
print( "Pretty printing our keys and values" )
for key, value in dict_from_json[ 'inventory' ].items():
	print( key, 'contains' )
	
	for item, quantity in value.items():
		print( quantity, item )
	
	print( '\n' )
