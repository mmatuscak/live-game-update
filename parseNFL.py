import requests
import json
from termcolor import colored

NFL_URL = "http://www.nfl.com/liveupdate/scorestrip/ss.json"

def print_week(week, games):
    """Prints Scores. VISITOR: ##  HOME: ##""" 

    print(colored("-------- WEEK {} --------".format(week), 'white'))
    print(colored("VISITOR", 'red'),'\t', colored("HOME", 'blue'))

    day_prev = games[0]['d']
    print(colored("{}".format(day_prev), 'white'))

    for game in games:
        day = game['d']
        time = game['t'] # game start time, EST
        home = game['h']
        visitor = game['v']
        h_score = game['hs']
        v_score = game['vs']
        if day_prev != day:
            print(colored("{}".format(day), 'white'))
        print("{} - {:<4s}:{:>3d}\t{:<4s}:{:>3d}".format(time, visitor, v_score, home, h_score))
        day_prev = day

def get_json():
    r = requests.get(NFL_URL)
    j = json.dumps(r.json())
    j_data = json.loads(j)
    week = j_data['w']
    games = j_data['gms']

    return week, games
