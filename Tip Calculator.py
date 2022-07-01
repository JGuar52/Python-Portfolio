print('To begin, first enter the subtotal bill amount:')
subtotal = float(input('$'))

print('Next, what % tip would you like to add?')
tip = int(input('%'))
tip_adjusted = (tip * .01 + 1)

print('Finally, how many people will be splitting this bill?')
group = int(input(''))

tip_per = (subtotal * (tip * .01) / group)
tip_total = (tip_per * group)
per_total = (subtotal / group + tip_per)
final_total = (subtotal + tip_total)


print(f"Total tip: ${tip_total:.2f}")
print(f"Tip per person: ${tip_per:.2f}")
print(f"Each person should pay: ${per_total:.2f}")
print(f"Final bill: ${final_total:.2f}")
