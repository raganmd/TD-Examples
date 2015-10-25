my_dictionary_of_dictionaries = { 
	"apple" : {
		"quantity" : 10 ,
		"origin" : "Vermont" ,
		"organic" : True	
	} , 
	"orange" : {
		"quantity" : 20 ,
		"origin" : "California" ,
		"organic" : False
	} , 
	"kiwi" : {
		"quantity" : 26 ,
		"origin" : "Mexico" ,
		"organic" : False
	} , 
	"grapes" : {
		"quantity" : 50 ,
		"origin" : "Peru" ,
		"organic" : True
	}
}

print( my_dictionary_of_dictionaries.keys() )
print( my_dictionary_of_dictionaries.values() )

print( '\n' )
print( "Let's just look at apple" )
print( "quanitity -" , my_dictionary_of_dictionaries[ 'apple' ][ 'quantity' ] )
print( "origin -" , my_dictionary_of_dictionaries[ 'apple' ][ 'origin' ] )
print( "organic -" , my_dictionary_of_dictionaries[ 'apple' ][ 'organic' ] )

print( '\n' )
print( "Okay, what about Orange" )
print( "quanitity -" , my_dictionary_of_dictionaries[ 'orange' ][ 'quantity' ] )
print( "origin -" , my_dictionary_of_dictionaries[ 'orange' ][ 'origin' ] )
print( "organic -" , my_dictionary_of_dictionaries[ 'orange' ][ 'organic' ] )

print( '\n' )
print( "Then there's kiwi too..." )
print( "quanitity -" , my_dictionary_of_dictionaries[ 'kiwi' ][ 'quantity' ] )
print( "origin -" , my_dictionary_of_dictionaries[ 'kiwi' ][ 'origin' ] )
print( "organic -" , my_dictionary_of_dictionaries[ 'kiwi' ][ 'organic' ] )

print( '\n' )
print( "and we can't forget about grapes." )
print( "quanitity -" , my_dictionary_of_dictionaries[ 'grapes' ][ 'quantity' ] )
print( "origin -" , my_dictionary_of_dictionaries[ 'grapes' ][ 'origin' ] )
print( "organic -" , my_dictionary_of_dictionaries[ 'grapes' ][ 'organic' ] )