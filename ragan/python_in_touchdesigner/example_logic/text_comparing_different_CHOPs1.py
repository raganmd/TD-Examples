# define our variables
chop1_val1 = op( 'constant_CHOP1' )[ 'chan1' ]
chop1_val2 = op( 'constant_CHOP1' )[ 'chan2' ]
chop2_val1 = op( 'constant_CHOP2' )[ 'chan1' ]
chop2_val2 = op( 'constant_CHOP2' )[ 'chan2' ]

# compare chan1 in CHOP1 and CHOP2
if chop1_val1 == chop2_val1:
	print( "These values are equal" )

elif chop1_val1 > chop2_val1:
	print( "Chan1 in CHOP 1 is greater than Chan2 in CHOP 2" )

elif chop1_val1 < chop2_val1:
		print( "Chan1 in CHOP 1 is less than Chan2 in CHOP 2" )

# compare chan2 in CHOP1 and CHOP2
if chop1_val2 == chop2_val2:
	print( "These values are equal" )

elif chop1_val2 > chop2_val2:
	print( "Chan2 in CHOP 1 is greater than Chan2 in CHOP 2" )

elif chop1_val2 < chop2_val2:
		print( "Chan2 in CHOP 1 is less than Chan2 in CHOP 2" )