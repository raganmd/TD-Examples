# define our variables
# this approach takes advantage of the channel class
my_val1 = op( 'constant_CHOP1' ).chan( 0 )

print( "My value is " + str( my_val1 ) )
print( "My index is %r" % my_val1.index )
print( "My channel name is %r" % my_val1.name )
print( "My owner is %r" % my_val1.owner.name )