# define some variables
radio_buttons = op( 'container_radio_buttons' )

# Let's take a look at findChildren
# we can see all of the ops inside of our container with:
print( radio_buttons.findChildren() )

# What if we only wanted to see the buttons??
print( radio_buttons.findChildren( depth = 1 ) )

# That's fine as long as there aren't any other operators
# inside of our conatiner. If we wanted to make sure we only
# got a list of buttons, we could be even more specific with

print( radio_buttons.findChildren( type = buttonCOMP , depth = 1 ) )

# Okay... so?
# Well, what we get back is a list, so what if we did this?

print( radio_buttons.findChildren( type = buttonCOMP , depth = 1 )[ 0 ] )

# Maybe we don't want to see the whole path, we just want to see it's name
print( radio_buttons.findChildren( type = buttonCOMP , depth = 1 )[ 0 ].name )

# Or maybe just its digits
print( radio_buttons.findChildren( type = buttonCOMP , depth = 1 )[ 0 ].digits )

# We could even click on one of our buttons this way
radio_buttons.findChildren( type = buttonCOMP , depth = 1 )[ 0 ].click()