children = me.parent().findChildren( type = COMP , maxDepth = 1 )

for i in range( len( children ) ):
	print( str( children[ i ] ) + ' Cook off, Cook on' )
	op( children[ i ] ).allowCooking = False
	op( children[ i ] ).allowCooking = True