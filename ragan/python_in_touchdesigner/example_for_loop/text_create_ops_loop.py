# create a new variable called new_op
# this is also a copy of the operator out 1
new_op = parent().copy( op( 'moviefilein1' ) )

# since we've defind our new op with the variable
# name new_op we can continue to use this name
# our next step will be to give it a name
new_op.name = 'moviefilein_new_op'

# finally we're going to change the location of
# our new operator. In this example we want it
# created at a location in relation to our original
# operator. We start by finding the original operator's
# y position, and then subtract 200
new_op.nodeY = op( 'moviefilein1' ).nodeY - 100