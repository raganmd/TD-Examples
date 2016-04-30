old_ops		= parent().findChildren( type = containerCOMP, depth = 1 )
config_DAT	= op( 'select_config' )

def delete_old_ops():
	
	for each_op in old_ops:
		each_op.destroy()

	return

def create_new_ops():
	
	new_op						= parent().create( containerCOMP, 'container_' + config_DAT[ 0, 0 ] )
	new_op.par.externaltox		= config_DAT[ 0, 1 ]
	new_op.par.savebackup		= 0
	new_op.par.reinitnet.pulse()

	return

delete_old_ops()
create_new_ops()