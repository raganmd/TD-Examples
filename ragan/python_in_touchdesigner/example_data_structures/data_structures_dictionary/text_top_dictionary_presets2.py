text_top_dictionary = { 
	'preset1' : { 
		'text_top' : {
			"text" : "CAT!" , 
			"fontsizex" : 20 ,
			"alignx" :  1 ,
			"aligny" : 1 ,
			"fontcolorr" : 0.0 ,
			"fontcolorg" : 1.0 ,
			"fontcolorb" : 0.0 ,
			"fontalpha" : 1.0 ,
			"bgcolorr" : 0.0 ,
			"bgcolorg" : 0.0 ,
			"bgcolorb" : 0.0 ,
			"bgalpha" : 0.5
		} ,
		'level_top' : {
			'invert' : 1.0
		}
	} , 
	'preset2' : { 
		'text_top' : {
			"text" : "Monkey" , 
			"fontsizex" : 15 ,
			"alignx" :  1 ,
			"aligny" : 1 ,
			"fontcolorr" : 1.0 ,
			"fontcolorg" : 0.0 ,
			"fontcolorb" : 0.0 ,
			"fontalpha" : 1.0 ,
			"bgcolorr" : 0.0 ,
			"bgcolorg" : 0.0 ,
			"bgcolorb" : 0.0 ,
			"bgalpha" : 1.0
		} , 
		'level_top' : {
			'invert' : 0.5
		}
	} , 
	'preset3' : { 
		'text_top' : {
			"text" : "DOG" , 
			"fontsizex" : 80 ,
			"alignx" :  1 ,
			"aligny" : 1 ,
			"fontcolorr" : 0.0 ,
			"fontcolorg" : 0.0 ,
			"fontcolorb" : 1.0 ,
			"fontalpha" : 1.0 ,
			"bgcolorr" : 1.0 ,
			"bgcolorg" : 1.0 ,
			"bgcolorb" : 1.0 ,
			"bgalpha" : 1.0
		} , 
		'level_top' : {
			'invert' : 0.0
		}
	}	
} 

top_preset = op( 'table_preset_selection1' )[ 0 , 0 ].val
target_text = op( 'text2' )
target_level = op( 'level1' )

target_text.par.text = text_top_dictionary[ top_preset ][ 'text_top' ][ 'text' ]
target_text.par.fontsizex = text_top_dictionary[ top_preset ][ 'text_top' ][ 'fontsizex' ]
target_text.par.alignx = text_top_dictionary[ top_preset ][ 'text_top' ][ 'alignx' ]
target_text.par.aligny = text_top_dictionary[ top_preset ][ 'text_top' ][ 'aligny' ]
target_text.par.fontcolorr = text_top_dictionary[ top_preset ][ 'text_top' ][ 'fontcolorr' ]
target_text.par.fontcolorg = text_top_dictionary[ top_preset ][ 'text_top' ][ 'fontcolorg' ]
target_text.par.fontcolorb = text_top_dictionary[ top_preset ][ 'text_top' ][ 'fontcolorb' ]
target_text.par.fontalpha = text_top_dictionary[ top_preset ][ 'text_top' ][ 'fontalpha' ]
target_text.par.bgcolorr = text_top_dictionary[ top_preset ][ 'text_top' ][ 'bgcolorr' ]
target_text.par.bgcolorg = text_top_dictionary[ top_preset ][ 'text_top' ][ 'bgcolorg' ]
target_text.par.bgcolorb = text_top_dictionary[ top_preset ][ 'text_top' ][ 'bgcolorb' ]
target_text.par.bgalpha = text_top_dictionary[ top_preset ][ 'text_top' ][ 'bgalpha' ]
target_level.par.invert = text_top_dictionary[ top_preset ][ 'level_top' ][ 'invert' ]