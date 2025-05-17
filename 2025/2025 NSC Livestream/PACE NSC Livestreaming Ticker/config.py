import obswebsocket
from obswebsocket import *
import threading
import time
import linecache
import os
import tkinter as tk
from tkinter import ttk
from enum import *
import json
import re
import requests
from requests.auth import HTTPBasicAuth
from PIL import ImageFont, ImageDraw, Image
from functools import cmp_to_key, partial
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import urllib.request
import data, sss, unicodedata
from bs4 import BeautifulSoup
import fss, cornerstone, spotify, PyATEMMax, harry
from secrets import *

LIVE = False

NUM_TEAMS = 84



PRELIMS_START_ROUND = 1
PRELIMS_END_ROUND = 5


#ATEM Variables
ATEM_IP = "192.168.10.240"

ATEM_COMPUTER_INPUT = 1
ATEM_TEAM1 = 3
ATEM_TEAM2 = 4
ATEM_HOST_AREA = 6
ATEM_INTERVIEW = 7
ATEM_SIDESHOT = 8

# Define connection parameters
OBS_HOST = "192.168.1.15"  # Replace with the IP address if running on another machine
OBS_PORT = 4455         # Default WebSocket port
OBS_PASSWORD = "tpv5M8fcv2UQlFFU"  # Replace with your WebSocket password

#MAIN SCENES
GAME_ROOM = "Game Room"
HOST_AREA = "Host Area"
INTERVIEW_AREA = "Interview Area"

#SIDE SCENES
DONATE_TO_PACE = "Donate to PACE"
START_A_TEAM = "Start a Team"
FULL_SCREEN_STATS = "Full Screen Stats"
SIDE_SCREEN_STATS = "Side Screen Stats"
SIDESHOT = "Sideshot"
AWARDS = "Awards Area"

#FULL SCREEN STATS
FSS_BRACKETS_6_4TEAMS = "Full Screen - Brackets - 4 Teams - Six"
FSS_BRACKETS_5_4TEAMS = "Full Screen - Brackets - 4 Teams - Five"
FSS_BRACKETS_4_4TEAMS = "Full Screen - Brackets - 4 Teams - Four"
FSS_BRACKETS_3_4TEAMS = "Full Screen - Brackets - 4 Teams - Three"
FSS_BRACKETS_2_4TEAMS = "Full Screen - Brackets - 4 Teams - Two"
FSS_BRACKETS_1_4TEAMS = "Full Screen - Brackets - 4 Teams - One"
FSS_BRACKETS_3_5TEAMS = "Full Screen - Brackets - 5 Teams - Three"
FSS_BRACKETS_2_5TEAMS = "Full Screen - Brackets - 5 Teams - Two"
FSS_BRACKETS_1_5TEAMS = "Full Screen - Brackets - 5 Teams - One"
FSS_BRACKETS_3_6TEAMS = "Full Screen - Brackets - 6 Teams - Three"
FSS_BRACKETS_2_6TEAMS = "Full Screen - Brackets - 6 Teams - Two"
FSS_BRACKETS_1_6TEAMS = "Full Screen - Brackets - 6 Teams - One"
FSS_BRACKETS_3_7TEAMS = "Full Screen - Brackets - 7 Teams - Three"
FSS_BRACKETS_2_7TEAMS = "Full Screen - Brackets - 7 Teams - Two"
FSS_BRACKETS_1_7TEAMS = "Full Screen - Brackets - 7 Teams - One"
FSS_BRACKETS_3_8TEAMS = "Full Screen - Brackets - 8 Teams - Three"
FSS_BRACKETS_2_8TEAMS = "Full Screen - Brackets - 8 Teams - Two"
FSS_BRACKETS_1_8TEAMS = "Full Screen - Brackets - 8 Teams - One"
FSS_INDIVIDUAL = "Full Screen - Individual"
FSS_RESULTS_1 = "Full Screen - Results - 1 Match"
FSS_RESULTS_2 = "Full Screen - Results - 2 Matches"
FSS_RESULTS_3 = "Full Screen - Results - 3 Matches"
FSS_RESULTS_4 = "Full Screen - Results - 4 Matches"
FSS_MATCHUPS_1 = "Full Screen - Matchups - 1 Match"
FSS_MATCHUPS_2 = "Full Screen - Matchups - 2 Matches"
FSS_MATCHUPS_3 = "Full Screen - Matchups - 3 Matches"
FSS_MATCHUPS_4 = "Full Screen - Matchups - 4 Matches"
FSS_ANNOUNCEMENTS = "Announcements"
FSS_PLAYOFF_TEAMS = "Full Screen - Playoff Teams"

#SIDE SCREEN STATS
SSS_BRACKETS_4_TEAMS = "Side - Brackets - 4 Teams"
SSS_BRACKETS_5_TEAMS = "Side - Brackets - 5 Teams"
SSS_BRACKETS_6_TEAMS = "Side - Brackets - 6 Teams"
SSS_BRACKETS_7_TEAMS = "Side - Brackets - 7 Teams"
SSS_BRACKETS_8_TEAMS = "Side - Brackets - 8 Teams"
SSS_STANDINGS_4_TEAMS = "Side - Standings - 4 Teams"
SSS_STANDINGS_5_TEAMS = "Side - Standings - 5 Teams"
SSS_STANDINGS_6_TEAMS = "Side - Standings - 6 Teams"
SSS_STANDINGS_7_TEAMS = "Side - Standings - 7 Teams"
SSS_STANDINGS_8_TEAMS = "Side - Standings - 8 Teams"
SSS_INDIVIDUAL = "Side - Individual Standings"
SSS_RESULTS_1 = "Side - Results - 1 Match"
SSS_RESULTS_2 = "Side - Results - 2 Matches"
SSS_RESULTS_3 = "Side - Results - 3 Matches"
SSS_RESULTS_4 = "Side - Results - 4 Matches"
SSS_MATCHUPS_1 = "Side - Matchups - 1 Match"
SSS_MATCHUPS_2 = "Side - Matchups - 2 Matches"
SSS_MATCHUPS_3 = "Side - Matchups - 3 Matches"
SSS_MATCHUPS_4 = "Side - Matchups - 4 Matches"

#LEFT SIDE SCREEN STATS
LEFT_SSS_BRACKETS_4_TEAMS = "Left Side - Brackets - 4 Teams"
LEFT_SSS_BRACKETS_5_TEAMS = "Left Side - Brackets - 5 Teams"
LEFT_SSS_BRACKETS_6_TEAMS = "Left Side - Brackets - 6 Teams"
LEFT_SSS_BRACKETS_7_TEAMS = "Left Side - Brackets - 7 Teams"
LEFT_SSS_BRACKETS_8_TEAMS = "Left Side - Brackets - 8 Teams"
LEFT_SSS_STANDINGS_4_TEAMS = "Left Side - Standings - 4 Teams"
LEFT_SSS_STANDINGS_5_TEAMS = "Left Side - Standings - 5 Teams"
LEFT_SSS_STANDINGS_6_TEAMS = "Left Side - Standings - 6 Teams"
LEFT_SSS_STANDINGS_7_TEAMS = "Left Side - Standings - 7 Teams"
LEFT_SSS_STANDINGS_8_TEAMS = "Left Side - Standings - 8 Teams"
LEFT_SSS_INDIVIDUAL = "Left Side - Individual Standings"
LEFT_SSS_RESULTS_1 = "Left Side - Results - 1 Match"
LEFT_SSS_RESULTS_2 = "Left Side - Results - 2 Matches"
LEFT_SSS_RESULTS_3 = "Left Side - Results - 3 Matches"
LEFT_SSS_RESULTS_4 = "Left Side - Results - 4 Matches"
LEFT_SSS_MATCHUPS_1 = "Left Side - Matchups - 1 Match"
LEFT_SSS_MATCHUPS_2 = "Left Side - Matchups - 2 Matches"
LEFT_SSS_MATCHUPS_3 = "Left Side - Matchups - 3 Matches"
LEFT_SSS_MATCHUPS_4 = "Left Side - Matchups - 4 Matches"

#RIGHT SIDE SCREEN STATS
RIGHT_SSS_BRACKETS_4_TEAMS = "Right Side - Brackets - 4 Teams"
RIGHT_SSS_BRACKETS_5_TEAMS = "Right Side - Brackets - 5 Teams"
RIGHT_SSS_BRACKETS_6_TEAMS = "Right Side - Brackets - 6 Teams"
RIGHT_SSS_BRACKETS_7_TEAMS = "Right Side - Brackets - 7 Teams"
RIGHT_SSS_BRACKETS_8_TEAMS = "Right Side - Brackets - 8 Teams"
RIGHT_SSS_STANDINGS_4_TEAMS = "Right Side - Standings - 4 Teams"
RIGHT_SSS_STANDINGS_5_TEAMS = "Right Side - Standings - 5 Teams"
RIGHT_SSS_STANDINGS_6_TEAMS = "Right Side - Standings - 6 Teams"
RIGHT_SSS_STANDINGS_7_TEAMS = "Right Side - Standings - 7 Teams"
RIGHT_SSS_STANDINGS_8_TEAMS = "Right Side - Standings - 8 Teams"
RIGHT_SSS_INDIVIDUAL = "Right Side - Individual Standings"
RIGHT_SSS_RESULTS_1 = "Right Side - Results - 1 Match"
RIGHT_SSS_RESULTS_2 = "Right Side - Results - 2 Matches"
RIGHT_SSS_RESULTS_3 = "Right Side - Results - 3 Matches"
RIGHT_SSS_RESULTS_4 = "Right Side - Results - 4 Matches"
RIGHT_SSS_MATCHUPS_1 = "Right Side - Matchups - 1 Match"
RIGHT_SSS_MATCHUPS_2 = "Right Side - Matchups - 2 Matches"
RIGHT_SSS_MATCHUPS_3 = "Right Side - Matchups - 3 Matches"
RIGHT_SSS_MATCHUPS_4 = "Right Side - Matchups - 4 Matches"

class SIDE:
    MIN=0
    LEFT = 1
    RIGHT = 2
    MAX=3

#SCOREBUG

#TOP OF SCREEN
TOP_OF_SCREEN = "Top of Screen"

#BOTTOM OF SCREEN
BOTTOM_OF_SCREEN = "Bottom of Screen"
BOS_BRACKETS = "Bottom of Screen Text - Brackets"
BOS_MATCHUPS = "Bottom of Screen Text - Matchups"
BOS_RESULTS = "Bottom of Screen Text - Results"
BOS_INDIVIDUAL = "Bottom of Screen Text - Individual Standings"
BOS_STANDINGS = "Bottom of Screen Text - Standings"

SCORE_TICKER = "Score Ticker"

#-Bottom of Screen Sources
TICKER_LOGO = "Logo"
PHASE_OF_TICKER = "Phase of Ticker"

#-Bottom of Screen - Brackets Sources
BRACKETS_CITY_NAME = "Brackets - City Name"
BRACKETS_TEAM_NAME = "Brackets - Team Name"
BRACKETS_NAME = "Bracket Name"

#-Bottom of Screen - Matchups Sources
MATCHUPS_TEAM_1 = "Matchups Team 1"
MATCHUPS_TEAM_2 = "Matchups Team 2"
MATCHUPS_TEAM_1_CITY = "Matchups Team 1 City"
MATCHUPS_TEAM_2_CITY = "Matchups Team 2 City"
MATCHUPS_DASH = "Matchups Dash"

#-Bottom of Screen - Results Sources
RESULTS_BRACKET = "Results - Bracket Name"
RESULTS_TEAM1 = "Results - Team 1"
RESULTS_TEAM1_CITY = "Results - Team 1 City"
RESULTS_TEAM1_SCORE = "Results - Team 1 Score"
RESULTS_TEAM2 = "Results - Team 2"
RESULTS_TEAM2_CITY = "Results - Team 2 City"
RESULTS_TEAM2_SCORE = "Results - Team 2 Score"
RESULTS_STATUS = "Results - Status"
RESULTS_PROTEST_PENDING = "Results - Protest Pending"

#-Bottom of Screen - Individual Standings Sources
INDIVIDUAL_RANK = "Individual - Rank"
INDIVIDUAL_PLAYER = "Individual - Player"
INDIVIDUAL_GRADE = "Individual - Grade"
INDIVIDUAL_SCHOOL = "Individual - School"
INDIVIDUAL_CITY = "Individual - City"
INDIVIDUAL_STATS = "Individual - Stats"
INDIVIDUAL_POWERS = "Individual - Powers"
INDIVIDUAL_TOSSUPS = "Individual - Tossups"
INDIVIDUAL_TUH = "Individual - TUH"

#-Bottom of Screen - Team Standings Sources
STANDINGS_BRACKET = "Standings - Bracket"
STANDINGS_RANK = "Standings - Rank"
STANDINGS_TEAM = "Standings - Team"
STANDINGS_CITY = "Standings - City"
STANDINGS_RECORD = "Standings - Record"
STANDINGS_PPG = "Standings - PPG"
STANDINGS_PPB = "Standings - PPB"

OPACITY_FILTER = "opacity"

#---GROUPS---
BRACKET_1_6 = "Bracket 1 - 6 Teams"
BRACKET_2_6 = "Bracket 2 - 6 Teams"
BRACKET_3_6 = "Bracket 3 - 6 Teams"
BRACKET_1_8 = "Bracket 1 - 8 Teams"
BRACKET_2_8 = "Bracket 2 - 8 Teams"
BRACKET_3_8 = "Bracket 3 - 8 Teams"

#---STANDINGS---
STANDINGS_4 = "Full Screen - Standings - 4 Teams"
STANDINGS_5 = "Full Screen - Standings - 5 Teams"
STANDINGS_6 = "Full Screen - Standings - 6 Teams"
STANDINGS_7 = "Full Screen - Standings - 7 Teams"
STANDINGS_8 = "Full Screen - Standings - 8 Teams"

PHASES=["Preliminary Rounds",
        "Preliminary Tiebreakers",
        "Playoff Rounds",
        "Playoff Tiebreakers",
        "Superplayoff Rounds",
        "Superplayoff Tiebreakers",
        "Finals",
        "3rd Place Game",
        "Placement Games",
        "Awards Ceremony"]

GUI_PHASES=["Prelims", "Playoffs", "Superplayoffs"]

class TOURNAMENT_PHASE:
    MIN=0
    BEFORE_PRELIMS = 1
    PRELIMS = 2
    POST_PRELIMS = 3
    PRE_PLAYOFFS = 4
    PLAYOFFS = 5
    POST_PLAYOFFS_D1 = 6
    PRE_SUPERPLAYOFFS_D2 = 7
    SUPERPLAYOFFS = 8
    PRE_FINALS = 9
    FINALS = 10
    POST_FINALS = 11
    MAX=12

current_phase = TOURNAMENT_PHASE.BEFORE_PRELIMS
start_round = 1
end_round = 1

ticker_phases_before_prelims=["Brackets", "Matchups"] #Transition when all rooms have started Round 1
ticker_phases_prelims=["Results", "Standings", "Individual Standings"]
ticker_phases_post_prelims=["Results", "Standings", "Individual Standings"]
ticker_phases_pre_playoffs=["Individual Standings", "Brackets", "Matchups"]
ticker_phases_playoffs=["Results", "Standings"]
ticker_phases_post_playoffs=["Results", "Standings"]
ticker_phases_pre_superplayoffs=["Brackets", "Matchups"]
ticker_phases_rest_of_day=["Standings", "Results"]

SLEEP_TIME = 2
SHOW_TIME = 5
 
class CORNERSTONE_PHASES:
    MIN=0
    PRELIMS = 1
    PLAYOFFS = 2
    SUPERPLAYOFFS = 3
    MAX=4

ws = obsws(OBS_HOST, OBS_PORT, OBS_PASSWORD)
switcher = PyATEMMax.ATEMMax()

def init():
    response = ws.connect()

    #switcher.connect(ATEM_IP)
    #switcher.waitForConnection(infinite=False, waitForFullHandshake=False)

    print("Connected")
    print(response)
    
def stop():
    ws.disconnect()
    switcher.disconnect()
    print("Disconnected from OBS WebSocket.")