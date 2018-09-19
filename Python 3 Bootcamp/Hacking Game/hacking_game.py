"""Quick project to recreate the hacking game from the Fallout series, 
roughly 2hr work. First experiment with calling data from external files and manipulating it."""
# Importing words in to module
import random
GAME_STATE = True


def difficulty_selector(no_words_ranges, no_letters_ranges):
    """Function to determine the ranges for selecting the number of words and letters"""
    while GAME_STATE is True:
        difficulty = int(input("Please enter a number for difficulty level - 1 being very easy, 5 being very hard: "))
        if difficulty > 5:
            print("Please enter a number that is between 1-5.")
            continue
        else:
            break

    if difficulty == 1:
        no_words_ranges = (5, 8)
        no_letters_ranges = (4, 8)
    else:
        no_words_ranges = (difficulty*2+2, difficulty*2+5)
        no_letters_ranges = (difficulty*2+1, difficulty*2+5)
        print(no_letters_ranges)

    return no_words_ranges,no_letters_ranges


def words_letters_selector(no_words_ranges, no_letters_ranges):
    """Function to determine the number of words and letters to select"""
    no_words = random.randint(no_words_ranges[0], no_words_ranges[1])
    no_letters = random.randint(no_letters_ranges[0], no_letters_ranges[1])

    return no_words, no_letters


def hacker_game():
    """Function that determines the body of the game"""
    print("Welcome. From the list of words below you will need to figure out which has been randomly chosen as the password. After typing in a word you will be told how many letters that are in the same position as those in the password match. You have 4 attempts. Good luck!\n")
    word_list = []
    password_list = []
    guess_counter = 0
    no_words_ranges = (0, 0)
    no_letters_ranges = (0, 0)
    words = open("enable1.txt", "r")
    no_words_ranges, no_letters_ranges = difficulty_selector(no_words_ranges, no_letters_ranges)
    no_words, no_letters = words_letters_selector(no_words_ranges, no_letters_ranges)
    for word in words:
        if len(word) == no_letters:
            word_list.append(word)

    password = word_list[random.randint(0, len(word_list))]

    # Ensuring that 4 of the words match the password
    while len(password_list) != 4:
        matching_letters = 0
        word_to_add = word_list[random.randint(0, len(word_list))]
        for n in range(0, len(word_to_add)):
            if word_to_add[n] == password[n]:
                matching_letters += 1
        if matching_letters >= 4:
            if word_to_add != password:
                password_list.append(str(word_to_add))

    # Adding the password to the list
    password_list.append(password)

    # Adding red herrings to the list
    while len(password_list) is not no_words:
        word_to_add = word_list[random.randint(0, len(word_list))]
        if word_to_add not in password_list:
            password_list.append(word_to_add)

    random.shuffle(password_list)

    for word in password_list:
        print(word.upper())

    for i in range(0,4):
        guess = str(input(f"What is your guess? You have {4-guess_counter} tries remaining. ")).lower()
        matching_letters = 0
        if str(guess)+"\n" == str(password):
            play_again = input("Congratulations! You guessed the word. Would you like to play again? ").lower()
            if play_again == "yes":
                hacker_game()
            else:
                exit()

        for n in range(0, len(guess)):
            if guess[n] == password[n]:
                matching_letters += 1
        guess_counter += 1
        print(f'You got {matching_letters}/{len(password)-1} letters right.')
        if guess_counter == 4:
            play_again = input("Out of tries! Would you like to play again? ").lower()
            if play_again == "yes":
                hacker_game()
            else:
                exit()


hacker_game()
