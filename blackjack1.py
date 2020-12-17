##Blackjack game on python
#computer dealer and a human player: create a deck of cards on python
suits = ("hearts","diamonds","spades","club")
ranks_temp = "two three four five six seven eight nine ten jack queen king ace"
ranks = tuple(ranks_temp.split())
values_1 = {"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "jack":10, "queen":10, "king":10, "ace":11 }
values_11 = {"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "jack":10, "queen":10, "king":10, "ace":1 }
class Card():
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.values1 = values_1[rank]
        self.values11 = values_11[rank]
    def __str__(self):
        return self.rank +" of "+ self.suit
##########################################################################################################################

import random
class Deck1():
    def __init__(self):
        self.card = []
        self.complete_deck = []
        for i in range(0,4):
            for j in range(0,13):
                self.card = Card(ranks[j],suits[i])
                self.complete_deck.append(self.card)
                
    def shuffle_deck(self):
        random.shuffle(self.complete_deck)
        
    def deal_one(self):
        return self.complete_deck.pop()
    
        
#############################################################################################################################

import numpy as np
class Player():
    def __init__(self,name,chips):
        self.name = name
        self.cards = []
        self.chips = chips
        
    def bet_chips(self,num_chips_bet):
        if self.chips == 0:
            print("Sorry you do not have enough chips")
            
        else:
            self.chips = self.chips - num_chips_bet
            
    def add_chips(self,num_chips):
        self.chips = self.chips+num_chips
            
    def add_one_card(self,card):
        self.cards.append(card)
    
    def __str__(self):
        return f"{self.name} has {self.chips} chips"
############################################################################################################################

class Dealer():
    def __init__ (self):
        self.cards = []
        self.name = "Computer"
    def add_one_card (self,card):
        self.cards.append(card)
    def remove_one_card (self):
        self.cards.pop()
    pass


## Blackjack logic#########################
game_on = True
ranks_pl1 = []
suits_pl1 = []
values_pl1 = []
suits_dlr = []
ranks_dlr = []
values_dlr = []
total_chips = int(input("How many chips do you want to buy in? "))
betting_amount  = 0
remaining_chips = total_chips
#player1 = Player("Chinmay", total_chips)
#deck1 = Deck()
#dealer1 = Dealer()
#print(len(list(deck1.cards)))
while game_on == True:
    
    player1 = Player("Chinmay", remaining_chips)
    sum_pl1 = 0
    sum_dlr = 0
    ranks_pl1 = []
    suits_pl1 = []
    values_pl1 = []
    suits_dlr = []
    ranks_dlr = []
    values_dlr = []
    deck1 = Deck1()
    deck1.shuffle_deck()
    deck_list = []
    for i in deck1.complete_deck:
        deck_list.append(i)
    print(len(deck_list))
    dealer1 = Dealer()
    betting_amount = int(input("How many chips do you want to bet: "))
    remaining_chips_1 = remaining_chips-betting_amount
    if remaining_chips == 0:
        print("Nothing left to bet")
        break
    
    while remaining_chips_1 < 0:
        print(f"Not enough chips, remaining chips = {remaining_chips}")
        betting_amount = int(input("How many chips do you want to bet: "))
        remaining_chips_1 = remaining_chips-betting_amount
    remaining_chips = remaining_chips_1
    player1_wins_flag = 0
    dealer_wins_flag = 0
    ###DEAL the cards####
    for i in range(2):
        player1.add_one_card(deck_list.pop())
        dealer1.add_one_card(deck_list.pop())
    print("Chinmay has:1")
    for item in player1.cards:
        print(item.rank + " of " + item.suit)
    print(f"dealer has an uncovered card: {list(dealer1.cards)[0]}")
    ######A condition for burst needs to be added here#####
    for item in player1.cards:
        ranks_pl1.append(item.rank)
        values_pl1.append(item.values1)
        suits_pl1.append(item.suit)
    print(values_pl1)
    
    if ranks_pl1.count("ace") == 0:
        sum_pl1 = np.sum(values_pl1)
    if ranks_pl1.count("ace") == 1:
        sum_pl1 = np.sum(values_pl1)+10
    if ranks_pl1.count("ace") == 2:
        sum_pl1 = 12
        
    if sum_pl1>21:
        dealer_wins_flag = 1
        player1_wins_flag = 0
        print("Dealer wins")
    elif sum_pl1 == 21:
        player1_wins_flag = 1
        dealer_wins_flag = 0
        print("Chinmay wins")
    ###if sum of player_cards.values >21, player loses. else everything else.
    
    else:
        hit = True
        while hit == True:
            player_action = input("Do you want to hit or stay?: ")
            if player_action == "hit":
                player1.add_one_card(deck_list.pop())
                print("Chinmay has1:")
                for item in player1.cards:
                    print(item.rank + " of " + item.suit)
            else:
                hit  = False
                break
    ######A condition for burst needs to be added here#####
        print(len(deck_list))
        ranks_pl1.clear()
        values_pl1.clear()
        suits_pl1.clear()
        for item in player1.cards:
            ranks_pl1.append(item.rank)
            values_pl1.append(item.values1)
            suits_pl1.append(item.suit)
        print(f"Values of the card that player has are {values_pl1}")
        if ranks_pl1.count("ace") == 0:
            sum_pl1 = np.sum(values_pl1)
        if ranks_pl1.count("ace") == 1:
            sum_pl1 = np.sum(values_pl1) + 10
            if sum_pl1 > 21:
                sum_pl1 = sum_pl1 -10
            else:
                pass
        if ranks_pl1.count("ace") >= 2:
            sum_pl1 = np.sum(values_pl1)
            if sum_pl1 + 10 <=21:
                sum_pl1 = sum_pl1 + 10
            else:
                pass
        print(f"sum of the cards that are with the player is {sum_pl1}")
        if sum_pl1>21:
            dealer_wins_flag = 1
            player1_wins_flag = 0
            print("Dealer wins")
        elif sum_pl1 == 21:
            player1_wins_flag = 1
            dealer_wins_flag = 0
            print("Chinmay wins")
    ###if sum of player_cards.values >21, player loses. else everything else.
    ####Dealer's turn###########
        else:
                ##Dealer's turn###
                print(len(deck_list))
                print("Dealer has:")
                for item in dealer1.cards:
                    print(item.rank + " of " + item.suit)
                
                for item in dealer1.cards:
                    ranks_dlr.append(item.rank)
                    suits_dlr.append(item.suit)
                    values_dlr.append(item.values1)
                    
                number_of_aces_dlr = ranks_dlr.count("ace")
                print(len(deck_list))
                print(sum(values_dlr))
    ##while sum of dealer's cards <17, hit
                while sum(values_dlr) < 17:
                    dealer1.add_one_card(deck_list.pop(0))
                    values_dlr.append(dealer1.cards[-1].values1)
                
                print("Dealer has:")
                for item in dealer1.cards:
                    print(item.rank + " of " + item.suit)
                    
                ranks_dlr.clear()
                suits_dlr.clear()
                values_dlr.clear()
                for item in dealer1.cards:
                    ranks_dlr.append(item.rank)
                    suits_dlr.append(item.suit)
                    values_dlr.append(item.values1)
                print(values_dlr)
                sum_dlr = sum(values_dlr)
                print(ranks_dlr)
                print(suits_dlr)
                number_of_aces_dlr = ranks_dlr.count("ace")
    #### if sum of dealer's cards>=17, print his cards.
    ####if sum of dealer's cards >21, print(Dealer has been busted)
                if number_of_aces_dlr >=1 :
                    if 21 - sum_dlr>=10:
                        sum_dlr = sum_dlr+10
                print(f"the sum of the values of dealer's cards is {sum_dlr}")
                if sum_dlr>sum_pl1 and sum_dlr<=21:
                    player1_wins_flag = 0
                    dealer_wins_flag = 1
                    print("Dealer wins")
                elif sum_dlr<sum_pl1 and sum_dlr<21:
                    player1_wins_flag = 1
                    dealer_wins_flag = 0
                    print("Chinmay wins")
                elif sum_dlr > 21:
                    print("Chinmay wins")
                    player1_wins_flag = 1
                    dealer_wins_flag = 0
                elif sum_dlr==sum_pl1:
                    print("Its a draw")
                    player1_wins_flag = 0
                    dealer_wins_flag = 0
    ####else if sum of player_cards>sum_of dealer cards, player wins player gets 3/2 the number of chips he bet.
    #### else if sum of player_cards < sum_of dealers cards,
    if player1_wins_flag ==1 :
        player1.add_chips(2*betting_amount)
    elif dealer_wins_flag == 1:
        player1.bet_chips(betting_amount)
    player1_wins_flag = 0
    dealer_wins_flag = 0
    print(player1)
    intentions = input("Do you want to keep playing? yes/no: ")
    if intentions == "yes":
        game_on = True
    else:
        game_on = False
    #### player loses all the chips. Player gets a prompt if he wants to keep playing
    ### two flags player_wins and dealer_ wins will be used to decide the fate of the chips.
    ## the cards that are with the players need to be added back to the deck.

