import random
sum=0
while True:
    randomNumber = random.randint(10, 30)
    sum += randomNumber
    if randomNumber == 15 or randomNumber == 25:
        break  
    

print(sum)
        