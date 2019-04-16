# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:19:21 2019

@author: Frank Nardone
"""

from scr.roster import getGameId, getRoster, getTeamId

leaugeId = 59224

try:
    #gameId = getGameId("mlb")
    #print(getRoster(388, leaugeId,8))
    print(getTeamId(388, leaugeId, 'f'))
except:
    print("Exception!!!!!")

