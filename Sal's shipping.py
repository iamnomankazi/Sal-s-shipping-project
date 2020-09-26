# Write a program that asks the user for the weight of their package and 
# then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

# All the charges are in USD.
# All the weights are in lb(pound).


# Ground Shipping Charges
ground_charge_1 = 1.50
ground_charge_2 = 3.0
ground_charge_3 = 4.0
ground_charge_4 = 4.75

# Premium Ground Shipping Charges
premium_ground_charge = 125.0

# Drone Shipping Charges
drone_charge_1 = 4.50
drone_charge_2 = 9.0
drone_charge_3 = 12.0
drone_charge_4 = 14.25



# Calculate Ground Shipping
def ground_shipping(weight):
  cost1 = (weight * ground_charge_1) + 20
  cost2 = (weight * ground_charge_2) + 20
  cost3 = (weight * ground_charge_3) + 20
  cost4 = (weight * ground_charge_4) + 20
  
  if weight <= 2:
    return cost1
  elif 2 < weight <= 6:
    return cost2
  elif 6 < weight <= 10:
    return cost3
  else:
    return cost4 #over 10 lb

# print("Your ground shipping charge is: " + str(ground_shipping(8.4)) + " USD")



# Premium Ground Shipping
premium_ground_shipping_charge = 125



# Calculate Drone Shipping
def drone_shipping(weight):
  cost1 = (weight * drone_charge_1) #since its flat charge is $0.0 we don't need to add this in our code.
  cost2 = (weight * drone_charge_2)
  cost3 = (weight * drone_charge_3)
  cost4 = (weight * drone_charge_4)

  if weight <= 2:
    return cost1
  elif 2 < weight <= 6:
    return cost2
  elif 6 < weight <= 10:
    return cost3
  else:
    return cost4

# print("Your Drone shipping charge is: " + str(drone_shipping(1.5)) + " USD")


# Which shipping service is cheapest ?
# How much it would cost to ship a package of said weight using this service ?
def cheapest_shipping_service(weight):
  ground_shipping_charge = ground_shipping(weight)
  drone_shipping_charge =  drone_shipping(weight)

  if ground_shipping_charge < drone_shipping_charge and ground_shipping_charge < premium_ground_shipping_charge:
    return "The cheapest shipping service is Ground Shipping Service. " + "It costs " + str(ground_shipping_charge)
  elif drone_shipping_charge < ground_shipping_charge and drone_shipping_charge < premium_ground_shipping_charge:
    return "The cheapest shipping service is Drone Shipping Service. " + "It costs " + str(drone_shipping_charge)
  else:
    return "The cheapest shipping service is Premium Ground Shipping Service. " + "It costs " + str(premium_ground_shipping_charge)

# What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

# What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

# So Let's check it out where our code is works or not.

print(cheapest_shipping_service(4.8))
print(cheapest_shipping_service(41.5))

