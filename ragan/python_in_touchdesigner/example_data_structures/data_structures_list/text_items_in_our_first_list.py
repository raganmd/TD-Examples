# let's first create our first list
my_int_list = [ 1 , 2 , 3 , 4 ]
my_float_list = [ 1.235 , 1.5679 , 9.454 , 4.23485 ]
my_string_list = [ 'apple' , 'kiwi' , 'orange' , 'pineapple' ]
my_bool_list = [ True , True , False , True, False ]
my_mixed_list = [ 1.234 , 5 , 'apple' , True , 3.45 ]
line_break = '\n'
dotted_break = '\n' + '- ' * 20 + '\n'


print( 'We can start with our int_list' )
print( my_int_list[ 0 ] )
print( my_int_list[ 1 ] )
print( my_int_list[ 2 ] )
print( my_int_list[ 3 ] )

print( 'The item in the 0 position of my_int_list is %d' % my_int_list[ 0 ] )
print( 'The item in the 1 position of my_int_list is %d' % my_int_list[ 1 ] )
print( 'The item in the 2 position of my_int_list is %d' % my_int_list[ 2 ] )
print( 'The item in the 3 position of my_int_list is %d' % my_int_list[ 3 ] )
print( 'The sum of the numbers in list this is %d' % sum( my_int_list ) )

print( line_break )

print( 'We can also see only items up to a position in a list' , my_int_list[ :2 ] )
print( 'We can also see only items up to a position in a list' , my_int_list[ :3 ] )
print( 'We can also see only items up to a position in a list' , my_int_list[ 2: ] )
print( 'We can also see only items up to a position in a list' , my_int_list[ 3: ] )

print( dotted_break )

print( 'Next, how about our float list' )
print( 'The item in the 0 position of my_float_list is %r' % my_float_list[ 0 ] )
print( 'The item in the 1 position of my_float_list is %r' % my_float_list[ 1 ] )
print( 'The item in the 2 position of my_float_list is %r' % my_float_list[ 2 ] )
print( 'The item in the 3 position of my_float_list is %r' % my_float_list[ 3 ] )
print( 'The sum of the numbers in list this is %r' % sum( my_float_list ) )

print( line_break )

print( 'We can also see only items up to a position in a list' , my_float_list[ :2 ] )
print( 'We can also see only items up to a position in a list' , my_float_list[ :3 ] )
print( 'We can also see only items up to a position in a list' , my_float_list[ 2: ] )
print( 'We can also see only items up to a position in a list' , my_float_list[ 3: ] )

print( dotted_break )

print( 'What about that string list?' )
print( 'The item in the 0 position of my_string_list is %r' % my_string_list[ 0 ] )
print( 'The item in the 1 position of my_string_list is %r' % my_string_list[ 1 ] )
print( 'The item in the 2 position of my_string_list is %r' % my_string_list[ 2 ] )
print( 'The item in the 3 position of my_string_list is %r' % my_string_list[ 3 ] )
print( 'We can not not sum a list of strings' )

print( line_break )

print( 'We can also see only items up to a position in a list' , my_string_list[ :2 ] )
print( 'We can also see only items up to a position in a list' , my_string_list[ :3 ] )
print( 'We can also see only items up to a position in a list' , my_string_list[ 2: ] )
print( 'We can also see only items up to a position in a list' , my_string_list[ 3: ] )

print( dotted_break )

print( 'Okay, so this will work with our bool_list too, right?' )
print( 'The item in the 0 position of my_bool_list is %r' % my_bool_list[ 0 ] )
print( 'The item in the 1 position of my_bool_list is %r' % my_bool_list[ 1 ] )
print( 'The item in the 2 position of my_bool_list is %r' % my_bool_list[ 2 ] )
print( 'The item in the 3 position of my_bool_list is %r' % my_bool_list[ 3 ] )

print( line_break )

print( 'We can also see only items up to a position in a list' , my_bool_list[ :2 ] )
print( 'We can also see only items up to a position in a list' , my_bool_list[ :3 ] )
print( 'We can also see only items up to a position in a list' , my_bool_list[ 2: ] )
print( 'We can also see only items up to a position in a list' , my_bool_list[ 3: ] )

print( dotted_break )

print( 'Last but not least, what about our mixed list?' )
print( 'The item in the 0 position of my_mixed_list is %r' % my_mixed_list[ 0 ] )
print( 'The item in the 1 position of my_mixed_list is %r' % my_mixed_list[ 1 ] )
print( 'The item in the 2 position of my_mixec_list is %r' % my_mixed_list[ 2 ] )
print( 'The item in the 3 position of my_mixed_list is %r' % my_mixed_list[ 3 ] )

print( line_break )

print( 'We can also see only items up to a position in a list' , my_mixed_list[ :2 ] )
print( 'We can also see only items up to a position in a list' , my_mixed_list[ :3 ] )
print( 'We can also see only items up to a position in a list' , my_mixed_list[ 2: ] )
print( 'We can also see only items up to a position in a list' , my_mixed_list[ 3: ] )