import os
import time
import random
from modules_blackjack import *
from colorama import Fore, Back, Style, init
init(autoreset = True)

def main():

    # this is main() and where the blackjack game is started.
    #
    # while game_in_play will call play_blackjack(player_objects_list, dealer, deck)
    #
    # play_blackjack(player_objects_list, dealer, deck)
    # - cards dealt
    # - bets placed
    # - Hits and Stays
    # - BlackJack, BUST, Win, Draw, Lose are determined
    #
    # Players are given option to play again and will return result of play_again to main()

    # clear the screen following by 2 carriage returns
    for i in range(10):
        clear_screen()

    # print the welcome banner
    welcome_banner()

    # create deck object
    # create the deck
    # shuffle the deck
    deck = Deck()
    deck.create_deck()
    deck.shuffle_deck()

    # call function create_players() --> will ask how many players and each player's name
    # list player_list will be created and returned player_list = ['x', 'name1', 'name2', 'etc']
    player_list = create_players()

    # create_player_objects
    # pass parameter player_list and create_player_objects() will create an object for each player and return a list
    # player_objects_list = ['x', object_for_player1, object_for_player2, etc]
    player_objects_list = create_player_objects(player_list)

    # update player name in player object
    # create each players bank
    # this should be the last time list player_list is used
    update_player_name(player_list, player_objects_list)
    start_player_bank(player_objects_list)

    # create dealer object and call dealer.update_name(dealer_name)
    dealer = Dealer()
    dealer.name = dealer.random_dealer_name()

    # assign game_in_play = True
    # this will remain True after the cuurrent hand is played and players choose to play again
    # if players choose not to play again game_in_play will be assigned False
    game_in_play = True

    while game_in_play:

        # call check_player_bank(player_objects_list)
        #
        # if any player on the player_objects_list has a bank == 0
        #     player index will be removed from player_objects_list
        player_objects_list = check_player_bank(player_objects_list)

        # check to see if there are any players left on the player_objects_list
        # index0 of the list is 'x' so the list has minimum 1 item
        if len(player_objects_list) == 1:

            clear_screen()

            print("There are no more players sitting at the table!")
            print('\n')
            break     # main() and the blackjack game will end

        # call continue_to_play = play_blackjack(player_objects_list, dealer, deck)
        #
        # play_blackjack(player_objects_list, dealer) will return
        # True (continue to play)
        # False (do not continue to play)
        continue_to_play = play_blackjack(player_objects_list, dealer, deck)

        # assign game_in_play to False if continue_to_play is False
        if not continue_to_play:
            game_in_play = False
            break

        # game_in_play == True
        # prepare for the next game of blckjack
        else:
            
            # do clean up of object attributes to start again
            # function play_again_init()
            play_again_init(player_objects_list, dealer)

            # create a brand new deck of cards to start next blackjack game
            # shuffle the deck
            deck.create_deck()
            deck.shuffle_deck()

    # the table is no longer playing blackjack
    #
    # players may have chose not to play again or..
    # all players have bank == 0
    #
    # game is terminated
    thank_you_for_playing_banner()

# **** End of function main() **** #


def clear_screen():
    clear_screen = lambda: os.system('cls')
    clear_screen()
    print('\n')
    print('\n')

# **** End of function clear_screen() **** #


def welcome_banner():

    first_string = ("Welcome to the game of BlackJack!")
    second_string = ("There are 7 seats at the table. Please have a seat!")

    banner_object = assign_banner_attributes(first_string, second_string)

    # call display_banner
    display_banner(banner_object)

# **** End of function welcome_banner() **** #


def lets_play_blackjack_banner():

    first_string = ("Let's Play BlackJack!")
    second_string = ("Place Your Bets!")

    banner_object = assign_banner_attributes(first_string, second_string)

    # call display_banner
    display_banner(banner_object)

# **** End of function lets_play_blackjack_banner() **** #


def thank_you_for_playing_banner():

    first_string = ("The Game is Over!")
    second_string = ("Thank You for playing BlackJack!")

    banner_object = assign_banner_attributes(first_string, second_string)

    # call display_banner
    display_banner(banner_object)

# **** End of function thank_you_for_playing_banner() **** #


def player_removed_from_table_banner(name, bank):

    # variable 'name' format is 'Player: <name>'.  slice off the first 8 chars
    first_string = ("{}'s Bank = $0.00. {} is being removed from the table".format(name[8:], name[8:]))
    second_string = ("Thank You for playing BlackJack {}!".format(name[8:]))

    banner_object = assign_banner_attributes(first_string, second_string)
    
    # call display_banner
    display_banner(banner_object)

# **** End of function player_removed_from_table_banner() **** #


def assign_banner_attributes(*args):

    # assign string(s) passed in as args to string_list
    string_list = []

    for arg in args:
        string_list.append(arg)

    # generate a blackjack hand to display in this banner
    hand_list = generate_blackjack_hand_for_banners()
    cards = convert_hand_to_playing_cards(hand_list)

    # create banner_obect and pass in cards, string_list
    # 1. create first and last row in banner_object
    # 2. create blank space row in banner_object
    # 3. create string list row in banner_object
    # 4. create cards list row in banner_object
    banner_object = Banner(cards, string_list)
    banner_object.create_first_and_last_row()
    banner_object.create_blank_space_row()
    banner_object.create_string_list()
    banner_object.create_cards_list()

    return banner_object

# **** End of function assign_banner_attributes() **** #


def generate_blackjack_hand_for_banners():

    # this is going to create every combination of a winning blackjack hand
    # a blackjack hand will be displayed in the banner
    ace = 'A'
    suites = ['Hearts','Diamonds','Clubs','Spades']
    royals = ['10','J','Q','K']
    hand_list = []

    for item in suites:
        for suite in suites:
            for face in royals:
                hand_list.append([[item, ace],[suite, face]])
                hand_list.append([[suite, face],[item, ace]])

    # get a random number between 50-200
    # the random number will determine the number of time to shuffle hand_list
    # shuffle hand_list
    num = random.randint(50,200)

    for i in range (num):
            random.shuffle(hand_list)

    return hand_list[0]

# **** End of function generate_blackjack_hand_for_banners() **** #


def display_banner(banner):

    ####################################################
    #
    #           PRINT THE BANNER
    #
    ####################################################

    # print the 1st row and 2nd row of banner
    print(banner.get_first_and_last_row())
    print(banner.get_blank_space_row())

    # print the strings in welcome_banner.get_string_list()
    for i in range(len(banner.get_string_list())):
        print(banner.get_string_list()[i])
        print(banner.get_blank_space_row())

    # print the blackjack playing cards
    for i in range(len(banner.get_cards_list())):
        print(banner.get_cards_list()[i])

    # print the next to last and last row of banner
    print(banner.get_blank_space_row())
    print(banner.get_first_and_last_row())
    print('\n')
    print('\n')

# **** End of display_banner() **** #


def create_players():

    # assign is_int to False for while loop
    is_int = False

    # while loop will ensure valid int is provided as input
    while not is_int:

        try:
            # ask how many players will be playing blackjack
            num = int(input("How many players will play Black Jack? "))
            print('\n')

        except:
            print('\n')
            print("You did not enter a valid number!")
            print("Try Again!")
            print('\n')

        else:

            # check to be sure 0 has not been entered or a number greater than 7
            #
            # There are 7 seats at the blackjack table
            #
            # at least 1 player needs to sit to play the game and no more than 7 can play 
            if num == 0 or num > 7:
                print("There are only 7 seats at the table. Please try again, and enter a number from 1 to 7")
                #print("Please try again, and enter a number from 1 to 7")
                print('\n')

            else:
                # valid int given for input. Terminate while loop
                is_int = True

    # ask for player names
    # for loop will iterate in order to get all player names
    # player names will be appended to player_list['x']
    # player_list is initialized 'x' at index 0 so players are in sequence from 1 - n
    player_list = ['x']

    for i in range(1,(num+1)):

        x = str(i)

        valid_name = False

        while not valid_name:
            name = input("Enter Player{}'s name: ".format(x))

            # if name == '': is a check to make sure user did not hit Enter by mistake for player name
            if name == '':
                print("Please enter a name. Try Again!")
            else:
                valid_name = True
        
        player_list.append('Player: ' + name.title())

    # all names for players in backjack are given
    # carriage return needed
    print('\n')

    return player_list

# **** End of function create_players() **** #


def create_player_objects(player_list):

    # create the player_objects_list and assign index 0 to 'x'
    player_objects_list = ['x']

    # create a player object for each item in the player_list
    # player_list = ['x', 'player1_name', 'player2_name', 'player3_name', etc]
    # when creating player object the name of the player (from player_list) is passed to Player
    for i in range(1, len(player_list)):
        player = Player()
        player_objects_list.append(player)

    return player_objects_list

# **** End of function create_player_objects() **** #


def update_player_name(player_list, player_objects_list):

    # iterate through each item of player_objects_list ['x', player_object_1, player_object_2, etc]
    # call player.update_player_name(player_list[i]) to update player_name in player object
    for i in range(1,len(player_objects_list)):
        player = player_objects_list[i]

        # assign player name in player object Player() self.name
        player.name = player_list[i]

# **** End of function update_player_name() **** #


def start_player_bank(player_objects_list):

    # ask for the bank for each player
    for i in range(1, len(player_objects_list)):

        # assign player object
        player = player_objects_list[i]

        # is_int = False will control the while loop and ensure user provides an integer for input
        is_int = False
        while not is_int:

            try:
                amount = int(input("{:20s}: how much money are you playing BlackJack with?  $".format(player.get_name())))

                # minimum bank is 10
                if amount < 10:
                    print('\n')
                    print('The minimum Bank Amount is $10.00. Enter a Bank Amount of $10.00 or more!')
                    print('\n')
                else:
                    is_int = True

            except:
                print('\n')
                print("{}: you did not enter a valid $ amount. Try Again".format(player.get_name()))
                print('\n')

        # update player object with input amount
        player.add_bank(amount)

    # for loop ended. All players entered valid bank amount
    # add a carriage return for screen formatting
    print('\n')

# **** End of function create_player_bank() **** #


def check_player_bank(player_objects_list):

    # check_player_bank() will determine if player's bank == 0
    #
    # if player's bank == 0 the player's player_object will be removed from player_objects_list
    #
    # assign original_length to len(player_objects_list)
    # original_length will help determine if player objects have been removed from player_objects_list
    #
    # an announcement will be made for each player removed and 'Press Enter to continue' input wil be 
    # needed if player(s) removed
    original_length = len(player_objects_list)

    # check to be sure each player on player_objects_list has a bank != 0
    # if player bank == 0
    #     pop player index off the player_objects_list
    #
    # pop_list will be used to store the indexes of players on player_objects_list which have a bank == 0
    # pop_list will be used later in this function to pop players off player_objects_list
    pop_list = []

    for i in range(1, len(player_objects_list)):

        player = player_objects_list[i]

        # if player's bank is 0 the player is removed from the table
        if player.get_bank() == 0:
            index = i

            # call player_removed_from_table_banner() to announce player is being removed from game
            player_removed_from_table_banner(player.get_name(), player.get_bank())

            # append index to pop_list. pop_list will be used in the while loop
            pop_list.append(index)

    # pop the players off player_objects_list until all items on pop_list are taken care of
    while len(pop_list) != 0:

        # pop index off player_objects_list
        player_objects_list.pop(pop_list[0])

        # pop index0 off pop_list
        pop_list.pop(0)

        # decrement remaining items on pop_list -= 1, because player_objects_list has 1 item popped
        # indexes for remaining items on player_objects_list have decremented -= 1
        for i in range(len(pop_list)):
            pop_list[i] -= 1

    # all players with bank == 0 need to be removed and banners need to be displayed before input
    if original_length != len(player_objects_list):
        input("Press Enter to continue..... ")

    return player_objects_list    

# **** End of function check_player_bank() **** #


def place_bets(player_objects_list):

    # get player name and bank
    # ask player to place bet and check if bank >= bet
    for i in range(1, len(player_objects_list)):
        player = player_objects_list[i]

        # while loop will make sure player places a valid integer bet
        # while loop will make sure player places a bet that does not exceed player bank
        bet_valid = False
        while not bet_valid:
            try:
                bet = int(input("{:20s} Bank = ${:10.2f}      --> place your bet!  $".format(player.get_name(), \
                                                                                             player.get_bank())))
            except:
                print("{} you did not enter a valid number for your bet. Try again!".format(player.get_name()[8:]))
            else:
                # bet must be <= player's bank to be a valid bet
                if bet <= player.get_bank() and bet > 0:
                    bet_valid = True

                # check to make sure player is not betting more than what is in player's bank
                elif bet > player.get_bank():
                    print('\n')
                    print("{} your bet exceeds your bank amount. Your bank amount is ${:.2f}".format(player.get_name()[8:], \
                                                                                                     player.get_bank()))
                    print("Try again!")
                    print('\n')

                # make sure bet is not 0
                elif bet <= 0:
                    print('\n')
                    print("{} your bet needs to be greater than $0.00. Your bank amount is ${:.2f}".format(player.get_name()[8:], \
                                                                                                           player.get_bank()))
                    print("Try again!")
                    print('\n')

        print('\n')
        # bet is now valid and player's bank needs to be adjusted
        player.minus_bank(bet)
        player.update_bet(bet)

    # all bets placed. Add carriage return for screen formatting
    print('\n')

# **** End of function place_bet() **** #


def play_blackjack(player_objects_list, dealer, deck):

    # This is where the hand of black jack is played
    #
    # How to deal cards in Black Jack
    # 1. players place bets
    # 2. each player is dealt 1st card face-up
    # 3. dealer is dealt 1st card face-down
    # 4. each player is dealt 2nd card face-up
    # 5. dealer is dealt 2nd card face-up

    clear_screen()
    lets_play_blackjack_banner()

    ###########################################################################
    #
    #  1.      PLACE BETS
    #
    ###########################################################################

    # call place_bets so each player can place their bet before cards are dealt
    place_bets(player_objects_list)

    time.sleep(1)

    ###########################################################################
    #
    #  2.      DEAL FIRST TWO CARDS
    #
    ###########################################################################

    # deal 2 cards to players and 2 cards to dealer
    deal_first_two_cards(player_objects_list, dealer, deck)

    ###########################################################################
    #
    #  3.      UPDATE HAND STATUS
    #
    ###########################################################################

    # call update_hand_status(player_objects_list, dealer)
    # update_hand_status will check if player has blackjack
    # if no blackjack update_hand_status() will calculate total points in the player's hand
    update_hand_status(player_objects_list, dealer)

    ###########################################################################
    #
    #  4.      DISPLAY HANDS
    #
    ###########################################################################

    # clear_screen for screen formatting
    clear_screen()

    print("First Two Cards are Dealt to all Players and Dealer!")
    print('\n')
    
    display_hand(dealer)    # pass dealer object to display_hand()

    # call player_hand = player.get_display_hand
    # player.get_display_hand will return a list in the following format
    # [['2', 'Diamonds'], ['K', 'Spades']] ---> if player
    for i in range(1, len(player_objects_list)):
        player = player_objects_list[i]

        display_hand(player)    # pass player object to display_hand()

    # just return from display_hand
    input("Press Enter to continue..... ")

    ###########################################################################
    #
    #  5.      PLAYER(S) HIT OR STAY
    #
    ###########################################################################

    # clear screen for screen formatting
    for i in range(10):
        clear_screen()

    # it is time for each player to decide whether to hit or stay
    for i in range(1, len(player_objects_list)):

        player = player_objects_list[i]
        player_hit_or_stay(deck, player, dealer)

    ###########################################################################
    #
    #  6.      DEALER HIT OR STAY
    #
    ###########################################################################
    dealer_hit_or_stay(deck, player_objects_list, dealer)

    ###########################################################################
    #
    #  7.      WIN, LOSE or DRAW
    #          - determine if each player has a Win, Lose or Draw
    #
    ###########################################################################
    win_lose_or_draw(player_objects_list, dealer)

    ###########################################################################
    #
    #  8.      SETTLE_WINS_DRAWS_LOSE
    #          - reward winners
    #          - return bet for Draw
    #          - keep bet for Lose
    #
    ###########################################################################
    settle_wins_draws_lose(player_objects_list)

    ###########################################################################
    #
    #  9.      UPDATE FINAL RESULT
    #          - update dealer and players Win, Lose, Draw, BUST, BlackJack
    #            in player objects and dealer object
    #
    ###########################################################################
    update_final_result(player_objects_list, dealer)

    ###########################################################################
    #
    #  10.      DISPLAY FINAL HANDS - THIS GAME IS OVER
    #
    ###########################################################################

    # clear screen for screen formatting
    for i in range(10):
        clear_screen()

    print("Final Results of Game are...............")
    print('\n')

    display_hand(dealer)    # pass dealer object to display_hand()

    for i in range(1, len(player_objects_list)):
        # get the player --> name, total, hand, bust, blackjack, final
        player = player_objects_list[i]

        display_hand(player)    # pass ddealer object to display_hand()

    # just return from display_hand
    input("Game is Over. To view Final player summary, Press Enter to continue..... ")

    ###########################################################################
    #
    #  11.      DISPLAY FINAL SUMMARY - THIS GAME IS OVER
    #
    ###########################################################################

    # clear screen for screen formatting
    for i in range(10):
        clear_screen()

    display_final_summary(player_objects_list, dealer)

    ###########################################################################
    #
    #  12.      GAME OVER - PLAY AGAIN?
    #
    ###########################################################################

    # will need to call play_blackjack_again()
    # play_blackjack_again will return True or False
    # True - play again
    # False - do not play again
    #
    # for now return False
    #return False
    play_again = play_blackjack_again()

    # return to main()
    return play_again


# **** End of function play_blackjack() **** #


def deal_first_two_cards(player_objects_list, dealer, deck):

    # How to deal cards in Black Jack
    # 1. each player is dealt 1st card face-up
    # 2. dealer is dealt 1st card face-down
    # 3. each player is dealt 2nd card face-up
    # 4. dealer is dealt 2nd card face-up

    deal_count = 1

    while deal_count <= 2:

        # deal each player a card
        for i in range(1, len(player_objects_list)):
            player = player_objects_list[i]
            player.hand.append(deck.deal_card())

        # deal dealer a card
        dealer.hand.append(deck.deal_card())

        # increment deal_count to control while loop
        deal_count += 1

# **** End of function deal_first_two_cards() **** #


def update_hand_status(player_objects_list, dealer):

    # update_hand_status() will 
    #
    # update self.blackjack = True if hand is a blackjack by calling 
    # player or dealer.is_blackjack()
    #
    # calculate player or dealer's hand total by calling player or dealer.calculate_hand()


    for i in range(1, len(player_objects_list)):
        player = player_objects_list[i]
        player.is_blackjack()
        player.calculate_hand()

    dealer.is_blackjack()
    dealer.calculate_hand()

# **** End of function update_hand_status() **** #


def display_hand(player_or_dealer):

    # display the hand
    #
    # player_or_dealer object will be either a player object or dealer object
    #
    # get the player_or_dealer object name, total, hand, blackjack, bust, final
    # if the player_or_dealer object is a player object then get the bet and bank
    name      = player_or_dealer.get_name()
    total     = player_or_dealer.get_total()
    hand      = player_or_dealer.get_hand()
    blackjack = player_or_dealer.get_blackjack()
    bust      = player_or_dealer.get_bust()
    final     = player_or_dealer.get_final()
    try:
        bet   = player_or_dealer.get_bet()
        bank  = player_or_dealer.get_bank()
    except:
        pass

    # if dealer only has two cards and 2nd card is still facedown the dealer's total is 0
    # this if statement is to handle the dealer case.
    # a player will never have a total == 0.
    if total == 0:
        total = 'Unknown'

    # convert_hand_to_playing_cards() will convert hand list to playing cards
    playing_card_hand = convert_hand_to_playing_cards(hand)


    print("**********************************************************************************************************")
    print("*")

    try:
        print("*       {:30s}     Bet = ${:10.2f}     Bank = ${:10.2f}".format(name, bet, bank))
    except:
        print("*       {:30s}".format(name))
    else:
        pass

    print("*")

    if final != '':
        print("*       Hand Total: {:2d}     {}".format(total, final))
    elif blackjack:
        print("*       Hand Total: {:2d}     **** BLACKJACK ****".format(total))
    elif bust:
        print("*       Hand Total: {:2d}     **** BUST ****".format(total))
    else:
        try:
            print("*       Hand Total: {:2d}".format(total))
        except:
            print("*       Hand Total: {}".format(total))

    #print("*")
    #print("*       {}".format(hand))
    print("*")

    # print the 9 rows of the card hand 
    for i in range(len(playing_card_hand)):
        print("*" + "       " + playing_card_hand[i])

    print("*")
    print("**********************************************************************************************************")

# **** End of function display_hand() **** #


def convert_hand_to_playing_cards(hand_list):

    def card_color(suite, value):

        #   HEART   = "\u2665"
        #   DIAMOND = "\u2666"
        #   SPADE   = "\u2660"
        #   CLUB    = "\u2663"

        HEART   = (Fore.RED + Style.BRIGHT + "\u2665" + Style.RESET_ALL)
        DIAMOND = (Fore.RED + Style.BRIGHT + "\u2666" + Style.RESET_ALL)
        SPADE   = "\u2660"
        CLUB    = "\u2663"

        if suite == 'Hearts':
            suite = HEART

        elif suite == 'Diamonds':
            suite = DIAMOND
 
        elif suite == 'Clubs':
            suite = CLUB

        elif suite == 'Spades':
            suite = SPADE
        
        return(suite, value)

    # **** End of function card_color() **** #


    def build_playing_card(card):

        #
        #                                value != 'facedown'
        #          value == '10'            value != '10'         value == 'facedown'
        #              
        #   row1 = '┌─────────┐'     row1 = '┌─────────┐'     row1 = '┌─────────┐'
        #   row2 = '|{}       |'     row2 = '|{}        |'    row2 = '|#########|'
        #   row3 = '|         |'     row3 = '|         |'     row3 = '|#########|'
        #   row4 = '|         |'     row4 = '|         |'     row4 = '|#########|'
        #   row5 = '|    {}    |'    row5 = '|    {}    |'    row5 = '|#########|'
        #   row6 = '|         |'     row6 = '|         |'     row6 = '|#########|'
        #   row7 = '|         |'     row7 = '|         |'     row7 = '|#########|'
        #   row8 = '|       {}|'     row8 = '|        {}|'    row8 = '|#########|'
        #   row9 = '└─────────┘'     row9 = '└─────────┘'     row9 = '└─────────┘'
        #

        if card[0] == 'Facedown':
            suite = card[0]
            value = '0'

        else:
            suite = card[0]
            value = card[1]

        # smaller cards
        if value == '10':
            # for single digit numbers
            row1 = '┌─────┐'
            row2 = '|{}   |'
            row3 = '|  {}  |'
            row4 = '|   {}|'
            row5 = '└─────┘'

        elif value != '10' and suite != 'Facedown':
            # for single digit numbers
            row1 = '┌─────┐'
            row2 = '|{}    |'
            row3 = '|  {}  |'
            row4 = '|    {}|'
            row5 = '└─────┘'

        if suite != 'Facedown':
            row2 = row2.format(value)
            row3 = row3.format(suite)
            row4 = row4.format(value)

        if suite == 'Facedown':
            # for facedown card
            row1 = '┌─────┐'
            row2 = '|#####|'
            row3 = '|#####|'
            row4 = '|#####|'
            row5 = '└─────┘'

        return (row1,row2,row3,row4,row5)

        # **** End of function build_playing_card() **** #


    # hand_list is a list representing each card in the hand
    # hand_list = [['Clubs', '2', 2],['Diamonds', 'A', 1],['Spades', 'K', 10],['Hearts', '10', 10]]
    new_hand = []

    for card in hand_list:

        if card[0] == 'Facedown':
            suite = card[0]
            value = 0

        else:
            suite = card[0]
            value = card[1]

        # card_color returns a tuple (value,suite)
        card = card_color(suite, value)

        # build_playing_card() returns a tuple (row1,row2,row3,row4,row5,row6,row7,row8,row9)
        # row1-9 are the nine rows of the playing card
        playing_card_rows = build_playing_card(card)

        if len(new_hand) == 0:

            # this is the 1st card in the hand
            for i in range(len(playing_card_rows)):

                # 9 items in playing_card_rows = (row1,row2,row3,row4,row5,row6,row7,row8,row9)
                # new_hand will have 9 items of playing_card_rows after append is complete
                row = playing_card_rows[i]
                new_hand.append(row)

        else:

            # this is NOT the 1st card in the hand
            for i in range(len(playing_card_rows)):

                # 9 items in playing_card_rows = (row1,row2,row3,row4,row5,row6,row7,row8,row9)
                # new_hand will have 9 items of playing_card_rows after append is complete
                new_hand[i] = new_hand[i] + " " + playing_card_rows[i]

    return new_hand

# **** End of function convert_hand_to_playing_cards() **** #


def player_hit_or_stay(deck, player, dealer):

    # def player_hit_or_stay will prompt player to decie whether to hit or stay.
    #
    # if player decides to hit a card will be given to player
    # - player's hand will be updated with new card
    # - hand total will be calculated
    # - if player bust then player.self bust will be assigned True
    #
    # if player decides to stay
    # - player is satisfied with current total
    # - if player has blackjack with 1st two cards the player will automatically stay

    print("{}'s turn to Hit or Stay ..................".format(player.get_name()))
    print('\n')

    # stop_taking_hit will control the while loop
    stop_taking_hits = False

    while not stop_taking_hits and not player.get_blackjack() and not player.get_bust():

        ######################################################################
        #
        #  1.      DISPLAY DEALER'S HAND and DISPLAY PLAYER'S HAND
        #
        ######################################################################
        display_hand(dealer)  # pass dealer object to display_hand()
        display_hand(player)  # pass player object to display_hand()

        ######################################################################
        #
        #  2.      ASK PLAYER TO HIT or STAY
        #
        ######################################################################
        answer_valid = False

        while not answer_valid:

            answer = input("{} do you want to Hit or Stay? 'h' or 's' ".format(player.get_name()))

            # clear_screen for screen formatting
            for i in range(10):
                clear_screen()

            if answer.upper() != 'H' and answer.upper() != 'S':

                print("{} you did not enter a 'h' or 's'. Please Try again!".format(player.get_name()))
                print('\n')

                display_hand(dealer)  # pass dealer object to display_hand()
                display_hand(player)  # pass player object to display_hand()

            else:
                answer_valid = True

        ######################################################################
        #
        #  3.      HIT or STAY ANSWER PROVIDED
        #
        #          'H' = HIT
        #          'S' = STAY --> stop_taking_hits
        #                         while not stop_taking_hits: will terminate
        #
        ######################################################################
        if answer.upper() == 'S':
            stop_taking_hits = True

        else:
            # player decided to hit. deal card and then update hand with new card.
            player.update_hand(deck.deal_card())

            # make a call to sum the total with all cards in players hand
            player.calculate_hand()

    if player.get_blackjack() or player.get_bust():
        display_hand(dealer)   # pass dealer object to display_hand()
        display_hand(player)   # pass player object to display_hand()

        # just return from display_hand
        input("Press Enter to continue..... ")

        # clear screen for screen formatting
        for i in range(10):
            clear_screen()

# **** End of function player_hit_or_stay() **** #


def dealer_hit_or_stay(deck, player_objects_list, dealer):

    ##################################################################################
    #
    #  When the dealer has served every player, his face-down card is turned up. 
    #
    #  If the total is 17 or more, he must stand. 
    #
    #  If the total is 16 or under, he must take a card. 
    #
    #  He must continue to take cards until the total is 17 or more, at which point 
    #  the dealer must stand. 
    #
    #  If the dealer has an ace, and counting it as 11 would bring his total to 17 or 
    #  more (but not over 21), he must count the ace as 11 and stand. 
    #
    #  The dealer's decisions, then, are automatic on all plays, whereas the player 
    #  always has the option of taking one or more cards.
    #
    ##################################################################################

    # it is the dealer's turn to hit or stay
    # call dealer.no_facedown() which will reveal dealer's 2nd card
    # call dealer.is_blackjack() not that dealer's 2nd card is revealed.
    # call dealer.calculate_hand() to sum the total of hand
    dealer.no_facedown()
    dealer.is_blackjack()
    dealer.calculate_hand()

    print("{}'s 2nd card is now face-up.    {}'s turn to Hit or Stay.".format(dealer.get_name(), dealer.get_name()[8:]))
    print('\n')

    # stop_taking_hit will control the while loop
    stop_taking_hits = False

    while not stop_taking_hits and \
          not dealer.get_blackjack() and \
          not dealer.get_bust() and \
          not (dealer.get_total() >= 17 and dealer.get_total() <= 21):

        ######################################################################
        #
        #  1.      DISPLAY DEALER'S HAND and DISPLAY PLAYER'S HAND
        #
        ######################################################################
        display_hand(dealer)   # pass dealer object to display_hand()

        for i in range(1,len(player_objects_list)):
            player = player_objects_list[i]
            display_hand(player)    # pass player object to display_hand()

        # just return from display_hand
        input("Press Enter to see if Dealer Hits or Stays ")

        # clear_screen for screen formatting
        for i in range(10):
            clear_screen()

        ######################################################################
        #
        #  2.      DEALER HIT or STAY
        #
        #          HIT  - dealer will hit if hand total is < 17
        #          STAY - dealer will stay if hand total is >= 17 
        #                 while not stop_taking_hits: will terminate
        #
        ######################################################################

        if dealer.get_total() < 17:
            # dealer is goint to take a hit. deal card and then update hand with new card.
            dealer.update_hand(deck.deal_card())

            # make a call to sum the total with all cards in dealers hand
            dealer.calculate_hand()

            print("{} took a Hit!".format(dealer.get_name()))
            print('\n')

        elif dealer.get_total() > 21:
            dealer.self.bust = True

        else:
            stop_taking_hits = True

    # dealer did not take a Hit or is no longer taking Hits. Check for... 
    # blackjack or
    # bust or 
    # total >= 17 and <= 21.
    if dealer.get_blackjack():
        print("{} has **** BlackJack **** and will stay!".format(dealer.get_name()))

    elif dealer.get_bust():
        print("{} has **** BUST **** with a total of {}!".format(dealer.get_name(), dealer.get_total()))

    elif dealer.get_total() >= 17 and dealer.get_total() <= 21:
        print("{} has {} and will stay!".format(dealer.get_name(), dealer.get_total()))

    # need extra carriage return before display_hand() is called
    print('\n')

    display_hand(dealer)    # pass dealer object to display_hand()

    for i in range(1,len(player_objects_list)):
        player = player_objects_list[i]

        # display_hand for current player
        display_hand(player)    # pass player object to display_hand()

    # just return from display_hand and dealer hit or stay is done
    input("Press Enter to continue..... ")

# **** End of function dealer_hit_or_stay() **** # 


def win_lose_or_draw(player_objects_list, dealer):
    
    # win_lose_or_draw() will determine if a player wins, loses or draws by comparing the score 
    # of the player to the dealer.
    #
    # player object will be updated with the results.

    for i in range(1, len(player_objects_list)):

        player = player_objects_list[i]

        ############################################
        #                   WIN                    #
        ############################################

        if player.get_blackjack() and not dealer.get_blackjack():
            player.set_win()

        elif player.get_total() > dealer.get_total() and not player.get_bust():
            player.set_win()

        elif not player.get_bust() and dealer.get_bust():
            player.set_win()

        ############################################
        #                  DRAW                    #
        ############################################

        elif player.get_blackjack() and dealer.get_blackjack():
            player.set_draw()

        elif player.get_total() == dealer.get_total() and not player.get_bust():
            player.set_draw()

        ############################################
        #                  LOSE                    #
        ############################################

        elif not player.get_blackjack() and dealer.get_blackjack():
            player.set_lose()

        elif player.get_total() < dealer.get_total() and not dealer.get_bust():
            player.set_lose()

        elif player.get_bust():
            player.set_lose()


# **** End of function win_lose_or_draw() **** #


def settle_wins_draws_lose(player_objects_list):

    # determine if player wins, draws or lose 
    #
    # player gets paid for the winnings
    # player is returned bet if player end game with a draw
    # player loses bet if lose (bet is already decremented during bet time)
    #
    # player.get_win()  will return True or False
    # player.get_draw() will return True or False
    # player.get_lose() will return True or False 

    for i in range(1, len(player_objects_list)):
        player = player_objects_list[i]

        if player.get_win():
            player.receive_win()

        elif player.get_draw():
            player.receive_draw()

        elif player.get_lose():
            # do nothing. bet is already removed from player self.bank
            pass

# **** End of function settle_wins_draws_lose() **** #


def update_final_result(player_objects_list, dealer):

    # udpate_final_result() will call player and dealer.update_final()
    #
    # update.final() will determine if player and dealer ends the hand with
    # blackjack - player and dealer will be updated respectively (player and dealer)
    # win   - if players total > than dealer total and player is not bust (player)
    # draw  - if player total == dealer total and player not bust (player)
    # lose  - if player total < dealer total (player)
    # final - will be assigned final result
    #       - if player wins and has blackjack then final will be assigned blackjack
    #       - if player has blackjack and dealer has blackjack then final will be assigned draw

    dealer.update_final()

    for i in range(1, len(player_objects_list)):
        player = player_objects_list[i]
        player.update_final()

# **** End of function update_final_result() **** #


def display_final_summary(player_objects_list, dealer):

    # display_final_summary will display a summary of hand for all players
    # BLACKJACK, WIN, DRAW, BUST, LOSE will be displayed per player respectivley

    # print final summary for player
    # dealer name's format is 'Dealer: <name.'.   dealer.get_name()[8:] will slice on the name portion
    print('\n')
    print("Dealer Name ............ {}".format(dealer.get_name()[8:]))
    print('\n')

    if dealer.get_final() != '': 
        print("    Hand Total ......... {}     {}".format(dealer.get_total(), dealer.get_final()))
    else:
        print("    Hand Total ......... {}".format(dealer.get_total()))

    print('\n')

    for i in range(1, len(player_objects_list)):
        player = player_objects_list[i]

        # print final summary for player
        # player name's format is 'Player: '.  player.get_name()[8:] will slice on the name portion
        print("Player Name ............ {}".format(player.get_name()[8:]))
        print('\n')
        print("    Hand Total ......... {}     {}".format(player.get_total(), player.get_final()))
        print("    Bet ................ ${}".format(player.get_bet()))
        print("    Bank ............... ${}".format(player.get_bank()))
        print('\n')


# **** End of function display_final_summary() **** #


def play_blackjack_again():
    '''
    play_blackjack_again() function is to determine if another blackjack game will be played
    '''
    
    loop_continue = True

    while loop_continue:
        answer = input("Do you want to play another hand of Black Jack? Enter 'y' or 'n'  ")

        if answer.upper() == 'Y' or answer.upper() == 'YES':
            loop_continue = False
            play_again = True

        elif answer.upper() == 'N' or answer.upper() == 'NO':
            loop_continue = False
            play_again = False

        else:
            print('\n')
            print("You need to answer 'y' or 'n'. Please try again")
            print('\n')

    print('\n')
    print('\n')

    return play_again

# **** End of function play_blackjack_again() **** #


def play_again_init(player_objects_list, dealer):

    # play_again_init() will call init_new_game() for the dealer and each player
    # for dealer --> dealer.init_new_game()
    # for player --> player.init_new_game()
    #
    # init_new_game() returns all attributes (except for player's self.bank) to default so the new game can start clean

    #######################################################################
    #
    #   Dealer init all attributes ---> dealer.init_new_game()
    #
    #   Player init all attributes ---> player.init_new_game()
    #
    #######################################################################

    dealer.init_new_game()

    for i in range(1, len(player_objects_list)):
        player = player_objects_list[i]
        player.init_new_game()

# **** End of function play_again_init() **** #

