import random
print("#######################################")
print("##### Welcome to the Hangman Game! #####")
print("#######################################")
print("You have 10 attempts\n You lose 1 attempt if you guess a letter and 2 if you guess the whole word.")
print("Correct letter and word guesses do not consume attempts.")
print("Guess the word correctly to win!")

def draw_word():
    with open("words.txt", "r", encoding="utf-8") as word_list:
        words = word_list.readlines()
        random_word = random.choice(words).strip()
        return random_word

def game_data():
    secret_word = draw_word()
    correct_letters = ["_"] * len(secret_word)
    incorrect_letters = []
    remaining_attempts = 10
    guessed_letter = ""
    guessed_word = ""
    response = ""
    
    return secret_word, correct_letters, incorrect_letters, remaining_attempts, guessed_letter, guessed_word, response

def ask_to_guess(response):
    while True:
        response = input("Do you want to guess the word? Y/N ").strip().lower()
        
        if response == "y":
            return response
        elif response == "n":
            return response
        else:
            continue

def play_again(try_again, secret_word):
    while True:
        print(f"The word was {secret_word}!")
        print("Press Y to play again or N to quit.")
        try_again = input("Y/N ").lower().strip()
        if try_again == "y" or try_again == "n":
            return try_again
        else:
            print("Invalid response")
            continue

def validate_letter(letter):
    while True:
        letter = input("Enter a letter: ").lower().strip()
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input! Enter a single letter.")
            continue
        else:
            return letter

def guess_letter(word, correct_list, incorrect_list, attempts, letter):
    while True:
        letter = validate_letter(letter)
        
        if letter in correct_list or letter in incorrect_list:
            print(f"The letter {letter} has already been guessed. Try another one.")
            print(f"Current word: {' '.join(correct_list)}")
            print(f"Incorrect letters: {', '.join(incorrect_list)}")
            continue
            
        elif letter in word:
            print("The letter is in the word!")
            for index, word_letter in enumerate(word):
                if word_letter == letter:
                    correct_list[index] = letter
            print(f"Current word: {' '.join(correct_list)}")
                        
        else:
            attempts -= 1
            incorrect_list.append(letter)
            print(f"The letter {letter} is not in the secret word.")    
            print(f"Remaining attempts: {attempts}")
            print(f"Incorrect letters: {', '.join(incorrect_list)}")
        
        return attempts  

def guess_word(word, attempts, correct_list, incorrect_list, guess, letter, response):
    while guess != word:
        while True:
            if attempts <= 0:
                return False
            attempts = guess_letter(word, correct_list, incorrect_list, attempts, letter)
            response = ask_to_guess(response)
            if response == "y":
                guess = input("Enter your guess: ").lower().strip()
                if guess == word:
                    print("Congratulations! You won the Hangman game!")
                    print(f"Incorrect attempts before success: {abs(attempts - 10)}")
                    print("       ___________      ")
                    print("      '._==_==_=_.'     ")
                    print("      .-\\:      /-.    ")
                    print("     | (|:.     |) |    ")
                    print("      '-|:.     |-'     ")
                    print("        \\::.    /      ")
                    print("         '::. .'        ")
                    print("           ) (          ")
                    print("         _.' '._        ")
                    print("        '-------'       ")
                    return guess
                else:
                    attempts -= 2
                    print("Wrong guess!")
                    print(f"Remaining attempts: {attempts}")

            elif response == "n":
                print(f"Current word: {' '.join(correct_list)}")
                print(f"Incorrect letters: {', '.join(incorrect_list)}")

def game_system():
    while True:
        secret_word, correct_letters, incorrect_letters, remaining_attempts, guessed_letter, guessed_word, response = game_data()
        guess_word(secret_word, remaining_attempts, correct_letters, incorrect_letters, guessed_word, guessed_letter, response)
        return secret_word

def hangman_game():
    try_again = "y"
    while try_again != "n":             
        secret_word = game_system()
        try_again = play_again(try_again, secret_word)

hangman_game()
print("Thanks for playing!")

