import random

def randomword(word_list):
    return random.choice(word_list)

def get_user_input():

    while True:
        guess = input("Enter your 5-letter guess: ").lower()
        if len(guess) != 5:
            print("Enter a 5-letter word. Did you fail English?")
        elif not guess.isalpha():
            print("ONLY LETTERS!!!!!")
        else:
            return guess

def check_guess(guess, word):
    feedback = []
    for i in range(5):
        if guess[i] == word[i]:
            feedback.append("🟩")
        elif guess[i] in word:
            feedback.append("🟨")
        else:
            feedback.append("⬛️")
    return feedback

def play_wordle():
    print("Welcome to Wordle! You have 6 chances to guess a 5-letter word.")
    word_list = [
        "about", "above", "abuse", "acuse", "acred",
        "actor", "acute", "admit", "adopt", "adult","being","beans","brain","barns","count","craps","capes","crate","chair","chose","dying","death","dread","duffs","eager","elegy","elder","fruit","fried","great","grate","genie","gyatt","hyped","hides","issue","infra","jokes","joust","kench","knead","knees","loser","lists","maces","maker","macho","niece","needs","obese","oaken","older","prank","prats","pyros","quest","queue","roped","rolls","smart","start","tally","trade","unify","vague","valor","wired","water","xenox","xenyl","yours","yacht","yahoo","zooms","zombs"
    ]

    word = randomword(word_list)
    guesses = 0

    while guesses < 6:
        guess = get_user_input()
        feedback = check_guess(guess, word)
        print("".join(feedback))

        if feedback == ["🟩"] * 5:
            print("Congratulations! You guessed the word correctly. Now do it again >:(")
            return
        guesses += 1


    print("Skill issue. Try harder next time. The word was", word)

if __name__ == "__main__":
    play_wordle()
