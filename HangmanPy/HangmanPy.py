#!/use/bin/env python3
import random
import time


def word_processing(secret_word, alphabet, letter, hashed, losing, man):
    """Handling of word arrays. hashing, validation and removing.

    Args: 
        secret_word (str): The word to be guessed,
        alphabet (str): The remaining letters of the alphabet available to gusess,
        letter (char): The selected letter of the alphabet,
        hashed (list): List of hashes with size equal to alphabet,
        losing (int): Count of failed attempts,
        man (int): Pleyer.
    """
    secret_letters = list(secret_word)
    pure_hash = hashed.copy()           # Value of hashed saved going into function
    index = 0
    for l in secret_letters:
        if letter == l:
            hashed[index] = l
        index += 1
    if hashed == pure_hash:
        try:
            alphabet.remove(letter + ' ')
        except ValueError:
            print("\nInsanity: 'Repeating the same actions and expecting a different result'\n")
            time.sleep(1)
        else:
            losing += 1
            print("                                     You chose poorly\nlives", str(10 - losing) + man[losing])
            time.sleep(1)
            print('                                     The word to guess: ' + ''.join(hashed))
    else:
        try:
            alphabet.remove(letter + ' ')
        except ValueError:
            print("\n                        Insanity: 'Repeating the same actions and expecting a different result'\n")
        else:
            alphabet.append(' ')
            print("                                         You chose wisely!\nlives", str(10 - losing) + man[losing])
            time.sleep(1)
            print('                                         The word to guess: ' + ''.join(hashed))


def screen_change():
    """A intro screen.
    """
    loading = "To The Gallows"
    for i in range(91):
        loading += '*'
        print(loading)
        time.sleep(0.01)
    for x in range(1000):
        print("*********************&*******************&******************&************************&**************"
              "*****")
    time.sleep(1)
    print("********************(XX)****************(XX)***************(XX)*********************(XX)************"
          "*****")
    print("*********************&&******************&&*****************&&***********************&&*************"
          "*****")
    print("********************/||\\****************/||\\***************/||\\*********************/||\\************"
          "*****")
    print("********************/**\\****************/**\\***************/**\\*********************/**\\************"
          "*****")
    print("*******************/****\\**************/****\\*************/****\\*******************/****\\***********"
          "*****")


def letter_guess(secret_word, hashed, alphabet, losses, the_hang_man):
    """Letter selection function.

    Args:
        secret_word (str): The word required for success.
        hashed (str): Hashes representing the word.
        alphabet (str): Full list of available letters.
        losses (int): Number of incorrect attempts so far.
        the_hang_man ()
    """
    print("\nYour Turn ...............................................................................................")
    print("Choices: " + ''.join(alphabet))
    guess = input("Guess a letter: ")
    if guess.isupper():
        guess = guess.lower()
    elif guess == "exit":
        print("\n**************************************     The word was " + secret_word + "    ***********************"
                                                                                           "******")
        exit(0)
    word_processing(secret_word, alphabet, guess, hashed, losses, the_hang_man)


def main():
    """Main run function. Used to start an instance of the game.

    Returns:
        1 : True
        0 : False
    """
    title = "********************************************    HANGMAN    **********************************************"
    the_hang_man = [
     "\n-------------"
     "\n|            |"
     "\n|            0"
     "\n|           /|\\"
     "\n|           / \\"
     "\n|____",
     "\n-------------"
     "\n|            |"
     "\n|            0"
     "\n|           /|\\"
     "\n|           / "
     "\n|____",
     "\n-------------"
     "\n|            |"
     "\n|            0"
     "\n|           /|\\"
     "\n|"
     "\n|____",
     "\n-------------"
     "\n|            |"
     "\n|            0"
     "\n|           /|"
     "\n|"
     "\n|____",
     "\n-------------"
     "\n|            |"
     "\n|            0"
     "\n|            |"
     "\n|"
     "\n|____",
     "\n-------------"
     "\n|            |"
     "\n|            0"
     "\n|"
     "\n|"
     "\n|____",
     "\n-------------"
     "\n|            |"
     "\n|"
     "\n|"
     "\n|"
     "\n|____",
     "\n-------------"
     "\n|"
     "\n|"
     "\n|"
     "\n|"
     "\n|____",
     "\n|"
     "\n|"
     "\n|"
     "\n|"
     "\n|____",
     "|____",
     ""]
    the_hang_man.reverse()
    print(title)
    play_choice = input("Is there an executioner with you? (y/n): ")

    if play_choice == 'n':    # Single-player Multi-player mode selection
        # Get some words from a word file...
        with open('./wordlist.txt') as word_list:
            valid_words = list(word_list.read().split('\n'))
        secret_word = random.choice(valid_words)
    elif play_choice == 'y':
        secret_message = input("Executioner. Enter the word and it shall be the key: ")
        secret_word = ''.join(c for c in secret_message if c.isalnum()).lower()  # removes spaces and special characters
    else:
        print("Invalid Selection, Defaulting to single-player mode...")
        # Get some words from a word file...
        with open('./wordlist.txt') as word_list:
            valid_words = list(word_list.read().split('\n'))
        secret_word = random.choice(valid_words)
        time.sleep(5)

    alphabet = ['a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ',
                'n ', 'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 'y ', 'z ']
    hashed = []
    for i in range(len(secret_word)):
        hashed.append('?')
    screen_change()
    print(title)
    while ''.join(hashed) != secret_word:
        loss = 26 - len(alphabet)
        if loss < 10:
            letter_guess(secret_word, hashed, alphabet, loss, the_hang_man)
        else:
            break
    if ''.join(hashed) == secret_word:
        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    WINNER !!!    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    else:
        print("\n**************************************     The word was " + secret_word + "    ***********************")
                                                                                           "******")
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    GAME OVER    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    play_again = input("Play Again (y/n): ")
    if play_again == 'y':
        main()
    else:
        return 0


if __name__ == "__main__":
    main()
