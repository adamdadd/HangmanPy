import string


def word_processing(secret_word: type(string), letter: type(string), hashed: type(list), loss: type(int)):
    secret_letters = list(secret_word)
    pure_hash = hashed.copy()
    index = 0
    for l in secret_letters:
        if letter == l:
            print(loss)
            hashed[index] = l
            print("                                         You chose wisely!\n")
            print('                                     The word to guess: ' + ''.join(hashed))
            losing = loss - 1
            return losing
        index += 1
    if hashed == pure_hash:
            print("                                          You chose poorly\n")
            print('                                     The word to guess: ' + ''.join(hashed))


def screen_change():
    for x in range(1000):
        print("*********************8*******************8******************8************************8**************"
              "*****")
    print("********************(XX)****************(XX)***************(XX)*********************(XX)************"
          "*****")
    print("*******************--||--**************--||--*************--||--*******************--||--***********"
          "*****")
    print("********************/***\\***************/**\\***************/**\\*********************/**\\************"
          "*****")
    print("*******************/*****\\*************/****\\*************/****\\*******************/****\\***********"
          "*****")


def letter_guess(secret_word: type(string), hashed: type(list), alphabet: type(list), loss: type(int), the_hang_man: type(list)):
    print("\nPLayer 2...............................................................................................")
    print("Choices: " + ''.join(alphabet))
    guess = input("Guess a letter: ")
    if guess == "exit":
        print("****************************       The word was " + secret_word + "    *******************************")
        exit(0)
    else:
        alphabet.remove(guess + ' ')
        word_processing(secret_word, guess, hashed, loss)
        print("\n" + the_hang_man[loss] + "\n")


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
     "|____"]
    print(title)
    secret_word = input("Player 1: Enter secret word: ")
    alphabet = ['a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ',
                'n ', 'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 'y ', 'z ']
    hashed = []
    for i in range(len(secret_word)):
        hashed.append('?')
    screen_change()
    print(title)
    while ''.join(hashed) != secret_word:
        if len(alphabet) > 16:
            loss = 27 - len(alphabet)       # TODO: fix bug each move is a loss
            letter_guess(secret_word, hashed, alphabet, loss, the_hang_man)
        else:
            break
    if ''.join(hashed) == secret_word:
        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    WINNER !!!    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return 0
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    GAME OVER    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return 0


if __name__ == "__main__":
    main()

