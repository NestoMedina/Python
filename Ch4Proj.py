date = "Monday 2019-03-18"
time = "10:05:34 AM"
average_astronaut_mass_kg = 80.7
fuel_mass_kg = 760000
ship_mass_kg = 74842.31
fuel_level = 100

number_of_astronauts = input("Enter how many astronauts")
crew_status = input("Are you ready? Enter: 'Ready' or Not 'Ready'")

total_mass_of_crew = number_of_astronauts * average_astronaut_mass_kg
total_mass_of_ship = total_mass_of_crew + ship_mass_kg + fuel_mass_kg

print("Launch Checklist\n" + date + time + "\nShip Info")