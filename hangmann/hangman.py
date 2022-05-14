

import random

from click import clear

import hangman_words




end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
live = 6

from hangman_art import logo, stages
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
          print("You have already guessed letter {guess}")
          

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        live-=1
        print(f"yoy have guessed wrong,you have {live} remaining")     
        if live==0:
            end_of_game=True
            print("you lose")   
               



    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[live])
      
        

