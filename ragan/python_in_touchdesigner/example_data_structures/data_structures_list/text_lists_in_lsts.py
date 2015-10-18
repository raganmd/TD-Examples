# let's make a set of lists in a list
inventory = [ 
	[ 'fruit' , 
	'apple' , 
	'kiwi' , 
	'orange' ] ,
	[ 'baked-goods' , 
	'bread' , 
	'bagles' , 
	'pies' ] , 
	[ 'soft-drinks' , 
	'sprite' , 
	'coke' , 
	'dr. Pepper' ]
]

print( 'We can see the whole list of lists' )
print( 'Though, truth be told, that is overwhelming' )
print( inventory )

print( '\n' )

print( 'Instead, maybe we just want to look at one list' )
print( inventory[ 0 ] )

print( '\n' )

print( 'We planned ahead, and the first item in our list' )
print( 'is our header. So we could do something like this:' )

print( '\n' )

print( 'In our %s department we have:' % inventory[ 0 ][ 0 ] )
print( inventory[ 0 ][ 1: ] )

print( '\n' )

print( 'We can find just a single item in a list with:' )
print( inventory[ 0 ][ 0 ] )