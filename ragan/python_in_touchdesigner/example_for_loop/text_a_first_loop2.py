# what if we don't have a list, and instead
# just want to run a loop a set number of
# times. Surely that's possible, right?

# In fact it is!

loop_count	= 10

print( "This is our first loop" )
for item in range( loop_count ):
	print( item )

# that works great, but what's a range?!
# let's print one out so we can better
# see what that's about:

print( '\n' )
print( "This is the range of our loop_count" )
print( range( loop_count ) )

# printing this out we can see what we
# get a tuple with a starting and
# ending position in the list
# this might seem to imply that we can 
# use a range, or list, but start at a 
# position other than the first item.

print( '\n' )
print( "This is loop starting at position 5 going to the end" )
for item in range( loop_count )[ 5: ]:
	print( item )

print( '\n' )
print( "This is loop starting at the beginning and going to postiion 5" )
for item in range( loop_count )[ :5 ]:
	print( item )