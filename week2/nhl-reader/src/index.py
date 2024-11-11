import requests
from player import Player

def if_player_fin(player_dict):
    return player_dict['nationality'] == "FIN"

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    fin_players = filter(if_player_fin, response)
    players = []

    for player_dict in fin_players:
        player = Player(player_dict)
        players.append(player)

    players.sort(reverse=True)

    print("Players from FIN\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
