# let's start by making an empty list

my_list = []

print( 'As we go, we will print our list at each' )
print( 'step along the way' )
print( 'My List' ,  my_list )

my_list.append( 1 )

print( '\n' )

print( 'So we just added a single number out our list' )
print( 'what does that look like now?' )
print( 'My List' ,  my_list )

my_list.append( 23 )

print( '\n' )

print( 'So we just added another number out our list' )
print( 'what does that look like now?' )
print( 'My List' ,  my_list )

my_list.extend( [ 45 , 2 , 100 , 6 ] )

print( '\n' )

print( 'Can we add multiple items at once?' )
print( 'My List' ,  my_list )

print( 'We sure can, we just need to use .extend' )
print( 'instead of .append' )

print( '\n' )

print( 'One last handy trick to know is that ' )
print( 'we can reverse our list' )

my_list.reverse()

print( my_list )
