# okay, but why do we care?

# define some variables
noise1 = op( 'noise1' )

# we can use what we've learned working with the .chans().vals
# to help us understand a little bit more about our CHOP
# for example, if our channel is a list of values, we can
# access those values just like we might in a list

print( noise1[ 'chan1' ][ 0 ] )
print( noise1[ 'chan1' ][ 1 ] )
print( noise1[ 'chan1' ][ 2 ] )

# we can even do the same things we might do in python here
print( len( noise1[ 'chan1' ] ) )

# though if we look at the wiki, we'll find that there's already
# a method to do just this called .numSamples
# and a method called numChans - which tells us how many channels
# If we think of our CHOP as a list of lists... then we can both
# see how many lists, and the length of the lists.

print( noise1.numSamples )
print( noise1.numChans )