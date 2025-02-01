import random
def g():
    print("Как тебя зовут?")
    name = input()
    number_to_guess = random.randint(1, 20)
    print(name, "я загадал число от 1 до 20.")
    print("Попробуй угадать.")
    guesses_taken = 0
    while True:
        guess = int(input())
        guesses_taken += 1
        if guess < number_to_guess:
            print("Твое число слишком маленькое.")
        elif guess > number_to_guess:
            print("Твое число слишком большое.")
        else:
            print(name,"Ты угадал мое число за",guesses_taken,"попыток!")
            break 
g()
