import config
import obs, atem
from teams import teams

lbl_changePhase_before = None
lbl_changePhase_current=None
lbl_changePhase_after=None

# Function to handle button click
def change_scene(scene):
    if scene==0:
        obs.set_scene(config.GAME_ROOM)
    elif scene==1:
        obs.set_scene(config.HOST_AREA)
        atem.transition(config.ATEM_HOST_AREA)
    elif scene==2:
        obs.set_scene(config.INTERVIEW_AREA)
        atem.transition(config.ATEM_INTERVIEW)
    elif scene==3:
        obs.set_scene(config.DONATE_TO_PACE)
    elif scene==4:
        obs.set_scene(config.START_A_TEAM)
    elif scene==5:
        obs.set_scene(config.SIDESHOT)
        atem.transition(config.ATEM_SIDESHOT)
    elif scene==6:
        obs.set_scene(config.AWARDS)
    elif scene==7:
        obs.set_scene(config.FULL_SCREEN_STATS)
    elif scene==8:
        obs.set_scene("Waiting Area")
    elif scene==9:
        obs.set_scene("Left Team")
    elif scene==10:
        obs.set_scene("Right Team")

def change_phase(phase):
    
    global lbl_changePhase_before
    global lbl_changePhase_current
    global lbl_changePhase_after

    newPhase = 0

    if phase==0 and (config.current_phase-1) == config.TOURNAMENT_PHASE.MIN:
        return
    if phase==1 and (config.current_phase+1) == config.TOURNAMENT_PHASE.MAX:
        return
    
    if phase==0:
        newPhase = config.current_phase - 1
    elif phase==1:
        newPhase = config.current_phase + 1

    config.current_phase=newPhase

    if newPhase==config.TOURNAMENT_PHASE.BEFORE_PRELIMS:
        change_label_text(lbl_changePhase_before, "")
        change_label_text(lbl_changePhase_current, "Before Prelims")
        change_label_text(lbl_changePhase_after, "Prelims")
        config.start_round=1
        config.end_round=1
    elif newPhase==config.TOURNAMENT_PHASE.PRELIMS:
        change_label_text(lbl_changePhase_before, "Before Prelims")
        change_label_text(lbl_changePhase_current, "Prelims")
        change_label_text(lbl_changePhase_after, "Post Prelims")
        config.start_round=1
        config.end_round=1
    elif newPhase==config.TOURNAMENT_PHASE.POST_PRELIMS:
        change_label_text(lbl_changePhase_before, "Prelims")
        change_label_text(lbl_changePhase_current, "Post Prelims")
        change_label_text(lbl_changePhase_after, "Pre Playoffs")
        config.start_round=1
        config.end_round=5.2
    elif newPhase==config.TOURNAMENT_PHASE.PRE_PLAYOFFS:
        change_label_text(lbl_changePhase_before, "Post Prelims")
        change_label_text(lbl_changePhase_current, "Pre Playoffs")
        change_label_text(lbl_changePhase_after, "Playoffs")
        config.start_round=1
        config.end_round=6
    elif newPhase==config.TOURNAMENT_PHASE.PLAYOFFS:
        change_label_text(lbl_changePhase_before, "Pre Playoffs")
        change_label_text(lbl_changePhase_current, "Playoffs")
        change_label_text(lbl_changePhase_after, "Post Playoffs Day 1")
        config.start_round=6
        config.end_round=6
    elif newPhase==config.TOURNAMENT_PHASE.POST_PLAYOFFS_D1:
        change_label_text(lbl_changePhase_before, "Playoffs")
        change_label_text(lbl_changePhase_current, "Post Playoffs Day 1")
        change_label_text(lbl_changePhase_after, "Pre Superplayoffs Day 2")
        config.start_round=6
        config.end_round=10
    elif newPhase==config.TOURNAMENT_PHASE.PRE_SUPERPLAYOFFS_D2:
        change_label_text(lbl_changePhase_before, "Post Playoffs Day 1")
        change_label_text(lbl_changePhase_current, "Pre Superplayoffs Day 2")
        change_label_text(lbl_changePhase_after, "Superplayoffs")
        config.start_round=11
        config.end_round=11
    elif newPhase==config.TOURNAMENT_PHASE.SUPERPLAYOFFS:
        change_label_text(lbl_changePhase_before, "Pre Superplayoffs Day 2")
        change_label_text(lbl_changePhase_current, "Superplayoffs")
        change_label_text(lbl_changePhase_after, "Pre-Finals")
        config.start_round=11
        config.end_round=16
    elif newPhase==config.TOURNAMENT_PHASE.PRE_FINALS:
        change_label_text(lbl_changePhase_before, "Superplayoffs")
        change_label_text(lbl_changePhase_current, "Pre-Finals")
        change_label_text(lbl_changePhase_after, "Finals")
        config.start_round=11
        config.end_round=16
    elif newPhase==config.TOURNAMENT_PHASE.FINALS:
        change_label_text(lbl_changePhase_before, "Pre-Finals")
        change_label_text(lbl_changePhase_current, "Finals")
        change_label_text(lbl_changePhase_after, "Post Finals")
        config.start_round=11
        config.end_round=20
    elif newPhase==config.TOURNAMENT_PHASE.POST_FINALS:
        change_label_text(lbl_changePhase_before, "Playoffs")
        change_label_text(lbl_changePhase_current, "Post Finals")
        change_label_text(lbl_changePhase_after, "")
        config.start_round=11
        config.end_round=20

    return

def change_label_text(label, new_text):
    label.config(text=new_text)

def set_start_round(round):
    config.start_round=round

def set_end_round(round):
    config.end_round=round

def update_teams(info):
    
    updated_team1 = info['team1']
    updated_team2 = info['team2']
    updated_city1 = info['city1']
    updated_city2 = info['city2']

    if(info['ovr_team1'] != ""):
        updated_team1 = info['ovr_team1']
    if(info['ovr_team2'] != ""):
        updated_team2 = info['ovr_team2']
    if(info['ovr_city1'] != ""):
        updated_city1 = info['ovr_city1']
    if(info['ovr_city2'] != ""):
        updated_city2 = info['ovr_city2']

    path = "./Text Files/Game Room/"
    team1_file = path + "Active Left Team Name.txt"
    team2_file = path + "Active Right Team Name.txt"
    city1_file = path + "Active Left Team City.txt"
    city2_file = path + "Active Right Team City.txt"

    with open(team1_file, 'w') as file:
        file.write(updated_team1)
    with open(team2_file, 'w') as file:
        file.write(updated_team2)
    with open(city1_file, 'w') as file:
        file.write(updated_city1)
    with open(city2_file, 'w') as file:
        file.write(updated_city2)

def update_scores(info):
    path = "./Text Files/Game Room/"
    score1_file = path +"Active Left Team Score.txt"
    score2_file = path + "Active Right Team Score.txt"
    cycle_file = path + "Current Cycle.txt"
    round_file = path + "Current Round.txt"


    if(info['update_s1']):
        with open(score1_file, 'w') as file:
            file.write(info['score1'])
    if(info['update_s2']):
        with open(score2_file, 'w') as file:
            file.write(info['score2'])
    if(info['update_cycle']):
        with open(cycle_file, 'w') as file:
            file.write(info['cycle'] + "/20")
    if(info['update_round']):
        obs.set_round(info['round'])

def toggle_awards_overlay(visibility):
    if visibility:
        obs.toggle_source_visibility(config.AWARDS, "Awards Overlay", True)
        obs.toggle_source_visibility("Awards Info Overlay", "Awards - Top Overlay", True)
    else:
        obs.toggle_source_visibility(config.AWARDS, "Awards Overlay", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Player", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Team", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Caption", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Rank", False)
    
def update_awards(info):
    path = "./Text Files/Info Overlays/Awards/"
    caption_file = path + "Caption.txt"
    city_file = path + "City.txt"
    grade_team_file = path + "Grade and Team.txt"
    player_file = path + "Player.txt"
    ppg_file = path + "PPG.txt"
    rank_file = path + "Rank.txt"
    team_file = path + "Team.txt"

    caption_text = ""

    city = config.data.get_city(info['info']['team'])

    if info['is_team']:

        obs.toggle_source_visibility(config.AWARDS, "Awards - Player", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Team", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Caption", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Rank", False)
        
        if(info['info']['type'] == "Overall"):
            obs.toggle_source_visibility("Awards Info Overlay", "Awards - Top Overlay", False)
        else:
            obs.toggle_source_visibility("Awards Info Overlay", "Awards - Top Overlay", True)
            if info['info']['type'] == "JV":
                caption_text = "Junior Varsity Awards"
            else:
                caption_text = "Small School Awards"

        with open(caption_file, 'w') as file:
            file.write(caption_text)
        with open(rank_file, 'w') as file:
            file.write(info['info']['rank'])
        with open(team_file, 'w') as file:
            file.write(info['info']['team'])
        with open(city_file, 'w') as file:
            file.write(city)

        config.time.sleep(config.SLEEP_TIME)

        obs.toggle_source_visibility(config.AWARDS, "Awards - Team", True)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Caption", True)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Rank", True)
        obs.toggle_source_visibility(config.AWARDS, "Awards Overlay", True)
    else:
        obs.toggle_source_visibility(config.AWARDS, "Awards - Player", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Team", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Caption", False)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Rank", False)
        obs.toggle_source_visibility("Awards Info Overlay", "Awards - Top Overlay", True)

        team_grade_text = ""

        if int(info['info']['grade']) == 12:
            team_grade_text = "Senior - " + info['info']['team']
        elif int(info['info']['grade']) == 11:
            team_grade_text = "Junior - " + info['info']['team']
        elif int(info['info']['grade']) == 10:
            team_grade_text = "Sophomore - " + info['info']['team']
        elif int(info['info']['grade']) == 9:
            team_grade_text = "Freshman - " + info['info']['team']
        else:
            team_grade_text = info['info']['grade'] + "th Grade - " + info['info']['team']

        if info['info']['type'] == "Overall":
            caption_text = "Individual Scoring Awards"
        else:
            caption_text = "Rising Star Awards"

        with open(caption_file, 'w') as file:
            file.write(caption_text)
        with open(city_file, 'w') as file:
            file.write(city)
        with open(grade_team_file, 'w') as file:
            file.write(team_grade_text)
        with open(player_file, 'w') as file:
            file.write(info['info']['player'])
        with open(ppg_file, 'w') as file:
            file.write(info['info']['ppg'])
        with open(rank_file, 'w') as file:
            file.write(info['info']['rank'])
        with open(team_file, 'w') as file:
            file.write(info['info']['team'])

        config.time.sleep(config.SLEEP_TIME)
        
        obs.toggle_source_visibility(config.AWARDS, "Awards - Player", True)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Caption", True)
        obs.toggle_source_visibility(config.AWARDS, "Awards - Rank", True)
        obs.toggle_source_visibility(config.AWARDS, "Awards Overlay", True)
        
def update_hostArea(info):
    path = "./Text Files/Info Overlays/Commentator Overlays"
    p1name_file = path + "/Person 1/Name.txt"
    p1role_file = path + "/Person 1/Role.txt"
    p2name_file = path + "/Person 2/Name.txt"
    p2role_file = path + "/Person 2/Role.txt"
    p3name_file = path + "/Person 3/Name.txt"
    p3role_file = path + "/Person 3/Role.txt"

    obs.toggle_source_visibility(config.HOST_AREA, "1 Commentator Overlay", False)
    obs.toggle_source_visibility(config.HOST_AREA, "2 Commentator Overlay", False)
    obs.toggle_source_visibility(config.HOST_AREA, "3 Commentator Overlay", False)

    if info['vis1']:
        with open(p1name_file, 'w') as file:
            file.write(info['comm1'])
        with open(p1role_file, 'w') as file:
            file.write(info['role1'])
    if info['vis2']:
        with open(p2name_file, 'w') as file:
            file.write(info['comm2'])
        with open(p2role_file, 'w') as file:
            file.write(info['role2'])
    if info['vis3']:
        with open(p3name_file, 'w') as file:
            file.write(info['comm3'])
        with open(p3role_file, 'w') as file:
            file.write(info['role3'])

    sum = 0
    if info['vis1']:
        sum +=1
    if info['vis2']:
        sum +=1
    if info['vis3']:
        sum +=1
    
    config.time.sleep(config.SLEEP_TIME)

    if sum >= 1:
        obs.toggle_source_visibility(config.HOST_AREA, str(sum)+" Commentator Overlay", True)

def toggle_int_data(visibility):
    obs.toggle_source_visibility(config.INTERVIEW_AREA, "Interview Info Overlay", visibility)
    obs.toggle_source_visibility(config.INTERVIEW_AREA, "Interview - Text", visibility)

def update_InterviewArea(info):
    path = "./Text Files/Info Overlays/Interview Overlays/"
    subject_file = path + "Line 1.txt"
    line1_file = path + "Line 2.txt"
    line2_file = path + "Line 3.txt"
    caption_file = path + "Caption.txt"

    with open(subject_file, 'w') as file:
            file.write(info['subject'])
    with open(line1_file, 'w') as file:
            file.write(info['line1'])
    with open(line2_file, 'w') as file:
            file.write(info['line2'])
    with open(caption_file, 'w') as file:
            file.write(info['caption'])

    config.time.sleep(config.SLEEP_TIME)

    toggle_int_data(True)

def test_ping(index):
    global lbl_API_api_name, lbl_API_api_status, btn_API_checkPing
    
    ping = False

    if index==0:
        ping = config.cornerstone.ping()
    elif index == 1:
        ping = obs.ping()
    elif index == 3:
        ping = config.spotify.ping()

    if ping:
        lbl_API_api_status[index].config(text="Ping!")
    else:
        lbl_API_api_status[index].config(text="NO PING!")

###---BEGIN SS RESULTS---###

def ss_results_select_phases_update_combobox(self):
    global dpd_SS_RES_PhaseSelect, dpd_SS_RES_IndividualMatches_Bracket, dpd_SS_RES_IndividualMatches_Round, dpd_SS_RES_IndividualMatches_Matchup
    global dpd_SS_RES_BracketinRound_Bracket, dpd_SS_RES_BracketinRound_Round

    selected_phase = dpd_SS_RES_PhaseSelect.get()

    brackets =  config.data.get_bracket_list(selected_phase)
    rounds = ["1","2","3","4","5"]
    matches = []

    if selected_phase == "Playoffs":
        rounds = ["6","7","8","9","10"]
    if selected_phase == "Superplayoffs":
        rounds = ["11","12","13","14","15","16"]
    
    matches = []

    for round in rounds:
        rnd_matches = config.data.get_results(int(round))
        for match in rnd_matches:
            matches.append(match['team1'] + " vs. " +match['team2'] + "- " + match['team1_score'] + " - " +match['team2_score'] )

    dpd_SS_RES_BracketinRound_Round.config(values=rounds)
    dpd_SS_RES_BracketinRound_Bracket.config(values=brackets)

    dpd_SS_RES_BracketinRound_Round.set("")
    dpd_SS_RES_BracketinRound_Bracket.set("")

    for i in range(4):
        dpd_SS_RES_IndividualMatches_Bracket[i].config(values=brackets)
        dpd_SS_RES_IndividualMatches_Round[i].config(values=rounds)
        dpd_SS_RES_IndividualMatches_Matchup[i].config(values=matches)

        dpd_SS_RES_IndividualMatches_Bracket[i].set("")
        dpd_SS_RES_IndividualMatches_Round[i].set("")
        dpd_SS_RES_IndividualMatches_Matchup[i].set("")

def ss_results_select_bracket_update_combobox(index, event):
    global dpd_SS_RES_PhaseSelect
    global dpd_SS_RES_IndividualMatches_Bracket, dpd_SS_RES_IndividualMatches_Round, dpd_SS_RES_IndividualMatches_Matchup

    selected_bracket = dpd_SS_RES_IndividualMatches_Bracket[index].get()
    rounds = None
    current_round = dpd_SS_RES_IndividualMatches_Round[index].get()

    if current_round == "":
        rounds = dpd_SS_RES_IndividualMatches_Round[index].cget("values")
    else:
        rounds = [dpd_SS_RES_IndividualMatches_Round[index].get()]

    matchups = []

    for round in rounds:
        rec_matchups = config.data.get_results(int(round))

        for matchup in rec_matchups:
            if matchup['bracket'] == selected_bracket:
                matchups.append(matchup['team1'] + " vs. " +matchup['team2'] + "- " + matchup['team1_score'] + " - " +matchup['team2_score'] )

    dpd_SS_RES_IndividualMatches_Matchup[index].config(values=matchups)

def ss_results_select_round_update_combobox(index, event):
    global dpd_SS_RES_PhaseSelect
    global dpd_SS_RES_IndividualMatches_Bracket, dpd_SS_RES_IndividualMatches_Round, dpd_SS_RES_IndividualMatches_Matchup

    selected_round = dpd_SS_RES_IndividualMatches_Round[index].get()
    bracket = None
    current_bracket = dpd_SS_RES_IndividualMatches_Bracket[index].get()

    if current_bracket == "":
        brackets = dpd_SS_RES_IndividualMatches_Bracket[index].cget("values")
    else:
        brackets = [dpd_SS_RES_IndividualMatches_Bracket[index].get()]

    rec_matchups = config.data.get_results(int(selected_round))
    matchups = []

    for matchup in rec_matchups:
        for bracket in brackets:
            if matchup['bracket'] == bracket:
                matchups.append(matchup['team1'] + " vs. " +matchup['team2'] + "- " + matchup['team1_score'] + " - " +matchup['team2_score'])

    dpd_SS_RES_IndividualMatches_Matchup[index].config(values=matchups)

def display_ss_results(index):

    global dpd_SS_RES_IndividualMatches_Bracket, dpd_SS_RES_IndividualMatches_Round, dpd_SS_RES_IndividualMatches_Matchup
    global radvar_SS_RES_Side, SS_RES_LastCount

    SS_RES_LastCount = index + 1

    raw_matches = []
    matches = []

    selected_round = []
    selected_bracket = []

    for i in range(index + 1):
        rounds = []

        current_round = dpd_SS_RES_IndividualMatches_Round[i].get()

        if current_round == "":
            rounds = dpd_SS_RES_IndividualMatches_Round[i].cget("values")
        else:
            rounds = [dpd_SS_RES_IndividualMatches_Round[i].get()]

        rec_matchups = []

        for round in rounds:
            matchups = config.data.get_results(int(round))
            rec_matchups += matchups

        selected_matchup = dpd_SS_RES_IndividualMatches_Matchup[i].get().strip()
        parts = selected_matchup.split(" vs. ")
        team1 = parts[0].strip()
        team2 = parts[1].split("-")[0].strip()

        for matchup in matchups:
            if matchup['team1'] == team1 and matchup['team2'] == team2:
                matches.append(matchup)

    send_side = config.SIDE.LEFT

    if radvar_SS_RES_Side.get() == "Right":
        send_side = config.SIDE.RIGHT

    config.sss.display_round_results(matches, send_side, "Selected Matches", False)

def toggle_ss_results_display(info):
    global SS_RES_LastCount
    
    side = "Left Side"

    if info['side'] == "Right":
        side = "Right Side"

    if info['visibility']:
        if SS_RES_LastCount == 1:
            obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, side + " Results - 1 Match", True)
        else:
            obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, side + " Results - " + str(SS_MAT_LastCount) + " Matches", True)
    else:
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Results - 1 Match", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Results - 2 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Results - 3 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Results - 4 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Results - 1 Match", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Results - 2 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Results - 3 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Results - 4 Matches", False)

def display_ss_results_allResultsPerBracketRound(bracket, round, side):
    rec_matches = config.data.get_results(int(round))
    send_matches = []

    send_side = config.SIDE.LEFT

    if side == "Right":
        send_side = config.SIDE.RIGHT

    for match in rec_matches:
        if match['bracket'] == bracket:
            send_matches.append(match)

    config.sss.display_round_results(send_matches, send_side ,"Round " +round + " - " +bracket, False)

###---END SS RESULTS---###
###---BEGIN FS RESULTS---###

def fs_results_select_phases_update_combobox(self):
    global dpd_FS_RES_PhaseSelect, dpd_FS_RES_IndividualMatches_Bracket, dpd_FS_RES_IndividualMatches_Round, dpd_FS_RES_IndividualMatches_Matchup
    global dpd_FS_RES_BracketinRound_Bracket, dpd_FS_RES_BracketinRound_Round

    selected_phase = dpd_FS_RES_PhaseSelect.get()

    brackets =  config.data.get_bracket_list(selected_phase)
    rounds = ["1","2","3","4","5"]
    matches = []

    if selected_phase == "Playoffs":
        rounds = ["6","7","8","9","10"]
    if selected_phase == "Superplayoffs":
        rounds = ["11","12","13","14","15","16"]
    
    matches = []

    for round in rounds:
        rnd_matches = config.data.get_results(int(round))
        for match in rnd_matches:
            matches.append(match['team1'] + " vs. " +match['team2'] + "- " + match['team1_score'] + " - " +match['team2_score'] )

    dpd_FS_RES_BracketinRound_Round.config(values=rounds)
    dpd_FS_RES_BracketinRound_Bracket.config(values=brackets)

    dpd_FS_RES_BracketinRound_Round.set("")
    dpd_FS_RES_BracketinRound_Bracket.set("")

    for i in range(4):
        dpd_FS_RES_IndividualMatches_Bracket[i].config(values=brackets)
        dpd_FS_RES_IndividualMatches_Round[i].config(values=rounds)
        dpd_FS_RES_IndividualMatches_Matchup[i].config(values=matches)

        dpd_FS_RES_IndividualMatches_Bracket[i].set("")
        dpd_FS_RES_IndividualMatches_Round[i].set("")
        dpd_FS_RES_IndividualMatches_Matchup[i].set("")

def fs_results_select_bracket_update_combobox(index, event):
    global dpd_FS_RES_PhaseSelect
    global dpd_FS_RES_IndividualMatches_Bracket, dpd_FS_RES_IndividualMatches_Round, dpd_FS_RES_IndividualMatches_Matchup

    selected_bracket = dpd_FS_RES_IndividualMatches_Bracket[index].get()
    rounds = None
    current_round = dpd_FS_RES_IndividualMatches_Round[index].get()

    if current_round == "":
        rounds = dpd_FS_RES_IndividualMatches_Round[index].cget("values")
    else:
        rounds = [dpd_FS_RES_IndividualMatches_Round[index].get()]

    matchups = []

    for round in rounds:
        rec_matchups = config.data.get_results(int(round))

        for matchup in rec_matchups:
            if matchup['bracket'] == selected_bracket:
                matchups.append(matchup['team1'] + " vs. " +matchup['team2'] + "- " + matchup['team1_score'] + " - " +matchup['team2_score'] )

    dpd_FS_RES_IndividualMatches_Matchup[index].config(values=matchups)

def fs_results_select_round_update_combobox(index, event):
    global dpd_FS_RES_PhaseSelect
    global dpd_FS_RES_IndividualMatches_Bracket, dpd_FS_RES_IndividualMatches_Round, dpd_FS_RES_IndividualMatches_Matchup

    selected_round = dpd_FS_RES_IndividualMatches_Round[index].get()
    bracket = None
    current_bracket = dpd_FS_RES_IndividualMatches_Bracket[index].get()

    if current_bracket == "":
        brackets = dpd_FS_RES_IndividualMatches_Bracket[index].cget("values")
    else:
        brackets = [dpd_FS_RES_IndividualMatches_Bracket[index].get()]

    rec_matchups = config.data.get_results(int(selected_round))
    matchups = []

    for matchup in rec_matchups:
        for bracket in brackets:
            if matchup['bracket'] == bracket:
                matchups.append(matchup['team1'] + " vs. " +matchup['team2'] + "- " + matchup['team1_score'] + " - " +matchup['team2_score'])

    dpd_FS_RES_IndividualMatches_Matchup[index].config(values=matchups)

def display_fs_results(index):

    global dpd_FS_RES_IndividualMatches_Bracket, dpd_FS_RES_IndividualMatches_Round, dpd_FS_RES_IndividualMatches_Matchup
    global FS_RES_LastCount

    FS_RES_LastCount = index + 1

    raw_matches = []
    matches = []

    selected_round = []
    selected_bracket = []

    for i in range(index + 1):
        rounds = []

        current_round = dpd_FS_RES_IndividualMatches_Round[i].get()

        if current_round == "":
            rounds = dpd_FS_RES_IndividualMatches_Round[i].cget("values")
        else:
            rounds = [dpd_FS_RES_IndividualMatches_Round[i].get()]

        rec_matchups = []

        for round in rounds:
            matchups = config.data.get_results(int(round))
            rec_matchups += matchups

        selected_matchup = dpd_FS_RES_IndividualMatches_Matchup[i].get().strip()
        parts = selected_matchup.split(" vs. ")
        team1 = parts[0].strip()
        team2 = parts[1].split("-")[0].strip()

        for matchup in matchups:
            if matchup['team1'] == team1 and matchup['team2'] == team2:
                matches.append(matchup)

    config.fss.loop_ind_results(matches)

def toggle_fs_results_display(info):
    global FS_RES_LastCount
    print(FS_RES_LastCount)

    if info['visibility']:
        if FS_RES_LastCount == 1:
            obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - 1 Match", True)
        else:
            obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - " + str(FS_RES_LastCount) + " Matches", True)
    else:
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - 1 Match", False)
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - 2 Matches", False)
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - 3 Matches", False)
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - 4 Matches", False)

def display_fs_results_allResultsPerBracketRound(bracket, round):
    global FS_RES_LastCount
    
    rec_matches = config.data.get_results(int(round))
    send_matches = []

    for match in rec_matches:
        if match['bracket'] == bracket:
            send_matches.append(match)

    FS_RES_LastCount = len(send_matches)
    print(FS_RES_LastCount)

    config.fss.loop_ind_results(send_matches)

###---END FS RESULTS---###
###---BEGIN SS MATCHES---###

def ss_matches_select_phases_update_combobox(self):
    global dpd_SS_MAT_PhaseSelect, dpd_SS_MAT_IndividualMatches_Bracket, dpd_SS_MAT_IndividualMatches_Round, dpd_SS_MAT_IndividualMatches_Matchup
    global dpd_SS_MAT_BracketinRound_Bracket, dpd_SS_MAT_BracketinRound_Round

    selected_phase = dpd_SS_MAT_PhaseSelect.get()

    brackets =  config.data.get_bracket_list(selected_phase)
    rounds = ["1","2","3","4","5"]
    matches = []

    if selected_phase == "Playoffs":
        rounds = ["6","7","8","9","10"]
    if selected_phase == "Superplayoffs":
        rounds = ["11","12","13","14","15","16"]
    
    matches = []

    for round in rounds:
        rnd_matches = config.data.get_matchups(int(round))
        for match in rnd_matches:
            matches.append(match['team1'] + " vs. " +match['team2'])

    dpd_SS_MAT_BracketinRound_Round.config(values=rounds)
    dpd_SS_MAT_BracketinRound_Bracket.config(values=brackets)

    dpd_SS_MAT_BracketinRound_Round.set("")
    dpd_SS_MAT_BracketinRound_Bracket.set("")

    for i in range(4):
        dpd_SS_MAT_IndividualMatches_Bracket[i].config(values=brackets)
        dpd_SS_MAT_IndividualMatches_Round[i].config(values=rounds)
        dpd_SS_MAT_IndividualMatches_Matchup[i].config(values=matches)

        dpd_SS_MAT_IndividualMatches_Bracket[i].set("")
        dpd_SS_MAT_IndividualMatches_Round[i].set("")
        dpd_SS_MAT_IndividualMatches_Matchup[i].set("")

def ss_matches_select_bracket_update_combobox(index, event):
    global dpd_SS_MAT_PhaseSelect
    global dpd_SS_MAT_IndividualMatches_Bracket, dpd_SS_MAT_IndividualMatches_Round, dpd_SS_MAT_IndividualMatches_Matchup

    selected_bracket = dpd_SS_MAT_IndividualMatches_Bracket[index].get()
    rounds = None
    current_round = dpd_SS_MAT_IndividualMatches_Round[index].get()

    if current_round == "":
        rounds = dpd_SS_MAT_IndividualMatches_Round[index].cget("values")
    else:
        rounds = [dpd_SS_MAT_IndividualMatches_Round[index].get()]

    matchups = []

    for round in rounds:
        rec_matchups = config.data.get_matchups(int(round))

        for matchup in rec_matchups:
            if matchup['bracket'] == selected_bracket:
                matchups.append(matchup['team1'] + " vs. " +matchup['team2'])

    dpd_SS_MAT_IndividualMatches_Matchup[index].config(values=matchups)

def ss_matches_select_round_update_combobox(index, event):
    global dpd_SS_MAT_PhaseSelect
    global dpd_SS_MAT_IndividualMatches_Bracket, dpd_SS_MAT_IndividualMatches_Round, dpd_SS_MAT_IndividualMatches_Matchup

    selected_round = dpd_SS_MAT_IndividualMatches_Round[index].get()
    bracket = None
    current_bracket = dpd_SS_MAT_IndividualMatches_Bracket[index].get()

    if current_bracket == "":
        brackets = dpd_SS_MAT_IndividualMatches_Bracket[index].cget("values")
    else:
        brackets = [dpd_SS_MAT_IndividualMatches_Bracket[index].get()]

    rec_matchups = config.data.get_matchups(int(selected_round))
    matchups = []

    for matchup in rec_matchups:
        for bracket in brackets:
            if matchup['bracket'] == bracket:
                matchups.append(matchup['team1'] + " vs. " +matchup['team2'])

    dpd_SS_MAT_IndividualMatches_Matchup[index].config(values=matchups)
        
def display_ss_matches(index):

    global dpd_SS_MAT_IndividualMatches_Bracket, dpd_SS_MAT_IndividualMatches_Round, dpd_SS_MAT_IndividualMatches_Matchup
    global radvar_SS_MAT_Side, SS_MAT_LastCount

    SS_MAT_LastCount = index + 1

    raw_matches = []
    matches = []

    selected_round = []
    selected_bracket = []

    for i in range(index + 1):
        rounds = []

        current_round = dpd_SS_MAT_IndividualMatches_Round[i].get()

        if current_round == "":
            rounds = dpd_SS_MAT_IndividualMatches_Round[i].cget("values")
        else:
            rounds = [dpd_SS_MAT_IndividualMatches_Round[i].get()]

        rec_matchups = []

        for round in rounds:
            matchups = config.data.get_matchups(int(round))
            rec_matchups += matchups

        selected_matchup = dpd_SS_MAT_IndividualMatches_Matchup[i].get().strip()
        team1 = selected_matchup.split(" vs. ")[0]
        team2 = selected_matchup.split(" vs. ")[1]

        for matchup in matchups:
            if matchup['team1'] == team1 and matchup['team2'] == team2:
                matches.append(matchup)

    send_side = config.SIDE.LEFT

    if radvar_SS_MAT_Side.get() == "Right":
        send_side = config.SIDE.RIGHT

    config.sss.display_matchups(matches, send_side, "Selected Matches")

def toggle_ss_matches_display(info):
    global SS_MAT_LastCount
    
    side = "Left Side"

    if info['side'] == "Right":
        side = "Right Side"

    if info['visibility']:
        if SS_MAT_LastCount == 1:
            obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, side + " Matchups - 1 Match", True)
        else:
            obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, side + " Matchups - " + str(SS_MAT_LastCount) + " Matches", True)
    else:
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Matchups - 1 Match", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Matchups - 2 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Matchups - 3 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Matchups - 4 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Matchups - 1 Match", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Matchups - 2 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Matchups - 3 Matches", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Matchups - 4 Matches", False)

def display_ss_matches_allMatchesPerBracketRound(bracket, round, side):
    rec_matches = config.data.get_matchups(int(round))
    send_matches = []

    send_side = config.SIDE.LEFT

    if side == "Right":
        send_side = config.SIDE.RIGHT

    for match in rec_matches:
        if match['bracket'] == bracket:
            send_matches.append(match)

    config.sss.display_matchups(send_matches, send_side ,"Round " +round + " - " +bracket)

###---END SS MATCHES---###
###---BEGIN FS MATCHES---###

def fs_matches_select_phases_update_combobox(self):
    global dpd_FS_MAT_PhaseSelect, dpd_FS_MAT_IndividualMatches_Bracket, dpd_FS_MAT_IndividualMatches_Round, dpd_FS_MAT_IndividualMatches_Matchup
    global dpd_FS_MAT_BracketinRound_Bracket, dpd_FS_MAT_BracketinRound_Round

    selected_phase = dpd_FS_MAT_PhaseSelect.get()

    brackets =  config.data.get_bracket_list(selected_phase)
    rounds = ["1","2","3","4","5"]
    matches = []

    if selected_phase == "Playoffs":
        rounds = ["6","7","8","9","10"]
    if selected_phase == "Superplayoffs":
        rounds = ["11","12","13","14","15","16"]
    
    matches = []

    for round in rounds:
        rnd_matches = config.data.get_matchups(int(round))
        for match in rnd_matches:
            matches.append(match['team1'] + " vs. " +match['team2'])

    dpd_FS_MAT_BracketinRound_Round.config(values=rounds)
    dpd_FS_MAT_BracketinRound_Bracket.config(values=brackets)

    dpd_FS_MAT_BracketinRound_Round.set("")
    dpd_FS_MAT_BracketinRound_Bracket.set("")

    for i in range(4):
        dpd_FS_MAT_IndividualMatches_Bracket[i].config(values=brackets)
        dpd_FS_MAT_IndividualMatches_Round[i].config(values=rounds)
        dpd_FS_MAT_IndividualMatches_Matchup[i].config(values=matches)

        dpd_FS_MAT_IndividualMatches_Bracket[i].set("")
        dpd_FS_MAT_IndividualMatches_Round[i].set("")
        dpd_FS_MAT_IndividualMatches_Matchup[i].set("")

def fs_matches_select_bracket_update_combobox(index, event):
    global dpd_FS_MAT_PhaseSelect
    global dpd_FS_MAT_IndividualMatches_Bracket, dpd_FS_MAT_IndividualMatches_Round, dpd_FS_MAT_IndividualMatches_Matchup

    selected_bracket = dpd_FS_MAT_IndividualMatches_Bracket[index].get()
    rounds = None
    current_round = dpd_FS_MAT_IndividualMatches_Round[index].get()

    if current_round == "":
        rounds = dpd_FS_MAT_IndividualMatches_Round[index].cget("values")
    else:
        rounds = [dpd_FS_MAT_IndividualMatches_Round[index].get()]

    matchups = []

    for round in rounds:
        rec_matchups = config.data.get_matchups(int(round))

        for matchup in rec_matchups:
            if matchup['bracket'] == selected_bracket:
                matchups.append(matchup['team1'] + " vs. " +matchup['team2'])

    dpd_FS_MAT_IndividualMatches_Matchup[index].config(values=matchups)

def fs_matches_select_round_update_combobox(index, event):
    global dpd_FS_MAT_PhaseSelect
    global dpd_FS_MAT_IndividualMatches_Bracket, dpd_FS_MAT_IndividualMatches_Round, dpd_FS_MAT_IndividualMatches_Matchup

    selected_round = dpd_FS_MAT_IndividualMatches_Round[index].get()
    bracket = None
    current_bracket = dpd_FS_MAT_IndividualMatches_Bracket[index].get()

    if current_bracket == "":
        brackets = dpd_FS_MAT_IndividualMatches_Bracket[index].cget("values")
    else:
        brackets = [dpd_FS_MAT_IndividualMatches_Bracket[index].get()]

    rec_matchups = config.data.get_matchups(int(selected_round))
    matchups = []

    for matchup in rec_matchups:
        for bracket in brackets:
            if matchup['bracket'] == bracket:
                matchups.append(matchup['team1'] + " vs. " +matchup['team2'])

    dpd_FS_MAT_IndividualMatches_Matchup[index].config(values=matchups)
        
def display_fs_matches(index):

    global dpd_FS_MAT_IndividualMatches_Bracket, dpd_FS_MAT_IndividualMatches_Round, dpd_FS_MAT_IndividualMatches_Matchup
    global FS_MAT_LastCount

    FS_MAT_LastCount = index + 1

    raw_matches = []
    matches = []

    selected_round = []
    selected_bracket = []

    selected_phase = dpd_FS_MAT_PhaseSelect.get()

    for i in range(index + 1):
        rounds = []

        current_round = dpd_FS_MAT_IndividualMatches_Round[i].get()

        if current_round == "":
            rounds = dpd_FS_MAT_IndividualMatches_Round[i].cget("values")
        else:
            rounds = [dpd_FS_MAT_IndividualMatches_Round[i].get()]

        rec_matchups = []

        for round in rounds:
            matchups = config.data.get_matchups(int(round))
            rec_matchups += matchups

        selected_matchup = dpd_FS_MAT_IndividualMatches_Matchup[i].get().strip()
        team1 = selected_matchup.split(" vs. ")[0]
        team2 = selected_matchup.split(" vs. ")[1]

        for matchup in matchups:
            if matchup['team1'] == team1 and matchup['team2'] == team2:
                matches.append(matchup)

    config.fss.show_ind_matchup(matches, selected_phase)

def toggle_fs_matches_display(info):
    global FS_MAT_LastCount

    if info['visibility']:
        if FS_MAT_LastCount == 1:
            obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - 1 Match", True)
        else:
            obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - " + str(FS_MAT_LastCount) + " Matches", True)
    else:
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - 1 Match", False)
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - 2 Matches", False)
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - 3 Matches", False)
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - 4 Matches", False)

def display_fs_matches_allMatchesPerBracketRound(bracket, round):
    global FS_MAT_LastCount
    
    rec_matches = config.data.get_matchups(int(round))
    send_matches = []

    selected_phase = dpd_FS_MAT_PhaseSelect.get()

    for match in rec_matches:
        if match['bracket'] == bracket:
            send_matches.append(match)

    FS_MAT_LastCount = len(send_matches)

    config.fss.show_ind_matchup(send_matches, selected_phase)

###---END FS MATCHES---###
###---BEGIN SS BRACKET---###

def update_bracket_gui():
    global ss_bracket_side, ss_brackets, ss_bracketLen, ss_ActiveBracketIndex
    global lbl_SS_BRA_Bracket_Previous, lbl_SS_BRA_Bracket_Current, lbl_SS_BRA_Bracket_Next, ss_NumBrackets

    if ss_ActiveBracketIndex == 0:
        lbl_SS_BRA_Bracket_Previous.config(text="")
    else:
        lbl_SS_BRA_Bracket_Previous.config(text=ss_brackets[ss_ActiveBracketIndex-1]['bracket'])

    lbl_SS_BRA_Bracket_Current.config(text=ss_brackets[ss_ActiveBracketIndex]['bracket'])

    if ss_ActiveBracketIndex == ss_NumBrackets-1:
        lbl_SS_BRA_Bracket_Next.config(text="")
    else:
        lbl_SS_BRA_Bracket_Next.config(text=ss_brackets[ss_ActiveBracketIndex+1]['bracket'])

def cycle_brackets(info):
    global ss_bracket_side, ss_brackets, ss_bracketLen, ss_ActiveBracketIndex, btn_SS_BRA_Next, ss_NumBrackets
    
    ss_brackets = config.data.get_brackets_with_teams(info['phase'])
    #print(ss_brackets[0]['teams'])
    ss_bracketLen = len(ss_brackets[0]['teams'])
    ss_NumBrackets = 72/ss_bracketLen
    ss_ActiveBracketIndex = 0

    if info['side'] == "Left":
        ss_bracket_side = config.SIDE.LEFT
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Brackets - " + str(ss_bracketLen) + " Teams", True)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Brackets - " + str(ss_bracketLen) + " Teams", False)
    else:
        ss_bracket_side = config.SIDE.RIGHT
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Brackets - " + str(ss_bracketLen) + " Teams", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Brackets - " + str(ss_bracketLen) + " Teams", True)

    config.sss.show_individual_bracket(ss_brackets[0], ss_bracket_side)
    update_bracket_gui()
    btn_SS_BRA_Next.config(state=config.tk.NORMAL)

def change_ss_bracket_state(info):
    global btn_SS_BRA_GoBack, btn_SS_BRA_Next, ss_ActiveBracketIndex, ss_bracketLen, ss_bracket_side, ss_NumBrackets

    ss_ActiveBracketIndex = ss_ActiveBracketIndex + info

    if info == -1:
        if ss_ActiveBracketIndex == 0:
            btn_SS_BRA_GoBack.config(state=config.tk.DISABLED)
        btn_SS_BRA_Next.config(state=config.tk.NORMAL)
    else:
        if ss_ActiveBracketIndex == ss_NumBrackets-1:
            btn_SS_BRA_Next.config(state=config.tk.DISABLED)
        btn_SS_BRA_GoBack.config(state=config.tk.NORMAL)
    
    update_bracket_gui()
    config.sss.show_individual_bracket(ss_brackets[ss_ActiveBracketIndex], ss_bracket_side)

def toggle_ss_bracket_display(info):

    global ss_brackets

    if info == -1:
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Brackets - 6 Teams", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Brackets - 8 Teams", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Brackets - 6 Teams", False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Brackets - 8 Teams", False)
    else:
        numTeams = 6

        try:
            numTeams = len(ss_brackets[0]['teams'])
        except Exception as e:
            numTeams = 6

        scene = ""

        if numTeams == 6:
            scene = config.SSS_BRACKETS_6_TEAMS
        else:
            scene = config.LEFT_SSS_BRACKETS_8_TEAMS

        obs.toggle_source_visibility(scene, "SS - Brackets - Title - Text", info['visibility'])

        for i in range(numTeams):
            obs.toggle_source_visibility(scene, "SS - Brackets - Team " +str(i+1), info['visibility'])

        if info['side'] == "Left":
            obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Brackets - " + str(numTeams) + " Teams", info['visibility'])
            obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Brackets - " + str(numTeams) + " Teams", False)
        else:
            obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Brackets - " + str(numTeams) + " Teams", info['visibility'])
            obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Brackets - " + str(numTeams) + " Teams", False)

def ss_display_ind_bracket(info):
    
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Brackets - 6 Teams", False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Brackets - 6 Teams", False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Brackets - 8 Teams", False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Brackets - 8 Teams", False)

    numTeams = 6

    side = config.SIDE.LEFT

    if info['side'] == "Right":
        side = config.SIDE.RIGHT

    if info['phase'] == "Superplayoffs":
        numTeams = 8

    brackets = config.data.get_brackets_with_teams(info['phase'])
    brack = None

    for bracket in brackets:
        if bracket['bracket'] == info['bracket']:
            brack = bracket

    config.sss.show_individual_bracket(brack, side)

def ss_update_bracket_combobox(self):
    global dpd_SS_BRA_Phase, dpd_SS_BRA_Bracket

    brackets = config.data.get_bracket_list(dpd_SS_BRA_Phase.get())
    dpd_SS_BRA_Bracket.config(values=brackets)

###---END SS BRACKET---###
###---BEGIN FS BRACKET---###

def update_fs_bracket_gui(prev_number_brackets, current_number_brackets, post_number_brackets):
    global fs_brackets, fs_bracketLen, fs_ActiveBracketIndex
    global lbl_FS_BRA_Bracket_Previous, lbl_FS_BRA_Bracket_Current, lbl_FS_BRA_Bracket_Next, fs_NumBrackets

    for i in range(prev_number_brackets):
        lbl_FS_BRA_Bracket_Previous[i].config(text=fs_brackets[fs_ActiveBracketIndex+i-prev_number_brackets]['bracket'])
        
    if prev_number_brackets < 5:
        for i in range(5, prev_number_brackets, -1):
            lbl_FS_BRA_Bracket_Previous[i-1].config(text="")

    for i in range(current_number_brackets):
        lbl_FS_BRA_Bracket_Current[i].config(text=fs_brackets[fs_ActiveBracketIndex+i]['bracket'])

    if current_number_brackets < 5:
        for i in range(5, current_number_brackets, -1):
            lbl_FS_BRA_Bracket_Current[i-1].config(text="")

    for i in range(post_number_brackets):
        lbl_FS_BRA_Bracket_Next[i].config(text=fs_brackets[fs_ActiveBracketIndex+i+post_number_brackets]['bracket'])
        
    if post_number_brackets < 5:
        for i in range(5, post_number_brackets, -1):
            lbl_FS_BRA_Bracket_Next[i-1].config(text="")

def cycle_fs_brackets(info):
    global fs_brackets, fs_bracketLen, fs_ActiveBracketIndex, btn_FS_BRA_Next, fs_NumBrackets, during_num_brackets
    
    fs_brackets = config.data.get_brackets_with_teams(info['phase'])
    fs_bracketLen = len(fs_brackets[0]['teams'])
    if info['phase'] == "Superplayoffs":
        fs_NumBrackets = 18
    else:
        fs_NumBrackets = 84/fs_bracketLen
    fs_ActiveBracketIndex = 0

    during_num_brackets = 3

    toggle_fs_bracket_display({
        #'brackets':fs_brackets[0:3],
        'visibility':True,
        'all':False
    })

    config.fss.show_ind_bracket(fs_brackets[:3], True, fs_NumBrackets, fs_bracketLen)
    if info['phase'] == "Superplayoffs":
        update_fs_bracket_gui(0,3,5)
    else:
        update_fs_bracket_gui(0,3,3)
    btn_FS_BRA_Next.config(state=config.tk.NORMAL)

def change_fs_bracket_state(info, phase):
    global btn_FS_BRA_GoBack, btn_FS_BRA_Next, fs_ActiveBracketIndex, fs_bracketLen, fs_NumBrackets, during_num_brackets

    indexChange = 3

    before_num_brackets = 3
    during_num_brackets = 3
    after_num_brackets = 3

    if phase == "Prelims" and fs_ActiveBracketIndex == 12 and info == 1:
        indexChange = 2
    elif phase == "Superplayoffs":
        if info == 1:
            if fs_ActiveBracketIndex != 0:
                indexChange = 5
        elif info == -1:
            if fs_ActiveBracketIndex != 3:
                indexChange = 5

    fs_ActiveBracketIndex = fs_ActiveBracketIndex + (info * indexChange)

    if fs_ActiveBracketIndex == 0:
        before_num_brackets = 0

    if phase == "Superplayoffs":
        fs_NumBrackets == 18
        if fs_ActiveBracketIndex != 0:
            fs_bracketLen = 4
        else:
            fs_bracketLen = 8

    if phase == "Prelims" and fs_ActiveBracketIndex == 9:
        after_num_brackets = 2
    elif phase == "Prelims" and fs_ActiveBracketIndex == 12:
        during_num_brackets = 2
        after_num_brackets = 0
    elif phase == "Playoffs" and fs_ActiveBracketIndex == 9:
        after_num_brackets = 0
    elif phase == "Superplayoffs":
        if fs_ActiveBracketIndex == 0:
            after_num_brackets = 5
        elif fs_ActiveBracketIndex == 3:
            during_num_brackets = 5
            after_num_brackets = 5
        elif fs_ActiveBracketIndex == 8:
            before_num_brackets = 5
            during_num_brackets = 5
            after_num_brackets = 5
        elif fs_ActiveBracketIndex == 13:
            before_num_brackets = 5
            during_num_brackets = 5
            after_num_brackets = 0   

    if info == -1:
        if fs_ActiveBracketIndex == 0:
            btn_FS_BRA_GoBack.config(state=config.tk.DISABLED)
        btn_FS_BRA_Next.config(state=config.tk.NORMAL)
    else:
        if fs_ActiveBracketIndex + indexChange >= fs_NumBrackets-1:
            btn_FS_BRA_Next.config(state=config.tk.DISABLED)
        btn_FS_BRA_GoBack.config(state=config.tk.NORMAL)

    update_fs_bracket_gui(before_num_brackets, during_num_brackets, after_num_brackets)
    if phase != "Superplayoffs":
        config.fss.show_ind_bracket(fs_brackets[fs_ActiveBracketIndex:(fs_ActiveBracketIndex+indexChange)], False, fs_NumBrackets, fs_bracketLen)
    else:
        config.fss.show_ind_bracket(fs_brackets[fs_ActiveBracketIndex:(fs_ActiveBracketIndex+during_num_brackets)], False, indexChange)

def toggle_fs_bracket_display(info):

    global fs_brackets, fs_bracketLen, dpd_FS_BRA_Bracket, dpd_FS_BRA_Phase, fs_ActiveBracketIndex, during_num_brackets

    numTeams = 6
    active_brackets = []

    for i in range(6):
        if dpd_FS_BRA_Bracket[i].get() != "":
            active_brackets.append(dpd_FS_BRA_Bracket[i].get())

    if len(active_brackets) == 0:
        numBrackets = during_num_brackets
    else:
        numBrackets = len(active_brackets)

    try:
        numTeams = len(fs_brackets[fs_ActiveBracketIndex]['teams'])
    except Exception as e:
        teams = config.data.get_teams_in_bracket(dpd_FS_BRA_Phase.get(), active_brackets[0])
        numTeams = len(teams)

    scene = ""

    if numTeams == 4:
        if numBrackets == 1:
            scene = config.FSS_BRACKETS_1_4TEAMS
        elif numBrackets == 2:
            scene = config.FSS_BRACKETS_2_4TEAMS
        elif numBrackets == 3:
            scene = config.FSS_BRACKETS_3_4TEAMS
        elif numBrackets == 4:
            scene = config.FSS_BRACKETS_4_4TEAMS
        elif numBrackets == 5:
            scene = config.FSS_BRACKETS_5_4TEAMS
        else:
            scene = config.FSS_BRACKETS_6_4TEAMS
    elif numTeams == 5:
        if numBrackets == 1:
            scene = config.FSS_BRACKETS_1_5TEAMS
        elif numBrackets == 2:
            scene = config.FSS_BRACKETS_2_5TEAMS
        else:
            scene = config.FSS_BRACKETS_3_5TEAMS
    elif numTeams == 6:
        if numBrackets == 1:
            scene = config.FSS_BRACKETS_1_6TEAMS
        elif numBrackets == 2:
            scene = config.FSS_BRACKETS_2_6TEAMS
        else:
            scene = config.FSS_BRACKETS_3_6TEAMS
    elif numTeams == 7:
        if numBrackets == 1:
            scene = config.FSS_BRACKETS_1_7TEAMS
        elif numBrackets == 2:
            scene = config.FSS_BRACKETS_2_7TEAMS
        else:
            scene = config.FSS_BRACKETS_3_7TEAMS
    else:
        if numBrackets == 1:
            scene = config.FSS_BRACKETS_1_8TEAMS
        elif numBrackets == 2:
            scene = config.FSS_BRACKETS_2_8TEAMS
        else:
            scene = config.FSS_BRACKETS_3_8TEAMS

    print(scene)
    if info['all']:
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, scene, info['visibility'])
    else:
        for i in range(numBrackets):
            obs.toggle_source_visibility(scene, "FS - Brackets - Bracket " +str(i+1) + " - Title", info['visibility'])
            #obs.toggle_source_visibility(scene, "Bracket " +str(i+1) + " - Title", info['visibility'])

def fs_display_ind_bracket(info):
    
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_6TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_6TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_6TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_8TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_8TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_8TEAMS, False)

    numTeams = 6

    if info['phase'] == "Superplayoffs":
        numTeams = 8

    all_brackets = config.data.get_brackets_with_teams(info['phase'])
    selected_brackets = info['brackets']
    toSend_brackets = []

    for current_all_bracket in all_brackets:
        for current_selected_bracket in selected_brackets:
            if current_selected_bracket == current_all_bracket['bracket']:
                toSend_brackets.append(current_all_bracket)

    config.fss.toggle_brackets_visibility(False)
    config.fss.show_ind_bracket(toSend_brackets, False)

def fs_update_bracket_combobox(self):
    global dpd_FS_BRA_Phase, dpd_FS_BRA_Bracket
    phase = dpd_FS_BRA_Phase.get()

    brackets = config.data.get_bracket_list(dpd_FS_BRA_Phase.get())



    for i in range(3):
        dpd_FS_BRA_Bracket[i].config(values=brackets)

    for i in range(3, 6):
        if phase == "Superplayoffs":
            remove_strings = {"Championship", "9-16", "17-24"}

            filtered_list = [item for item in brackets if item not in remove_strings]
            dpd_FS_BRA_Bracket[i].config(values=filtered_list, state="normal")
        else:
            dpd_FS_BRA_Bracket[i].config(values=[], state="disabled")

###---END FS BRACKET---###
###---BEGIN SS INDIVIDUAL---###

def update_individual_gui():

    global ss_players
    global ss_startRank

    global lbl_SS_IND_Prev_Rank, lbl_SS_IND_Prev_Name, lbl_SS_IND_Prev_PPG
    global lbl_SS_IND_Curr_Rank, lbl_SS_IND_Curr_Name, lbl_SS_IND_Curr_PPG
    global lbl_SS_IND_Next_Rank, lbl_SS_IND_Next_Name, lbl_SS_IND_Next_PPG

    global btn_SS_IND_GoBack, btn_SS_IND_Next

    for i in range(6):
        if ss_startRank == 0:
            lbl_SS_IND_Prev_Rank[i].config(text="")
            lbl_SS_IND_Prev_Name[i].config(text="")
            lbl_SS_IND_Prev_PPG[i].config(text="")
        else:
            lbl_SS_IND_Prev_Rank[i].config(text=ss_players[ss_startRank-6+i]['rank'])
            lbl_SS_IND_Prev_Name[i].config(text=ss_players[ss_startRank-6+i]['name'])
            lbl_SS_IND_Prev_PPG[i].config(text=ss_players[ss_startRank-6+i]['ppg'])

        lbl_SS_IND_Curr_Rank[i].config(text=ss_players[ss_startRank+i]['rank'])
        lbl_SS_IND_Curr_Name[i].config(text=ss_players[ss_startRank+i]['name'])
        lbl_SS_IND_Curr_PPG[i].config(text=ss_players[ss_startRank+i]['ppg'])

        if ss_startRank == 24:
            lbl_SS_IND_Next_Rank[i].config(text="")
            lbl_SS_IND_Next_Name[i].config(text="")
            lbl_SS_IND_Next_PPG[i].config(text="")
        else:
            lbl_SS_IND_Next_Rank[i].config(text=ss_players[ss_startRank+6+i]['rank'])
            lbl_SS_IND_Next_Name[i].config(text=ss_players[ss_startRank+6+i]['name'])
            lbl_SS_IND_Next_PPG[i].config(text=ss_players[ss_startRank+6+i]['ppg'])

def cycle_individual(info):
    global ss_startRank
    global ss_players

    ss_startRank = 0
    ss_players = config.data.get_players()
    btn_SS_IND_Next.config(state=config.tk.NORMAL)

    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Header", True)

    if info['side'] == "Left":
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Individual Standings", True)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Individual Standings", False)
    else:
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Individual Standings", True)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Individual Standings", False)

    update_individual_gui()
    config.sss.show_individual_page(ss_players[(ss_startRank):(ss_startRank+6)])

def change_ss_individual_state(info):
    global btn_SS_IND_GoBack, btn_SS_IND_Next
    global ss_startRank

    if info == -1:
        ss_startRank = ss_startRank - 6

        if ss_startRank == 0:
            btn_SS_IND_GoBack.config(state=config.tk.DISABLED)
        btn_SS_IND_Next.config(state=config.tk.NORMAL)

    else:
        ss_startRank = ss_startRank + 6

        if ss_startRank == 24:
            btn_SS_IND_Next.config(state=config.tk.DISABLED)
        btn_SS_IND_GoBack.config(state=config.tk.NORMAL)

    update_individual_gui()
    config.sss.show_individual_page(ss_players[(ss_startRank):(ss_startRank+6)])

def toggle_ss_ind_display(info):

    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Header", info['visibility'])

    for i in range(6):
        obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player " + str(i), info['visibility'])

    if info['side'] == "Left":
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Individual Standings", info['visibility'])
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Individual Standings", False)
    else:
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Right Side - Individual Standings", info['visibility'])
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, "Left Side - Individual Standings", False)

###---END SS INDIVIDUAL---###
###---BEGIN FS INDIVIDUAL---###

def update_fs_individual_gui():

    global FS_players
    global fs_startRank

    global lbl_FS_IND_Prev_Rank, lbl_FS_IND_Prev_Name, lbl_FS_IND_Prev_PPG
    global lbl_FS_IND_Curr_Rank, lbl_FS_IND_Curr_Name, lbl_FS_IND_Curr_PPG
    global lbl_FS_IND_Next_Rank, lbl_FS_IND_Next_Name, lbl_FS_IND_Next_PPG

    global btn_FS_IND_GoBack, btn_FS_IND_Next

    for i in range(10):
        if fs_startRank == 0:
            lbl_FS_IND_Prev_Rank[i].config(text="")
            lbl_FS_IND_Prev_Name[i].config(text="")
            lbl_FS_IND_Prev_PPG[i].config(text="")
        else:
            lbl_FS_IND_Prev_Rank[i].config(text=FS_players[fs_startRank-10+i]['rank'])
            lbl_FS_IND_Prev_Name[i].config(text=FS_players[fs_startRank-10+i]['name'])
            lbl_FS_IND_Prev_PPG[i].config(text=FS_players[fs_startRank-10+i]['ppg'])

        lbl_FS_IND_Curr_Rank[i].config(text=FS_players[fs_startRank+i]['rank'])
        lbl_FS_IND_Curr_Name[i].config(text=FS_players[fs_startRank+i]['name'])
        lbl_FS_IND_Curr_PPG[i].config(text=FS_players[fs_startRank+i]['ppg'])

        if fs_startRank == 20:
            lbl_FS_IND_Next_Rank[i].config(text="")
            lbl_FS_IND_Next_Name[i].config(text="")
            lbl_FS_IND_Next_PPG[i].config(text="")
        else:
            lbl_FS_IND_Next_Rank[i].config(text=FS_players[fs_startRank+10+i]['rank'])
            lbl_FS_IND_Next_Name[i].config(text=FS_players[fs_startRank+10+i]['name'])
            lbl_FS_IND_Next_PPG[i].config(text=FS_players[fs_startRank+10+i]['ppg'])

def cycle_fs_individual(info):
    global fs_startRank
    global FS_players

    fs_startRank = 0
    FS_players = config.data.get_players()
    btn_FS_IND_Next.config(state=config.tk.NORMAL)

    update_fs_individual_gui()
    config.fss.show_individual_ranking(FS_players[(fs_startRank):(fs_startRank+10)])
    toggle_FS_ind_display({
        'visibility':True,
        'all':True
    })

def change_FS_individual_state(info):
    global btn_FS_IND_GoBack, btn_FS_IND_Next
    global fs_startRank

    if info == -1:
        fs_startRank = fs_startRank - 10

        if fs_startRank == 0:
            btn_FS_IND_GoBack.config(state=config.tk.DISABLED)
        btn_FS_IND_Next.config(state=config.tk.NORMAL)

    else:
        fs_startRank = fs_startRank + 10

        if fs_startRank == 20:
            btn_FS_IND_Next.config(state=config.tk.DISABLED)
        btn_FS_IND_GoBack.config(state=config.tk.NORMAL)

    update_fs_individual_gui()
    toggle_FS_ind_display({'visibility':False, 'all':False})
    config.fss.show_individual_ranking(FS_players[(fs_startRank):(fs_startRank+10)])
    config.time.sleep(config.SLEEP_TIME)
    toggle_FS_ind_display({'visibility':True, 'all':False})

def toggle_FS_ind_display(info):

    if info['all']:
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_INDIVIDUAL, info['visibility'])

    for i in range(10):
        obs.toggle_source_visibility(config.FSS_INDIVIDUAL, "FS - Individual - P" + str(i+1), info['visibility'])
        obs.toggle_source_visibility(config.FSS_INDIVIDUAL, "FS - Individual - P" + str(i+1) + " - Rank - Text", info['visibility'])
        obs.toggle_source_visibility(config.FSS_INDIVIDUAL, "FS - Individual - P" + str(i+1) + " - PPG - Text", info['visibility'])

###---END FS INDIVIDUAL---###
###---BEGIN SS STANDINGS---###

def ss_standings_select_phases_update_combobox(self):
    global dpd_SS_STA_PhaseSelect, dpd_SS_STA_BracketSelect

    selected_phase = dpd_SS_STA_PhaseSelect.get()
    brackets =  config.data.get_bracket_list(selected_phase)

    dpd_SS_STA_BracketSelect.config(values=brackets)

def ss_standings_changeStandings(side):
    global dpd_SS_STA_PhaseSelect, dpd_SS_STA_BracketSelect

    selected_phase = dpd_SS_STA_PhaseSelect.get()
    selected_bracket_name = dpd_SS_STA_BracketSelect.get()
    selected_side = config.SIDE.LEFT
    scene_choice = config.SSS_STANDINGS_6_TEAMS
    dir_scene_choice = config.LEFT_SSS_STANDINGS_6_TEAMS

    print(side)

    if side == "Right":
        selected_side = config.SIDE.RIGHT

    standings = config.data.get_standings(selected_phase)

    if selected_phase == "Superplayoffs":
        if selected_side == config.SIDE.LEFT:
            dir_scene_choice = config.LEFT_SSS_STANDINGS_8_TEAMS
        else:
            dir_scene_choice = config.RIGHT_SSS_STANDINGS_8_TEAMS
        scene_choice = config.SSS_STANDINGS_8_TEAMS
    elif selected_side == config.SIDE.RIGHT:
        dir_scene_choice = config.RIGHT_SSS_STANDINGS_6_TEAMS

    for bracket in standings:
        if bracket['name'] == selected_bracket_name:
            team_count = 1

            for school in bracket['teams']:
                obs.toggle_source_visibility(scene_choice, "SS - Standings - Team " + str(team_count), False)
                team_count +=1

            team_count = 1
            obs.toggle_source_visibility(scene_choice, "SS - Standings - Title - Text", False)

            config.time.sleep(config.SLEEP_TIME)

            config.sss.show_individual_standings(bracket, scene_choice, dir_scene_choice)

def toggle_ss_standings_display(info):
    global dpd_SS_STA_PhaseSelect

    selected_phase = dpd_SS_STA_PhaseSelect.get()
    scene_select = config.SSS_STANDINGS_6_TEAMS
    dir_scene_select = config.LEFT_SSS_STANDINGS_6_TEAMS

    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_STANDINGS_6_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_STANDINGS_8_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_STANDINGS_6_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_STANDINGS_8_TEAMS, False)

    print(info["side"])

    if selected_phase == "Superplayoffs":
        scene_select = config.SSS_STANDINGS_8_TEAMS

        if info["side"] == "Right":
            dir_scene_select == config.RIGHT_SSS_STANDINGS_8_TEAMS
        else:
            dir_scene_select == config.LEFT_SSS_STANDINGS_8_TEAMS
    elif info["side"] == "Right":
        dir_scene_select = config.RIGHT_SSS_STANDINGS_6_TEAMS

    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene_select, info["visibility"])

    if(info["visibility"] == False):
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_STANDINGS_6_TEAMS, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_STANDINGS_8_TEAMS, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_STANDINGS_6_TEAMS, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_STANDINGS_8_TEAMS, False)

###---END SS STANDINGS---###
###---BEGIN FS STANDINGS---###

def fs_standings_select_phases_update_combobox(self):
    global dpd_FS_STA_PhaseSelect, dpd_FS_STA_BracketSelect

    selected_phase = dpd_FS_STA_PhaseSelect.get()
    brackets =  config.data.get_bracket_list(selected_phase)

    dpd_FS_STA_BracketSelect.config(values=brackets)

def fs_standings_changeStandings():
    global dpd_FS_STA_PhaseSelect, dpd_FS_STA_BracketSelect

    selected_phase = dpd_FS_STA_PhaseSelect.get()
    selected_bracket_name = dpd_FS_STA_BracketSelect.get()
    scene_choice = config.SSS_STANDINGS_6_TEAMS
    dir_scene_choice = config.LEFT_SSS_STANDINGS_6_TEAMS

    standings = config.data.get_standings(selected_phase)

    if selected_phase == "Superplayoffs":
        if selected_bracket_name == "Championship" or selected_bracket_name == "9-16" or selected_bracket_name == "17-24":
            scene_choice = config.STANDINGS_8
        else:
            scene_choice = config.STANDINGS_4
    elif selected_phase == "Playoffs":
        scene_choice = config.STANDINGS_7
    else:
        scene_choice = config.STANDINGS_6

    obs.toggle_source_visibility(scene_choice, "FS - Standings - Title", False)

    for bracket in standings:
        if bracket['name'] == selected_bracket_name:
            team_count = 1

            for school in bracket['teams']:
                obs.toggle_source_visibility(scene_choice, "FS - Standings - Team " + str(team_count), False)
                team_count +=1

            team_count = 1

            config.time.sleep(config.SLEEP_TIME)
            config.fss.show_ind_standings(selected_phase, bracket)
            break

def toggle_fs_standings_display(info):
    global dpd_FS_STA_PhaseSelect, dpd_FS_STA_BracketSelect

    selected_phase = dpd_FS_STA_PhaseSelect.get()
    scene_select = config.STANDINGS_6

    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_4, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_5, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_6, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_7, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_8, False)

    bracket = dpd_FS_STA_BracketSelect.get()

    if selected_phase == "Superplayoffs":
        if bracket == "Championship" or bracket == "9-16" or bracket == "17-24":
            scene_select = config.STANDINGS_8
        else:
            scene_select = config.STANDINGS_4

    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, scene_select, info["visibility"])

###---END FS STANDINGS---###

###---ANNOUNCEMENT---###

def make_announcement():
    global txt_ANN_Announcement
    path = "./Text Files/Announcement.txt"
    text_input = txt_ANN_Announcement.get("1.0", "end-1c")

    with open(path, 'w') as file:
        file.write(text_input)

def toggle_announcement_display(show):
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Announcements", show)

###---TIMER---###

def update_specificTime():
    global txt_TIM_Choose_ST
    path = "./Text Files/Timer/Specific Time.txt"

    time = txt_TIM_Choose_ST.get()
    time = time + " CDT"

    with open(path, 'w') as file:
        file.write(time)

def toggle_timer_display(show):
    global txt_TIM_Choose_ST, radvar_TIM_Type

    if show:
        if radvar_TIM_Type.get() == "Countdown":
            obs.toggle_source_visibility("Timer", "Timer - Countdown", True)
            obs.toggle_source_visibility("Timer", "Timer - Time", False)
        else:
            obs.toggle_source_visibility("Timer", "Timer - Countdown", False)
            obs.toggle_source_visibility("Timer", "Timer - Time", True)

        config.time.sleep(config.SLEEP_TIME)
    obs.toggle_source_visibility("Waiting Scene", "Timer", show)

###---END TIMER---###
###---BEGIN CORNERSTONE---###

def checkTeamsBracketed():
    global lbl_API_CRN_PhaseName, lbl_API_CRN_TeamsBracketed, btn_API_CRN_CheckTeamsBracketed, btn_API_CRN_GetData, lbl_API_CRN_isDone

    pools = config.cornerstone.get_no_bracket_numbers()

    lbl_API_CRN_TeamsBracketed[0].config(text=str(pools['Prelims']))
    lbl_API_CRN_TeamsBracketed[1].config(text=str(pools['Playoffs']))
    lbl_API_CRN_TeamsBracketed[2].config(text=str(pools['Superplayoffs']))

def getCornerstoneData(phase):
    indexNo = 0
    startRound = 1
    endRound = 5
    global lbl_API_CRN_PhaseName, lbl_API_CRN_TeamsBracketed, btn_API_CRN_CheckTeamsBracketed, btn_API_CRN_GetData, lbl_API_CRN_isDone

    if phase == "Playoffs":
        indexNo=1
        startRound=6
        endRound=10
    elif phase == "Superplayoffs":
        indexNo=2
        startRound=11
        endRound=16
    
    brackets = config.data.get_brackets_with_teams(phase)

    with open("./Data/Brackets/" + phase + ".json", 'w') as f:
        config.json.dump(brackets, f)

    for i in range(startRound, endRound+1):
        round_matchups = config.data.get_matchups(i)

        if not round_matchups == []:
            with open("./Data/Matchups/Round " +str(i) + ".json", 'w') as f:
                config.json.dump(round_matchups, f)

    lbl_API_CRN_isDone[indexNo].config(text="Done!")

###---END CORNERSTONE---###
###---BEGIN FSS QUESTIONS---###

def toggle_question_display(info):
    
    global dpd_FS_Q_Round, dpd_FS_Q_Question, dpd_FS_Q_TU_Bonus

    tu_bonus = dpd_FS_Q_TU_Bonus.get()

    if info == 1:
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Question Scene", True)
        obs.toggle_source_visibility("Question Scene", "Question - Header", True)

        if tu_bonus == "Tossup":
            obs.toggle_source_visibility("Question Scene", "Question - Tossup", True)
        else:
            obs.toggle_source_visibility("Question Scene", "Question - Bonus", True)
    else:
        obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Question Scene", False)
        obs.toggle_source_visibility("Question Scene", "Question - Header", False)
        obs.toggle_source_visibility("Question Scene", "Question - Tossup", False)
        obs.toggle_source_visibility("Question Scene", "Question - Bonus", False)

def update_Question_rounds():
    global dpd_FS_Q_Round, dpd_FS_Q_Question, dpd_FS_Q_TU_Bonus

    path = "./Data/Questions/"

    round_numbers = []

    for filename in config.os.listdir(path):
        match = config.re.match(r"Round (\d+)\.json", filename)

        if match:
            round_numbers.append(int(match.group(1)))

    round_numbers.sort()
    round_numbers_str = [f"{num:02d}" for num in round_numbers]

    dpd_FS_Q_Round.config(values=round_numbers) 

def apply_question():

    global dpd_FS_Q_Round, dpd_FS_Q_Question, dpd_FS_Q_TU_Bonus

    round_number = int(dpd_FS_Q_Round.get())
    question_number = int(dpd_FS_Q_Question.get())
    isTU = False

    if dpd_FS_Q_TU_Bonus.get() == "Tossup":
        isTU = True

    config.fss.load_question(round_number, question_number, isTU)

###---END FSS QUESTIONS---###
###---BEGIN GAME ROOM SCORES---###

def updateTeams():
    global lbl_GR_Team1_name, lbl_GR_Team2_name, lbl_CR_Team1_score, lbl_CR_Team2_score, dpd_Team1, dpd_Team2, lbl_GR_currentQ

    path = "./Text Files/Game Room/"
    if dpd_Team1.get() == "":
        with open(path + "Active Left Team Name.txt", 'r') as file:
            lbl_GR_Team1_name.config(text=file.read())
    else:
        lbl_GR_Team1_name.config(text=dpd_Team1.get())

    if dpd_Team2.get() == "":
        with open(path + "Active Right Team Name.txt", 'r') as file:
            lbl_GR_Team2_name.config(text=file.read())
    else:
        lbl_GR_Team2_name.config(text=dpd_Team2.get())

    with open(path + "Active Left Team Score.txt", 'r') as file:
        lbl_CR_Team1_score.config(text=file.read())
    with open(path + "Active Right Team Score.txt", 'r') as file:
        lbl_CR_Team2_score.config(text=file.read())

    with open (path + "Current Cycle.txt", 'r') as file:
        lbl_GR_currentQ.config(text=file.read())

def changeScore(team, increment):
    global lbl_GR_Team1_name, lbl_GR_Team2_name, lbl_CR_Team1_score, lbl_CR_Team2_score, dpd_Team1, dpd_Team2

    path = "./Text Files/Game Room/"

    if team == 1:
        team1score=0

        with open(path + "Active Left Team Score.txt", 'r') as file:
            team1score = int(file.read())
        
        if increment:
            team1score = team1score + 10
        else:
            team1score = team1score - 10

        lbl_CR_Team1_score.config(text=str(team1score))

        with open(path + "Active Left Team Score.txt", 'w') as file:
            file.write(str(team1score))
    else:
        team2score=0

        with open(path + "Active Right Team Score.txt", 'r') as file:
            team2score = int(file.read())

        if increment:
            team2score = team2score + 10
        else:
            team2score = team2score - 10

        lbl_CR_Team2_score.config(text=str(team2score))

        with open(path + "Active Right Team Score.txt", 'w') as file:
            file.write(str(team2score))

def clearScores():
    global lbl_GR_Team1_name, lbl_GR_Team2_name, lbl_CR_Team1_score, lbl_CR_Team2_score, dpd_Team1, dpd_Team2

    path = "./Text Files/Game Room/"

    with open(path + "Active Left Team Score.txt", 'w') as file:
        file.write("0")
        lbl_CR_Team1_score.config(text="0")
    with open(path + "Active Right Team Score.txt", 'w') as file:
        file.write("0")
        lbl_CR_Team2_score.config(text="0")

def changeQ(inc, isTU):
    global numTUsInGame, lbl_GR_currentQ
    
    path = "./Text Files/Game Room/Current Cycle.txt"
    qText = ""

    with open (path, 'r') as file:
        qText = file.read()

    qNumber = int(qText.split(" ")[1].split("/")[0])

    if inc == 1:
        qNumber+=1
    elif inc == -1 and qNumber > 1:
        qNumber-=1

    if isTU:
        qText = "Tossup " + str(qNumber) + "/" + str(numTUsInGame)
    else:
        qText = "Bonus " + str(qNumber) + "/" + str(numTUsInGame)

    with open (path, 'w') as file:
        file.write(qText)

    lbl_GR_currentQ.config(text=qText)

###---END GAME ROOM SCORES---###
###---BEGIN GAME ROOM ROUND---###

def change_Round():
    global dpd_Rounds, numTUsInGame, lbl_GR_currentQ

    roundText = ""
    path = "./Text Files/Game Room/Current Round.txt"

    if dpd_Rounds.get() == "Finals":
        roundText = "Finals"
    else:
        roundText = "Round " + dpd_Rounds.get()

    with open (path, 'w') as file:
        file.write(roundText)

    if "." in dpd_Rounds.get():
        numTUsInGame = 10
    else:
        numTUsInGame = 20

    qText = ""
    path = "./Text Files/Game Room/Current Cycle.txt"

    with open (path, 'r') as file:
        qText = file.read()

    qText = qText.split("/")[0] + "/" + str(numTUsInGame)

    with open (path, 'w') as file:
        file.write(qText)

    lbl_GR_currentQ.config(text=qText)

def ResetQCounter():
    global numTUsInGame, lbl_GR_currentQ

    path = "./Text Files/Game Room/Current Cycle.txt"

    qText = "Tossup 1/" + str(numTUsInGame)

    with open (path, 'w') as file:
        file.write(qText)

    lbl_GR_currentQ.config(text=qText)

###---END GAME ROOM ROUND---###
###---BEGIN INIT---###

def init_gui():
    global lbl_changePhase_before
    global lbl_changePhase_current
    global lbl_changePhase_after

    global lbl_SS_IND_Prev_Rank, lbl_SS_IND_Prev_Name, lbl_SS_IND_Prev_PPG
    global lbl_SS_IND_Curr_Rank, lbl_SS_IND_Curr_Name, lbl_SS_IND_Curr_PPG
    global lbl_SS_IND_Next_Rank, lbl_SS_IND_Next_Name, lbl_SS_IND_Next_PPG

    global btn_SS_IND_GoBack, btn_SS_IND_Next
    global dpd_FS_Q_Round, dpd_FS_Q_Question, dpd_FS_Q_TU_Bonus

    global startRank
    startRank = 0

    global lbl_SS_BRA_Bracket_Previous, lbl_SS_BRA_Bracket_Current, lbl_SS_BRA_Bracket_Next
    global btn_SS_BRA_GoBack, btn_SS_BRA_Next
    global dpd_SS_BRA_Phase, dpd_SS_BRA_Bracket
    global dpd_SS_MAT_PhaseSelect, dpd_SS_MAT_IndividualMatches_Bracket, dpd_SS_MAT_IndividualMatches_Round, dpd_SS_MAT_IndividualMatches_Matchup
    global dpd_SS_MAT_BracketinRound_Bracket, dpd_SS_MAT_BracketinRound_Round, radvar_SS_MAT_Side
    global SS_MAT_LastCount

    global dpd_SS_RES_PhaseSelect, dpd_SS_RES_IndividualMatches_Bracket, dpd_SS_RES_IndividualMatches_Round, dpd_SS_RES_IndividualMatches_Matchup
    global dpd_SS_RES_BracketinRound_Bracket, dpd_SS_RES_BracketinRound_Round, radvar_SS_RES_Side
    global SS_RES_LastCount

    global dpd_SS_STA_PhaseSelect, dpd_SS_STA_BracketSelect

    SS_MAT_LastCount = 1
    SS_RES_LastCount = 1

    global lbl_FS_IND_Prev_Rank, lbl_FS_IND_Prev_Name, lbl_FS_IND_Prev_PPG
    global lbl_FS_IND_Curr_Rank, lbl_FS_IND_Curr_Name, lbl_FS_IND_Curr_PPG
    global lbl_FS_IND_Next_Rank, lbl_FS_IND_Next_Name, lbl_FS_IND_Next_PPG

    global btn_FS_IND_GoBack, btn_FS_IND_Next

    global FS_startRank
    startRank = 0

    global lbl_FS_BRA_Bracket_Previous, lbl_FS_BRA_Bracket_Current, lbl_FS_BRA_Bracket_Next
    global btn_FS_BRA_GoBack, btn_FS_BRA_Next
    global dpd_FS_BRA_Phase, dpd_FS_BRA_Bracket
    global dpd_FS_MAT_PhaseSelect, dpd_FS_MAT_IndividualMatches_Bracket, dpd_FS_MAT_IndividualMatches_Round, dpd_FS_MAT_IndividualMatches_Matchup
    global dpd_FS_MAT_BracketinRound_Bracket, dpd_FS_MAT_BracketinRound_Round
    global FS_MAT_LastCount

    global dpd_FS_RES_PhaseSelect, dpd_FS_RES_IndividualMatches_Bracket, dpd_FS_RES_IndividualMatches_Round, dpd_FS_RES_IndividualMatches_Matchup
    global dpd_FS_RES_BracketinRound_Bracket, dpd_FS_RES_BracketinRound_Round
    global FS_RES_LastCount

    global dpd_FS_STA_PhaseSelect, dpd_FS_STA_BracketSelect

    global lbl_API_api_name, lbl_API_api_status, btn_API_checkPing

    global txt_ANN_Announcement
    global txt_TIM_Choose_ST, radvar_TIM_Type

    global lbl_API_CRN_PhaseName, lbl_API_CRN_TeamsBracketed, btn_API_CRN_CheckTeamsBracketed, btn_API_CRN_GetData, lbl_API_CRN_isDone

    global lbl_GR_Team1_name, lbl_GR_Team2_name, lbl_CR_Team1_score, lbl_CR_Team2_score, dpd_Team1, dpd_Team2
    global dpd_Rounds, lbl_GR_currentQ, numTUsInGame
    FS_MAT_LastCount = 1
    FS_RES_LastCount = 1

    numTUsInGame = 20

    # Create the main window
    root = config.tk.Tk()
    root.title("PACE NSC OBS Helper")
    root.geometry("1400x600")  # Set the size of the window

    notebook = config.ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    #Create the Tabs
    main_tab = config.ttk.Frame(notebook)
    gameRoomTab = config.ttk.Frame(notebook)
    hostArea_tab = config.ttk.Frame(notebook)
    interviewArea_tab = config.ttk.Frame(notebook)
    sideshot_tab = config.ttk.Frame(notebook)
    awards_tab = config.ttk.Frame(notebook)
    status_tab = config.ttk.Frame(notebook)
    other_tab = config.ttk.Frame(notebook)
    fss_tab = config.ttk.Frame(notebook)
    timer_tab = config.ttk.Frame(notebook)
    announcement_tab = config.ttk.Frame(notebook)

    notebook.add(main_tab, text="Main Control")
    notebook.add(gameRoomTab, text="Game Room")
    notebook.add(hostArea_tab, text="Host Area")
    notebook.add(interviewArea_tab, text="Interview Area")
    notebook.add(sideshot_tab, text="Sideshot")
    notebook.add(fss_tab, text="Full Screen Stats")
    notebook.add(awards_tab, text="Awards")
    notebook.add(announcement_tab, text="Announcements")
    notebook.add(timer_tab, text="Timer")
    notebook.add(status_tab, text="API Status")
    notebook.add(other_tab, text="Other")

    ss_notebook = config.ttk.Notebook(sideshot_tab)
    ss_notebook.pack(expand=True, fill="both")

    fs_notebook = config.ttk.Notebook(fss_tab)
    fs_notebook.pack(expand=True, fill="both")

    api_notebook = config.ttk.Notebook(status_tab)
    api_notebook.pack(expand=True, fill="both")
    
    GR_notebook = config.ttk.Notebook(gameRoomTab)
    GR_notebook.pack(expand=True, fill="both")

    gameRoom_Teams_tab = config.ttk.Frame(gameRoomTab)
    gameRoom_Score_tab = config.ttk.Frame(gameRoomTab)
    gameRoom_Round_tab = config.ttk.Frame(gameRoomTab)

    ss_brackets = config.ttk.Frame(sideshot_tab)
    ss_ind = config.ttk.Frame(sideshot_tab)
    ss_matchups = config.ttk.Frame(sideshot_tab)
    ss_results = config.ttk.Frame(sideshot_tab)
    ss_standings = config.ttk.Frame(sideshot_tab)

    GR_notebook.add(gameRoom_Teams_tab, text="Teams")
    GR_notebook.add(gameRoom_Score_tab, text="Score")
    GR_notebook.add(gameRoom_Round_tab, text="Settings")

    ss_notebook.add(ss_brackets, text="Brackets")
    ss_notebook.add(ss_ind, text="Individual Standings")
    ss_notebook.add(ss_matchups, text="Matchups")
    ss_notebook.add(ss_results, text="Results")
    ss_notebook.add(ss_standings, text="Standings")

    fs_brackets = config.ttk.Frame(fss_tab)
    fs_ind = config.ttk.Frame(fss_tab)
    fs_matchups = config.ttk.Frame(fss_tab)
    fs_results = config.ttk.Frame(fss_tab)
    fs_standings = config.ttk.Frame(fss_tab)
    fs_questions = config.ttk.Frame(fss_tab)

    fs_notebook.add(fs_brackets, text="Brackets")
    fs_notebook.add(fs_ind, text="Individual Standings")
    fs_notebook.add(fs_matchups, text="Matchups")
    fs_notebook.add(fs_results, text="Results")
    fs_notebook.add(fs_standings, text="Standings")
    fs_notebook.add(fs_questions, text="Questions")

    api_general = config.ttk.Frame(status_tab)
    api_cornerstone = config.ttk.Frame(status_tab)

    api_notebook.add(api_general, text="All")
    api_notebook.add(api_cornerstone, text="Cornerstone")
    
    # Main Tab Buttons
    btn_changeScene_GameRoom = config.ttk.Button(main_tab, text="Game Room", command=lambda:change_scene(0))
    btn_changeScene_HostArea = config.ttk.Button(main_tab, text="Host Area", command=lambda:change_scene(1))
    btn_changeScene_Interview = config.ttk.Button(main_tab, text="Interview Area", command=lambda:change_scene(2))
    btn_changeScene_Donate = config.ttk.Button(main_tab, text="Donate to PACE!", command=lambda:change_scene(3))
    btn_changeScene_StartaTeam = config.ttk.Button(main_tab, text="Start a Team!", command=lambda:change_scene(4))
    
    lbl_Scenes = config.ttk.Label(main_tab, text="Change Scenes:")

    lbl_Phase_stream = config.tk.Label(main_tab, text="Change Stream Phase:")
    lbl_Phase_stream.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    dpd_Phase_stream = config.ttk.Combobox(main_tab, values=config.PHASES)
    dpd_Phase_stream.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    btn_changePhase_stream = config.ttk.Button(main_tab, text="Apply Stream Phase Change", command=lambda:obs.set_phase(dpd_Phase_stream.get()))
    btn_changePhase_stream.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    
    lbl_Scenes.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    btn_changeScene_GameRoom.grid(row=1, column=0, padx=5, pady=5)
    btn_changeScene_HostArea.grid(row=1, column=1, padx=5, pady=5)
    btn_changeScene_Interview.grid(row=1, column=2, padx=5, pady=5)
    btn_changeScene_Donate.grid(row=2, column=0, padx=10, pady=10)
    btn_changeScene_StartaTeam.grid(row=2, column=1, padx=10, pady=10)

    #Game Room Tab
    lbl_goToGameRoom = config.ttk.Label(gameRoom_Teams_tab, text="Go to Game Room: ")
    btn_changeScene_GR = config.ttk.Button(gameRoom_Teams_tab, text="Game Room", command=lambda:change_scene(0))

    lbl_changeTeam1 = config.ttk.Label(gameRoom_Teams_tab, text="Choose Team 1")
    dpd_Team1 = config.ttk.Combobox(gameRoom_Teams_tab, values=list(teams.keys()))
    lbl_changeTeam2 = config.ttk.Label(gameRoom_Teams_tab, text="Choose Team 2")
    dpd_Team2 = config.ttk.Combobox(gameRoom_Teams_tab, values=list(teams.keys()))

    lbl_OvrTeams = config.ttk.Label(gameRoom_Teams_tab, text="Override Team Names")
    lbl_OvrTeam1 = config.ttk.Label(gameRoom_Teams_tab, text="Override Team 1")
    txt_OvrTeam1 = config.ttk.Entry(gameRoom_Teams_tab)
    lbl_OvrTeam2 = config.ttk.Label(gameRoom_Teams_tab, text="Override Team 2")
    txt_OvrTeam2 = config.ttk.Entry(gameRoom_Teams_tab)

    lbl_OvrCity = config.ttk.Label(gameRoom_Teams_tab, text="Override City")
    lbl_OvrCity1 = config.ttk.Label(gameRoom_Teams_tab, text="Override City 1")
    txt_OvrCity1 = config.ttk.Entry(gameRoom_Teams_tab)
    lbl_OvrCity2 = config.ttk.Label(gameRoom_Teams_tab, text="Override City 2")
    txt_OvrCity2 = config.ttk.Entry(gameRoom_Teams_tab)

    btn_applyGROvr = config.ttk.Button(gameRoom_Teams_tab, text="Update Teams", command=lambda:update_teams({
        'team1':dpd_Team1.get().strip(),
        'team2':dpd_Team2.get().strip(),
        'city1':teams[dpd_Team1.get()]['city'].strip(),
        'city2':teams[dpd_Team2.get()]['city'].strip(),
        'ovr_team1':txt_OvrTeam1.get().strip(),
        'ovr_team2':txt_OvrTeam2.get().strip(),
        'ovr_city1':txt_OvrCity1.get().strip(),
        'ovr_city2':txt_OvrCity2.get().strip()
    }))

    lbl_updT1score = config.ttk.Label(gameRoom_Teams_tab, text="Update Team 1 Score")
    txt_updT1Score = config.ttk.Entry(gameRoom_Teams_tab)
    lbl_updT2score = config.ttk.Label(gameRoom_Teams_tab, text="Update Team 2 Score")
    txt_updT2Score = config.ttk.Entry(gameRoom_Teams_tab)
    lbl_updCycle = config.ttk.Label(gameRoom_Teams_tab, text="Update Cycle")
    txt_updCycle = config.ttk.Entry(gameRoom_Teams_tab)
    lbl_updRound = config.ttk.Label(gameRoom_Teams_tab, text="Update Round")
    txt_updRound = config.ttk.Entry(gameRoom_Teams_tab)
    btn_updScore = config.ttk.Button(gameRoom_Teams_tab, text="Update Score Override", command=lambda:update_scores({
        'score1':txt_updT1Score.get(),
        'score2':txt_updT2Score.get(),
        'cycle':txt_updCycle.get(),
        'round':txt_updRound.get(),
        'update_s1':(txt_updT1Score.get() != ""),
        'update_s2':(txt_updT2Score.get() != ""),
        'update_cycle':(txt_updCycle.get() != ""),
        'update_round':(txt_updRound.get() != "")
    }))
    
    lbl_goToGameRoom.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_changeScene_GR.grid(row=0, column=2, padx=10, pady=10)
    lbl_changeTeam1.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    dpd_Team1.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
    lbl_changeTeam2.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    dpd_Team2.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

    lbl_OvrTeams.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
    lbl_OvrTeam1.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    txt_OvrTeam1.grid(row=6, column=2, columnspan=2, padx=10, pady=10)
    lbl_OvrTeam2.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    txt_OvrTeam2.grid(row=7, column=2, columnspan=2, padx=10, pady=10)
    lbl_OvrCity.grid(row=5, column=5, columnspan=4, padx=10, pady=10)
    lbl_OvrCity1.grid(row=6, column=5, columnspan=2, padx=10, pady=10)
    txt_OvrCity1.grid(row=6, column=7, columnspan=2, padx=10, pady=10)
    lbl_OvrCity2.grid(row=7, column=5, columnspan=2, padx=10, pady=10)
    txt_OvrCity2.grid(row=7, column=7, columnspan=2, padx=10, pady=10)
    btn_applyGROvr.grid(row=8, column=0, columnspan=8, padx=10, pady=10)

    lbl_updT1score.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
    txt_updT1Score.grid(row=10, column=2, columnspan=2, padx=10, pady=10)
    lbl_updT2score.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
    txt_updT2Score.grid(row=11, column=2, columnspan=2, padx=10, pady=10)
    lbl_updCycle.grid(row=10, column=5, columnspan=2, padx=10, pady=10)
    txt_updCycle.grid(row=10, column=7, columnspan=2, padx=10, pady=10)
    lbl_updRound.grid(row=11, column=5, columnspan=2, padx=10, pady=10)
    txt_updRound.grid(row=11, column=7, columnspan=2, padx=10, pady=10)
    btn_updScore.grid(row=12, column=0, columnspan=8, padx=10, pady=10)

    #Scores tab

    lbl_goToGameRoom = config.ttk.Label(gameRoom_Score_tab, text="Go to Game Room: ")
    btn_changeScene_GR = config.ttk.Button(gameRoom_Score_tab, text="Game Room", command=lambda:change_scene(0))

    btn_GR_UpdateTeams = config.ttk.Button(gameRoom_Score_tab, text="Update Teams", command=lambda:updateTeams())

    lbl_GR_Team1_name = config.ttk.Label(gameRoom_Score_tab, text="Team 1")
    lbl_GR_Team2_name = config.ttk.Label(gameRoom_Score_tab, text="Team 2")
    lbl_CR_Team1_score = config.ttk.Label(gameRoom_Score_tab, text="0")
    lbl_CR_Team2_score = config.ttk.Label(gameRoom_Score_tab, text="0")

    btn_GR_Team1_addScore = config.ttk.Button(gameRoom_Score_tab, text="+", command=lambda:changeScore(1, True))
    btn_GR_Team2_addScore = config.ttk.Button(gameRoom_Score_tab, text="+", command=lambda:changeScore(2, True))
    btn_GR_Team1_subScore = config.ttk.Button(gameRoom_Score_tab, text="-", command=lambda:changeScore(1, False))
    btn_GR_Team2_subScore = config.ttk.Button(gameRoom_Score_tab, text="-", command=lambda:changeScore(2, False))

    btn_GR_Team1Cut = config.ttk.Button(gameRoom_Score_tab, text="Cut to Team 1", command=lambda:change_scene(9))
    btn_GR_Team2Cut = config.ttk.Button(gameRoom_Score_tab, text="Cut to Team 2", command=lambda:change_scene(10))

    btn_GR_ClearScores = config.ttk.Button(gameRoom_Score_tab, text="Clear Scores", command=lambda:clearScores())

    lbl_GR_ChangeQ = config.ttk.Label(gameRoom_Score_tab, text="Change Question Number")

    btn_GR_PrevTU = config.ttk.Button(gameRoom_Score_tab, text="Previous Tossup", command=lambda:changeQ(-1, True))
    btn_GR_PrevBonus = config.ttk.Button(gameRoom_Score_tab, text="Previous Bonus", command=lambda:changeQ(-1, False))
    btn_GR_NextTU = config.ttk.Button(gameRoom_Score_tab, text="Next Tossup", command=lambda:changeQ(1, True))
    btn_GR_NextBonus = config.ttk.Button(gameRoom_Score_tab, text="Next Bonus", command=lambda:changeQ(1, False))
    lbl_GR_currentQ = config.ttk.Label(gameRoom_Score_tab, text="Current Question")

    btn_GR_Reset = config.ttk.Button(gameRoom_Score_tab, text="Reset", command=lambda:ResetQCounter())

    lbl_goToGameRoom.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_changeScene_GR.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    btn_GR_UpdateTeams.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    lbl_GR_Team1_name.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    lbl_GR_Team2_name.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

    btn_GR_Team1_addScore.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    btn_GR_Team2_addScore.grid(row=4, column=2, columnspan=2, padx=10, pady=10)
    lbl_CR_Team1_score.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    lbl_CR_Team2_score.grid(row=5, column=2, columnspan=2, padx=10, pady=10)
    btn_GR_ClearScores.grid(row=5, column=4, columnspan=2, padx=10, pady=10)
    btn_GR_Team1_subScore.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    btn_GR_Team2_subScore.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

    btn_GR_Team1Cut.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
    btn_GR_Team2Cut.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

    lbl_GR_ChangeQ.grid(row=10, column=0, columnspan=6, padx=10, pady=10)
    btn_GR_PrevTU.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
    btn_GR_PrevBonus.grid(row=12, column=0, columnspan=2, padx=10, pady=10)
    lbl_GR_currentQ.grid(row=11, column=2, columnspan=2, rowspan=2, padx=10, pady=10)
    btn_GR_NextTU.grid(row=11, column=4, columnspan=2, padx=10, pady=10)
    btn_GR_NextBonus.grid(row=12, column=4, columnspan=2, padx=10, pady=10)
    btn_GR_Reset.grid(row=13, column=0, columnspan=6, padx=10, pady=10)

    #Game Room Rounds

    rounds = ["1", "2", "3", "4", "5", "5.1", "5.2",
              "6", "7", "8", "9", "10", "11", "12", "12.1", "12.2",
              "13", "14", "15", "16", "17", "18", "18.1", "18.2", "Finals"]
    
    lbl_Rounds = config.ttk.Label(gameRoom_Round_tab, text="Select Round")
    dpd_Rounds = config.ttk.Combobox(gameRoom_Round_tab, values=rounds)
    btn_ChangeRound = config.ttk.Button(gameRoom_Round_tab, text="Change Round", command=lambda:change_Round())

    lbl_Rounds.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    dpd_Rounds.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
    btn_ChangeRound.grid(row=1, column=0, columnspan=4, padx=10, pady=10)


    #Host Area Tab
    lbl_goToHostArea = config.ttk.Label(hostArea_tab, text="Go to Host Room: ")
    btn_changeScene_HA = config.ttk.Button(hostArea_tab, text="Host Area", command=lambda:change_scene(1))

    lbl_Commentator1 = config.ttk.Label(hostArea_tab, text="Commentator 1")
    lbl_Commentator2 = config.ttk.Label(hostArea_tab, text="Commentator 2")
    lbl_Commentator3 = config.ttk.Label(hostArea_tab, text="Commentator 3")
    lbl_Name = config.ttk.Label(hostArea_tab, text="Name")
    lbl_Role = config.ttk.Label(hostArea_tab, text="Role")
    lbl_Visible = config.ttk.Label(hostArea_tab, text="Visible")

    txt_name1 = config.ttk.Entry(hostArea_tab)
    txt_name2 = config.ttk.Entry(hostArea_tab)
    txt_name3 = config.ttk.Entry(hostArea_tab)
    txt_role1 = config.ttk.Entry(hostArea_tab)
    txt_role2 = config.ttk.Entry(hostArea_tab)
    txt_role3 = config.ttk.Entry(hostArea_tab)

    ckb_val1 = config.tk.BooleanVar(value=False)
    ckb_val2 = config.tk.BooleanVar(value=False)
    ckb_val3 = config.tk.BooleanVar(value=False)

    ckb_comm1 = config.ttk.Checkbutton(hostArea_tab, variable=ckb_val1)
    ckb_comm2 = config.ttk.Checkbutton(hostArea_tab, variable=ckb_val2)
    ckb_comm3 = config.ttk.Checkbutton(hostArea_tab, variable=ckb_val3)

    btn_Update_HostArea = config.ttk.Button(hostArea_tab, text="Update Host Area", command=lambda:update_hostArea({
        'comm1':txt_name1.get(),
        'comm2':txt_name2.get(),
        'comm3':txt_name3.get(),
        'role1':txt_role1.get(),
        'role2':txt_role2.get(),
        'role3':txt_role3.get(),
        'vis1':ckb_val1.get(),
        'vis2':ckb_val2.get(),
        'vis3':ckb_val3.get()
    }))

    lbl_goToHostArea.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_changeScene_HA.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
    lbl_Commentator1.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
    lbl_Commentator2.grid(row=2, column=4, columnspan=2, padx=10, pady=10)
    lbl_Commentator3.grid(row=2, column=6, columnspan=2, padx=10, pady=10)
    lbl_Name.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    txt_name1.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    txt_name2.grid(row=3, column=4, columnspan=2, padx=10, pady=10)
    txt_name3.grid(row=3, column=6, columnspan=2, padx=10, pady=10)
    lbl_Role.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    txt_role1.grid(row=4, column=2, columnspan=2, padx=10, pady=10)
    txt_role2.grid(row=4, column=4, columnspan=2, padx=10, pady=10)
    txt_role3.grid(row=4, column=6, columnspan=2, padx=10, pady=10)
    lbl_Visible.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    ckb_comm1.grid(row=5, column=2, columnspan=2, padx=10, pady=10)
    ckb_comm2.grid(row=5, column=4, columnspan=2, padx=10, pady=10)
    ckb_comm3.grid(row=5, column=6, columnspan=2, padx=10, pady=10)
    btn_Update_HostArea.grid(row=6, column=0, columnspan=8, padx=10, pady=10)

    #Interview Area Tab
    lbl_goToIntArea = config.ttk.Label(interviewArea_tab, text="Go to Interview Room: ")
    btn_changeScene_IA = config.ttk.Button(interviewArea_tab, text="Interview Area", command=lambda:change_scene(2))

    lbl_intArea_lines = config.ttk.Label(interviewArea_tab, text="Change Values")
    lbl_Subject = config.ttk.Label(interviewArea_tab, text="Subject")
    lbl_Line1 = config.ttk.Label(interviewArea_tab, text="Line 1")
    lbl_Line2 = config.ttk.Label(interviewArea_tab, text="Line 2")
    lbl_caption = config.ttk.Label(interviewArea_tab, text="Caption")

    txt_subject = config.ttk.Entry(interviewArea_tab)
    txt_line1 = config.ttk.Entry(interviewArea_tab)
    txt_line2 = config.ttk.Entry(interviewArea_tab)
    txt_caption = config.ttk.Entry(interviewArea_tab)

    btn_hideOverlay = config.ttk.Button(interviewArea_tab, text="Hide Overlay", command=lambda:toggle_int_data(False))
    btn_showOverlay = config.ttk.Button(interviewArea_tab, text="Show Overlay", command=lambda:toggle_int_data(True))
    btn_ApplyChanges = config.ttk.Button(interviewArea_tab, text="Apply and Show", command=lambda:update_InterviewArea({
        'subject':txt_subject.get(),
        'line1':txt_line1.get(),
        'line2':txt_line2.get(),
        'caption':txt_caption.get()
    }))

    lbl_goToIntArea.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_changeScene_IA.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
    lbl_intArea_lines.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    lbl_Subject.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    lbl_Line1.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    lbl_Line2.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    lbl_caption.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    txt_subject.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    txt_line1.grid(row=4, column=2, columnspan=2, padx=10, pady=10)
    txt_line2.grid(row=5, column=2, columnspan=2, padx=10, pady=10)
    txt_caption.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

    btn_ApplyChanges.grid(row=7, column=0, columnspan=4, padx=10, pady=10)
    btn_hideOverlay.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
    btn_showOverlay.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

    #Awards Tab
    lbl_AWD_goToAwards = config.ttk.Label(awards_tab, text="Go to Awards:")
    btn_AWD_goToAwards = config.ttk.Button(awards_tab, text="Awards", command=lambda:change_scene(6))

    lbl_AWD_IND_Category = config.ttk.Label(awards_tab, text="Pick Individual Category")
    radvar_AWD_IND_Category = config.tk.StringVar()
    rad_AWD_IND_Overall = config.ttk.Radiobutton(awards_tab, text="Overall", variable=radvar_AWD_IND_Category, value="Overall")
    rad_AWD_Ind_Rising = config.ttk.Radiobutton(awards_tab, text="Rising Star", variable=radvar_AWD_IND_Category, value="Rising Star")

    lbl_AWD_TEAM_Category = config.ttk.Label(awards_tab, text="Pick Team Category")
    radvar_AWD_TEAM_Category = config.tk.StringVar()
    rad_AWD_TEAM_Overall = config.ttk.Radiobutton(awards_tab, text="Overall", variable=radvar_AWD_TEAM_Category, value="Overall")
    rad_AWD_TEAM_SS = config.ttk.Radiobutton(awards_tab, text="Small School", variable=radvar_AWD_TEAM_Category, value="Small School")
    rad_AWD_TEAM_JV = config.ttk.Radiobutton(awards_tab, text="JV", variable=radvar_AWD_TEAM_Category, value="JV")

    lbl_AWD_IND_Info = config.ttk.Label(awards_tab,text="Individual Info")
    lbl_AWD_TEAM_Info = config.ttk.Label(awards_tab,text="Team Info")

    lbl_AWD_IND_Rank = config.ttk.Label(awards_tab, text="Rank")
    txt_AWD_IND_Rank = config.ttk.Entry(awards_tab)
    lbl_AWD_IND_Player = config.ttk.Label(awards_tab, text="Player")
    txt_AWD_IND_Player = config.ttk.Entry(awards_tab)
    lbl_AWD_IND_Grade = config.ttk.Label(awards_tab, text="Grade")
    txt_AWD_IND_Grade = config.ttk.Entry(awards_tab)
    lbl_AWD_IND_Team = config.ttk.Label(awards_tab, text="Team")
    dpd_AWD_IND_Team = config.ttk.Combobox(awards_tab, values=list(teams.keys()))
    lbl_AWD_IND_PPG = config.ttk.Label(awards_tab, text="PPG")
    txt_AWD_IND_PPG = config.ttk.Entry(awards_tab)

    lbl_AWD_TEAM_Rank = config.ttk.Label(awards_tab, text="Rank")
    txt_AWD_TEAM_Rank = config.ttk.Entry(awards_tab)
    lbl_AWD_TEAM_Team = config.ttk.Label(awards_tab, text="Team")
    dpd_AWD_TEAM_Team = config.ttk.Combobox(awards_tab, values=list(teams.keys()))

    btn_AWD_Change_IND = config.ttk.Button(awards_tab, text="Change Individual", command=lambda:update_awards({
        'is_team':False,
        'info':{
            'type':radvar_AWD_IND_Category.get(),
            'rank':txt_AWD_IND_Rank.get(),
            'player':txt_AWD_IND_Player.get(),
            'grade':txt_AWD_IND_Grade.get(),
            'team':dpd_AWD_IND_Team.get(),
            'ppg':txt_AWD_IND_PPG.get()
        }
    }))
    btn_AWD_CHANGE_TEAM = config.ttk.Button(awards_tab, text="Change Team", command=lambda:update_awards({
        'is_team':True,
        'info':{
            'type':radvar_AWD_TEAM_Category.get(),
            'rank':txt_AWD_TEAM_Rank.get(),
            'team':dpd_AWD_TEAM_Team.get()
        }
    }))
    btn_AWD_HideAwards = config.ttk.Button(awards_tab, text="Hide Awards", command=lambda:toggle_awards_overlay(False))
    btn_AWD_ShowAwards = config.ttk.Button(awards_tab, text="Show Awards", command=lambda:toggle_awards_overlay(True))

    lbl_AWD_goToAwards.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    btn_AWD_goToAwards.grid(row=0, column=2, columnspan=3, padx=10, pady=10)

    lbl_AWD_IND_Category.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    rad_AWD_IND_Overall.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    rad_AWD_Ind_Rising.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    lbl_AWD_TEAM_Category.grid(row=2, column=3, columnspan=3, padx=10, pady=10)
    rad_AWD_TEAM_Overall.grid(row=3, column=3, columnspan=3, padx=10, pady=10)
    rad_AWD_TEAM_SS.grid(row=4, column=3, columnspan=3, padx=10, pady=10)
    rad_AWD_TEAM_JV.grid(row=5, column=3, columnspan=3, padx=10, pady=10)

    lbl_AWD_IND_Info.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
    lbl_AWD_TEAM_Info.grid(row=7, column=3, columnspan=3, padx=10, pady=10)

    lbl_AWD_IND_Rank.grid(row=9, column=0, padx=10, pady=10)
    txt_AWD_IND_Rank.grid(row=9, column=1, columnspan=2, padx=10, pady=10)
    lbl_AWD_IND_Player.grid(row=10, column=0, padx=10, pady=10)
    txt_AWD_IND_Player.grid(row=10, column=1, columnspan=2, padx=10, pady=10)
    lbl_AWD_IND_Grade.grid(row=11, column=0, padx=10, pady=10)
    txt_AWD_IND_Grade.grid(row=11, column=1, columnspan=2, padx=10, pady=10)
    lbl_AWD_IND_Team.grid(row=12, column=0, padx=10, pady=10)
    dpd_AWD_IND_Team.grid(row=12, column=1, columnspan=2, padx=10, pady=10)
    lbl_AWD_IND_PPG.grid(row=13, column=0, padx=10, pady=10)
    txt_AWD_IND_PPG.grid(row=13, column=1, columnspan=2, padx=10, pady=10)
    btn_AWD_Change_IND.grid(row=15, column=0, columnspan=3, padx=10, pady=10)

    lbl_AWD_TEAM_Rank.grid(row=9, column=3, padx=10, pady=10)
    txt_AWD_TEAM_Rank.grid(row=9, column=4, columnspan=2, padx=10, pady=10)
    lbl_AWD_TEAM_Team.grid(row=10, column=3, padx=10, pady=10)
    dpd_AWD_TEAM_Team.grid(row=10, column=4, columnspan=2, padx=10, pady=10)
    btn_AWD_CHANGE_TEAM.grid(row=15, column=4, columnspan=3, padx=10, pady=10)

    btn_AWD_HideAwards.grid(row=17, column=0, columnspan=3, padx=10, pady=10)
    btn_AWD_ShowAwards.grid(row=17, column=3, columnspan=3, padx=10, pady=10)

    #Side Shot Tab - Individual
    lbl_SS_gotoSS = config.ttk.Label(ss_ind, text="Go to Sideshot")
    btn_SS_gotoSS = config.ttk.Button(ss_ind, text="Sideshot", command=lambda:change_scene(5))

    radvar_SS_IND_Side = config.tk.StringVar()
    lbl_SS_IND_PickSide = config.ttk.Label(ss_ind, text="Pick a Side")
    rad_SS_IND_Side_Left = config.ttk.Radiobutton(ss_ind, text="Left", variable=radvar_SS_IND_Side, value="Left")
    rad_SS_IND_Side_Right = config.ttk.Radiobutton(ss_ind, text="Right", variable=radvar_SS_IND_Side, value="Right")

    btn_SS_IND_Cycle_Ind = config.ttk.Button(ss_ind, text="Cycle Individual", command=lambda:cycle_individual({
        'side':radvar_SS_IND_Side.get()
    }))

    lbl_SS_IND_Title_Previous = config.ttk.Label(ss_ind, text="Previous 6")
    lbl_SS_IND_Title_Current = config.ttk.Label(ss_ind, text="Current 6")
    lbl_SS_IND_Title_Next = config.ttk.Label(ss_ind, text="Next 6")

    lbl_SS_IND_Prev_Rank = []
    lbl_SS_IND_Prev_Name = []
    lbl_SS_IND_Prev_PPG = []

    lbl_SS_IND_Curr_Rank = []
    lbl_SS_IND_Curr_Name = []
    lbl_SS_IND_Curr_PPG = []

    lbl_SS_IND_Next_Rank = []
    lbl_SS_IND_Next_Name = []
    lbl_SS_IND_Next_PPG = []

    for i in range(6):
        lbl_SS_IND_Prev_Rank.append(config.ttk.Label(ss_ind, text=""))
        lbl_SS_IND_Prev_Name.append(config.ttk.Label(ss_ind, text=""))
        lbl_SS_IND_Prev_PPG.append(config.ttk.Label(ss_ind, text=""))
        lbl_SS_IND_Curr_Rank.append(config.ttk.Label(ss_ind, text=""))
        lbl_SS_IND_Curr_Name.append(config.ttk.Label(ss_ind, text=""))
        lbl_SS_IND_Curr_PPG.append(config.ttk.Label(ss_ind, text=""))
        lbl_SS_IND_Next_Rank.append(config.ttk.Label(ss_ind, text=""))
        lbl_SS_IND_Next_Name.append(config.ttk.Label(ss_ind, text=""))
        lbl_SS_IND_Next_PPG.append(config.ttk.Label(ss_ind, text=""))

    btn_SS_IND_GoBack = config.ttk.Button(ss_ind, text="Go Back", state=config.tk.DISABLED, command=lambda:change_ss_individual_state(-1))
    btn_SS_IND_Next = config.ttk.Button(ss_ind, text="Next", state=config.tk.DISABLED, command=lambda:change_ss_individual_state(1))

    btn_SS_IND_ShowIND = config.ttk.Button(ss_ind, text="Show", command=lambda:toggle_ss_ind_display({
        'visibility':True,
        'side':radvar_SS_IND_Side.get()
    }))
    btn_SS_IND_HideIND = config.ttk.Button(ss_ind, text="Hide", command=lambda:toggle_ss_ind_display({
        'visibility':False,
        'side':radvar_SS_IND_Side.get()
    }))

    lbl_SS_gotoSS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
    btn_SS_gotoSS.grid(row=0, column=4, columnspan=2, padx=10, pady=10)

    lbl_SS_IND_PickSide.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_IND_Side_Left.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_IND_Side_Right.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    btn_SS_IND_Cycle_Ind.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    lbl_SS_IND_Title_Previous.grid(row=2, column=2, columnspan=4, padx=10, pady=10)
    lbl_SS_IND_Title_Current.grid(row=2, column=6, columnspan=4, padx=10, pady=10)
    lbl_SS_IND_Title_Next.grid(row=2, column=10, columnspan=4, padx=10, pady=10)

    for i in range(6):
        lbl_SS_IND_Prev_Rank[i].grid(row=i+3, column=2, padx=5, pady=5)
        lbl_SS_IND_Prev_Name[i].grid(row=i+3, column=3, columnspan=2, padx=5, pady=5)
        lbl_SS_IND_Prev_PPG[i].grid(row=i+3, column=5, padx=5, pady=5)
        lbl_SS_IND_Curr_Rank[i].grid(row=i+3, column=6, padx=5, pady=5)
        lbl_SS_IND_Curr_Name[i].grid(row=i+3, column=7, columnspan=2, padx=5, pady=5)
        lbl_SS_IND_Curr_PPG[i].grid(row=i+3, column=9, padx=5, pady=5)
        lbl_SS_IND_Next_Rank[i].grid(row=i+3, column=10, padx=5, pady=5)
        lbl_SS_IND_Next_Name[i].grid(row=i+3, column=11, columnspan=2, padx=5, pady=5)
        lbl_SS_IND_Next_PPG[i].grid(row=i+3, column=13, padx=5, pady=5)

    btn_SS_IND_GoBack.grid(row=10, column=2, columnspan=2, padx=10, pady=10)
    btn_SS_IND_Next.grid(row=10, column=4, columnspan=2, padx=10, pady=10)

    btn_SS_IND_ShowIND.grid(row=11, column=4, columnspan=2, padx=10, pady=10)
    btn_SS_IND_HideIND.grid(row=11, column=2, columnspan=2, padx=10, pady=10)

    #Side Shot - Brackets

    lbl_SS_gotoSS = config.ttk.Label(ss_brackets, text="Go to Sideshot")
    btn_SS_gotoSS = config.ttk.Button(ss_brackets, text="Sideshot", command=lambda:change_scene(5))

    radvar_SS_BRA_Side = config.tk.StringVar()
    lbl_SS_BRA_PickSide = config.ttk.Label(ss_brackets, text="Pick a Side")
    rad_SS_BRA_Side_Left = config.ttk.Radiobutton(ss_brackets, text="Left", variable=radvar_SS_BRA_Side, value="Left")
    rad_SS_BRA_Side_Right = config.ttk.Radiobutton(ss_brackets, text="Right", variable=radvar_SS_BRA_Side, value="Right")

    lbl_SS_BRA_Phase = config.ttk.Label(ss_brackets, text="Phase:")
    dpd_SS_BRA_Phase = config.ttk.Combobox(ss_brackets, values=config.GUI_PHASES)
    lbl_SS_BRA_Bracket = config.ttk.Label(ss_brackets, text="Bracket:")
    dpd_SS_BRA_Bracket = config.ttk.Combobox(ss_brackets, values=[])

    btn_SS_BRA_Cycle_Brackets = config.ttk.Button(ss_brackets, text="Loop Brackets", command=lambda:cycle_brackets({
        'side':radvar_SS_BRA_Side.get(),
        'phase':dpd_SS_BRA_Phase.get()
    }))

    btn_SS_BRA_Display_Bracket = config.ttk.Button(ss_brackets, text="Display Bracket", command=lambda:ss_display_ind_bracket({
        'side':radvar_SS_BRA_Side.get(),
        'phase':dpd_SS_BRA_Phase.get(),
        'bracket':dpd_SS_BRA_Bracket.get()
    }))

    lbl_SS_BRA_Title_Previous = config.ttk.Label(ss_brackets, text="Previous Bracket")
    lbl_SS_BRA_Title_Current = config.ttk.Label(ss_brackets, text="Current Bracket")
    lbl_SS_BRA_Title_Next = config.ttk.Label(ss_brackets, text="Next Bracket")

    lbl_SS_BRA_Bracket_Previous = config.ttk.Label(ss_brackets, text="")
    lbl_SS_BRA_Bracket_Current = config.ttk.Label(ss_brackets, text="")
    lbl_SS_BRA_Bracket_Next = config.ttk.Label(ss_brackets, text="")

    btn_SS_BRA_GoBack = config.ttk.Button(ss_brackets, text="Go Back", state=config.tk.DISABLED, command=lambda:change_ss_bracket_state(-1))
    btn_SS_BRA_Next = config.ttk.Button(ss_brackets, text="Next", state=config.tk.DISABLED, command=lambda:change_ss_bracket_state(1))
    
    btn_SS_BRA_Show = config.ttk.Button(ss_brackets, text="Show", command=lambda:toggle_ss_bracket_display({
        'visibility':True,
        'side':radvar_SS_BRA_Side.get()
    }))
    btn_SS_BRA_Hide = config.ttk.Button(ss_brackets, text="Hide", command=lambda:toggle_ss_bracket_display({
        'visibility':False,
        'side':radvar_SS_BRA_Side.get()
    }))

    lbl_SS_gotoSS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
    btn_SS_gotoSS.grid(row=0, column=4, columnspan=2, padx=10, pady=10)

    lbl_SS_BRA_PickSide.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_BRA_Side_Left.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_BRA_Side_Right.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    btn_SS_BRA_Cycle_Brackets.grid(row = 6, column=0, columnspan=2, padx=10, pady=10)

    lbl_SS_BRA_Phase.grid(row=2, column=2, padx=10, pady=10)
    lbl_SS_BRA_Bracket.grid(row=3, column=2, padx=10, pady=10)
    dpd_SS_BRA_Phase.grid(row=2, column=3, columnspan=2, padx=10, pady=10)
    dpd_SS_BRA_Bracket.grid(row=3, column=3, columnspan=2, padx=10, pady=10)
    btn_SS_BRA_Display_Bracket.grid(row=5, column=2, columnspan=3, padx=10, pady=10)

    lbl_SS_BRA_Title_Previous.grid(row=2, column=5, columnspan=2, padx=5, pady=5)
    lbl_SS_BRA_Title_Current.grid(row=2, column=7, columnspan=2, padx=5, pady=5)
    lbl_SS_BRA_Title_Next.grid(row=2, column=9, columnspan=2, padx=5, pady=5)

    lbl_SS_BRA_Bracket_Previous.grid(row=3, column=5, columnspan=2, padx=5, pady=5)
    lbl_SS_BRA_Bracket_Current.grid(row=3, column=7, columnspan=2, padx=5, pady=5)
    lbl_SS_BRA_Bracket_Next.grid(row=3, column=9, columnspan=2, padx=5, pady=5)

    btn_SS_BRA_GoBack.grid(row=5, column=6, columnspan=2, padx=10, pady=10)
    btn_SS_BRA_Next.grid(row=5, column=8, columnspan=2, padx=10, pady=10)
    btn_SS_BRA_Hide.grid(row=6, column=6, columnspan=2, padx=10, pady=10)
    btn_SS_BRA_Show.grid(row=6, column=8, columnspan=2, padx=10, pady=10)

    dpd_SS_BRA_Phase.bind("<<ComboboxSelected>>", ss_update_bracket_combobox)

    #Sideshot - Matches

    lbl_SS_gotoSS = config.ttk.Label(ss_matchups, text="Go to Sideshot")
    btn_SS_gotoSS = config.ttk.Button(ss_matchups, text="Sideshot", command=lambda:change_scene(5))

    radvar_SS_MAT_Side = config.tk.StringVar()
    lbl_SS_MAT_PickSide = config.ttk.Label(ss_matchups, text="Pick a Side")
    rad_SS_MAT_Side_Left = config.ttk.Radiobutton(ss_matchups, text="Left", variable=radvar_SS_MAT_Side, value="Left")
    rad_SS_MAT_Side_Right = config.ttk.Radiobutton(ss_matchups, text="Right", variable=radvar_SS_MAT_Side, value="Right")

    lbl_SS_MAT_PhaseSelect = config.ttk.Label(ss_matchups, text="Phase")
    dpd_SS_MAT_PhaseSelect = config.ttk.Combobox(ss_matchups, values=config.GUI_PHASES)
    dpd_SS_MAT_PhaseSelect.bind("<<ComboboxSelected>>", ss_matches_select_phases_update_combobox)
    
    lbl_SS_MAT_BracketinRound = config.ttk.Label(ss_matchups, text="All Matches in Bracket per Round")
    lbl_SS_MAT_BracketinRound_Bracket = config.ttk.Label(ss_matchups, text="Bracket: ")
    lbl_SS_MAT_BracketinRound_Round = config.ttk.Label(ss_matchups, text="Round: ")
    dpd_SS_MAT_BracketinRound_Bracket = config.ttk.Combobox(ss_matchups, values=[])
    dpd_SS_MAT_BracketinRound_Round = config.ttk.Combobox(ss_matchups, values=[])
    btn_SS_MAT_ShowMatches = config.ttk.Button(
        ss_matchups, text="Show Matches",
        command=lambda:display_ss_matches_allMatchesPerBracketRound(
            dpd_SS_MAT_BracketinRound_Bracket.get(),dpd_SS_MAT_BracketinRound_Round.get(), radvar_SS_MAT_Side.get()))

    lbl_SS_MAT_IndividualMatches = config.ttk.Label(ss_matchups, text="Individual Matches")
    lbl_SS_MAT_IndividualMatches_Header = []
    lbl_SS_MAT_IndividualMatches_Bracket = []
    lbl_SS_MAT_IndividualMatches_Round = []
    lbl_SS_MAT_IndividualMatches_Matchup = []
    dpd_SS_MAT_IndividualMatches_Bracket = []
    dpd_SS_MAT_IndividualMatches_Round = []
    dpd_SS_MAT_IndividualMatches_Matchup = []
    btn_SS_MAT_IndividualMatches_Post = []

    for i in range(4):
        lbl_SS_MAT_IndividualMatches_Header.append(config.ttk.Label(ss_matchups, text="Matchup " + str(i+1)))
        lbl_SS_MAT_IndividualMatches_Bracket.append(config.ttk.Label(ss_matchups, text="Bracket: "))
        lbl_SS_MAT_IndividualMatches_Round.append(config.ttk.Label(ss_matchups, text="Round: "))
        lbl_SS_MAT_IndividualMatches_Matchup.append(config.ttk.Label(ss_matchups, text="Matchup: "))
        dpd_SS_MAT_IndividualMatches_Bracket.append(config.ttk.Combobox(ss_matchups, values=[]))
        dpd_SS_MAT_IndividualMatches_Round.append(config.ttk.Combobox(ss_matchups, values=[]))
        dpd_SS_MAT_IndividualMatches_Matchup.append(config.ttk.Combobox(ss_matchups, values=[]))
        

        dpd_SS_MAT_IndividualMatches_Bracket[i].bind(
            "<<ComboboxSelected>>", config.partial(ss_matches_select_bracket_update_combobox, i))
        dpd_SS_MAT_IndividualMatches_Round[i].bind(
            "<<ComboboxSelected>>", config.partial(ss_matches_select_round_update_combobox, i))
        
    btn_SS_MAT_IndividualMatches_Post.append(config.ttk.Button(ss_matchups, text="Display Match (1)",
                                             command=lambda:display_ss_matches(0)))
    btn_SS_MAT_IndividualMatches_Post.append(config.ttk.Button(ss_matchups, text="Display Match (2)",
                                             command=lambda:display_ss_matches(1)))
    btn_SS_MAT_IndividualMatches_Post.append(config.ttk.Button(ss_matchups, text="Display Match (3)",
                                             command=lambda:display_ss_matches(2)))
    btn_SS_MAT_IndividualMatches_Post.append(config.ttk.Button(ss_matchups, text="Display Match (4)",
                                             command=lambda:display_ss_matches(3)))
    

    btn_SS_MAT_Show = config.ttk.Button(ss_matchups, text="Show", command=lambda:toggle_ss_matches_display({
        'visibility':True,
        'side':radvar_SS_MAT_Side.get()
    }))
    btn_SS_MAT_Hide = config.ttk.Button(ss_matchups, text="Hide", command=lambda:toggle_ss_matches_display({
        'visibility':False,
        'side':radvar_SS_MAT_Side.get()
    }))

    lbl_SS_gotoSS.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_SS_gotoSS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lbl_SS_MAT_PickSide.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_MAT_Side_Left.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_MAT_Side_Right.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    lbl_SS_MAT_PhaseSelect.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
    dpd_SS_MAT_PhaseSelect.grid(row=2, column=4, columnspan=2, padx=10, pady=10)

    lbl_SS_MAT_BracketinRound.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    lbl_SS_MAT_BracketinRound_Bracket.grid(row=4, column=2, padx=10, pady=10)
    lbl_SS_MAT_BracketinRound_Round.grid(row=5, column=2, padx=10, pady=10)
    dpd_SS_MAT_BracketinRound_Bracket.grid(row=4, column=3, padx=10, pady=10)
    dpd_SS_MAT_BracketinRound_Round.grid(row=5, column=3, padx=10, pady=10)
    btn_SS_MAT_ShowMatches.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

    lbl_SS_MAT_IndividualMatches.grid(row=3, column=6, columnspan=8, padx=10, pady=10)

    for i in range(4):
        lbl_SS_MAT_IndividualMatches_Header[i].grid(row=4, column=4+(2*i), columnspan=2, padx=5, pady=5)
        lbl_SS_MAT_IndividualMatches_Bracket[i].grid(row=5, column=4+(2*i), padx=5, pady=5)
        lbl_SS_MAT_IndividualMatches_Round[i].grid(row=6, column=4+(2*i), padx=5, pady=5)
        lbl_SS_MAT_IndividualMatches_Matchup[i].grid(row=7, column=4+(2*i), padx=5, pady=5)
        dpd_SS_MAT_IndividualMatches_Bracket[i].grid(row=5, column=5+(2*i), padx=5, pady=5)
        dpd_SS_MAT_IndividualMatches_Round[i].grid(row=6, column=5+(2*i), padx=5, pady=5)
        dpd_SS_MAT_IndividualMatches_Matchup[i].grid(row=7, column=5+(2*i), padx=5, pady=5)
        btn_SS_MAT_IndividualMatches_Post[i].grid(row=8, column=4+(2*i), columnspan=2, padx=5, pady=5)
        
    btn_SS_MAT_Hide.grid(row=10, column=2, columnspan=2, padx=10, pady=10)
    btn_SS_MAT_Show.grid(row=10, column=4, columnspan=2, padx=10, pady=10)

    #Sideshot - Results

    lbl_SS_gotoSS = config.ttk.Label(ss_results, text="Go to Sideshot")
    btn_SS_gotoSS = config.ttk.Button(ss_results, text="Sideshot", command=lambda:change_scene(5))

    radvar_SS_RES_Side = config.tk.StringVar()
    lbl_SS_RES_PickSide = config.ttk.Label(ss_results, text="Pick a Side")
    rad_SS_RES_Side_Left = config.ttk.Radiobutton(ss_results, text="Left", variable=radvar_SS_RES_Side, value="Left")
    rad_SS_RES_Side_Right = config.ttk.Radiobutton(ss_results, text="Right", variable=radvar_SS_RES_Side, value="Right")

    lbl_SS_RES_PhaseSelect = config.ttk.Label(ss_results, text="Phase")
    dpd_SS_RES_PhaseSelect = config.ttk.Combobox(ss_results, values=config.GUI_PHASES)
    dpd_SS_RES_PhaseSelect.bind("<<ComboboxSelected>>", ss_results_select_phases_update_combobox)
    
    lbl_SS_RES_BracketinRound = config.ttk.Label(ss_results, text="All Results in Bracket per Round")
    lbl_SS_RES_BracketinRound_Bracket = config.ttk.Label(ss_results, text="Bracket: ")
    lbl_SS_RES_BracketinRound_Round = config.ttk.Label(ss_results, text="Round: ")
    dpd_SS_RES_BracketinRound_Bracket = config.ttk.Combobox(ss_results, values=[])
    dpd_SS_RES_BracketinRound_Round = config.ttk.Combobox(ss_results, values=[])
    btn_SS_RES_ShowMatches = config.ttk.Button(
        ss_results, text="Show Results",
        command=lambda:display_ss_results_allResultsPerBracketRound(
            dpd_SS_RES_BracketinRound_Bracket.get(),dpd_SS_RES_BracketinRound_Round.get(), radvar_SS_RES_Side.get()))

    lbl_SS_RES_IndividualMatches = config.ttk.Label(ss_results, text="Individual Results")
    lbl_SS_RES_IndividualMatches_Header = []
    lbl_SS_RES_IndividualMatches_Bracket = []
    lbl_SS_RES_IndividualMatches_Round = []
    lbl_SS_RES_IndividualMatches_Matchup = []
    dpd_SS_RES_IndividualMatches_Bracket = []
    dpd_SS_RES_IndividualMatches_Round = []
    dpd_SS_RES_IndividualMatches_Matchup = []
    btn_SS_RES_IndividualMatches_Post = []

    for i in range(4):
        lbl_SS_RES_IndividualMatches_Header.append(config.ttk.Label(ss_results, text="Result " + str(i+1)))
        lbl_SS_RES_IndividualMatches_Bracket.append(config.ttk.Label(ss_results, text="Bracket: "))
        lbl_SS_RES_IndividualMatches_Round.append(config.ttk.Label(ss_results, text="Round: "))
        lbl_SS_RES_IndividualMatches_Matchup.append(config.ttk.Label(ss_results, text="Matchup: "))
        dpd_SS_RES_IndividualMatches_Bracket.append(config.ttk.Combobox(ss_results, values=[]))
        dpd_SS_RES_IndividualMatches_Round.append(config.ttk.Combobox(ss_results, values=[]))
        dpd_SS_RES_IndividualMatches_Matchup.append(config.ttk.Combobox(ss_results, values=[]))
        

        dpd_SS_RES_IndividualMatches_Bracket[i].bind(
            "<<ComboboxSelected>>", config.partial(ss_results_select_bracket_update_combobox, i))
        dpd_SS_RES_IndividualMatches_Round[i].bind(
            "<<ComboboxSelected>>", config.partial(ss_results_select_round_update_combobox, i))
        
    btn_SS_RES_IndividualMatches_Post.append(config.ttk.Button(ss_results, text="Display Result (1)",
                                             command=lambda:display_ss_results(0)))
    btn_SS_RES_IndividualMatches_Post.append(config.ttk.Button(ss_results, text="Display Result (2)",
                                             command=lambda:display_ss_results(1)))
    btn_SS_RES_IndividualMatches_Post.append(config.ttk.Button(ss_results, text="Display Result (3)",
                                             command=lambda:display_ss_results(2)))
    btn_SS_RES_IndividualMatches_Post.append(config.ttk.Button(ss_results, text="Display Result (4)",
                                             command=lambda:display_ss_results(3)))
    

    btn_SS_RES_Show = config.ttk.Button(ss_results, text="Show", command=lambda:toggle_ss_results_display({
        'visibility':True,
        'side':radvar_SS_RES_Side.get()
    }))
    btn_SS_RES_Hide = config.ttk.Button(ss_results, text="Hide", command=lambda:toggle_ss_results_display({
        'visibility':False,
        'side':radvar_SS_RES_Side.get()
    }))

    lbl_SS_gotoSS.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_SS_gotoSS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lbl_SS_RES_PickSide.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_RES_Side_Left.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_RES_Side_Right.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    lbl_SS_RES_PhaseSelect.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
    dpd_SS_RES_PhaseSelect.grid(row=2, column=4, columnspan=2, padx=10, pady=10)

    lbl_SS_RES_BracketinRound.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    lbl_SS_RES_BracketinRound_Bracket.grid(row=4, column=2, padx=10, pady=10)
    lbl_SS_RES_BracketinRound_Round.grid(row=5, column=2, padx=10, pady=10)
    dpd_SS_RES_BracketinRound_Bracket.grid(row=4, column=3, padx=10, pady=10)
    dpd_SS_RES_BracketinRound_Round.grid(row=5, column=3, padx=10, pady=10)
    btn_SS_RES_ShowMatches.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

    lbl_SS_RES_IndividualMatches.grid(row=3, column=6, columnspan=8, padx=10, pady=10)

    for i in range(4):
        lbl_SS_RES_IndividualMatches_Header[i].grid(row=4, column=4+(2*i), columnspan=2, padx=5, pady=5)
        lbl_SS_RES_IndividualMatches_Bracket[i].grid(row=5, column=4+(2*i), padx=5, pady=5)
        lbl_SS_RES_IndividualMatches_Round[i].grid(row=6, column=4+(2*i), padx=5, pady=5)
        lbl_SS_RES_IndividualMatches_Matchup[i].grid(row=7, column=4+(2*i), padx=5, pady=5)
        dpd_SS_RES_IndividualMatches_Bracket[i].grid(row=5, column=5+(2*i), padx=5, pady=5)
        dpd_SS_RES_IndividualMatches_Round[i].grid(row=6, column=5+(2*i), padx=5, pady=5)
        dpd_SS_RES_IndividualMatches_Matchup[i].grid(row=7, column=5+(2*i), padx=5, pady=5)
        btn_SS_RES_IndividualMatches_Post[i].grid(row=8, column=4+(2*i), columnspan=2, padx=5, pady=5)
        
    btn_SS_RES_Hide.grid(row=10, column=2, columnspan=2, padx=10, pady=10)
    btn_SS_RES_Show.grid(row=10, column=4, columnspan=2, padx=10, pady=10)

    #Sideshot - Standings

    lbl_SS_gotoSS = config.ttk.Label(ss_standings, text="Go to Sideshot")
    btn_SS_gotoSS = config.ttk.Button(ss_standings, text="Sideshot", command=lambda:change_scene(5))

    radvar_SS_STA_Side = config.tk.StringVar()
    lbl_SS_STA_PickSide = config.ttk.Label(ss_standings, text="Pick a Side")
    rad_SS_STA_Side_Left = config.ttk.Radiobutton(ss_standings, text="Left", variable=radvar_SS_STA_Side, value="Left")
    rad_SS_STA_Side_Right = config.ttk.Radiobutton(ss_standings, text="Right", variable=radvar_SS_STA_Side, value="Right")

    lbl_SS_STA_PhaseSelect = config.ttk.Label(ss_standings, text="Phase")
    dpd_SS_STA_PhaseSelect = config.ttk.Combobox(ss_standings, values=config.GUI_PHASES)
    lbl_SS_STA_BracketSelect = config.ttk.Label(ss_standings, text="Bracket: ")
    dpd_SS_STA_BracketSelect = config.ttk.Combobox(ss_standings, values=[])

    dpd_SS_STA_PhaseSelect.bind("<<ComboboxSelected>>", ss_standings_select_phases_update_combobox)

    btn_SS_STA_ApplyStandings = config.ttk.Button(ss_standings, text="Apply", command=lambda:ss_standings_changeStandings(radvar_SS_STA_Side.get()))
    btn_SS_STA_Show = config.ttk.Button(ss_standings, text="Show", command=lambda:toggle_ss_standings_display({
        'visibility':True,
        'side':radvar_SS_STA_Side.get()
    }))
    btn_SS_STA_Hide = config.ttk.Button(ss_standings, text="Hide", command=lambda:toggle_ss_standings_display({
        'visibility':False,
        'side':radvar_SS_STA_Side.get()
    }))

    lbl_SS_gotoSS.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_SS_gotoSS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lbl_SS_STA_PickSide.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_STA_Side_Left.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    rad_SS_STA_Side_Right.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    lbl_SS_STA_PhaseSelect.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
    dpd_SS_STA_PhaseSelect.grid(row=2, column=4, columnspan=2, padx=10, pady=10)
    lbl_SS_STA_BracketSelect.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    dpd_SS_STA_BracketSelect.grid(row=3, column=4, columnspan=2, padx=10, pady=10)

    btn_SS_STA_ApplyStandings.grid(row=4, column=2, columnspan=4, padx=10, pady=10)
    btn_SS_STA_Hide.grid(row=6, column=2, columnspan=2, padx=10, pady=10)
    btn_SS_STA_Show.grid(row=6, column=4, columnspan=2, padx=10, pady=10)

    #Full Screen Tab - Individual
    lbl_FS_gotoSS = config.ttk.Label(fs_ind, text="Go Full Screen:")
    btn_FS_gotoSS = config.ttk.Button(fs_ind, text="Full Screen", command=lambda:change_scene(7))

    btn_fs_ind_Cycle_Ind = config.ttk.Button(fs_ind, text="Cycle Individual", command=lambda:cycle_fs_individual({}))

    lbl_fs_ind_Title_Previous = config.ttk.Label(fs_ind, text="Previous 10")
    lbl_fs_ind_Title_Current = config.ttk.Label(fs_ind, text="Current 10")
    lbl_fs_ind_Title_Next = config.ttk.Label(fs_ind, text="Next 10")

    lbl_FS_IND_Prev_Rank = []
    lbl_FS_IND_Prev_Name = []
    lbl_FS_IND_Prev_PPG = []

    lbl_FS_IND_Curr_Rank = []
    lbl_FS_IND_Curr_Name = []
    lbl_FS_IND_Curr_PPG = []

    lbl_FS_IND_Next_Rank = []
    lbl_FS_IND_Next_Name = []
    lbl_FS_IND_Next_PPG = []

    for i in range(10):
        lbl_FS_IND_Prev_Rank.append(config.ttk.Label(fs_ind, text=""))
        lbl_FS_IND_Prev_Name.append(config.ttk.Label(fs_ind, text=""))
        lbl_FS_IND_Prev_PPG.append(config.ttk.Label(fs_ind, text=""))
        lbl_FS_IND_Curr_Rank.append(config.ttk.Label(fs_ind, text=""))
        lbl_FS_IND_Curr_Name.append(config.ttk.Label(fs_ind, text=""))
        lbl_FS_IND_Curr_PPG.append(config.ttk.Label(fs_ind, text=""))
        lbl_FS_IND_Next_Rank.append(config.ttk.Label(fs_ind, text=""))
        lbl_FS_IND_Next_Name.append(config.ttk.Label(fs_ind, text=""))
        lbl_FS_IND_Next_PPG.append(config.ttk.Label(fs_ind, text=""))

    btn_FS_IND_GoBack = config.ttk.Button(fs_ind, text="Go Back", state=config.tk.DISABLED, command=lambda:change_FS_individual_state(-1))
    btn_FS_IND_Next = config.ttk.Button(fs_ind, text="Next", state=config.tk.DISABLED, command=lambda:change_FS_individual_state(1))

    btn_fs_ind_ShowIND = config.ttk.Button(fs_ind, text="Show", command=lambda:toggle_FS_ind_display({
        'visibility':True,
        'all':True
    }))
    btn_fs_ind_HideIND = config.ttk.Button(fs_ind, text="Hide", command=lambda:toggle_FS_ind_display({
        'visibility':False,
        'all':True
    }))

    lbl_FS_gotoSS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
    btn_FS_gotoSS.grid(row=0, column=4, columnspan=2, padx=10, pady=10)
    btn_fs_ind_Cycle_Ind.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    lbl_fs_ind_Title_Previous.grid(row=2, column=2, columnspan=4, padx=10, pady=10)
    lbl_fs_ind_Title_Current.grid(row=2, column=6, columnspan=4, padx=10, pady=10)
    lbl_fs_ind_Title_Next.grid(row=2, column=10, columnspan=4, padx=10, pady=10)

    for i in range(10):
        lbl_FS_IND_Prev_Rank[i].grid(row=i+3, column=2, padx=5, pady=5)
        lbl_FS_IND_Prev_Name[i].grid(row=i+3, column=3, columnspan=2, padx=5, pady=5)
        lbl_FS_IND_Prev_PPG[i].grid(row=i+3, column=5, padx=5, pady=5)
        lbl_FS_IND_Curr_Rank[i].grid(row=i+3, column=6, padx=5, pady=5)
        lbl_FS_IND_Curr_Name[i].grid(row=i+3, column=7, columnspan=2, padx=5, pady=5)
        lbl_FS_IND_Curr_PPG[i].grid(row=i+3, column=9, padx=5, pady=5)
        lbl_FS_IND_Next_Rank[i].grid(row=i+3, column=10, padx=5, pady=5)
        lbl_FS_IND_Next_Name[i].grid(row=i+3, column=11, columnspan=2, padx=5, pady=5)
        lbl_FS_IND_Next_PPG[i].grid(row=i+3, column=13, padx=5, pady=5)

    btn_FS_IND_GoBack.grid(row=14, column=2, columnspan=2, padx=10, pady=10)
    btn_FS_IND_Next.grid(row=14, column=4, columnspan=2, padx=10, pady=10)

    btn_fs_ind_ShowIND.grid(row=15, column=4, columnspan=2, padx=10, pady=10)
    btn_fs_ind_HideIND.grid(row=15, column=2, columnspan=2, padx=10, pady=10)

	#Full Screen - Brackets

    lbl_FS_gotoFS = config.ttk.Label(fs_brackets, text="Full Screen:")
    btn_FS_gotoFS = config.ttk.Button(fs_brackets, text="Full Screen", command=lambda:change_scene(7))

    lbl_FS_BRA_Phase = config.ttk.Label(fs_brackets, text="Phase:")
    dpd_FS_BRA_Phase = config.ttk.Combobox(fs_brackets, values=config.GUI_PHASES)
    
    lbl_FS_BRA_Bracket = []
    dpd_FS_BRA_Bracket = []
    for i in range(6):
        lbl_FS_BRA_Bracket.append(config.ttk.Label(fs_brackets, text="Bracket:"))
        dpd_FS_BRA_Bracket.append(config.ttk.Combobox(fs_brackets, values=[]))

    dpd_FS_BRA_Phase.bind("<<ComboboxSelected>>", fs_update_bracket_combobox)

    btn_FS_BRA_Cycle_Brackets = config.ttk.Button(fs_brackets, text="Loop Brackets", command=lambda:cycle_fs_brackets({
        'phase':dpd_FS_BRA_Phase.get()
    }))

    btn_FS_BRA_Display_Bracket = config.ttk.Button(fs_brackets, text="Display Bracket", command=lambda:fs_display_ind_bracket({
        'phase':dpd_FS_BRA_Phase.get(),
        'brackets':[dpd_FS_BRA_Bracket[0].get(), dpd_FS_BRA_Bracket[1].get(), dpd_FS_BRA_Bracket[2].get(),
                    dpd_FS_BRA_Bracket[3].get(), dpd_FS_BRA_Bracket[4].get(), dpd_FS_BRA_Bracket[5].get()]
    }))

    lbl_FS_BRA_Title_Previous = config.ttk.Label(fs_brackets, text="Previous Bracket")
    lbl_FS_BRA_Title_Current = config.ttk.Label(fs_brackets, text="Current Bracket")
    lbl_FS_BRA_Title_Next = config.ttk.Label(fs_brackets, text="Next Bracket")

    lbl_FS_BRA_Bracket_Previous = []
    lbl_FS_BRA_Bracket_Current = []
    lbl_FS_BRA_Bracket_Next = []

    for i in range(5):
        lbl_FS_BRA_Bracket_Previous.append(config.ttk.Label(fs_brackets, text=""))
        lbl_FS_BRA_Bracket_Current.append(config.ttk.Label(fs_brackets, text=""))
        lbl_FS_BRA_Bracket_Next.append(config.ttk.Label(fs_brackets, text=""))

    btn_FS_BRA_GoBack = config.ttk.Button(fs_brackets, text="Go Back", state=config.tk.DISABLED, command=lambda:change_fs_bracket_state(-1, dpd_FS_BRA_Phase.get()))
    btn_FS_BRA_Next = config.ttk.Button(fs_brackets, text="Next", state=config.tk.DISABLED, command=lambda:change_fs_bracket_state(1, dpd_FS_BRA_Phase.get()))
    
    btn_FS_BRA_Show = config.ttk.Button(fs_brackets, text="Show", command=lambda:toggle_fs_bracket_display({
        #'brackets':[dpd_FS_BRA_Bracket[0].get(), dpd_FS_BRA_Bracket[1].get(), dpd_FS_BRA_Bracket[2].get()],
        'visibility':True,
        'all':True
    }))
    btn_FS_BRA_Hide = config.ttk.Button(fs_brackets, text="Hide", command=lambda:toggle_fs_bracket_display({
        #'brackets':[dpd_FS_BRA_Bracket[0].get(), dpd_FS_BRA_Bracket[1].get(), dpd_FS_BRA_Bracket[2].get()],
        'visibility':False,
        'all':True
    }))

    lbl_FS_gotoFS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
    btn_FS_gotoFS.grid(row=0, column=4, columnspan=2, padx=10, pady=10)

    btn_FS_BRA_Cycle_Brackets.grid(row = 8, column=0, columnspan=2, padx=10, pady=10)

    lbl_FS_BRA_Phase.grid(row=2, column=2, padx=10, pady=10)
    dpd_FS_BRA_Phase.grid(row=2, column=3, columnspan=2, padx=10, pady=10)

    for i in range(6):
        if i < 3:
            lbl_FS_BRA_Bracket[i].grid(row=8, column=2+(3*i), padx=10, pady=10)
            dpd_FS_BRA_Bracket[i].grid(row=8, column=3+(3*i), columnspan=2, padx=10, pady=10)
        else:
            lbl_FS_BRA_Bracket[i].grid(row=9, column=2+(3*(i-3)), padx=10, pady=10)
            dpd_FS_BRA_Bracket[i].grid(row=9, column=3+(3*(i-3)), columnspan=2, padx=10, pady=10)

    btn_FS_BRA_Display_Bracket.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

    lbl_FS_BRA_Title_Previous.grid(row=2, column=5, columnspan=2, padx=5, pady=5)
    lbl_FS_BRA_Title_Current.grid(row=2, column=7, columnspan=2, padx=5, pady=5)
    lbl_FS_BRA_Title_Next.grid(row=2, column=9, columnspan=2, padx=5, pady=5)

    for i in range(5):
        lbl_FS_BRA_Bracket_Previous[i].grid(row=3+i, column=5, columnspan=2, padx=5, pady=5)
        lbl_FS_BRA_Bracket_Current[i].grid(row=3+i, column=7, columnspan=2, padx=5, pady=5)
        lbl_FS_BRA_Bracket_Next[i].grid(row=3+i, column=9, columnspan=2, padx=5, pady=5)

    btn_FS_BRA_GoBack.grid(row=11, column=6, columnspan=2, padx=10, pady=10)
    btn_FS_BRA_Next.grid(row=11, column=8, columnspan=2, padx=10, pady=10)
    btn_FS_BRA_Hide.grid(row=12, column=6, columnspan=2, padx=10, pady=10)
    btn_FS_BRA_Show.grid(row=12, column=8, columnspan=2, padx=10, pady=10)

    #Full Screen - Matches

    lbl_FS_gotoSS = config.ttk.Label(fs_matchups, text="Go Full Screen:")
    btn_FS_gotoSS = config.ttk.Button(fs_matchups, text="Full Screen", command=lambda:change_scene(7))

    lbl_FS_MAT_PhaseSelect = config.ttk.Label(fs_matchups, text="Phase")
    dpd_FS_MAT_PhaseSelect = config.ttk.Combobox(fs_matchups, values=config.GUI_PHASES)
    dpd_FS_MAT_PhaseSelect.bind("<<ComboboxSelected>>", fs_matches_select_phases_update_combobox)
    
    lbl_FS_MAT_BracketinRound = config.ttk.Label(fs_matchups, text="All Matches in Bracket per Round")
    lbl_FS_MAT_BracketinRound_Bracket = config.ttk.Label(fs_matchups, text="Bracket: ")
    lbl_FS_MAT_BracketinRound_Round = config.ttk.Label(fs_matchups, text="Round: ")
    dpd_FS_MAT_BracketinRound_Bracket = config.ttk.Combobox(fs_matchups, values=[])
    dpd_FS_MAT_BracketinRound_Round = config.ttk.Combobox(fs_matchups, values=[])
    btn_FS_MAT_ShowMatches = config.ttk.Button(
        fs_matchups, text="Show Matches",
        command=lambda:display_fs_matches_allMatchesPerBracketRound(
            dpd_FS_MAT_BracketinRound_Bracket.get(),dpd_FS_MAT_BracketinRound_Round.get()))

    lbl_FS_MAT_IndividualMatches = config.ttk.Label(fs_matchups, text="Individual Matches")
    lbl_FS_MAT_IndividualMatches_Header = []
    lbl_FS_MAT_IndividualMatches_Bracket = []
    lbl_FS_MAT_IndividualMatches_Round = []
    lbl_FS_MAT_IndividualMatches_Matchup = []
    dpd_FS_MAT_IndividualMatches_Bracket = []
    dpd_FS_MAT_IndividualMatches_Round = []
    dpd_FS_MAT_IndividualMatches_Matchup = []
    btn_FS_MAT_IndividualMatches_Post = []

    for i in range(4):
        lbl_FS_MAT_IndividualMatches_Header.append(config.ttk.Label(fs_matchups, text="Matchup " + str(i+1)))
        lbl_FS_MAT_IndividualMatches_Bracket.append(config.ttk.Label(fs_matchups, text="Bracket: "))
        lbl_FS_MAT_IndividualMatches_Round.append(config.ttk.Label(fs_matchups, text="Round: "))
        lbl_FS_MAT_IndividualMatches_Matchup.append(config.ttk.Label(fs_matchups, text="Matchup: "))
        dpd_FS_MAT_IndividualMatches_Bracket.append(config.ttk.Combobox(fs_matchups, values=[]))
        dpd_FS_MAT_IndividualMatches_Round.append(config.ttk.Combobox(fs_matchups, values=[]))
        dpd_FS_MAT_IndividualMatches_Matchup.append(config.ttk.Combobox(fs_matchups, values=[]))
        

        dpd_FS_MAT_IndividualMatches_Bracket[i].bind(
            "<<ComboboxSelected>>", config.partial(fs_matches_select_bracket_update_combobox, i))
        dpd_FS_MAT_IndividualMatches_Round[i].bind(
            "<<ComboboxSelected>>", config.partial(fs_matches_select_round_update_combobox, i))
        
    btn_FS_MAT_IndividualMatches_Post.append(config.ttk.Button(fs_matchups, text="Display Match (1)",
                                             command=lambda:display_fs_matches(0)))
    btn_FS_MAT_IndividualMatches_Post.append(config.ttk.Button(fs_matchups, text="Display Match (2)",
                                             command=lambda:display_fs_matches(1)))
    btn_FS_MAT_IndividualMatches_Post.append(config.ttk.Button(fs_matchups, text="Display Match (3)",
                                             command=lambda:display_fs_matches(2)))
    btn_FS_MAT_IndividualMatches_Post.append(config.ttk.Button(fs_matchups, text="Display Match (4)",
                                             command=lambda:display_fs_matches(3)))
    

    btn_FS_MAT_Show = config.ttk.Button(fs_matchups, text="Show", command=lambda:toggle_fs_matches_display({
        'visibility':True
    }))
    btn_FS_MAT_Hide = config.ttk.Button(fs_matchups, text="Hide", command=lambda:toggle_fs_matches_display({
        'visibility':False
    }))

    lbl_FS_gotoSS.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_FS_gotoSS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lbl_FS_MAT_PhaseSelect.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
    dpd_FS_MAT_PhaseSelect.grid(row=2, column=4, columnspan=2, padx=10, pady=10)

    lbl_FS_MAT_BracketinRound.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    lbl_FS_MAT_BracketinRound_Bracket.grid(row=4, column=2, padx=10, pady=10)
    lbl_FS_MAT_BracketinRound_Round.grid(row=5, column=2, padx=10, pady=10)
    dpd_FS_MAT_BracketinRound_Bracket.grid(row=4, column=3, padx=10, pady=10)
    dpd_FS_MAT_BracketinRound_Round.grid(row=5, column=3, padx=10, pady=10)
    btn_FS_MAT_ShowMatches.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

    lbl_FS_MAT_IndividualMatches.grid(row=3, column=6, columnspan=8, padx=10, pady=10)

    for i in range(4):
        lbl_FS_MAT_IndividualMatches_Header[i].grid(row=4, column=4+(2*i), columnspan=2, padx=5, pady=5)
        lbl_FS_MAT_IndividualMatches_Bracket[i].grid(row=5, column=4+(2*i), padx=5, pady=5)
        lbl_FS_MAT_IndividualMatches_Round[i].grid(row=6, column=4+(2*i), padx=5, pady=5)
        lbl_FS_MAT_IndividualMatches_Matchup[i].grid(row=7, column=4+(2*i), padx=5, pady=5)
        dpd_FS_MAT_IndividualMatches_Bracket[i].grid(row=5, column=5+(2*i), padx=5, pady=5)
        dpd_FS_MAT_IndividualMatches_Round[i].grid(row=6, column=5+(2*i), padx=5, pady=5)
        dpd_FS_MAT_IndividualMatches_Matchup[i].grid(row=7, column=5+(2*i), padx=5, pady=5)
        btn_FS_MAT_IndividualMatches_Post[i].grid(row=8, column=4+(2*i), columnspan=2, padx=5, pady=5)
        
    btn_FS_MAT_Hide.grid(row=10, column=2, columnspan=2, padx=10, pady=10)
    btn_FS_MAT_Show.grid(row=10, column=4, columnspan=2, padx=10, pady=10)

    #Full Screen - Results

    lbl_FS_gotoFS = config.ttk.Label(fs_results, text="Full Screen:")
    btn_FS_gotoFS = config.ttk.Button(fs_results, text="Full Screen", command=lambda:change_scene(7))

    lbl_FS_RES_PhaseSelect = config.ttk.Label(fs_results, text="Phase")
    dpd_FS_RES_PhaseSelect = config.ttk.Combobox(fs_results, values=config.GUI_PHASES)
    dpd_FS_RES_PhaseSelect.bind("<<ComboboxSelected>>", fs_results_select_phases_update_combobox)
    
    lbl_FS_RES_BracketinRound = config.ttk.Label(fs_results, text="All Results in Bracket per Round")
    lbl_FS_RES_BracketinRound_Bracket = config.ttk.Label(fs_results, text="Bracket: ")
    lbl_FS_RES_BracketinRound_Round = config.ttk.Label(fs_results, text="Round: ")
    dpd_FS_RES_BracketinRound_Bracket = config.ttk.Combobox(fs_results, values=[])
    dpd_FS_RES_BracketinRound_Round = config.ttk.Combobox(fs_results, values=[])
    btn_FS_RES_ShowMatches = config.ttk.Button(
        fs_results, text="Show Results",
        command=lambda:display_fs_results_allResultsPerBracketRound(
            dpd_FS_RES_BracketinRound_Bracket.get(),dpd_FS_RES_BracketinRound_Round.get()))

    lbl_FS_RES_IndividualMatches = config.ttk.Label(ss_results, text="Individual Results")
    lbl_FS_RES_IndividualMatches_Header = []
    lbl_FS_RES_IndividualMatches_Bracket = []
    lbl_FS_RES_IndividualMatches_Round = []
    lbl_FS_RES_IndividualMatches_Matchup = []
    dpd_FS_RES_IndividualMatches_Bracket = []
    dpd_FS_RES_IndividualMatches_Round = []
    dpd_FS_RES_IndividualMatches_Matchup = []
    btn_FS_RES_IndividualMatches_Post = []

    for i in range(4):
        lbl_FS_RES_IndividualMatches_Header.append(config.ttk.Label(fs_results, text="Result " + str(i+1)))
        lbl_FS_RES_IndividualMatches_Bracket.append(config.ttk.Label(fs_results, text="Bracket: "))
        lbl_FS_RES_IndividualMatches_Round.append(config.ttk.Label(fs_results, text="Round: "))
        lbl_FS_RES_IndividualMatches_Matchup.append(config.ttk.Label(fs_results, text="Matchup: "))
        dpd_FS_RES_IndividualMatches_Bracket.append(config.ttk.Combobox(fs_results, values=[]))
        dpd_FS_RES_IndividualMatches_Round.append(config.ttk.Combobox(fs_results, values=[]))
        dpd_FS_RES_IndividualMatches_Matchup.append(config.ttk.Combobox(fs_results, values=[]))
        

        dpd_FS_RES_IndividualMatches_Bracket[i].bind(
            "<<ComboboxSelected>>", config.partial(fs_results_select_bracket_update_combobox, i))
        dpd_FS_RES_IndividualMatches_Round[i].bind(
            "<<ComboboxSelected>>", config.partial(fs_results_select_round_update_combobox, i))
        
    btn_FS_RES_IndividualMatches_Post.append(config.ttk.Button(fs_results, text="Display Result (1)",
                                             command=lambda:display_fs_results(0)))
    btn_FS_RES_IndividualMatches_Post.append(config.ttk.Button(fs_results, text="Display Result (2)",
                                             command=lambda:display_fs_results(1)))
    btn_FS_RES_IndividualMatches_Post.append(config.ttk.Button(fs_results, text="Display Result (3)",
                                             command=lambda:display_fs_results(2)))
    btn_FS_RES_IndividualMatches_Post.append(config.ttk.Button(fs_results, text="Display Result (4)",
                                             command=lambda:display_fs_results(3)))
    

    btn_FS_RES_Show = config.ttk.Button(fs_results, text="Show", command=lambda:toggle_fs_results_display({
        'visibility':True
    }))
    btn_FS_RES_Hide = config.ttk.Button(fs_results, text="Hide", command=lambda:toggle_fs_results_display({
        'visibility':False
    }))

    lbl_FS_gotoSS.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_FS_gotoSS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lbl_FS_RES_PhaseSelect.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
    dpd_FS_RES_PhaseSelect.grid(row=2, column=4, columnspan=2, padx=10, pady=10)

    lbl_FS_RES_BracketinRound.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    lbl_FS_RES_BracketinRound_Bracket.grid(row=4, column=2, padx=10, pady=10)
    lbl_FS_RES_BracketinRound_Round.grid(row=5, column=2, padx=10, pady=10)
    dpd_FS_RES_BracketinRound_Bracket.grid(row=4, column=3, padx=10, pady=10)
    dpd_FS_RES_BracketinRound_Round.grid(row=5, column=3, padx=10, pady=10)
    btn_FS_RES_ShowMatches.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

    lbl_FS_RES_IndividualMatches.grid(row=3, column=6, columnspan=8, padx=10, pady=10)

    for i in range(4):
        lbl_FS_RES_IndividualMatches_Header[i].grid(row=4, column=4+(2*i), columnspan=2, padx=5, pady=5)
        lbl_FS_RES_IndividualMatches_Bracket[i].grid(row=5, column=4+(2*i), padx=5, pady=5)
        lbl_FS_RES_IndividualMatches_Round[i].grid(row=6, column=4+(2*i), padx=5, pady=5)
        lbl_FS_RES_IndividualMatches_Matchup[i].grid(row=7, column=4+(2*i), padx=5, pady=5)
        dpd_FS_RES_IndividualMatches_Bracket[i].grid(row=5, column=5+(2*i), padx=5, pady=5)
        dpd_FS_RES_IndividualMatches_Round[i].grid(row=6, column=5+(2*i), padx=5, pady=5)
        dpd_FS_RES_IndividualMatches_Matchup[i].grid(row=7, column=5+(2*i), padx=5, pady=5)
        btn_FS_RES_IndividualMatches_Post[i].grid(row=8, column=4+(2*i), columnspan=2, padx=5, pady=5)
        
    btn_FS_RES_Hide.grid(row=10, column=2, columnspan=2, padx=10, pady=10)
    btn_FS_RES_Show.grid(row=10, column=4, columnspan=2, padx=10, pady=10)

    #Full Screen - Standings

    lbl_FS_gotoFS = config.ttk.Label(fs_standings, text="Full Screen:")
    btn_FS_gotoFS = config.ttk.Button(fs_standings, text="Full Screen", command=lambda:change_scene(7))

    lbl_FS_STA_PhaseSelect = config.ttk.Label(fs_standings, text="Phase")
    dpd_FS_STA_PhaseSelect = config.ttk.Combobox(fs_standings, values=config.GUI_PHASES)
    lbl_FS_STA_BracketSelect = config.ttk.Label(fs_standings, text="Bracket: ")
    dpd_FS_STA_BracketSelect = config.ttk.Combobox(fs_standings, values=[])

    dpd_FS_STA_PhaseSelect.bind("<<ComboboxSelected>>", fs_standings_select_phases_update_combobox)

    btn_FS_STA_ApplyStandings = config.ttk.Button(fs_standings, text="Apply", command=lambda:fs_standings_changeStandings())
    btn_FS_STA_Show = config.ttk.Button(fs_standings, text="Show", command=lambda:toggle_fs_standings_display({
        'visibility':True
    }))
    btn_FS_STA_Hide = config.ttk.Button(fs_standings, text="Hide", command=lambda:toggle_fs_standings_display({
        'visibility':False
    }))

    lbl_FS_gotoFS.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_FS_gotoFS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lbl_FS_STA_PhaseSelect.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
    dpd_FS_STA_PhaseSelect.grid(row=2, column=4, columnspan=2, padx=10, pady=10)
    lbl_FS_STA_BracketSelect.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    dpd_FS_STA_BracketSelect.grid(row=3, column=4, columnspan=2, padx=10, pady=10)

    btn_FS_STA_ApplyStandings.grid(row=4, column=2, columnspan=4, padx=10, pady=10)
    btn_FS_STA_Hide.grid(row=6, column=2, columnspan=2, padx=10, pady=10)
    btn_FS_STA_Show.grid(row=6, column=4, columnspan=2, padx=10, pady=10)

    #API Screen

    lbl_API_api_name = []
    lbl_API_api_status = []
    btn_API_checkPing = []

    lbl_API_api_name.append(config.ttk.Label(api_general, text="Cornerstone"))
    lbl_API_api_name.append(config.ttk.Label(api_general, text="OBS Websocket"))
    lbl_API_api_name.append(config.ttk.Label(api_general, text="PBDS"))
    lbl_API_api_name.append(config.ttk.Label(api_general, text="Spotify"))
    lbl_API_api_name.append(config.ttk.Label(api_general, text="TMS"))

    lbl_API_api_status.append(config.ttk.Label(api_general, text="Not Tested"))
    lbl_API_api_status.append(config.ttk.Label(api_general, text="Not Tested"))
    lbl_API_api_status.append(config.ttk.Label(api_general, text="Not Tested"))
    lbl_API_api_status.append(config.ttk.Label(api_general, text="Not Tested"))
    lbl_API_api_status.append(config.ttk.Label(api_general, text="Not Tested"))

    btn_API_checkPing.append(config.ttk.Button(api_general, text="Check Cornerstone Ping", command=lambda:test_ping(0)))
    btn_API_checkPing.append(config.ttk.Button(api_general, text="Check OBS Websocket Ping", command=lambda:test_ping(1)))
    btn_API_checkPing.append(config.ttk.Button(api_general, text="Check PBDS Ping", command=lambda:test_ping(2)))
    btn_API_checkPing.append(config.ttk.Button(api_general, text="Check Spotify Ping", command=lambda:test_ping(3)))
    btn_API_checkPing.append(config.ttk.Button(api_general, text="Check TMS Ping", command=lambda:test_ping(4)))

    for i in range(5):
        lbl_API_api_status[i].grid(row = i, column = 0, columnspan = 2, padx=10, pady=10)
        btn_API_checkPing[i].grid(row = i, column = 2, columnspan = 2, padx=10, pady=10)
        lbl_API_api_name[i].grid(row = i, column = 4, columnspan = 2, padx=10, pady=10)

    ###CORNERSTONE###

    phases = ["Prelims", "Playoffs", "Superplayoffs"]

    lbl_API_CRN_Title = config.ttk.Label(api_cornerstone, text="Cornerstone API Management")
    lbl_API_CRN_Headers = []

    lbl_API_CRN_PhaseName = []
    lbl_API_CRN_TeamsBracketed = []
    btn_API_CRN_CheckTeamsBracketed = []
    btn_API_CRN_GetData = []
    lbl_API_CRN_isDone = []

    for phase in phases:
        lbl_API_CRN_PhaseName.append(config.ttk.Label(api_cornerstone, text=phase))
        lbl_API_CRN_TeamsBracketed.append(config.ttk.Label(api_cornerstone, text="0"))
        lbl_API_CRN_isDone.append(config.ttk.Label(api_cornerstone, text="No"))

    lbl_API_CRN_Headers.append(config.ttk.Label(api_cornerstone, text="Phase"))
    lbl_API_CRN_Headers.append(config.ttk.Label(api_cornerstone, text="# Teams not bracketed"))
    lbl_API_CRN_Headers.append(config.ttk.Label(api_cornerstone, text="Check # Teams not bracketed"))
    lbl_API_CRN_Headers.append(config.ttk.Label(api_cornerstone, text="Get Bracket/Matchup Data"))
    lbl_API_CRN_Headers.append(config.ttk.Label(api_cornerstone, text="Data Retrieved?"))

    btn_API_CRN_CheckTeamsBracketed.append(config.ttk.Button(api_cornerstone, text="Check Teams", command=lambda:checkTeamsBracketed()))
    btn_API_CRN_GetData.append(config.ttk.Button(api_cornerstone, text="Get Data", command=lambda:getCornerstoneData("Prelims")))

    btn_API_CRN_CheckTeamsBracketed.append(config.ttk.Button(api_cornerstone, text="Check Teams", command=lambda:checkTeamsBracketed()))
    btn_API_CRN_GetData.append(config.ttk.Button(api_cornerstone, text="Get Data", command=lambda:getCornerstoneData("Playoffs")))

    btn_API_CRN_CheckTeamsBracketed.append(config.ttk.Button(api_cornerstone, text="Check Teams", command=lambda:checkTeamsBracketed()))
    btn_API_CRN_GetData.append(config.ttk.Button(api_cornerstone, text="Get Data", command=lambda:getCornerstoneData("Superplayoffs")))

    lbl_API_CRN_Title.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
    for i in range(5):
        lbl_API_CRN_Headers[i].grid(row=1, column=i, padx=10, pady=10)


    for i in range(3):
        lbl_API_CRN_PhaseName[i].grid(row=i+2, column=0, padx=10, pady=10)
        lbl_API_CRN_TeamsBracketed[i].grid(row=i+2, column=1, padx=10, pady=10)
        btn_API_CRN_CheckTeamsBracketed[i].grid(row=i+2, column=2, padx=10, pady=10)
        btn_API_CRN_GetData[i].grid(row=i+2, column=3, padx=10, pady=10)
        lbl_API_CRN_isDone[i].grid(row=i+2, column=4, padx=10, pady=10)



    ### ANNOUNCEMENTS ###

    lbl_FS_gotoFS = config.ttk.Label(announcement_tab, text="Full Screen:")
    btn_FS_gotoFS = config.ttk.Button(announcement_tab, text="Full Screen", command=lambda:change_scene(7))

    lbl_ANN_Announcements = config.ttk.Label(announcement_tab, text="Announce:")
    txt_ANN_Announcement = config.tk.Text(announcement_tab, wrap="word")
    btn_ANN_Announce = config.ttk.Button(announcement_tab, text="Make Announcement", command=lambda:make_announcement())

    btn_ANN_Hide = config.ttk.Button(announcement_tab, text="Hide", command=lambda:toggle_announcement_display(False))
    btn_ANN_Show = config.ttk.Button(announcement_tab, text="Show", command=lambda:toggle_announcement_display(True))

    lbl_FS_gotoFS.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_FS_gotoFS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lbl_ANN_Announcements.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
    txt_ANN_Announcement.grid(row=3, column=0, columnspan=4, rowspan=3, padx=10, pady=10)
    btn_ANN_Announce.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

    btn_ANN_Hide.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    btn_ANN_Show.grid(row=7, column=2, columnspan=2, padx=10, pady=10)

    ###TIMER###

    lbl_TIM_gotoWAIT = config.ttk.Label(timer_tab, text="Waiting Area:")
    btn_TIM_gotoWAIT = config.ttk.Button(timer_tab, text="Waiting Area", command=lambda:change_scene(8))

    radvar_TIM_Type = config.tk.StringVar()
    lbl_TIM_PickType = config.ttk.Label(timer_tab, text="Pick Timer Type")
    rad_TIM_Countdown = config.ttk.Radiobutton(timer_tab, text="Countdown", variable=radvar_TIM_Type, value="Countdown")
    rad_TIM_SpecificTime = config.ttk.Radiobutton(timer_tab, text="Specific Time", variable=radvar_TIM_Type, value="Specific Time")

    lbl_TIM_Choose_ST = config.ttk.Label(timer_tab, text="Choose Specific Time: ")
    txt_TIM_Choose_ST = config.ttk.Entry(timer_tab)
    lbl_TIM_Choose_ST_post = config.ttk.Label(timer_tab, text=" CDT")
    btn_TIM_Update_ST = config.ttk.Button(timer_tab, text="Update Specific Time", command=lambda:update_specificTime())

    btn_TIM_Show = config.ttk.Button(timer_tab, text="Show", command=lambda:toggle_timer_display(True))
    btn_TIM_Hide = config.ttk.Button(timer_tab, text="Hide", command=lambda:toggle_timer_display(False))

    lbl_TIM_gotoWAIT.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_TIM_gotoWAIT.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lbl_TIM_PickType.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    rad_TIM_Countdown.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    rad_TIM_SpecificTime.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    lbl_TIM_Choose_ST.grid(row=2, column=4, padx=10, pady=10)
    txt_TIM_Choose_ST.grid(row=2, column=5, padx=10, pady=10)
    lbl_TIM_Choose_ST_post.grid(row=2, column=6, padx=10, pady=10)
    btn_TIM_Update_ST.grid(row=2, column=7, padx=10, pady=10)

    btn_TIM_Hide.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    btn_TIM_Show.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

    #Questions Tab

    lbl_FS_gotoFS = config.ttk.Label(fs_questions, text="Full Screen:")
    btn_FS_gotoFS = config.ttk.Button(fs_questions, text="Full Screen", command=lambda:change_scene(7))

    lbl_FS_Q_Round = config.ttk.Label(fs_questions, text="Round: ")
    dpd_FS_Q_Round = config.ttk.Combobox(fs_questions, values=[])

    question_list = []
    for i in range(22):
        question_list.append(i)

    lbl_FS_Q_Question = config.ttk.Label(fs_questions, text="Question: ")
    dpd_FS_Q_Question = config.ttk.Combobox(fs_questions, values=question_list)

    lbl_FS_Q_TU_Bonus = config.ttk.Label(fs_questions, text="Tossup/Bonus?: ")
    dpd_FS_Q_TU_Bonus = config.ttk.Combobox(fs_questions, values=["Tossup", "Bonus"])

    btn_FS_Q_Update = config.ttk.Button(fs_questions, text="Update", command=lambda:update_Question_rounds())
    btn_FS_Q_Apply = config.ttk.Button(fs_questions, text="Apply", command=lambda:apply_question())
    btn_FS_Q_Hide = config.ttk.Button(fs_questions, text="Hide", command=lambda:toggle_question_display(-1))
    btn_FS_Q_Show = config.ttk.Button(fs_questions, text="Show", command=lambda:toggle_question_display(1))

    lbl_FS_gotoFS.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    btn_FS_gotoFS.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lbl_FS_Q_Round.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    dpd_FS_Q_Round.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

    lbl_FS_Q_Question.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    dpd_FS_Q_Question.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

    lbl_FS_Q_TU_Bonus.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    dpd_FS_Q_TU_Bonus.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

    btn_FS_Q_Update.grid(row=3, column=4, columnspan=2, padx=10, pady=10)
    btn_FS_Q_Apply.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    btn_FS_Q_Hide.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    btn_FS_Q_Show.grid(row=7, column=2, columnspan=2, padx=10, pady=10)

    '''    
    lbl_changePhase_SW = config.tk.Label(root, text="Change SW Phase")
    lbl_changePhase_SW.grid(row=9, column=0, columnspan=6, padx=10, pady=10)

    lbl_changePhase_before = config.tk.Label(root, text="")
    lbl_changePhase_before.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    lbl_changePhase_current = config.tk.Label(root, text="Before Prelims")
    lbl_changePhase_current.grid(row=10, column=3, columnspan=2, padx=10, pady=10)

    lbl_changePhase_after = config.tk.Label(root, text="Prelims")
    lbl_changePhase_after.grid(row=10, column=5, columnspan=2, padx=10, pady=10)

    btn_prevPhase = config.tk.Button(root, text="Previous Phase", command=lambda:change_phase(0))
    btn_prevPhase.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

    btn_nextPhase = config.tk.Button(root, text="Next Phase", command=lambda:change_phase(1))
    btn_nextPhase.grid(row=11, column=3, columnspan=3, padx=10, pady=10)

    #btn_changePhase = config.tk.Button(root, text"Change Phase")
    '''

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    config.init()
    init_gui()