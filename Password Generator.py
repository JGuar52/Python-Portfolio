#Password Generator Project
import secrets

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(
    "Note: it is recommended to use at least 12 characters, with at least one symbol, one number, one uppercase letter and one lowercase."
)
input_letters = int(input("\nHow many letters would you like in your password?\n"))
input_numbers = int(input("How many numbers?\n"))
input_symbols = int(input("How many symbols?\n"))

chars = input_letters + input_numbers + input_symbols
pre_pass = ""
#each function randomly selects user-defined number of characters from designated list, and assigns them to pre_pass
for L in range(1, input_letters + 1):
    Lrand = secrets.choice(letters)
    pre_pass += Lrand

for N in range(1, input_numbers + 1):
    Nrand = secrets.choice(numbers)
    pre_pass += Nrand

for S in range(1, input_symbols + 1):
    Srand = secrets.choice(symbols)
    pre_pass += Srand

#now pre_pass needs to be scrambled, with password being the final output
password = ""
for output in range(1, chars + 1):
    randomizer = secrets.choice(pre_pass)
    password += randomizer
    #**
    pre_pass = pre_pass.replace(randomizer, '', 1)
    #** after each iteration, the previously-selected character "randomizer" chose from pre_pass needs to be removed as not to create duplicates when randomly selecting the next character from pre_pass
print(f"\nYour {chars}-character password is: {password}\n")
