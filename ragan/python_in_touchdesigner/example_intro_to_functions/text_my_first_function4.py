def tip_calculator( total , tip_percentage  ):

	tip = total * ( tip_percentage / 100 )
	total_bill = total + tip

	return tip , total_bill

print( tip_calculator( 50 , 15 ) )