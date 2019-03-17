from War import *


class Player:
    def __init__(self, cards, res, out):
        self.cards = cards
        self.res = res
        self.out = out


def out_count(player_list):
    countera = 0
    for player in player_list:
        if not player.cards and not player.res:
            player.out = True
        if player.out:
            countera += 1
    return countera


def three_man_war():

    shuffle(full_deck)
    # assigns p1 first 17 card, p2 next 17, and p3 the last 18 cards from the shuffled full deck
    p1 = None
    p2 = None
    p3 = None
    p1 = Player(full_deck[:int(len(full_deck)/3)], [], False)
    p2 = Player(full_deck[int(len(full_deck)/3):int(len(full_deck)*2/3)], [], False)
    p3 = Player(full_deck[int(len(full_deck)*2/3):], [], False)
    players = [p1, p2, p3]
    id1 = ""
    id2 = ""

    while out_count(players) < 2:
        if out_count(players) == 1:
            empty_index = -1
            players = [p1, p2, p3]
            if not players[0].cards:
                empty_index = 0
                id1 = "2"
                id2 = "3"
            elif not players[1].cards:
                empty_index = 1
                id1 = "1"
                id2 = "3"
            else:
                empty_index = 2
                id1 = "1"
                id2 = "2"
            players.append(players.pop(empty_index))

            two_man_war(players[0].cards, players[0].res, players[1].cards, players[1].res, id1, id2)
            if not players[0].cards:
                players[0].out = False
            else:
                players[1].out = False
            break

        else:
            card1 = None
            card2 = None
            card3 = None
            try:
                # tries to get comparison cards from card reserve lists
                # this occurs after a war (even if main card list of a player is empty)
                card1 = p1.res.pop()
                card2 = p2.res.pop()
                card3 = p3.res.pop()
            except IndexError:
                # otherwise get comparison cards from main card lists
                # this occurs in standard play (no wars)
                card1 = p1.cards.pop(0)
                card2 = p2.cards.pop(0)
                card3 = p3.cards.pop(0)

            if card1.card.value > card2.card.value and card1.card.value > card3.card.value:  # player 1 wins battle
                # declaration of player 1's success
                print("Player 1 wins with " + str(card1) + " against 2's " + str(card2) + " and 3's " + str(card3))
                # appends the comparison cards and cards in reserve (if any) to player 1's main list
                p1.cards.append(card1)
                p1.cards.append(card2)
                p1.cards.append(card3)

                p1.cards.extend(p1.res + p2.res + p3.res)
                p1.res = []
                p2.res = []
                p3.res = []

            elif card2.card.value > card1.card.value and card2.card.value > card3.card.value:  # player 2 wins battle
                # declaration of player 2's success
                print("Player 2 wins with " + str(card2) + " against 3's " + str(card3) + " and 1's " + str(card1))
                # appends the comparison cards and cards in reserve (if any) to player 2's main list
                p2.cards.append(card2)
                p2.cards.append(card3)
                p2.cards.append(card1)

                p2.cards.extend(p2.res + p3.res + p1.res)
                p1.res = []
                p2.res = []
                p3.res = []

            elif card3.card.value > card1.card.value and card3.card.value > card2.card.value:  # player 3 wins battle
                # declaration of player 3's success
                print("Player 3 wins with " + str(card3) + " against 1's " + str(card1) + " and 2's " + str(card2))
                # appends the comparison cards and cards in reserve (if any) to player 3's main list
                p3.cards.append(card1)
                p3.cards.append(card2)
                p3.cards.append(card3)

                p3.cards.extend(p3.res + p1.res + p2.res)
                p1.res = []
                p2.res = []
                p3.res = []

            elif card1.card.value == card2.card.value and card1.card.value == card3.card.value:
                # Three Man War
                p1.res.append(card1)
                p2.res.append(card2)
                p3.res.append(card3)
                # declaration of war
                print("3-WAY WAR --> Player 1: " + str(card1) + " Player 2: " + str(card2) + " Player 3: " + str(card3))

                counter = 0
                while p1.cards and counter < 3:
                    p1.res.append(p1.cards.pop(0))
                    counter += 1
                counter = 0
                while p2.cards and counter < 3:
                    p2.res.append(p2.cards.pop(0))
                    counter += 1
                counter = 0
                while p3.cards and counter < 3:
                    p3.res.append(p3.cards.pop(0))
                    counter += 1

            else:  # means there is one pair of war that is higher in value than the remaining card
                # Two Man War
                unequal_index = -1
                players = [p1, p2, p3]

                if card1.card.value != card2.card.value and card1.card.value != card3.card.value:
                    unequal_index = 0
                    id1 = "2"
                    id2 = "3"
                elif card2.card.value != card1.card.value and card2.card.value != card3.card.value:
                    unequal_index = 1
                    id1 = "1"
                    id2 = "3"
                else:
                    unequal_index = 2
                    id1 = "1"
                    id2 = "2"
                players.append(players.pop(unequal_index))

                p1.res.append(card1)
                p2.res.append(card2)
                p3.res.append(card3)
                # declaration of war
                print("WAR --> Player " + id1 + ": " + str(players[0].res[-1]) + "   Player " + id2 +
                      ": " + str(players[1].res[-1]))
                war2(players[0].cards, players[0].res, players[1].cards, players[1].res)
        print("cards left 1: " + str(len(p1.cards)) + "      cards left 2: " + str(len(p2.cards)) +
              "      cards left 3: " + str(len(p3.cards)))

    if p1.cards:
        print("\nCongratulations player 1! You won the game!")
        return 1
    elif p2.cards:
        print("\nCongratulations player 2! You won the game!")
        return 2
    else:
        print("\nCongratulations player 3! You won the game!")
        return 3


one_win = 0
two_win = 0
three_win = 0
create_deck()
for x in range(1000):
    winner = three_man_war()
    if winner == 1:
        one_win += 1
    elif winner == 2:
        two_win += 1
    else:
        three_win += 1
print("Wins for Player One: " + str(one_win))
print("Wins for Player Two: " + str(two_win))
print("Wins for Player Three: " + str(three_win))
