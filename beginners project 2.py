import random

def fruits():
    fruits = ["banana", "apple", "rambutan", "blueberry", "jackfruit"]
    random.shuffle(fruits)
    return fruits

def monkey_encounter():
    correct_fruits = fruits()
    attempts = 3  
    while attempts > 0:
        user_fruits = input("Guess five fruits (no commas): ").split()
        if set(user_fruits) == set(correct_fruits):
            print("You've appeased the monkey! Keep going.")
            return True
        else:
            print(f"You're wrong! Try again. You have {attempts - 1} attempts left.")
            attempts -= 1
    print("You failed to appease the monkey. All hail the monkey. Game over.")
    return False

def tiger_crossing():
    height = int(input("How tall are you (in cm)?"))
    if height <= 160:
        print("You were too short to cross over (grow taller). Game over.")
    elif height > 180:
        print("The tiger spots you! (Too tall!) Game over.")
    else:
        print("You've made it across safely!")
        return True
    return False

def password_puzzle():
    password = str(random.randint(1000, 9999))
    attempts = 10
    while attempts > 0:
        guess = input("Guess the four-digit password: ")
        correct_digits = sum(c1 == c2 for c1, c2 in zip(password, guess))
        print(f"You have {correct_digits} correct digits. Attempts left: {attempts - 1}")
        if guess == password:
            print("You've unlocked the door!!1! You've found the treasure!!1!11!")
            return True
        attempts -= 1
    print("You used all your attempts. Game over.")
    return False

def main():
    print("Welcome to The Forest (UNLIKE the actual game). You will have to ")

    if monkey_encounter() and tiger_crossing() and password_puzzle():
        print("Congratulations! You've completed the treasure hunt. Now leave me a 5 star review!!")
    else:
        print("You didn't make it to the treasure. Womp womp and try again.")

if __name__ == "__main__":
    main()
