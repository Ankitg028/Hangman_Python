import random
from words import words_list
from termcolor import cprint

def get_word():
    word = random.choice(words_list)
    return word.upper()

def welcome():
    cprint("Welcome To Hangman Game!",'blue','on_green')
    name = input("Please enter a preferred name: ")
    if name.isalpha() == True:
        print(""">> Hi!""",name,"""Glad to have you here! <<<
                You will be playing against the computer today.
                The computer will randomly choose a word and you will try to guess what the word is.
                You can always invite your friends for a fun time together
                You have 6 Lives.
                ==========================================================
                Good Luck! Have fun playing""")
    else:
        cprint(""">> Try Again  \n Please enter only alphabet name""",'red',attrs=['bold'])



def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letter = []
    guessed_word = []
    lives = 6
    cprint('Lets Play Hangman!!', 'green', 'on_red', attrs=['bold'])
    print(display_hangman(lives))
    print(word_completion)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Enter a guess letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                cprint("You already guessed letter!",'red','on_yellow')
            elif guess not in word:
                print(guess,'is not in the word')
                lives -= 1
                guessed_letter.append(guess)
            else:
                print('Good Job',guess,'is in the word!')
                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print("You are already gussed word!!",guess)
            elif guess != word:
                print(guess,"is not the word")
                lives -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(word_completion)
        print('\n')
    if guessed:
        cprint("Congrats!! You guessed the word! You WIN!!",'red','on_yellow')
    else:
        print("Sorry, you ran out of lives. The word was "+word+" . Maybe Try next Time")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    welcome()
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()