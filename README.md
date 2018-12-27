# HangmanPy
![hangman.png](https://github.com/adamdadd/HangmanPy/blob/master/img/hangman.png)

## Overview
This is a command line hangman game written in only using "simple" python. 
A use of basic python functionality to create something fun and educational. 

I have not used any external libraries as this is a good way for beginners to better understand core python concepts.

## Requirements
For this you need  to have python 3.7 installed... and that's it!

You can check it's installed (on Unix) with:
```bash
$ python3 --version
```
or on windows:
```dos
> py3 --version
```
If you don't get a version number install python 3 to continue.

## Upcoming Features
    Ideas for additional features:
    - Strip spacecs and symbols from executioner message.
    - When quitting part way through a word it's saved and then loaded when re-entering the game.
    
The above features will be implemented and can be removed and changed as required from the HangmanPy.py file located in HangmanPy/HangmanPy/HangmanPy.py

## Installing
Download and unzip files, 
or use the git clone command as follows:
```
git clone <URL>
```
where <URL> is the  URL of the main package page (likely the one you're reading this on).
  
## Running
Run using python3 with the folowing command (in unix) while in the directory HangmanPy:

```bash
$ python3 HangmanPy.py
```
or on windows:
```dos
> py3 HangmanPy.py
```

### User Guide
Initially you will be greeted wth a 1 or 2 player selection screen.

If you choose 1, you will be enter single-player mode.

Choosing 2 will result in multi-player mode.

NOTE: If a different value is entered the game will default to
single-player mode.

#### Single-Player
If you're entering single-player mode, the word will be chosen randomly from the wordlist.txt file (contains most words in the english 
dictionary).

You will then have the available options for letters and can make your selection by entering the letter (UPPER or lowercase)
followed by the return key.

The hangman allows for 10 guesses good luck!

#### Local Multi-player
If you'd like to play with a friend, choose 2 when asked for play options. 
 
This allows for an "executioner", a player can enter a secret word or message (all one word for now) and press return.

## License
[MIT License](/LICENSE)

## Contact:
Any issue or questions feel free to e-mail: adam-dad@hotmail.co.uk
