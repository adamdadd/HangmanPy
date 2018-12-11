import string


def word_processing(secret_word: type(string), letter: type(string), hashed: type(list)):
    secret_letters = list(secret_word)
    index = 0
    for l in secret_letters:
        if letter == l:
            hashed[index] = l
        index += 1
    print(hashed)


def screen_change():
    for x in range(1000):
        print("X")


def letter_guess(secret_word: type(string), hashed: type(list)):
    print("Let's Play, Give to PLayer 2................")
    guess = input("Guess a letter: ")
    if guess == "exit":
        print("The word was", secret_word)
        exit(0)
    else:
        word_processing(secret_word, guess, hashed)


def main():
    secret_word = input("Player 1: Enter secret word: ")
    hashed = []
    for i in range(len(secret_word)):
        hashed.append('#')
    screen_change()
    for n in range(10):
        letter_guess(secret_word, hashed)


main()
