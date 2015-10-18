# define some variables
rectangle1 = op( 'rectangle1' )

# That's great... but what about geometry?
# Let's take a closer look at SOPs

print( 'Like with a sop we can print the path to rectangle1 operator' )
print( rectangle1 )

print( 'We can also look at the member .points' )
print( rectangle1.points )

print( 'Seeing that it is an object by itself, means we can look closer' )
print( 'What happens if we just ask for the first item in this object?' )
print( rectangle1.points[ 0 ] )

print( 'What if we ask to make the whole object a list, and the print it out?' )
print( list( rectangle1.points ) )