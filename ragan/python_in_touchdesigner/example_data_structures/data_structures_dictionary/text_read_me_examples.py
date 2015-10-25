grocery_list_org = [ 'eggs' , 'milk' , 'bread' , 'butter' , 'coffee' ]

print( "This is our original List" )
print( grocery_list_org )

grocery_list_list = [ 
    ['eggs' , '1 dozen' ] , 
    ['milk' , '1 pint' ] , 
    ['bread' , '2 loaves' ] , 
    ['butter' , '1 lb' ] , 
    ['coffee', '2 lbs' ]
]

print( '\n' )
print( "This is our list of lists" )
print( grocery_list_list )

grocery_list_dictionary = {
    'eggs' : '1 dozen' , 
    'milk' : '1 pint' , 
    'bread' : '2 loaves' , 
    'butter' : '1 lb' , 
    'coffee': '2 lbs'
}

print( '\n' )
print( "This is our dictionary" )
print( grocery_list_dictionary )

print( '\n' )
print( "Let's retrieve all of our values:" )
print( grocery_list_dictionary[ 'eggs' ] )
print( grocery_list_dictionary[ 'milk' ] )
print( grocery_list_dictionary[ 'bread' ] )
print( grocery_list_dictionary[ 'butter' ] )
print( grocery_list_dictionary[ 'coffee' ] )

print( '\n' )
print( "Let's imagine we want both the key and the values:" )
print( 'eggs' , grocery_list_dictionary[ 'eggs' ] )
print( 'milk' , grocery_list_dictionary[ 'milk' ] )
print( 'bread' , grocery_list_dictionary[ 'bread' ] )
print( 'butter' , grocery_list_dictionary[ 'butter' ] )
print( 'coffee' , grocery_list_dictionary[ 'coffee' ] )