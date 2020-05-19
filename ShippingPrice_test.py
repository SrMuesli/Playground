def ground_shipping(weight):
  if weight > 10:
    return (weight * 4.75) + 20.
  elif weight > 6 and weight <= 10:
    return (weight * 4.) + 20.
  elif weight > 2 and weight <= 6:
    return (weight * 3.) + 20.
  else:
    return (weight * 1.5) + 20.

def drone_shipping(weight):
  if weight > 10:
    return weight * 14.25
  elif weight > 6 and weight <= 10:
    return weight * 12.
  elif weight > 2 and weight <= 6:
    return weight * 9.
  else:
    return weight * 4.5
  
def shipping_cost(weight):
  drone = drone_shipping(weight)
  ground = ground_shipping(weight)
  premium = 125
  if drone < ground and drone < premium:
    return print("La forma mas barata es por dron, y cuesta: " + str(drone) + (" €."))
  elif ground < drone and ground < premium:
    return print("La forma mas barata es por tierra, y cuesta: " + str(ground) + (" €."))
  else:
    return print("La forma mas barata es envío premium por tierra, y cuesta: " + str(premium) + (" €."))

shipping_cost(50)
