import socket

system		= mod( 'text_system_config' ).uri
machines 	= list( mod( 'text_system_config' ).uri.keys() )
machine_ip	= socket.gethostbyname( socket.gethostname() )

project		= op.Project1

class Config:
	
	def __init__( self ):

		return

	def Touch_init( self ):
		print( 'Config touch init business' )

		guest	= self.Load_local_config()

		return guest

	def Load_local_config ( self ):
			
			# clear storage
			project.unstore( 'local_config' )

			# check for key match:
			system_machine = machine_ip in system

			# create a new empty dictionary
			local_config = {}

			# create system assignment based on ip
			if system_machine:	
				# print( 'I have a job for you' )
				local_config[ 'uri' ]			= machine_ip
				local_config[ 'local_id' ]		= system[ machine_ip ][ 'local_ID' ]
				local_config[ 'role' ]			= system[ machine_ip ][ 'role' ]
				local_config[ 'tox' ]			= system[ machine_ip ][ 'tox' ]
				local_config[ 'media_path' ]	= system[ machine_ip ][ 'media_path' ]
				local_config[ 'group' ]			= system[ machine_ip ][ 'group' ]
				local_config[ 'outputs' ]		= sum([local_config['group'][projector] for projector in [groupname for groupname in local_config['group']]], [])
				
				project.store( 'local_config' , local_config )

				guest							= False
			
			else:
				guest							= True

			return guest