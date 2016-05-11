operator = me

message ='''
Just a friendly message from your TouchDesigner Network.
Anything could go here, an error message an init message.

You dream it up, and it'll print
'''

# print and append log file with a verbose log message
mod( 'text_module1' ).Log_message( operator, message, verbose = True )

# print and append log file with a compact log message
# mod( 'text_module1' ).Log_message( operator, message )


# append log file with verbose log message
# mod( 'text_module1' ).Log_message( operator, message, verbose = True, text_port_print = False )


# print a compact log message
# mod( 'text_module1' ).Log_message( operator, message, append_log = False )
