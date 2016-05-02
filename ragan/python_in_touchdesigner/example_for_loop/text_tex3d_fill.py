# how else might we use for loops? We've seen how they
# might work with CHOPs and DATs, but what about TOPs?

# We might imagine a circumstance where we wanted to 
# fill a texture 3D - maybe for instancing, UI building
# or any number of things.

# We can do this with a for loop easily, with just a
# little bit of thought.

# define some variables
text_DAT		= op( 'table_tex3d' )
text_TOP		= op( 'text1' )
tex3d_TOP		= op( 'tex3d1' )

for item in range( text_DAT.numRows ):
	# change the text 
	text_TOP.par.text				= text_DAT[ item, 0 ]
	
	# use a random number to set the background color
	text_TOP.par.bgcolorr			= tdu.rand( item )
	text_TOP.par.bgcolorg			= tdu.rand( item + 1 )
	text_TOP.par.bgcolorb			= tdu.rand( item + 2 )

	# set the repalce index to match the row
	tex3d_TOP.par.replaceindex		= item
	
	# pulse fill the texture 3D
	tex3d_TOP.par.resetsinglepulse.pulse()