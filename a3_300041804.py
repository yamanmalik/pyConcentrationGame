#Created by Yaman Malik
#Concentration/Matching Game

import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    
    random.shuffle(deck)
    print("Shuffling the deck...")

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def print_revealed(discovered, p1, p2, board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
 
    if(board[p1]==board[p2]):
        discovered[p1]=board[p1]
        discovered[p2]=board[p2]
        print_board(discovered)
        wait_for_player()
        print_board(discovered)

    else:
        discovered[p1]=board[p1]
        discovered[p2]=board[p2]
        print_board(discovered)
        wait_for_player()
        discovered[p1]="*"
        discovered[p2]="*"
        print_board(discovered)
        
    
        
        

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str
    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]
   
    for x in range(len(l)):
        if l[x]!="*":
            playable_board.append(l[x])
    for x in range(len(l)):
        if playable_board.count(l[x])%2!=0:
            playable_board.remove(l[x])
    
    return playable_board

def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    
    for x in range(len(l)):
        if l.count(l[x])!=2:
            return False
    else:
        return True

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''
    # this is the funciton that plays the game
  
    print("Ready to play ...\n")
    discovered=["*"]*len(board)
    print_board(discovered)
    print("\nEnter two distinct positions on the board that you want revealed. \ni.e two integers in the range [1,"+str(len(board))+"]")
    p1=int(input("Enter Position 1:" ))-1
    p2=int(input("Enter Position 2:" ))-1
    print_revealed(discovered,p1,p2,board)
    guesses=1
    while (discovered!=board):
        
        print("\nEnter two distinct positions on the board that you want revealed. \ni.e two integers in the range [1,"+str(len(board))+"]")
        p1=int(input("Enter Position 1:" ))-1
        p2=int(input("Enter Position 2:" ))-1
        if(discovered[p1]==board[p1]) or (discovered[p2]==board[p2]):
            print("\nOne or both of your chosen positions has/have already been paired")
            print("This guess did not count. You are currently at: "+str(guesses)+" guesses.")
        else:
            print_revealed(discovered,p1,p2,board)
            guesses=guesses+1
    best=len(board)/2
    bestest=int(guesses-best)
    print("\nCongratulations! You completed the game with "+str(guesses)+" guesses! Thats "+str(bestest)+" more than the best possible!")
        




#main
def ascii_name_plaque(name):
     '''  (string)->string
     Takes a string into the function for variable 'name' and prints asciii symbols around it to create an ascii name plaque
     Precondition: None
     '''
     print("*"*len(name)+"*"*10)
     print("*"+" "*(len(name)+8)+"*")
     print("*"+" "*2+"_"*2+name+"_"*2+" "*2+"*")
     print("*"+" "*(len(name)+8)+"*")
     print("*"*len(name)+"*"*10)
     
ascii_name_plaque("Welcome to my Concentration game")
    
#  CODE TO GET A CHOICE 1 or CHOCE 2 from a player 
def options():
    '''()->(integer)
    Prompts user for integer 1 or 2 as input to determine whether user wants random deck generated, or deck read from file
    Precondition: input must be integer value 1 or 2
    '''
    print("Would you like(enter 1 or 2 to indicate your choice): \n(1) me to generate a rigorous deck of cards for you \n(2) or would you like me to read a deck from a file?")
    choice=int(input())
    while (choice!=1) and (choice!=2):
        print(str(choice)+" is not an existing option. Please try again. Enter 1 or 2 to indicate your choice")
        choice=int(input())
    if choice==1:
        print("You chose to have a rigorous deck generated for you\n")
        return choice
    else:
        return choice
        


# CODE FOR OPTION 1 
if options()==1:
    def optionone():
        '''(integer)->(string)
        Sets up and plays game if user selected option one, and wants random deck generated
        Precondition: input must equal integer value 1
        '''
        print("How many cards would you like to play with?")
        amount=int(input("Enter an even number between 0 and 52:"))
        while((amount<0) or (amount>52)) or ((amount<52) and (amount>0) and (amount%2==1)):
            print("How many cards would you like to play with?")
            amount=int(input("Enter an even number between 0 and 52:"))
        return amount
    board=create_board(optionone())
    wait_for_player()
    shuffle_deck(board)
    play_game(board)
    
else:
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file (eg 'bo1.txt', 'bo2.txt'): ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)
    if len(board)==0:
        ascii_name_plaque("This deck is now playable and rigorous and has "+str(len(board))+" cards")
        wait_for_player()
        print("The resulting board is empty. \nPlaying Concentration game with an empty board is impossible. \nGood bye")
    elif is_rigorous(board)==True:
        ascii_name_plaque("This deck is now playable and rigorous and has "+str(len(board))+" cards")
        wait_for_player()
        shuffle_deck(board)
        play_game(board)
    else:
        ascii_name_plaque("This deck is now playable but not rigorous and has "+str(len(board))+" cards")
        wait_for_player()
        shuffle_deck(board)
        play_game(board)
        

