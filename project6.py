import random as rndm

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
a = []
print("welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in you password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_number = int(input(f"How many number would you like?\n"))
for k in range (1,4,1):
    for i in range(0,nr_letters,1):
        z = rndm.choice(letters)
        password.append(z)
    for j in range(0,nr_symbols,1):
        q = rndm.choice(number)
        password.append(q)
    for x in range(0,nr_number,1):
        e = rndm.choice(symbols)
        password.append(e)
    break

print(''.join(password))
