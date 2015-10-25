top_dictionary = { 
	"preset1" : {
		"text" : 'monkey' , 
		"fontsizex" : 15 ,
		"alignx" : 1 ,
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
	"preset2" : {
		"text" : 'pig' , 
		"fontsizex" : 80 ,
		"alignx" : 1 ,
		"aligny" : 0 ,
		"fontcolorr" : 0.0 ,
		"fontcolorg" : 0.0 ,
		"fontcolorb" : 1.0 ,
		"fontalpha" : 1.0 ,
		"bgcolorr" : 1.0 ,
		"bgcolorg" : 1.0 ,
		"bgcolorb" : 1.0 ,
		"bgalpha" : 1.0
	}
}

target_text = op( 'text1' )
dictionary_preset = 'preset2'

target_text.par.text = top_dictionary[ dictionary_preset ][ 'text' ]
target_text.par.fontsizex = top_dictionary[ dictionary_preset ][ 'fontsizex' ]
target_text.par.alignx = top_dictionary[ dictionary_preset ][ 'alignx' ]
target_text.par.aligny = top_dictionary[ dictionary_preset ][ 'aligny' ]
target_text.par.fontcolorr = top_dictionary[ dictionary_preset ][ 'fontcolorr' ]
target_text.par.fontcolorg = top_dictionary[ dictionary_preset ][ 'fontcolorg' ]
target_text.par.fontcolorb = top_dictionary[ dictionary_preset ][ 'fontcolorb' ]
target_text.par.fontalpha = top_dictionary[ dictionary_preset ][ 'fontalpha' ]
target_text.par.bgcolorr = top_dictionary[ dictionary_preset ][ 'bgcolorr' ]
target_text.par.bgcolorg = top_dictionary[ dictionary_preset ][ 'bgcolorg' ]
target_text.par.bgcolorb = top_dictionary[ dictionary_preset ][ 'bgcolorb' ]
target_text.par.bgalpha = top_dictionary[ dictionary_preset ][ 'bgalpha' ]