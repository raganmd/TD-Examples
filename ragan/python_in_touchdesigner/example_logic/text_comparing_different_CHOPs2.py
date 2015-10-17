# define our variables
# this approach takes advantage of the channel class
my_val1 = op( 'constant_CHOP1' ).chan( 0 )
my_val2 = op( 'constant_CHOP1' ).chan( 1 )
my_val3 = op( 'constant_CHOP2' ).chan( 0 )
my_val4 = op( 'constant_CHOP2' ).chan( 1 )

# compare chan1 in CHOP1 and CHOP2
if my_val1 == my_val3:
	print( "These values are equal" )

elif my_val1 > my_val3:
	print( "my_val1 wins" )
	print( "That value is " + str( my_val1 ) )
	print( "It's index is %r" % my_val1.index )
	print( "It's channel name is %r" % my_val1.name )
	print( "It's owner is %r" % my_val1.owner.name )

elif my_val1 < my_val3:
	print( "my_val3 wins" )
	print( "That value is " + str( my_val3 ) )
	print( "It's index is %r" % my_val3.index )
	print( "It's channel name is %r" % my_val3.name )
	print( "It's owner is %r" % my_val3.owner.name )

# compare chan2 in CHOP1 and CHOP2
if my_val2 == my_val4:
	print( "These values are equal" )

elif my_val2 > my_val4:
	print( "my_val2 wins" )
	print( "That value is " + str( my_val2 ) )
	print( "It's index is %r" % my_val2.index )
	print( "It's channel name is %r" % my_val2.name )
	print( "It's owner is %r" % my_val2.owner.name )

elif my_val2 < my_val4:
	print( "my_val4 wins" )
	print( "That value is " + str( my_val4 ) )
	print( "It's index is %r" % my_val4.index )
	print( "It's channel name is %r" % my_val4.name )
	print( "It's owner is %r" % my_val4.owner.name )