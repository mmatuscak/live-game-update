import requests
from lxml import etree
from termcolor import colored

#NFL_URL = "http://www.nfl.com/liveupdate/scorestrip/ss.xml"
NFL_URL = "http://www.nfl.com/liveupdate/scorestrip/postseason/ss.xml"

def print_week(week, games):
    """Prints Scores. VISITOR: ##  HOME: ##""" 

    #print(colored("-------- WEEK {} --------".format(week), 'white'))
    print(colored("-------- Postseason --------".format(week), 'white'))
    #print(colored("VISITOR", 'red'),'\t', colored("HOME", 'blue'))

    day_prev = games[0].get('d')
    print(colored("{}".format(day_prev), 'white'))

    for game in games:
        day = game.get('d')
        time = game.get('t') # game start time, EST
        home = game.get('h')
        visitor = game.get('v')
        h_score = game.get('hs')
        v_score = game.get('vs')
        if day_prev != day:
            print(colored("{}".format(day), 'white'))
        #print("{} - {:<4d}:{:>3d}\t{:<4d}:{:>3d}".format(time, visitor, v_score, home, h_score))
        print("{} - {}:{} \t@\t{}:{}".format(time, visitor, v_score, home, h_score))
        day_prev = day

def get_json():
    r = requests.get(NFL_URL)
    xml = etree.XML(r.content)
    games = xml.find('gms')
    week = games.get('w')
    games = [g for g in games.findall('g')] 

    return week, games
