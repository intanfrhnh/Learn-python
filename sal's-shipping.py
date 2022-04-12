#input the weight in lb(pound) to check
weight = float(input('Weight of your item in lb: '))
print('-------------------------------------------------------')
cost = 0
coption = ''
#flat charge
fc = 20

#cost of drone shipping
dscost = 0

#cost of premium ground shipping
pgcost = 125

#Ground shipping
if weight < 2:
  cost = weight*1.5 + fc

elif weight <= 6 :
  cost = weight*3 + fc

elif weight <= 10:
  cost = weight*4 + fc

else:
  cost = weight*4.75 + fc

#Drone Shipping
if weight < 2:
  dscost = weight*4.5

elif weight <= 6 :
  dscost = weight*9 

elif weight <= 10:
  dscost = weight*12 

else:
  dscost = weight*14.25

#checking cheapest option
if cost < dscost and cost < pgcost:
  coption = 'Ground Shipping'

elif dscost<cost and dscost < pgcost:
  coption = 'Premium Ground Shipping'

else:
  coption = 'Drone Shipping'

#print receipt
print('Weight : {}lb'.format(weight))
print('Ground Shipping Cost : ${}'.format(cost))
print('Premium Ground Shipping Cost : ${}'.format(pgcost))
print('Drone Shipping Cost : ${}'.format(dscost))
print('\nCheapest option : {}'.format(coption))
