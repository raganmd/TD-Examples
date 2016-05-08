movie_a						= op( 'moviefilein_a' )
mono_a						= op( 'mono_a' )
level_a						= op( 'level_a' )
cue_list					= mod( op( 'text_cue_list' ) ).cue_list

cue							= 'cue2'

movie_a.par.file			= app.samplesFolder + cue_list[ cue ][ 'file' ]
mono_a.par.mono				= cue_list[ cue ][ 'mono' ]
level_a.par.invert			= cue_list[ cue ][ 'invert' ]
level_a.par.brightness1		= cue_list[ cue ][ 'brightness' ]
level_a.par.blacklevel		= cue_list[ cue ][ 'blacklevel' ]
level_a.par.contrast		= cue_list[ cue ][ 'contrast' ]