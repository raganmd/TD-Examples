# define our variables
# using modules means that we can use our dot notation to
# access an object inside of our text DAT
inventory = mod( 'text_test_dictionary' ).inventory
table = op( 'table_inventory' )
table_length = []
place_holder = 1

# first things first, let's clear out the contents of the table
table.clear()

# loop through the dictionary and add headers
for dictionary_key , dictionary_value in inventory.items():
    table.appendCol( [ dictionary_key ] )
    # add a blank column for next set of data points
    table.appendCol()

    # add to the list so we can determine the max length of the table
    table_length.append( len( dictionary_value ) )

# set the table length based on the maximum number of dictionary entries
table.setSize( max( table_length ) + 1 , table.numCols )

# loop through dictionary again to fill in table
for dictionary_key , dictionary_value in inventory.items():

# generate an enumerated list to loop through
    value_list = list( enumerate( dictionary_value ) )

# use enumerated list to fill in table 
    for item in value_list:
        table[ item[ 0 ] + 1 , dictionary_key  ] = item[ 1 ]
        table[ item[ 0 ] + 1 , place_holder ] = inventory[ dictionary_key ][ item[ 1 ] ]

# increment placeholder to ensure that our data goes in the right place
    place_holder += 2