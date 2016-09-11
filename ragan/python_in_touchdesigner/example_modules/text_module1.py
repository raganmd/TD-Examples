import datetime

log_file			= op( 'text_log' )

full_text 			= '''{now}

Current Year		| {year}
Current Month		| {month}
Current Day			| {day}
Current Hour		| {hour}
Current Minute		| {minute}
Current Second		| {second}
Current Microsecond	| {microsecond}
'''

verbose_log_message	= '''============================
VERBOSE MESSAGE

On {month}-{day}-{year} at {hour}:{minute}:{second}
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

def Full_date():
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

	formatted_text = full_text.format(
										now			= now,
										year		= year,
										month		= month,
										day			= day,
										hour		= hour,
										minute		= minute,
										second		= second,
										microsecond	= microsecond
										)
	return formatted_text

def Log_message( operator, message, verbose=False, text_port_print=True, append_log=True ):
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

	Returns
	---------------
	None

	Notes
	---------------
	You'll notice that some arguments receive default values. This is so you don't have
	to include them in the call. This means that by default the message will be compact, 
	will print to the text port, and will append the log file.
	'''

	now			= datetime.datetime.now()
	year		= datetime.datetime.now().year
	month		= datetime.datetime.now().month
	day			= datetime.datetime.now().day
	hour		= datetime.datetime.now().hour
	minute		= datetime.datetime.now().minute
	second		= datetime.datetime.now().second
	microsecond	= datetime.datetime.now().microsecond

	path 		= op( operator ).path
	op_name 	= op( operator ).name

	if verbose:
		message = verbose_log_message.format(
												month		= month,
												day			= day,
												year		= year,
												hour		= hour,
												minute 		= minute,
												second		= second,
												operator	= op_name,
												path		= path,
												message 	= message
											)
	else:
		message = log_message.format(
										now					= now,
										operator 			= op_name,
										path 				= path,
										message 			= message
									)
	
	if text_port_print:
		print( message )
	
	else:
		pass

	if append_log:
		log_file.write( '\n' + message )

	else:
		pass
	return