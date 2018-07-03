tip_input = raw_input('How much was your tip?')
tip = float(tip_input)

bill_input = raw_input('How much was your bill?')
bill = float(bill_input)

tip_ratio = tip/bill
    if tip_ratio < 0.10:
        print 'That was stingy!'
    elif tip_ratio <= 0.20:
        print 'That was generous!'
    else:
        print 'That was average'
