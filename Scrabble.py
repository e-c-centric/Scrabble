#scrabble game

import random
import time

#global variables
#list of letters
letters = ['A','A','A','A','A','A','A','A','A','B','B','C','C','D','D','D','D','E','E','E','E','E','E','E','E','E','E','E','E','F','F','G','G','G','H','H','I','I','I','I','I','I','I','I','I','J','K','L','L','L','L','M','M','N','N','N','N','N','N','O','O','O','O','O','O','O','O','P','P','Q','R','R','R','R','R','R','S','S','S','S','T','T','T','T','T','T','U','U','U','U','V','V','W','W','X','Y','Y','Z']
#list of points
points = [1,1,1,1,1,1,1,1,1,3,3,3,3,2,2,2,2,1,1,1,1,1,1,1,1,1,10,10,10,10,2,2,2,2,2,2,1,1,1,1,1,1,1,1,8,5,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,4,4,10,1,1,1,1,1,1,1,1,1,4,4,4,4,4,4,1,1,4,4,8,4,10,10,10,10,10,10,10,10,10,10,10]

#function to draw letters
def draw_letters():
    #list of letters drawn
    drawn_letters = []
    #draw 7 letters
    for i in range(7):
        #choose a random letter
        letter = random.choice(letters)
        #add letter to list
        drawn_letters.append(letter)
        #remove letter from letters
        letters.remove(letter)
    #return list of letters
    return drawn_letters

#function to calculate score
def calculate_score(word):
    #score
    score = 0
    #for each letter in word
    for i in range(len(word)):
        #find index of letter in letters
        index = letters.index(word[i])
        #add points to score
        score += points[index]
    #return score
    return score

#function to check if word is in dictionary
def check_word(word):
    #open dictionary
    with open('dictionary.txt') as f:
        #read lines
        lines = f.readlines()
        #for each line
        for line in lines:
            #if word is in line
            if word in line:
                #return true
                return True
        #return false
        return False

#function to check if word is in hand
def check_hand(word, hand):
    #for each letter in word
    for i in range(len(word)):
        #if letter is not in hand
        if word[i] not in hand:
            #return false
            return False
        #if letter is in hand
        else:
            #remove letter from hand
            hand.remove(word[i])
    #return true
    return True

#function to play game
def play_game():
    #draw letters
    hand = draw_letters()
    #print hand
    print('Your hand is: ' + str(hand))
    #get word from user
    word = input('Enter a word: ')
    #if word is in hand
    if check_hand(word, hand):
        #if word is in dictionary
        if check_word(word):
            #calculate score
            score = calculate_score(word)
            #print score
            print('Your score is: ' + str(score))
        #if word is not in dictionary
        else:
            #print error
            print('Word is not in dictionary')
    #if word is not in hand
    else:
        #print error
        print('Word is not in hand')



#main function
def main():
    #play game
    play_game()

#call main function
main()


