import random

class Deck():

    # class Deck() will be the playing deck for the blackjack game

    def __init__(self):

        # self.deck defined and is initialized to empty
        deck = []
        self.deck = deck
        self.deck_count = len(self.deck)

    # **** End of Deck.__init__() **** #

    
    def create_deck(self):

        # reinitialize self.deck to an empty list to be sure it is empty
        self.deck = []

        # create the deck of cards to play blackjack
        # deck -> create empty list to append to later in method
        # clubs, spades, diamonds, hearts -> create empty list to append to later in method
        clubs = []
        spades = []
        diamonds = []
        hearts = []

        # range is (2,11) to add cards 2-10
        for i in range(2,11):

            # each card will be created for each suite from 2-10
            # x = str(i) will be the card
            # i will be the value of the card

            # assign x = str(i)
            x = str(i)

            # append to list clubs, spades, diamonds, hearts
            # clubs.append(['Clubs',x,i])
            clubs.append(['Clubs',x,i])
            spades.append(['Spades',x,i])
            diamonds.append(['Diamonds',x,i])
            hearts.append(['Hearts',x,i])

        # create Royals or Facecards
        for facecard in ['A','J','Q','K']:

            # the Ace is a special case. Ace can have a value of 1 or 11.
            if facecard == 'A':
            	clubs.append(['Clubs','A',1])
            	spades.append(['Spades','A',1])
            	diamonds.append(['Diamonds','A',1])
            	hearts.append(['Hearts','A',1])

            else:
                clubs.append(['Clubs',facecard,10])
                spades.append(['Spades',facecard,10])
                diamonds.append(['Diamonds',facecard,10])
                hearts.append(['Hearts',facecard,10])

        # append suites to list deck
        for i in range(13):
        	self.deck.append(clubs[i])
        for i in range(13):
        	self.deck.append(spades[i])
        for i in range(13):
        	self.deck.append(diamonds[i])
        for i in range(13):
        	self.deck.append(hearts[i])

    # **** End of Deck.create_deck() **** #


    def get_deck(self):
    	return self.deck

    # **** End of Deck.get_deck() **** #


    def shuffle_deck(self):

        # shuffle the deck 10 times to be sure the deck is well shuffled
        for i in range (10):
            random.shuffle(self.deck)

    # **** End of Deck.shuffle_deck() **** #


    def deal_card(self):
        # method will take card from self.deck[0]
        # method will append card to self.hand
        # method will pop the card off of self.deck
        card = self.deck[0]
        self.deck.pop(0)
        self.deck_count = len(self.deck)

        return card

    # **** End of Deck.deal_player_card() **** #

# **** End of class Deck() **** #


class Hand():

    def __init__(self):

        self.name = ''
        self.hand = []
        self.total = 0
        self.bust = False
        self.blackjack = False
        self.final = ''        # self.final will be determined at the end of the game

    # **** End of Hand.__init__() **** #


    ##########################################
    #                                        #
    #         Methods for self.name          #
    #                                        #
    ##########################################

    def get_name(self):
        return self.name

    # **** End of Hand.get_name() **** #


    ##########################################
    #                                        #
    #         Methods for self.hand          #
    #                                        #
    ##########################################

    def update_hand(self, card):
        self.card = card
        self.hand.append(card)

    # **** End of Hand.update_hand() **** #


    def get_hand(self):
        return self.hand

    # **** End of Hand.get_hand() **** #


    ##########################################
    #                                        #
    #         Methods for self.total         #
    #                                        #
    ##########################################

    def get_total(self):
        return self.total

    # **** End of Hand.get_total() **** #

    ##########################################
    #                                        #
    #         Methods for self.bust          #
    #                                        #
    ##########################################

    def get_bust(self):
        return self.bust

    # **** End of Hand.get_bust() **** #


    ##########################################
    #                                        #
    #      Methods for self.blackjack        #
    #                                        #
    ##########################################

    def get_blackjack(self):
        return self.blackjack

    # **** End of Hand.get_blackjack() **** #


    def get_final(self):
        return self.final

    # **** End of Hand.final() **** #


class Dealer(Hand):

    def __init__(self):

    	# call Deck.__init__(self)
        Hand.__init__(self)

        # dealer facedown, hand, cards_total
        # the 1st card of dealer hand is facedown until all players are done taking hits
        self.facedown = True

        self.list_of_names = ['Wheeler Dealer Sam', \
                              'Shotgun Willy', \
                              'Dealer Jim', \
                              'Slick Sue', \
                              'Slim Jim', \
                              'Chuck the Shark', \
                              'Fast Fred', \
                              'Hank the Tank', \
                              'Smokey Joe', \
                              'Fat Frank', \
                              'Chubby Jon', \
                              'Dan the Man']

    # **** End of Dealer.__init__() **** #


    def init_new_game(self):

        # player's want to play again so assign attributes to default values
        #
        # initialize following attributes to default
        self.hand      = []
        self.total     = 0
        self.bust      = False
        self.blackjack = False
        self.facedown  = True
        self.final     = ''
    
    # **** End of Dealer.init_new_game() **** #


    def print_after_init_new_game(self):

        # this is for debugging purposes
        print("Initialized to")
        print("self.hand      = [] ......... Actual {}".format(self.hand))
        print("self.total     = 0  ......... Actual {}".format(self.total))
        print("self.bust      = False ...... Actual {}".format(self.bust))
        print("self.blackjack = False ...... Actual {}".format(self.blackjack))
        print("self.facedown  = True ....... Actual {}".format(self.facedown))
        print("self.final     = '' ......... Actual {}".format(self.final))

    # **** End of Dealer.init_new_game() **** #


    def random_dealer_name(self):

        # this method will create a random number from 50-100
        #
        # the random number will be used to shuffle self.list_of_names so the dealer name will be different each hand
        num = random.randint(50,101)
        count = 1

        while count != num:
            random.shuffle(self.list_of_names)
            count += 1

        index = random.randint(0, len(self.list_of_names)-1)

        return 'Dealer: ' + self.list_of_names[index]

    # **** End of Dealer.random_dealer_name() **** #


    def get_hand(self):

        # if self.facedown determines which card in dealer's hand will be facedown
        if self.facedown:
            hand = [['Facedown'], self.hand[1]]
            return hand

        # no card is facedown, both cards are face-up
        else:
            return self.hand

    # **** End of Dealer.get_hand() **** #


    def is_blackjack(self):

        # 1. 1st two cards dealt to each player
        # 2. all players have completed hit or stay
        # 3. dealers 2nd card is shown and checking for natural Black Jack for dealer
        # 
        # format of self.hand
        # [['Clubs',x,i], ['Spades','A',1], ['Diamonds','K',10]]
        if (self.hand[0][2] == 10 and self.hand[1][1] == 'A') and not self.facedown:
            self.total = 21
            self.blackjack = True

        elif (self.hand[1][2] == 10 and self.hand[0][1] == 'A') and not self.facedown:
            self.total = 21
            self.blackjack = True


    # **** End of Dealer.is_blackjack() **** #


    def calculate_hand(self):

        # if player does not have blackjack and if player has not busted
        # continue to calculate the total of all cards in hand
        if not self.blackjack and not self.bust and not self.facedown:

            # format of self.hand
            # [['Clubs',x,i], ['Spades','A',1], ['Diamonds','K',10]]
            #
            # assign ace_exist to False
            # if ace_exist = True you can add 10 to total and calculate if BUST or not-BUST
            ace_exist = False
            for card in self.hand:
                if card[1] == 'A':
                    ace_exist = True
                    break

            ##################################################################
            #
            #    calculate the sum of the dealer hand
            #
            ##################################################################

            # assign total to 0 before entering for loop to calculate total
            self.total = 0

            # calculate the sum for all cards in self.hand
            for card in self.hand:
                self.total += card[2]   # card example: card = ['Spades', '5', 5]

            if (ace_exist) and (self.total + 10 <= 21):
                self.total += 10

            ################################
            #
            #    check if dealer BUST
            #
            ################################

            if self.total > 21:
                self.bust = True

    # **** End of Dealer.calculate_hand() **** #


    def no_facedown(self):
        self.facedown = False

    # **** End of Dealer.no_facedown() **** #


    def update_final(self):

        if self.blackjack:
            self.final = '**** BLACKJACK ****'
        elif self.bust:
            self.final = '**** BUST ****'

    # **** End of Dealer.update_final() **** #


# **** End of class Dealer() **** #


class Player(Hand):

    def __init__(self):

        # call Hand.__init__(self)
        Hand.__init__(self)

        self.bank = 0
        self.bet  = 0

        # game result win, lose or draw
        self.win  = False
        self.lose = False
        self.draw = False

    # **** End of Player.__init__() **** #


    def init_new_game(self):

        # initialize following attributes to default
        self.hand      = []
        self.total     = 0
        self.bet       = 0
        self.bust      = False
        self.blackjack = False
        self.win       = False
        self.lose      = False
        self.draw      = False
        self.final     = ''
    
    # **** End of Player.init_new_game() **** #


    def print_after_init_new_game(self):

        # for debug purposes only
        print("Initialized to")
        print("self.hand      = [] ......... Actual {}".format(self.hand))
        print("self.total     = 0  ......... Actual {}".format(self.total))
        print("self.bet       = 0  ......... Actual {}".format(self.bet))
        print("self.bust      = False ...... Actual {}".format(self.bust))
        print("self.blackjack = False ...... Actual {}".format(self.blackjack))
        print("self.win       = False ...... Actual {}".format(self.win))
        print("self.lose      = False ...... Actual {}".format(self.lose))
        print("self.draw      = False ...... Actual {}".format(self.draw))
        print("self.final     = '' ......... Actual {}".format(self.final))

    # **** End of Player.init_new_game() **** #


    def is_blackjack(self):

        # 1st two cards dealt and checking for a natural Black Jack for each player
        # 
        # format of self.hand
        # [['Clubs',x,i], ['Spades','A',1], ['Diamonds','K',10]]
        if (self.hand[0][2] == 10 and self.hand[1][1] == 'A'):
            self.total = 21
            self.blackjack = True

        elif (self.hand[1][2] == 10 and self.hand[0][1] == 'A'):
            self.total = 21
            self.blackjack = True

    # **** End of Player.is_blackjack() **** #


    ##########################################
    #                                        #
    #         Methods for self.bank          #
    #                                        #
    ##########################################


    def get_bank(self):
        return self.bank

    # **** End of Player.get_bank() **** #


    def add_bank(self, amount):
    	self.bank += amount

    # **** End of Player.add_bank() **** #


    def minus_bank(self, amount):
    	self.bank -= amount

    # **** End of Player.minus_bank() **** #


    ##########################################
    #                                        #
    #         Methods for self.bet           #
    #                                        #
    ##########################################

    def update_bet(self, bet):
        self.bet += bet

    # **** End of Player.update_bet() **** #


    def get_bet(self):
        return self.bet

    # **** End of Player.get_bet() **** #


    ##########################################
    #                                        #
    #         Methods for self.win           #
    #                     self.lose          #
    #                     self.draw          #
    #                     self.final         #
    #                                        #
    ##########################################

    def set_win(self):
        self.win = True

    # **** End of Player.set_win() **** #


    def get_win(self):
        return self.win

    # **** End of Player.get_win() **** #


    def receive_win(self):

        if self.blackjack:
            self.bank += self.bet + (self.bet * 1.5)

        else:
            self.bank += self.bet * 2

    # **** End of Player.receive_win() **** #


    def set_lose(self):
        self.lose = True

    # **** End of Player.set_lose() **** #


    def get_lose(self):
        return self.lose

    # **** End of Player.get_lose() **** #


    def set_draw(self):
        self.draw = True

    # **** End of Player.set_draw() **** #


    def receive_draw(self):
        self.bank += self.bet

    # **** End of Player.receive_draw() **** #


    def get_draw(self):
        return self.draw

    # **** End of Player.get_draw() **** #


    def update_final(self):

        if self.win:
            if self.blackjack:
                self.final = '**** BLACKJACK ****'

            else:
                self.final = '**** WIN ****'

        elif self.draw:
            self.final     = '**** DRAW ****'

        elif self.lose:
            if self.bust:
                self.final = '**** BUST ****'

            else:
                self.final = '**** LOSE ****'


    # **** End of Player.update_final() **** #


    ##########################################
    #                                        #
    #       Method to calculate_hand         #
    #                                        #
    ##########################################

    def calculate_hand(self):

        # if player does not have blackjack and if player has not busted
        # continue to calculate the total of all cards in hand
        # if total > 21 then self.bust will be assigned True
        if not self.blackjack and not self.bust:

            # format of self.hand
            # [['Clubs',x,i], ['Spades','A',1], ['Diamonds','K',10]]
            #
            # assign ace_exist to False
            # if ace_exist = True you can add 10 to total and calculate if BUST or not-BUST
            ace_exist = False

            for card in self.hand:

                if card[1] == 'A':
                    ace_exist = True
                    break

            ##################################################################
            #
            #    calculate the sum of the player hand
            #
            ##################################################################

            # assign total to 0 before entering for loop to calculate total
            self.total = 0

            # calculate the sum for all cards in self.hand
            for card in self.hand:
                value = card[2]
                self.total += value

            if (ace_exist == True) and (self.total + 10 <= 21):
                self.total += 10

            ##################################################################
            #
            #    check if player BUST
            #
            ##################################################################

            if self.total > 21:
                self.bust = True

    # **** End of Player.calculate_hand() **** #  


# **** End of class Player() **** #


class Banner():
    '''
    class Banner() is a template used for creating different banners to display during the blackjack game.

    Functions that will create objects of class Banner()
    welcome_banner()
    lets_play_blackjack_banner()
    thank_you_for_playing_banner()
    player_removed_from_table_banner()
    generate_banner()
    '''

    def __init__(self, cards_list, string_list):

        self.row_length         = 77              # length of all banner rows
        self.first_and_last_row = ''              # 1st and last row of banner
        self.blank_space_row    = ''              # rows in banner with blank spaces
        self.string_list        = string_list     # a list of strings for string display
        self.cards_list         = cards_list      # a list of rows for cards display

    # **** End of Banner.__init__() **** #


    def create_first_and_last_row(self):

        # create_first_and_last_row will create a string of asterisks.
        # the number of asterisks == self.row_length
        for i in range(self.row_length):
            self.first_and_last_row = self.first_and_last_row + '*'

    # **** End of Banner.create_first_and_last_row() **** #


    def get_first_and_last_row(self):

        # return the self.first_and_last_row to display in banner
        return self.first_and_last_row

    # **** End of Banner.get_first_and_last_row() **** #


    def create_blank_space_row(self):

        # create_blank_space_row will create a string of with an asterisks as 1st character and last character.
        # characters between 1st and last asterisks will be a " "
        for i in range(self.row_length):
            if i == 0 or i == self.row_length -1:
                self.blank_space_row = self.blank_space_row + "*"
            else:
                self.blank_space_row = self.blank_space_row + " "


    # **** End of Banner.create_blank_space_row() **** #


    def get_blank_space_row(self):

        # return self.blank_space_row to display in banner
        return self.blank_space_row

    # **** End of Banner.get_blank_space_row() **** #


    def create_cards_list(self):

        # create_cards_row() will take the strings stored in self.cards_list and pad with " " so the cards strings
        # passed in as *args are placed in the middle of the self.row_length 
        # 
        # the 1st and last character of each string will be an asterisks*

        asterisk = "*"

        for i in range(len(self.cards_list)):

            # number of spaces and/or characters between the first and last asterisk in the new_string
            num_spaces = self.row_length -2

            # determine number of " "es before string and after string
            #
            # it appears colorama is adding length to the string of index[2]. Hard coding length as 15
            #before = int((num_spaces - len(self.cards_list[i])) / 2)   # number of spaces "before" self.cards_list[i]
            #after  = num_spaces - (before + len(self.cards_list[i]))   # number of spaces "after"  self.cards_list[i]
            before = int((num_spaces - 15) / 2)   # number of spaces "before" self.cards_list[i]
            after  = num_spaces - (before + 15)   # number of spaces "after"  self.cards_list[i]

            before_string_spaces = ''
            after_string_spaces  = ''

            for x in range(before):
                before_string_spaces = before_string_spaces + " "
            for x in range(after):
                after_string_spaces = after_string_spaces + " "

            self.cards_list[i] = asterisk + before_string_spaces + self.cards_list[i] + after_string_spaces + asterisk

    # **** End of Banner.create_cards_list() **** #


    def get_cards_list(self):

        # returns playing cards for banner display
        return self.cards_list

    # **** End of Banner.get_cards_list() **** #


    def create_string_list(self):

        # create_string_row() will take the strings stored in self.string_list and pad with " " so the strings
        # passed in as *args are placed in the middle of the self.row_length 
        # 
        # the 1st and last character of each string will be an asterisks*

        asterisk = "*"

        for i in range(len(self.string_list)):

            # number of spaces and/or characters between the first and last asterisk in the new_string
            num_spaces = self.row_length -2

            # determine number of " "es before string and after string
            before = int((num_spaces - len(self.string_list[i])) / 2)   # number of spaces "before" self.string_list[i]
            after  = num_spaces - (before + len(self.string_list[i]))   # number of spaces "after"  self.string_list[i]

            before_string_spaces = ''
            after_string_spaces  = ''

            for x in range(before):
                before_string_spaces = before_string_spaces + " "
            for x in range(after):
                after_string_spaces = after_string_spaces + " "

            self.string_list[i] = asterisk + before_string_spaces + self.string_list[i] + after_string_spaces + asterisk


    # **** End of Banner.create_string_list() **** #

    def get_string_list(self):

        # returns self.string_list for display in banner
        return self.string_list

    # **** End of Banner.get_string_list() **** #

# **** End of class Banner() **** #