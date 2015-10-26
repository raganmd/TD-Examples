def tip_calculator( total , tip_percentage  ):

	tip = total * ( tip_percentage / 100 )
	total_bill = total + tip

	return tip , total_bill

def display_total( tip_and_total_bill ):

	dotted_line = '- ' * 10
	tip_text = "Your total tip is {}"
	total_bill_text = "Your total bill is {}"
	
	print( dotted_line )
	print( tip_text.format( tip_and_total_bill[ 0 ] ) )
	print( total_bill_text.format( tip_and_total_bill[ 1 ] ) )
	print( dotted_line )

	return

total = 100
tip_percentage = 20

print( tip_calculator( total , tip_percentage ) )

display_total( tip_calculator( total , tip_percentage ) )