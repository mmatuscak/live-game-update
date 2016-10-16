import requests
import json
from termcolor import colored

NHL_URL = "http://live.nhl.com/GameData/RegularSeasonScoreboardv3.jsonp"

def get_short_name(city):
    teams = {"Pittsburgh":"PIT", "Philadelphia":"PHI", "Washington":"WAS", "NY Rangers":"NYR", \
            "Carolina":"CAR", "New Jersey":"NJD", "NY Islanders":"NYI", "Columbus":"CBJ", \
            "Florida":"FLA", "Tampa Bay":"TBL", "Ottawa":"OTT", "Montréal":"MTL", "Toronto":"TOR", \
            "Boston":"BOS", "Buffalo":"BUF", "Detroit":"DET", "St Louis":"STL", "Colorado":"COL", \
            "Dallas":"DAL", "Minnesota":"MIN", "Winnipeg":"WPG", "Nashville":"NSH", \
            "Chicago":"CHI", "Edmonton":"EDM", "San Jose":"SJS", "Arizona":"ARI", \
            "Vancouver":"VAN", "Calgary":"CGY", "Anaheim":"ANA", "Los Angeles":"LAK"}
    try:
        return teams[city]
    except KeyError:
        return city


def print_week(games):
    """Prints Scores. VISITOR: ##  HOME: ##""" 

    print('\t\t', colored("VISITOR", 'red'),'\t\t', colored("HOME", 'blue'))

    day_prev = games[0]['ts']
    print(colored("{}".format(day_prev), 'white'))

    for game in games:
        day = game['ts']
        time = game['bs'] # game start time, EST
        home = get_short_name(game['htn']) + ":"
        visitor = get_short_name(game['atn']) + ":"
        h_score = game['hts']
        v_score = game['ats']
        if day_prev != day:
            print(colored("{}".format(day), 'white'))
        print("{:<9s} - {:<4s} {}\t{:<5s}{}".format(time, visitor, v_score, home, h_score))
        day_prev = day

""" gets and parses jsonp """
""" returns all the games for the week """
def get_json():
    r = requests.get(NHL_URL)
    rjson = r.text[r.text.index("(") + 1 : r.text.rindex(")")]
    j_data = json.loads(rjson)
    games = j_data['games']

    return games
