import datetime

log_file			= op( 'text_log_file' )
log_path			= "example_extensions/log_files/log.txt"

full_text 			= '''{now}

Current Year		| {year}
Current Month		| {month}
Current Day			| {day}
Current Hour		| {hour}
Current Minute		| {minute}
Current Second		| {second}
Current Microsecond	| {microsecond}
'''

raw_date_time 		= "On {month}-{day}-{year} at {hour}:{minute}:{second}"

verbose_log_message	= '''============================
VERBOSE MESSAGE

{date_time}
----------------------------
operator			|| {operator}
At Network Location	|| {path}

----------------------------
Logged
{message}
============================
'''

log_message			= '''----------------------------
{now}
----------------------------
{operator}
{path}
{message}
'''

class Ext_example():

	def __init__( self ):
		'''The init function.

		We're not doing anything with our init function in this example
		so we'll leave this empty.

		Notes
		---------------
		'''	
		return

	def Log_date( self ):
		year						= datetime.datetime.now().year
		month						= datetime.datetime.now().month
		day							= datetime.datetime.now().day
		hour						= datetime.datetime.now().hour
		minute						= datetime.datetime.now().minute
		second						= datetime.datetime.now().second
		
		updated_log_date 			= log_date.format( 
														month 		= month,
														day 		= day,
														year 		= year,
														hours 		= hour,
														minutes 	= minute,
														seconds 	= second
													)
		
		return updated_log_date
	
	def Log_date_time( self ):
		'''Create a formatted time stamp

		A look at how we might create a formatted time stamp to use with
		various logging applications.
		
		Arguments
		---------------	
		None

		Returns
		---------------
		formatted_text( str ) - a string time stamp

		Notes
		---------------
		'''

		now			= datetime.datetime.now()
		year		= datetime.datetime.now().year
		month		= datetime.datetime.now().month
		day			= datetime.datetime.now().day
		hour		= datetime.datetime.now().hour
		minute		= datetime.datetime.now().minute
		second		= datetime.datetime.now().second
		microsecond	= datetime.datetime.now().microsecond

		date_time 	= raw_date_time.format( 
										month 	= month,
										day 	= day,
										year 	= year,
										hour 	= hour,
										minute 	= minute,
										second 	= second
										)

		return date_time

	def Log_message( self, operator, message, verbose=False, text_port_print=True, append_log=True ):
		'''Logging Method.

		A simple look at how you might start to think about building a logger for a TouchDesigner
		application. A logger is a great way to build out files with time stamped events. The
		more complex a project becomes, the more important it can become to have some means
		of logging the operations of your program. Here's a simple look at what that might
		look like.
		
		Arguments
		---------------	
		operator( touch object ) - the touch object whose path you'd like incldued in the log message
		message( str ) - a message to include in the log
		verbose( bool ) - a toggle for verbose or compact messages
		text_port_print( bool ) - a toggle to print to the text port, or not
		append_log( bool ) - a toggle to append to the log file , or not

		Example
		---------------	
		target_op		= op( 'constant1' )
		message 		= "This operator needs attention"

		parent().Log_message( target_op, message )

		also

		parent().Log_message( target_op, message, verbose = True )

		Returns
		---------------
		None

		Notes
		---------------
		You'll notice that some arguments receive default values. This is so you don't have
		to include them in the call. This means that by default the message will be compact, 
		will print to the text port, and will append the log file.
		'''

		path 		= operator.path
		op_name 	= operator.name

		# logic tests for verbose or compact
		if verbose:
			message = verbose_log_message.format(
													date_time 	= self.Log_date_time(),
													operator	= op_name,
													path		= path,
													message 	= message
												)

		else:
			message = log_message.format(
											now					= self.Log_date_time(),
											operator 			= op_name,
											path 				= path,
											message 			= message
										)
		
		# logic tests for text_port_print
		if text_port_print:
			print( message )
		
		else:
			pass

		# log tests for appending log
		if append_log:
			log_file.write( '\n' + message )

		else:
			pass

		# save the log file to disk - external from the TouchDesigner project	
		self.Save_log()

		return

	def Save_log( self ):
		'''Saves log to disk.

		This helper function saves the log file to disk.

		Notes
		---------------
		None
		'''

		op( log_file ).save( log_path )

		return

	def Clear_log( self ):
		'''Clears Log File.

		This helper function clears the text dat used to hold the log file.

		Notes
		---------------
		None
		'''

		op( log_file ).clear()

		return