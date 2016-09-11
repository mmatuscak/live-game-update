#!/usr/bin/env python

import requests
import exceptions
import sys
import json
from termcolor import colored

NFL_URL = "http://www.nfl.com/liveupdate/scorestrip/ss.json"
NHL_URL = "http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp"
# TODO: add NBA_URL

def print_week(week, games):
    """Prints Scores. VISITOR: ##  HOME: ##""" 

    print(colored("-------- WEEK {} --------".format(week), 'red'))
    print(colored("VISITOR", 'red'),'\t', colored("HOME", 'blue'))

    for game in games:
        day = game['d']
        time = game['t']
        home = game['h']
        visitor = game['v']
        h_score = game['hs']
        v_score = game['vs']
        print("{:<4s}:{:>3d}\t{:<4s}:{:>3d}".format(visitor, v_score, home, h_score))

def get_json(url):
    r = requests.get(NFL_URL)
    j = json.dumps(r.json())
    j_data = json.loads(j)
    week = j_data['w']
    games = j_data['gms']

    return week, games

def main():
    if (len(sys.argv) < 2):
        raise exceptions.tooFewArgsException

    leagues = ['nhl', 'nfl', 'nba']
    league = sys.argv[1]

    if league.lower() not in  leagues:
        raise exceptions.incorrectLeagueException
    else:
        week, games = get_json(NFL_URL)

    print_week(week, games)


if __name__ == '__main__':
    main()
