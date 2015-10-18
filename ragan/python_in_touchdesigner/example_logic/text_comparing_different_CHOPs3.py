# define our variables
# this approach takes advantage of the channel class
my_val1 = op( 'constant_CHOP1' ).chan( 0 )
my_val2 = op( 'constant_CHOP1' ).chan( 1 )
my_val3 = op( 'constant_CHOP2' ).chan( 0 )
my_val4 = op( 'constant_CHOP2' ).chan( 1 )

my_text = '''%r wins
That value is %r
It's index is %r
It's channel name is %r
It's owner is %r
'''

# compare chan1 in CHOP1 and CHOP2
if my_val1 == my_val3:
	print( "These values are equal" )

elif my_val1 > my_val3:
	print( my_text % (
		'my_val1' , 
		str( my_val1 ) , 
		my_val1.index , 
		my_val1.name , 
		my_val1.owner.name
		) )

elif my_val1 < my_val3:
	print( my_text % (
		'my_val3' , 
		str( my_val3 ) , 
		my_val3.index , 
		my_val3.name , 
		my_val3.owner.name
		) )

# compare chan2 in CHOP1 and CHOP2
if my_val2 == my_val4:
	print( "These values are equal" )

elif my_val2 > my_val4:
	print( my_text % (
		'my_val2' , 
		str( my_val2 ) , 
		my_val2.index , 
		my_val2.name , 
		my_val2.owner.name
		) )

elif my_val2 < my_val4:
	print( my_text % (
		'my_val4' , 
		str( my_val4 ) , 
		my_val4.index , 
		my_val4.name , 
		my_val4.owner.name
		) )