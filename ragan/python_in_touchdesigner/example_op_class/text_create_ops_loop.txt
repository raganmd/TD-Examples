# set some variables
new_ops_list = [
	'text_newop1' ,
	'text_newop2' ,
	'text_newop3'
	]

node_distance = 200

# create an enumerated list from the original
new_ops_enumerate = list( enumerate( new_ops_list) )

# loop through list
for item in new_ops_enumerate:
	# create and name op 
	new_op = parent().create( textDAT , item[ 1 ] )

	# set location of nodes ( x or y )
	#new_op.nodeX = item[ 0 ] * node_distance
	new_op.nodeY = - ( item[ 0 ] * node_distance )