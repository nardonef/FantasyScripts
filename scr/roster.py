# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:56:27 2019

@author: jjy
"""

from scr.yahoo.yahoologin import yahoologin

def updateroster(leagueid,numteams,gameid=388):
    oauth = yahoologin()
    # with open('./data/test.txt', 'w', newline = '') as outfile:
    #     csvwriter = csv.writer(outfile, delimiter='\t')
    #     outfile.truncate()
    #     csvwriter.writerow(['playerid','team'])
    #     for team in range(1, numteams+1): #assumes 10-team league
    #         url = 'https://fantasysports.yahooapis.com/fantasy/v2/team/'+str(gameid)+'.l.'+str(leagueid)+'.t.'+str(team)+'/roster'
    #         print(url)
    #         response = oauth.session.get(url, params={'format': 'json'})
    #         data = response.json()
    #         playercount = 0
    #         print(data)
    #         for item in (data["fantasy_content"]["team"][1]["roster"]["0"]["players"]):
    #             if 'count' not in item:
    #                 csvwriter.writerow([data["fantasy_content"]["team"][1]["roster"]["0"]["players"][str(playercount)]["player"][0][1]["player_id"],data["fantasy_content"]["team"][0][2]["name"]])
    #                 playercount = playercount + 1

def getGameId(gameType):
    oauth = yahoologin()
    url = 'https://fantasysports.yahooapis.com/fantasy/v2/game/' + str(gameType)
    response = oauth.session.get(url, params={'format': 'json'})
    data = response.json()

    if hasattr(data, "error"):
        return None

    return data["fantasy_content"]["game"][0]["game_id"]

def getRoster(gameid,leagueid,team):
    oauth = yahoologin()
    url = 'https://fantasysports.yahooapis.com/fantasy/v2/team/' + str(gameid) + '.l.' + str(leagueid) + '.t.' + str(team) + '/roster'
    response = oauth.session.get(url, params={'format': 'json'})
    data = response.json()
    playercount = 0
    players = []

    for item in (data["fantasy_content"]["team"][1]["roster"]["0"]["players"]):
        if 'count' not in item:
            players.append(data["fantasy_content"]["team"][1]["roster"]["0"]["players"][str(playercount)]["player"][0])
        playercount = playercount + 1

    return players

# TODO BE ABLE TO GET TEAMID BY PASSING IN
def getTeamId(gameid,leagueid):
    oauth = yahoologin()

    for team in range(1, 13):
        url = 'https://fantasysports.yahooapis.com/fantasy/v2/team/' + str(gameid) + '.l.' + str(leagueid) + '.t.' + str(team) + '/roster'
        response = oauth.session.get(url, params={'format': 'json'})
        data = response.json()

        if hasattr(data, "error"):
            return data

        if type(data["fantasy_content"]["team"][0][3]) == dict:
            return team