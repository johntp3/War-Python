from Playing_Cards import *
from random import *


def two_man_war(player1_cards, player1_reserve, player2_cards, player2_reserve, id1, id2):
    # loop will run if all of these lists are not empty
    while (player1_cards or player1_reserve) and (player2_cards or player2_reserve):
        # resets both comparison cards to null
        card1 = None
        card2 = None
        try:
            # tries to get comparison cards from card reserve lists
            # this occurs after a war (even if main card list of a player is empty)
            card1 = player1_reserve.pop()
            card2 = player2_reserve.pop()
        except IndexError:
            # otherwise get comparison cards from main card lists
            # this occurs in standard play (no wars)
            card1 = player1_cards.pop(0)
            card2 = player2_cards.pop(0)

        if card1.card.value > card2.card.value:  # player 1 wins battle
            # declaration of player 1's success
            print("Player " + id1 + " wins with " + str(card1) + " against Player " + id2 + "'s " + str(card2))
            # appends the comparison cards and cards in reserve (if any) to player 1's main list
            player1_cards.append(card1)
            player1_cards.append(card2)
            player1_cards.extend(player1_reserve+player2_reserve)
            player1_reserve = []
            player2_reserve = []
        elif card1.card.value < card2.card.value:  # player 2 wins battle
            # declaration of player 2's success
            print("Player " + id2 + " wins with " + str(card2) + " against Player " + id1 + "'s " + str(card1))
            # appends the comparison cards and cards in reserve (if any) to player 2's main list
            player2_cards.append(card2)
            player2_cards.append(card1)
            player2_cards.extend(player2_reserve+player1_reserve)
            player1_reserve = []
            player2_reserve = []
        else:  # WAR!
            # puts comparison cards in reserve lists
            player1_reserve.append(card1)
            player2_reserve.append(card2)
            # declaration of war
            print("WAR --> Player " + id1 + ": " + str(card1) + "   Player " + id2 + ": " + str(card2))
            war2(player1_cards, player1_reserve, player2_cards, player2_reserve)
        # shows the amount of cards in main list for each player after this loop's interaction
        print("cards left " + id1 + ": " + str(len(player1_cards)) +
              "      cards left " + id2 + ": " + str(len(player2_cards)))


def war2(player1_cards, player1_reserve, player2_cards, player2_reserve):
    counter = 0
    # puts 3 cards for war in reserve list if the player has enough cards in main list
    # if not, takes remaining cards and puts them in reserve list
    while player1_cards and counter < 3:
        player1_reserve.append(player1_cards.pop(0))
        counter += 1
    counter = 0
    while player2_cards and counter < 3:
        player2_reserve.append(player2_cards.pop(0))
        counter += 1


if __name__ == '__main__':
    create_deck()
    shuffle(full_deck)
    # assigns first half of random deck to player 1 and second half to player 2
    player1_cardsa = full_deck[:int(len(full_deck) / 2)]
    player2_cardsa = full_deck[int(len(full_deck) / 2):]
    # reserve lists are used to hold cards from war aftermath (prisoners of war)
    player1_reservea = []
    player2_reservea = []
    two_man_war(player1_cardsa, player1_reservea, player2_cardsa, player2_reservea, "1", "2")
    # declaration of game winner
    if player1_cardsa:
        print("\nCongratulations player 1! You won the game!")
    else:
        print("\nCongratulations player 2! You won the game!")
