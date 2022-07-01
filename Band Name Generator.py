print('Welcome to the Band Name Generator!')

city = input('What city did you grow up in? ')

petname = input('What was the name of your first pet? ')

city_a = (len(city))

petname_a = (len(petname))

part1 = int(city_a / 2)

part2 = int(petname_a / 2)

print('Your band name is ' + (city [:part1]) + (petname [part2:]) + '!')
