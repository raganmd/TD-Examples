# define our variables
decimal_places = 2
my_val1 = op( 'constant1' )[ 'chan1' ].vals
my_val2 = op( 'constant1' )[ 'chan2' ].vals

if my_val1 == my_val2:
	print( "These values are equal!" )

elif my_val1 > my_val2:
	print( "Integer 1 is greater than integer 2" )

elif my_val1 < my_val2:
	print( "Integer 1 is less than integer 2" )
	

text = '''Let's take a closer look...
Rounded to %d decimal places
My Val 1 is %r
My Val 2 is %r'''

print( text % ( 
	decimal_places , 
	round( my_val1[ 0 ] , decimal_places ), 
	round( my_val2[ 0 ] , decimal_places ) 
	) )