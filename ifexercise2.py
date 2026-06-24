weight = 41.5
flat_charge = 20
cost_premium_ground_shipping = 125

#Ground Shipping
if weight <= 2:
  cost = 1.5 * weight + flat_charge
  print(cost)
elif weight > 2 and weight <= 6:
  cost = 3 * weight + flat_charge
  print(cost)
elif weight > 6 and weight <= 10:
  cost = 4 * weight + flat_charge
  print(cost)
else:
  cost = 4.75 * weight + flat_charge
  print(cost)

#Ground Shipping Premium
if weight <= 2:
  cost = 1.5 * weight + flat_charge + cost_premium_ground_shipping
  print(cost)
elif weight > 2 and weight <= 6:
  cost = 3 * weight + flat_charge + cost_premium_ground_shipping
  print(cost)
elif weight > 6 and weight <= 10:
  cost = 4 * weight + flat_charge + cost_premium_ground_shipping
  print(cost)
else:
  cost = 4.75 * weight + flat_charge + cost_premium_ground_shipping
  print(cost)

#Drone Shipping
if weight <= 2:
  cost = 4.5 * weight
  print(cost)
elif weight > 2 and weight <= 6:
  cost = 9 * weight
  print(cost)
elif weight > 6 and weight <= 10:
  cost = 12 * weight
  print(cost)
else:
  cost = 14.25 * weight
  print(cost)
