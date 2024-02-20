import random 
from words import words 
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()


def hangman():
    word = get_valid_word(words)
    words_letter = set(word) #letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letter =set() #store guessed letters
    
    
    hp = 6
    #get user input     
    while len(words_letter) > 0 and hp > 0:
        print("you have used: " + ' '.join(used_letter))
        
        words_list = [letter if letter in used_letter else '-' for letter in word] #list comprehension 
        print('You hp is: ' + str(hp) + ' left and the current word list: ', ' '.join(words_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letter: 
            used_letter.add(user_letter)
            if user_letter in words_letter:
                words_letter.remove(user_letter)
                print(' ')
            else:
                hp -= 1
                
        elif user_letter in used_letter:
            print("You have already gusessed")

        else:
            print("Invalid character. Please try again.")
    
        
    if hp == 0:
        print('you dead, the word is ' + word)
    else:
        print('you won, congrulation')






        