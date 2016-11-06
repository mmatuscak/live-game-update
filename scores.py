#!/usr/bin/env python

import requests
import exceptions
import sys
import json
from termcolor import colored
import parseNFL
import parseNHL

# TODO: add NBA_URL

def main():
    if (len(sys.argv) < 2):
        raise exceptions.tooFewArgsException

    leagues = ['nhl', 'nfl', 'nba']
    league = sys.argv[1]

    if league.lower() not in  leagues:
        raise exceptions.incorrectLeagueException
    elif league == 'nfl':
        week, games = parseNFL.get_json()
        parseNFL.print_week(week, games)
    elif league == 'nhl':
        games = parseNHL.get_json()
        parseNHL.print_week(games)
    elif league == 'nba':
        return 


if __name__ == '__main__':
    main()
