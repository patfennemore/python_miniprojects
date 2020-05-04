
drive_distance = input("How many kilometres will you drive? ")
fuel_usage = input("How many litres per km does your car use? ")
price_fuel = input("What is the current price of fuel per litre? Amount and currency(eg. 10 USD) ")

split_currency_amount = price_fuel.split()

trip_cost = ((float(drive_distance)*float(fuel_usage))*float(split_currency_amount[0]))

print(str(trip_cost) + " " + split_currency_amount[1])
