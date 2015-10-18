# define some variables
noise1 = op( 'noise1' )

# understanding the channel operator make
# a big difference in the way we use TouchDesigner

# lets start by just printing our variable

print( 'If we just print our noise1 variable we see this' )
print( noise1 )

print( 'If we print chan1 in noise1 one we see this' )
print( noise1[ 'chan1' ] )

print( 'we can also access this by using .chan( channelIndexHere )' )
print( noise1.chan( 0 ) )

print( 'Finally, we can see the whole list of values if we use' )
print( '.vals as we... that looks like') 
print( 'noise1.( channelIndexHere ).vals' )
print( noise1.chan( 0 ).vals )