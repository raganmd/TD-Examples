# if we remember that channels are arrays of numbers, 
# we can quickly see how we might move through one
# of this arrays with a loop.

# first let's remember that we can access the number
# of samples in a CHOP with .numSamples. We can use
# this value to determine our range

# we should take a quick moment to think about how
# we can access a single sample in a CHOP:

print( "let's look at the value at position 0" )
print( op( 'pattern1' )[ 'chan1' ][ 0 ] )

# let's start with a simple task like printing out
# the value of each sample in a pattern CHOP.

# first let's simplify our code by using a variable
# to reference our pattern CHOP.
pattern = op( 'pattern1' )

# next we'll write a simple for loop that runs
# based on the number of samples in a CHOP.

print( '\n' )
print( "let's print out every sample" )
for sample in range( pattern.numSamples ):
	print( pattern[ 'chan1' ][ sample ] )

# let's go one step further and use .format()
# one more time to make for print statements
# that make more sense.

message	= "{} is the value in the {} position"
noise	= op( 'noise1' )

print( '\n' )
print( "let's print out every sample in noise" )
for sample in range( noise.numSamples ):
	print( message.format( 
			round( noise[ 'chan1' ][ sample ], 3 ) , 
			sample
			)
		)