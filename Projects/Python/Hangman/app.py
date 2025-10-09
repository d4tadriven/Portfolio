
import random

words = ["python", "java", "lua", "kotlin", "swift"] # words

chosen_word = random.choice(words) # Random word
word_display = ["_" for _ in chosen_word] # Replace letters by underscores (_)
totalAttempts = 8
attempts = totalAttempts # amount of attempts

print("Welcome to Hangman!")

while attempts > 0 and "_" in word_display:
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        attempts -= 1
        print(f"That letter doesn't appear in the word. Try again.\nYou have {str(attempts)} attempts left.")

# end
if attempts <= 0:
    print(f"The word was {chosen_word}. You didn't guess it loser!")

if "_" not in word_display:
    attempts = totalAttempts - attempts
    print(f"The word was {chosen_word}! You only made {str(attempts)} mistakes! You rock!")