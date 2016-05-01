# set some variables
new_ops_list = [
	'text_newop1' ,
	'text_newop2' ,
	'text_newop3'
	]

node_distance = 100

# loop through list
for item in enumerate( new_ops_list ):
	# create and name op 
	new_op = parent().create( textDAT , item[ 1 ] )

	# set location of nodes ( x or y )
	new_op.nodeX = me.nodeX
	new_op.nodeY = - ( item[ 0 ] * node_distance )