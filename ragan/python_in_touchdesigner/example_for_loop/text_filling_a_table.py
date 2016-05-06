# Loops are useful for any number of processes. Let's imagine 
# that we want to fill up a table with the RGBA values from
# a TOP.

# We could certainly use a TOP to CHOP, and then a CHOP to DAT, 
# but we might imagine a circumstance where we don't want this
# operation to happen all the time, only at times that we specify.

# Or we might want to sample an image for colors to use for another
# process, and we don't need a dedicated series of operators for this.

# At any rate, lets look at how we might do this.

# In this case I've set up a noise TOP to be 20 pixels tall, and 1 pixel
# wide. We can think of the number of pixels vertically as the range 
# for our loop. 

# We'll clear a table, and then append the contents for every pixel 
# in our TOP. Easy.

# First let's use some variables to make writing our loop easeir:

nosie_TOP			= op( 'noise2' )
pixel_vals_DAT		= op( 'table1' )
header				= [ 'r', 'g', 'b', 'a' ]

# In case there's anything left in our table, let's clear its
# contents first.
pixel_vals_DAT.clear()

# Next let's put some header information back into our dat, 
# so we know what each colum is:
pixel_vals_DAT.appendRow( header )

# Now we can loop through our pixels and append their values
# to our table.
for pixel in range( nosie_TOP.height ):
	pixel_vals_DAT.appendRow( nosie_TOP.sample( x = 0, y = pixel ) )