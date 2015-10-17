# define our variables
my_val1 = op( 'constant1' )[ 'chan1' ]
my_val2 = op( 'constant1' )[ 'chan2' ]

if my_val1 == my_val2:
	print( "These values are equal!" )

elif my_val1 > my_val2:
	print( "Integer 1 is greater than integer 2" )

elif my_val1 < my_val2:
	print( "Integer 1 is less than integer 2" )
	

text = '''Let's take a closer look...
My Val 1 is %r
My Val 2 is %r'''

print( text % ( my_val1 , my_val2 ) )