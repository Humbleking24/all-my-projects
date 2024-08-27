print('Welcom to the tip calculator!')
bill = float(input("What was the total bill? "))
tip_percent = int(input('How much tip would you like to give? 10,12, or 15?'))
split_people = int(input('How many people to split the bill'))

new_bill = (bill * (tip_percent/100)) + bill
split_bill = new_bill/split_people


print("Each person should pay:", round(split_bill, 2))