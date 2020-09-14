import random

run_game()

def get_random_word():
    movie_list = []

    with open("short movie list.txt", "r") as f:
        index = 0
        for line in f:
            if line != "\n":
                movie_list.append(line)
                index += 1

    random_word = movie_list[random.randint(0, index)].rstrip()

    return random_word

def update_visible_string(current_string, answer_string, letter):
    updated_string = ""

    index = 0
    while index < len(answer_string):
        if answer_string[index] == letter:
            updated_string = updated_string + letter + " "
        else:
            updated_string = updated_string + current_string[index:index + 2]
        index += 2

    return updated_string

def sortString(s):
    alpha_sort = sorted(s)
    new_s = ""

    for char in alpha_sort:
        new_s += char

    return new_s

def run_game():
    secret_word = get_random_word().upper()
    visible_string = ""
    answer_string = ""

    #fill out visible string and answer string
    for letter in secret_word:
        if letter.isspace():
            visible_string = visible_string + "  "
            answer_string = answer_string + "  "
        elif letter.isalpha() or letter.isdigit():
            visible_string = visible_string + "_ "
            answer_string = answer_string + letter + " "
        else:
            visible_string = visible_string + letter + " "
            answer_string = answer_string + letter + " "

    print("Welcome to the Hangman Guessing Game! \n\nTry to guess our secret word below.")
    print("At any point, you may guess the whole phrase if you would like.")

    won_game = False
    strikes_allowed = 6
    wrong_guesses = 0
    letters_guessed = ""

    while strikes_allowed - wrong_guesses > 0 and not(won_game):
        print(visible_string)
        print(f"\nYou have {strikes_allowed - wrong_guesses} strikes left.")

        must_guess = True
        while must_guess:
            print("Letters Guessed: " + letters_guessed)
            user_guess = input("What single letter (or number) would you like to guess? ").upper()

            #user has guessed the whole word
            if secret_word == user_guess:
                won_game = True
                must_guess = False

            #user already guessed that letter
            elif len(user_guess) == 1 and letters_guessed.find(user_guess) != -1:
                    print("\nYou have already guessed the letter.")

            #valid user guess
            elif len(user_guess) == 1:
                letters_guessed = sortString(letters_guessed + user_guess)
                must_guess = False

            #two many letters guessed, possibly by accident
            else:
                    print("\nYou have guessed too many letters that don't match the secret phrase.")
                    if len(user_guess) > 2:
                        wrong_guesses += 1
                        print(f"\nYou have {strikes_allowed - wrong_guesses} strikes left.")

        #user guess is correct
        if secret_word.find(user_guess) != -1:
            print("\nCorrect! ")
            visible_string = update_visible_string(visible_string, answer_string, user_guess)

            #game has been won after no empty spaces present
            if visible_string.find("_") == -1:
                won_game = True

        else:
            print("\nSorry! The letter \"" + user_guess + "\" does not match.")
            wrong_guesses += 1

    #strikes match max strikes or game has been won
    if won_game:
        print(f"\nCongratulations!\nYou guessed \"{secret_word}\" with {strikes_allowed - wrong_guesses} strikes remaining!")
    else:
        print(f"\nToo bad! The word was {secret_word}. Please try again.")
