import requests
import json
from termcolor import colored

NHL_URL = "http://live.nhl.com/GameData/RegularSeasonScoreboardv3.jsonp"

def print_week(games):
    """Prints Scores. VISITOR: ##  HOME: ##""" 

    print('\t\t', colored("VISITOR", 'red'),'\t\t', colored("HOME", 'blue'))

    day_prev = games[0]['ts']
    print(colored("{}".format(day_prev), 'white'))

    for game in games:
        day = game['ts']
        time = game['bs'] # game start time, EST
        home = game['htn'] + ":"
        visitor = game['atn'] + ":"
        h_score = game['hts']
        v_score = game['ats']
        if day_prev != day:
            print(colored("{}".format(day), 'white'))
        print("{:<9s} - {:<13s} {}\t{:<13s}{}".format(time, visitor, v_score, home, h_score))
        day_prev = day

def get_json():
    r = requests.get(NHL_URL)
    rjson = r.text[r.text.index("(") + 1 : r.text.rindex(")")]
    j_data = json.loads(rjson)
    games = j_data['games']

    return games
