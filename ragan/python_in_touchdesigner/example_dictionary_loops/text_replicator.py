# import any necessary modules

import socket

# define some variables

pos_x				= 3300
pos_y				= 0
replicator_table	= op( 'table_replicator_info' )
system_config		= mod( 'text_data' ).uri
displays			= mod( 'text_data' ).displays
local_ip			= socket.gethostbyname( socket.gethostname() )
default_ip			= op( 'text_default_ip' ).text
local_config		= {}
container_COMPs		= parent().findChildren( type = COMP , depth = 1 )

# clear contents of replicator_table
replicator_table.clear()

# delete existing continer COMPs
for items in container_COMPs:
	if op( items ).name != 'container_presets':
		op( items ).destroy()
	else:
		pass

# Test for local_ip in system config
in_system_config = local_ip in system_config

# if our IP matches with a URI in the system config, then we
# fill our dictionary with keys based on the system config file
if in_system_config == True:
	local_config[ 'name' ]		= system_config[ local_ip ][ 'name' ]
	local_config[ 'role' ]		= system_config[ local_ip ][ 'role' ]
	local_config[ 'displays' ]	= system_config[ local_ip ][ 'displays' ]
	local_config[ 'uri' ]		= local_ip

# if our IP doesn't match our system config file, then we fill our
# dictionary with keys based on the default IP address, which is 
# entered in the text dat called 'text_default_ip'
else:
	# assign ip address
	local_ip = default_ip
	local_config[ 'name' ]		= system_config[ local_ip ][ 'name' ]
	local_config[ 'role' ]		= system_config[ local_ip ][ 'role' ]
	local_config[ 'displays' ]	= system_config[ local_ip ][ 'displays' ]
	local_config[ 'uri' ]		= local_ip

# fill table with display information
for items in local_config[ 'displays' ]:
	replicator_table.appendRow( [ 
		items , 
		displays[ items ][ 'width' ] , 
		displays[ items ][ 'height' ] , 
		displays[ items ][ 'orientation' ] 
		] )

# check and correct height / width based on orientation flag
for row in range( replicator_table.numRows ):
	# create a temporary variable to store the width and height of the display
	width_height = [ replicator_table[ row , 1 ].val , replicator_table[ row , 2 ].val ]

	# test for orientation flag
	# if true, swap height and width
	if replicator_table[ row , 3 ] ==  1:
		replicator_table[ row , 1 ] = width_height[ 1 ]
		replicator_table[ row , 2 ] = width_height[ 0 ]

	# if false, we pass and do nothing
	else:
		pass

# create container COMPs based on our replicator table
for row in range( replicator_table.numRows ):
	# create our new container COMP, give it a name from our replciator table
	new_op = parent().create( containerCOMP , replicator_table[ row , 0 ] )
	
	# set the x position of the new container
	new_op.nodeX = pos_x
	
	# set the y position of the new container
	new_op.nodeY = pos_y

	# set the width of the new node based on the replicator table
	new_op.par.w = replicator_table[ row , 1 ]

	# set the height of the new node based on the replicator table
	new_op.par.h = replicator_table[ row , 2 ]

	# turn on the viewer flag
	new_op.viewer = True

	# increment the y position for the next loop
	pos_y -= 200