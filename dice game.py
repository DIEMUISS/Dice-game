import random
while True:
    choice = input("Roll the dice(y/n): ").lower()
    if choice == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1, 6)
        print(f"(dice 1= {dice1},dice 2= {dice2})")

    elif choice == "n":
        print("Thanks for playing")
        break
    else:
        print("invalid input")
    try_again = input('Roll again:(y/n)')
    if try_again == 'y':
        continue
    else:
        print("Thanks for playing")
        break
