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
#function to check if word is in dictionary and can be formed from hand and board letters
import nltk
nltk.download('words')
from nltk.corpus import words

#function to check if word is in dictionary and can be formed from hand and board letters
def check_word(word, board_letters, hand):
    #combine board letters and hand
    all_letters = board_letters + hand
    #for each letter in word
    for i in range(len(word)):
        #if letter is not in all letters
        if word[i] not in all_letters:
            #return false
            return False
        #if letter is in all letters
        else:
            #remove letter from all letters
            all_letters.remove(word[i])
    #if word is in nltk words corpus
    if word in words.words():
        #return true
        return True
    #if word is not in nltk words corpus
    else:
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
#initialize board with double word scores
board = [['DW', '', '', 'DL', '', '', '', 'DW', '', '', '', 'DL', '', 'DW'],
         ['', 'TW', '', '', '', 'TL', '', '', '', 'TL', '', '', '', 'TW'],
         ['', '', 'DW', '', '', '', 'DL', '', 'DL', '', '', '', 'DW', ''],
         ['DL', '', '', 'DW', '', '', '', 'DL', '', '', '', 'DW', '', 'DL'],
         ['', '', '', '', 'DW', '', '', '', '', '', 'DW', '', '', ''],
         ['', 'TL', '', '', '', 'TL', '', '', '', 'TL', '', '', '', ''],
         ['', '', 'DL', '', '', '', 'DL', '', 'DL', '', '', '', 'DL', ''],
         ['DW', '', '', 'DL', '', '', '', ' ', '', '', '', 'DL', '', 'DW'],
         ['', '', 'DL', '', '', '', 'DL', '', 'DL', '', '', '', 'DL', ''],
         ['', 'TL', '', '', '', 'TL', '', '', '', 'TL', '', '', '', ''],
         ['', '', '', '', 'DW', '', '', '', '', '', 'DW', '', '', ''],
         ['DL', '', '', 'DW', '', '', '', 'DL', '', '', '', 'DW', '', 'DL'],
         ['', '', 'DW', '', '', '', 'DL', '', 'DL', '', '', '', 'DW', ''],
         ['', 'TW', '', '', '', 'TL', '', '', '', 'TL', '', '', '', 'TW'],
         ['DW', '', '', 'DL', '', '', '', 'DW', '', '', '', 'DL', '', 'DW']]

#function to display board
def display_board(board):
    #print column numbers
    print('  ', end='')
    for i in range(len(board)):
        print(str(i+1).rjust(2), end=' ')
    print()
    #print rows
    for i in range(len(board)):
        #print row letter
        print(chr(i+65), end=' ')
        #print row
        for j in range(len(board[i])):
            if board[i][j] == '':
                print('.', end=' ')
            else:
                print(board[i][j], end=' ')
        print()

#function to play game
def play_game():
    #draw letters
    hand = draw_letters()
    #print hand
    print('Your hand is: ' + str(hand))
    #initialize board letters
    board_letters = ''
    #initialize score
    score = 0
    #initialize word count
    word_count = 0
    #initialize game over flag
    game_over = False
    #while game is not over
    while not game_over:
        #display board
        display_board(board)
        #get word from user
        word = input('Enter a word (or press enter to pass): ')
        #if user enters nothing
        if word == '':
            #if word count is 0
            if word_count == 0:
                #print error
                print('You must enter at least one word')
            #if word count is not 0
            else:
                #set game over flag to true
                game_over = True
        #if user enters a word
        else:
            #get row and column from user
            row = int(input('Enter row (1-15): ')) - 1
            col = int(input('Enter column (1-15): ')) - 1
            #if row and column are out of range
            if row < 0 or row > 14 or col < 0 or col > 14:
                #print error
                print('Row and column must be between 1 and 15')
            #if row and column are in range
            else:
                #get direction from user
                direction = input('Enter direction (across or down): ')
                #if direction is not valid
                if direction != 'across' and direction != 'down':
                    #print error
                    print('Direction must be either "across" or "down"')
                #if direction is valid
                else:
                    #if word is valid based on hand and board letters
                    if check_word(word, board_letters, hand):
                        #calculate word score
                        word_score = calculate_score(word)
                        #if direction is across
                        if direction == 'across':
                            #for each letter in word
                            for i in range(len(word)):
                                #if board position is empty
                                if board[row][col+i] == '':
                                    #add letter to board
                                    board[row][col+i] = word[i]
                                #if board position is not empty
                                else:
                                    #add letter to board letters
                                    board_letters += word[i]
                            #calculate word score with multipliers
                            for i in range(len(word)):
                                if board[row][col+i] == 'DL':
                                    word_score += calculate_score(word[i])
                                elif board[row][col+i] == 'TL':
                                    word_score += calculate_score(word[i]) * 2
                                elif board[row][col+i] == 'DW':
                                    word_score *= 2
                                elif board[row][col+i] == 'TW':
                                    word_score *= 3
                        #if direction is down
                        else:
                            #for each letter in word
                            for i in range(len(word)):
                                #if board position is empty
                                if board[row+i][col] == '':
                                    #add letter to board
                                    board[row+i][col] = word[i]
                                #if board position is not empty
                                else:
                                    #add letter to board letters
                                    board_letters += word[i]
                            #calculate word score with multipliers
                            for i in range(len(word)):
                                if board[row+i][col] == 'DL':
                                    word_score += calculate_score(word[i])
                                elif board[row+i][col] == 'TL':
                                    word_score += calculate_score(word[i]) * 2
                                elif board[row+i][col] == 'DW':
                                    word_score *= 2
                                elif board[row+i][col] == 'TW':
                                    word_score *= 3
                        #add word score to total score
                        score += word_score
                        #increment word count
                        word_count += 1
                        #remove letters from hand
                        for i in range(len(word)):
                            hand.remove(word[i])
                    #if word is not valid based on hand and board letters
                    else:
                        #print error
                        print('Word is not valid based on hand and board letters')
    #display final score
    print('Your final score is: ' + str(score))


#main function
def main():
    #play game
    play_game()

#call main function
main()


