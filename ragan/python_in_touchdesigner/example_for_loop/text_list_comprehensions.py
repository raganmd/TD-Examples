my_list = [ 10 , 4 , 6 , 20 ]

new_list1 = [ print( item ) for item in my_list ]

new_list2 = [ print( my_list.index( item ) ) for item in my_list ]

new_list3 = [ print( 'the index of this item is: ' + str( my_list.index( item ) ) , 'the acutal list item is: ' + str( item ) ) for item in my_list ]
