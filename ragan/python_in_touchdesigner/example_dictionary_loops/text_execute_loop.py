mono_defaults = mod( op( 'text_defaults' ) ).mono_defaults
level_defaults = mod( op( 'text_defaults' ) ).level_defaults

for keys, values in mono_defaults.items():
	
	#reset mono defaults for A 
	exec( "op( 'mono_a' ).par." + keys + " = " + str( values ) )
	
	# debut print so you can see what this is acutally doing
	# print( "op( 'mono_a.par' )." + keys + " = " + str( values ) )

for keys, values in level_defaults.items():
			
	#reset mono defaults for A 
	exec( "op( 'level_a' ).par." + keys + " = " + str( values ) )