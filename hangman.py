import string
import random
import time


def word_processing(secret_word: type(string), alphabet: type(list), letter: type(string), hashed: type(list), losing: type(int), man: type(list)):
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
            print('                                  The word to guess: ' + ''.join(hashed))
    else:
        print("                                         You chose wisely!\nlives", str(10 - losing) + man[losing])
        time.sleep(1)
        print('                                      The word to guess: ' + ''.join(hashed))


def screen_change():
    loading = "To The Gallows"
    for i in range(100):
        loading += '*'
        print(loading)
        time.sleep(0.1)
    for x in range(1000):
        print("*********************&*******************&******************&************************&**************"
              "*****")
    time.sleep(2)
    print("********************(XX)****************(XX)***************(XX)*********************(XX)************"
          "*****")
    print("*********************&&******************&&*****************&&***********************&&*************"
          "*****")
    print("********************/||\\****************/||\\***************/||\\*********************/||\\***********"
          "*****")
    print("********************/**\\****************/**\\***************/**\\*********************/**\\************"
          "*****")
    print("*******************/****\\**************/****\\*************/****\\*******************/****\\***********"
          "*****")


def letter_guess(secret_word: type(string), hashed: type(list), alphabet: type(list), losses: type(int), the_hang_man: type(list)):
    print("\nYour Turn ..............................................................................................")
    print("Choices: " + ''.join(alphabet))
    guess = input("Guess a letter: ")
    if guess.isupper():
        guess = guess.lower()
    elif guess == "exit":
        print("****************************       The word was " + secret_word + "    *******************************")
        exit(0)
    word_processing(secret_word, alphabet, guess, hashed, losses, the_hang_man)


def main():
    title = "********************************************    HANGMAN    **********************************************"
    the_hang_man = \
    ["-------------"
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
    # Get some words from a word file...
    with open('wordlist.txt') as word_list:
        valid_words = list(word_list.read().split('\n'))

    secret_word = random.choice(valid_words) #input("Player 1: Enter secret word: ")
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
        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    WINNER !!!    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return 0
    else:
        print("****************************       The word was " + secret_word + "    *******************************")
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    GAME OVER    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    play2 = input('Play Again (y/n): ')
    if play2 == 'y':
        main()
    else:
        return 0


if __name__ == "__main__":
    main()

