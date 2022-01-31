import random
from words import words_list
from os import system, name

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def show_game(word_size, letters_known):
    spaces = 0

    print("The Hanged Man Game\n")

    while(spaces < word_size ):
        if letters_known[spaces] == '?':
            print("_ ", end = " ")
        else:
            print(letters_known[spaces], end = " ")
        spaces += 1

def put_correct_letters(choice, letters_known):
    counter = 0
    while counter is not word_size:
        if choice == word_letters[counter]:
            letters_known[counter] = choice
        counter += 1
            

selected_word = random.choice(words_list)

word_size    = len(selected_word)
word_letters = []
letters_known= [] 

for letter in selected_word: 
    word_letters.append(letter)    
    letters_known.append('?')

print(" ")
    
chances = 5

while chances > 0 : 
    
    show_game(word_size, letters_known)
    
    print(f"\n\nYou still have {chances} chances \n")
    
    if '?' not in letters_known:
        print("You won the game")
        break 
    
    choice = input('Choose a letter : ')
    choice = choice.lower()
   
    clear()
   
    if choice in word_letters:
        put_correct_letters(choice, letters_known)
   
    else:
         chances -= 1
         if chances == 0:
            print(f"You've lost the game! \nthe word was : {selected_word}")
    
       
        
    
