def kinetic_energy(weight, speed):
  # Convert speed from km/h to m/s
  speed_in_m_per_s = speed / 3.6
  return 0.5 * weight * speed_in_m_per_s**2

def joules_to_newtons(joules, distance):
  return joules / distance

# Get weight and speed of first car at impact from user input
weight1 = float(input('Enter the weight of the first car at impact in kilograms: '))
speed1 = float(input('Enter the speed of the first car at impact in km/h: '))

# Calculate the kinetic energy of the first car at impact
ke1 = kinetic_energy(weight1, speed1)

# Get weight and speed of second car at impact from user input
weight2 = float(input('Enter the weight of the second car at impact in kilograms: '))
speed2 = float(input('Enter the speed of the second car at impact in km/h: '))

# Calculate the kinetic energy of the second car at impact
ke2 = kinetic_energy(weight2, speed2)

# Calculate and print the total kinetic energy of the car accident on impact
total_ke = ke1 + ke2

# Convert the total kinetic energy to newtons
distance = float(input('Enter the distance over which the force was applied in meters: '))
newtons = joules_to_newtons(total_ke, distance)
print(f'The total kinetic energy of the car accident on impact is {newtons} newtons')

# Calculate and print the mass that would feel like being pressed with the same force
mass = newtons / 9.81
print(f'It would feel like being pressed with a mass of {mass:.2f} kilograms')
