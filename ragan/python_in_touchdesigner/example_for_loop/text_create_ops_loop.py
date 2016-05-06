# we can also use loops to do all sorts of exciting things
# like creat and place operators.

# What we'll quikcly realize here is that for loops and
# the replicator COMP look very similar in the way they
# operate when it comes to creating ops!

# You might feel like the replicator is good enough, so why
# learn how this work?! Sometimes knowing exactly how a process
# works can help us better understand another process. 

# In this case, setting up our own replicator script can 
# teach us a lot about the replicator. 

# set some variables
new_ops_list = [
	'text_newop1' ,
	'text_newop2' ,
	'text_newop3'
	]

# We'll use this to determine the space between operators.
node_distance = 100

# loop through list
for item in enumerate( new_ops_list ):
	# create and name op 
	new_op = parent().create( textDAT , item[ 1 ] )

	# set location of nodes ( x or y )
	new_op.nodeX = me.nodeX
	new_op.nodeY = - ( item[ 0 ] * node_distance )