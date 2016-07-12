clear()
methods							= [
								"multi_by_two",
								"logic_test",
								"logic_test_two"
									]

doc_string_temp					= "mod( 'text_simple_reutrn' ).{target_function}.__doc__"



for method in methods:
	print( "The Doc Strings for {} are:".format( method ) )
	temp_doc 					= doc_string_temp.format( target_function = method )
	print( eval( temp_doc ) )
	print( "= "  * 10 )
