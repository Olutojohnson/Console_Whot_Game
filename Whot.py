import random


def play(move, player, card, market_):
    if move.lower() == "p":
        player.append(random.choice(market_))
        market_.pop(market_.index(player[-1]))
        return [market_, card, player]
    elif move in num:
        player_play_split = (player[int(move) - 1]).split(" ")
        play_card_split = card.split(" ")
        if player_play_split[1] == "Whot":
            card = player[int(move) - 1]
            player.pop(player.index(player[int(move) - 1]))
            while True:
                need = input("I need ").capitalize()
                if need == "Circle" or need == "Triangle" or need == "Cross" or need == "Square" or need == "Star":
                    return [market_, card, player, need]
                else:
                    print("Wrong card shape. Try again")
        elif player_play_split[0] == play_card_split[0] or player_play_split[1] == play_card_split[1]:
            card = player[int(move) - 1]
            player.pop(player.index(player[int(move) - 1]))
            return [market_, card, player]
        else:
            print("Wrong play")
            player.append(random.choice(market_))
            market_.pop(market_.index(player[-1]))
            return [market_, card, player]
    else:
        new = input("Enter valid option")
        return play(new, player, card, market_)


circle = ['1 Circle', '2 Circle', '3 Circle', '4 Circle', '5 Circle', '7 Circle', '8 Circle', '10 Circle', '11 Circle',
          '12 Circle', '13 Circle', '14 Circle']
triangle = ['1 Triangle', '2 Triangle', '3 Triangle', '4 Triangle', '5 Triangle', '7 Triangle', '8 Triangle',
            '10 Triangle', '11 Triangle', '12 Triangle', '13 Triangle', '14 Triangle']
cross = ['1 Cross', '2 Cross', '3 Cross', '5 Cross', '7 Cross', '10 Cross', '11 Cross', '13 Cross', '14 Cross']
square = ['1 Square', '2 Square', '3 Square', '5 Square', '7 Square', '10 Square', '11 Square', '13 Square',
          '14 Square']
star = ['1 Star', '2 Star', '3 Star', '4 Star', '5 Star', '7 Star', '8 Star']
whot = ["20 Whot", "20 Whot", "20 Whot"]
num = "0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354"
deck = circle + triangle + cross + square + star + whot
player_1 = []
player_2 = []
while len(player_1) < 5:
    draw = random.choice(deck)
    if draw not in player_1:
        player_1.append(draw)
        deck.pop(deck.index(draw))
while len(player_2) < 5:
    draw = random.choice(deck)
    if draw not in player_2:
        player_2.append(draw)
        deck.pop(deck.index(draw))
while True:
    playing_card = random.choice(deck)
    if playing_card.split(" ")[1] != "Whot":
        deck.pop(deck.index(playing_card))
        break
market = deck
res = ""
while len(market) > 0:
    if len(res) == 4:
        print(f"Play a {res[3]} card")
        playing_card = f"n {res[3]}"
    print(f"\t\t\t\t\t\t\t\tPLAYER 1\n{playing_card}")
    for i in range(len(player_1)):
        print(f"({i + 1}) {player_1[i]}", end=" ")
    player_1_play = str(input("\nEnter number corresponding to card to play or enter P to pick from the market"))
    res = play(player_1_play, player_1, playing_card, market)
    market = res[0]
    playing_card = res[1]
    player_1 = res[2]
    if len(player_1) == 0:
        print("\nCheck Up\nPLAYER 1 wins")
        break
    print("\t\t\t\t\t\t\t\tPLAYER 2")
    if len(res) == 4:
        print(f"Play a {res[3]} card")
        playing_card = f"n {res[3]}"
    print(playing_card)
    for i in range(len(player_2)):
        print(f"({i + 1}) {player_2[i]}", end=" ")
    player_2_play = str(input("\nEnter number corresponding to card to play or enter P to pick from the market"))
    res = play(player_2_play, player_2, playing_card, market)
    market = res[0]
    playing_card = res[1]
    player_2 = res[2]
    if len(player_2) == 0:
        print("\nCheck up\nPlayer 2 wins")
        break
if len(market) == 0:
    print("Market Empty")
    player_1_score = 0
    player_2_score = 0
    point = 0
    for i in range(len(player_1)):
        point = int(player_1[i].split(" ")[0])
        player_1_score += point
    for i in range(len(player_2)):
        point = int(player_1[i].split(" ")[0])
        player_2_score += point
    winner = min(player_1_score, player_2_score)
    if winner == player_1_score:
        print("\nPlayer 1 has a lesser score\nPLAYER 1 WINS!")
    else:
        print("\nPlayer 1 has a lesser score\nPLAYER 2 WINS")
