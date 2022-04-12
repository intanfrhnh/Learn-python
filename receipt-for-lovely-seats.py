#Lovely loveseat Catalog
## Lovely loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00

## Stylish Settee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price = 180.50

##Luxurious lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

#tax
sales_tax = 0.088

#First customer initial amount
customer_one_total = 0

#customer one itemization
customer_one_itemization = ""

#the first customer bought lovely loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

#the first customer add luxurious lamp into the purchase
customer_one_total += luxurious_lamp_price
customer_one_itemization += "\n" + luxurious_lamp_description

#adding tax to the total
customer_one_tax = customer_one_total*sales_tax

#total for first customer
customer_one_total += customer_one_tax

#Printing receipt
print("Customer One Items:")
print(customer_one_itemization)
print('\nCustomer One Total:')
print(customer_one_total)


