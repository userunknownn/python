import random

def guess(x):
    random_number = random.randint(1 , x)
    guess         = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))

        if guess > random_number:
            print("Your guess is bigger than the number")
        elif guess < random_number:
            print("Your guess is smaller than the number")
        else:
            print("Your guess is right, the number is : ", guess)


print("The game will be like this ")
print("there will be two numbers, the first one is the lower limit, ")
print("that will always be 1, and the second is the upper limit")
print("that will define the range of the game, the upper limit has to be bigger than 1")

ok = False
while ok is not True:
    x = int(input("Choose a number to be the upper limit on the game : "))

    if x > 1:
        ok = True
    elif x < 1:
        print(f"""That number can't be the upper limit, because\
        {x} is lesser than 1 """)
    else:
        print("""The upper limit can't be the same number as the lower limit !""")

guess(x)
