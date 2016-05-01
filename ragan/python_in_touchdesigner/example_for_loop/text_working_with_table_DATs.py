table	= op( 'table_simple_table' )

# lists are all well and good, but how do we use
# them in TouchDesigner?
# first lets look at how we might use some tables.

# looping through table rows

# one way to loop through our table's rows would be
# to use the number of rows to define a range, 
# then use our references to tables to move through
# its contents

print( "Here's one way to loop through our table" )
for item in range( table.numRows ):
	print( table[ item, 0 ] )


# another way to loop through our table would be to use
# the .col() method. This returns an object that's a 
# list of rows. To get the content of the cell, we 
# need to use .val.

print( '\n' )
print( "Here's another way to loop through our table" )
for item in table.col( 0 ):
	print( item.val )