print("Welcome to Python Pizza Delivery")
size = input('What size pizza do you want? S, M, L:')
pepperoni = input('Do you want pepperoni on your pizza? Y or N:')
extra_cheese = input('Do you want extra cheese? Y or N:')

bill = 0

S = 15
M = 20
L = 25

P_s = 2
P_M_l = 3

Ex_Cheese = 1

if (size == 'S' or size == 's'):
    bill += S
elif (size == 'M' or size == 'm'):
    bill += M
elif(size == 'L' or size == 'l'):
    bill += L
if(pepperoni == 'Y' or pepperoni == 'y' and size == 's' or size =='S'):
    bill += P_s
elif(pepperoni == 'Y' or pepperoni == 'y'):
    bill += P_M_l
elif(pepperoni == 'n' or pepperoni == 'N'):
    bill == bill
if(extra_cheese == 'y' or extra_cheese == 'Y'):
    bill += Ex_Cheese
    print('Your total is:$',bill)
else:
    print('Your total is:$',bill)
