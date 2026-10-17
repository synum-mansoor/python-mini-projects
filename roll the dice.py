import random

while True:
    option = input("Roll th Dice? (y/n):").lower()
    if option == 'y':
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print(f'({d1},{d2})')
    elif option == 'n':
        print("Better luck next time")
        break
    else:
        print("Invalid")
    
          
