# while we haven't yet talked about the pars() we can take advantage of this
# member of the page class.

# Any given operator with parameters has a page of parameters, with names
# and values. Knowing this we can find our way to the paramters of an
# op with some clever programming.

# Let's look at the anatomy of something like:
# op( 'constant_pars_target' ).pars( 'name0' )[ 0 ]

# pars() returns a list of parameters. For us, we can think of the above
# in plain english as the first list element in the 
# parameter 'name0' from constant_pars_target.

# Okay, so what can we do with that information?

# Well, we might make a table of par names and values, and set them by 
# looping through our table. Let's take a look at how that might work.

# First we'll make a table called 'table_pars_preset1'
# Let's fill that table with par names in one column, and par values
# in another.

# Next we'll create a stand in table where we can indicate which preset
# we want to use. Let's call that 'table_preset_selection'.

# In the first cell let's write 'table_pars_preset1'
# Alright, we're almost ready to write our for loop.

# Finally let's add a constant CHOP called 'constant_pars_target'

# Now let's write a loop!

# First we'll start with some variable names:

preset								= op( 'table_preset_selection' )[ 0, 0 ]
target								= op( 'constant_pars_target' )

# Here in our loop is where things get intersting.
# For starters we're going to use the op string name we've defined in our 
# preset table. 

for item in range( op( preset ).numRows )[ 1: ]:

	# As we go through the loop we'll use two variables one as our 
	# targed op_parameter, and another as a our parameter_value
	op_par							= op( preset )[ item, 0 ]
	par_val							= op( preset )[ item, 1 ]
	
	# Finally, we'll use those two varibles to change some varibles.
	target.pars( op_par )[ 0 ].val	=	par_val
	
	# We can use our preset statement to see how those two work together:
	print( 'target parameter: ', op_par )
	print( 'target value: ', par_val )

	# Let's also look at what that script would be if we were to write it
	# out by hand:
	script = 'op( "{op}" ).{par} = {par_val}'
	
	print( 'The script we run each loop:' )
	print( script.format( op = target.name, par = op_par, par_val = par_val ) )

	print( '\n' )

