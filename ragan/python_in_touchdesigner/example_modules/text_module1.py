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