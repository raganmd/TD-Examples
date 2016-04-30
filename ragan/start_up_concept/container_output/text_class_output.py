import socket

machine_ip		= socket.gethostbyname( socket.gethostname() )
old_ops			= parent().findChildren( type = containerCOMP, depth = 1 )
project			= op.Project1
choose_config	= op( 'container_choose_config' )

class Output:
	
	def __init__( self ):

		return

	def Touch_init( self, guest ):
		print( 'Output Touch init stuffs' )
		
		if guest:
			choose_config.par.display	= 1

		else:
			self.Delete_old_ops()
			self.Create_new_ops()

		return

	def Delete_old_ops( self ):
		
		for each_op in old_ops:
			if each_op.name == 'container_choose_config' :
				pass
			else:
				op( each_op ).destroy()

		return

	def Create_new_ops( self ):
		
		local_config					= project.fetch( 'local_config' )

		new_op							= parent().create( containerCOMP, 'container_' + local_config[ 'role' ] )
		new_op.par.externaltox			= local_config[ 'tox' ]
		new_op.par.savebackup			= 0
		new_op.par.reinitnet.pulse()

		return

	def Guest_set_up( self, role, tox ):

		project.unstore( 'local_config' )

		local_config = {}
		
		local_config[ 'uri' ]			= machine_ip
		local_config[ 'local_id' ]		= 'guest'
		local_config[ 'role' ]			= role
		local_config[ 'tox' ]			= tox
		local_config[ 'media_path' ]	= 'c://'
		
		project.store( 'local_config' , local_config )
		
		choose_config.par.display		= 0

		self.Create_new_ops()
		
		return