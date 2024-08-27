i = 0
for j in range(1,101):
    i = i + 1
    print (i)
    if(i % 3 == 0 and i % 5 == 0):
        print('FizzBuzz')
    elif(i % 5 == 0):
        print("Buzz")
    elif (i % 3 == 0):
        print('Fizz')
    elif(i == 100):
        break