from arepl_dump import dump

#1
adding_practice = [273.15]
adding_practice.append(42)
adding_practice.append("hello")
print(adding_practice)

#2
adding_practice = adding_practice + [False, -4.6, '87']
print(adding_practice)

#3
cargo_hold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']

cargo_hold[5] = 'space tether'
cargo_hold[0] = 'pop'
cargo_hold[-1] = 'pop'

print(cargo_hold)

#part 2

cargo_hold.insert(2, 'keys')

