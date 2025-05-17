import config
import obs
import data

#Full Screen Stats

def hide_all_overlays():
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_4TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_2_4TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_3_4TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_4_4TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_5_4TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_6_4TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_5TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_2_5TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_3_5TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_6TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_2_6TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_3_6TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_7TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_2_7TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_3_7TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_1_8TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_2_8TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_BRACKETS_3_8TEAMS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_INDIVIDUAL, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_RESULTS_1, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_RESULTS_2, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_RESULTS_3, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_RESULTS_4, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_MATCHUPS_1, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_MATCHUPS_2, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_MATCHUPS_3, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_MATCHUPS_4, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_4, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_5, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_6, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_7, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.STANDINGS_8, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_ANNOUNCEMENTS, False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_PLAYOFF_TEAMS, False)

#BEGIN BRACKET#

def toggle_brackets_visibility(toggle):

    obs.toggle_source_visibility(config.FSS_BRACKETS_1_4TEAMS, "Bracket 1 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_1_4TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_4TEAMS, "Bracket 1 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_4TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_4TEAMS, "Bracket 2 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_4TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_4TEAMS, "Bracket 1 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_4TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_4TEAMS, "Bracket 2 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_4TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_4TEAMS, "Bracket 3 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_4TEAMS, "FS - Brackets - Bracket 3 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_4_4TEAMS, "Bracket 1 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_4_4TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_4_4TEAMS, "Bracket 2 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_4_4TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_4_4TEAMS, "Bracket 3 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_4_4TEAMS, "FS - Brackets - Bracket 3 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_4_4TEAMS, "Bracket 4 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_4_4TEAMS, "FS - Brackets - Bracket 4 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "Bracket 1 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "Bracket 2 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "Bracket 3 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "FS - Brackets - Bracket 3 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "Bracket 4 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "FS - Brackets - Bracket 4 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "Bracket 5 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_5_4TEAMS, "FS - Brackets - Bracket 5 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "Bracket 1 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "Bracket 2 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "Bracket 3 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "FS - Brackets - Bracket 3 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "Bracket 4 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "FS - Brackets - Bracket 4 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "Bracket 5 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "FS - Brackets - Bracket 5 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "Bracket 6 - 4 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_6_4TEAMS, "FS - Brackets - Bracket 6 - Title", toggle)

    obs.toggle_source_visibility(config.FSS_BRACKETS_1_5TEAMS, "Bracket 1 - 5 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_1_5TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_5TEAMS, "Bracket 1 - 5 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_5TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_5TEAMS, "Bracket 2 - 5 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_5TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_5TEAMS, "Bracket 1 - 5 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_5TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_5TEAMS, "Bracket 2 - 5 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_5TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_5TEAMS, "Bracket 3 - 5 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_5TEAMS, "FS - Brackets - Bracket 3 - Title", toggle)

    obs.toggle_source_visibility(config.FSS_BRACKETS_1_6TEAMS, "Bracket 1 - 6 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_1_6TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_6TEAMS, "Bracket 1 - 6 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_6TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_6TEAMS, "Bracket 2 - 6 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_6TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_6TEAMS, "Bracket 1 - 6 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_6TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_6TEAMS, "Bracket 2 - 6 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_6TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_6TEAMS, "Bracket 3 - 6 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_6TEAMS, "FS - Brackets - Bracket 3 - Title", toggle)

    obs.toggle_source_visibility(config.FSS_BRACKETS_1_7TEAMS, "Bracket 1 - 7 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_1_7TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_7TEAMS, "Bracket 1 - 7 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_7TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_7TEAMS, "Bracket 2 - 7 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_7TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_7TEAMS, "Bracket 1 - 7 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_7TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_7TEAMS, "Bracket 2 - 7 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_7TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_7TEAMS, "Bracket 3 - 7 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_7TEAMS, "FS - Brackets - Bracket 3 - Title", toggle)

    obs.toggle_source_visibility(config.FSS_BRACKETS_1_8TEAMS, "Bracket 1 - 8 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_1_8TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_8TEAMS, "Bracket 1 - 8 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_8TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_8TEAMS, "Bracket 2 - 8 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_2_8TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_8TEAMS, "Bracket 1 - 8 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_8TEAMS, "FS - Brackets - Bracket 1 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_8TEAMS, "Bracket 2 - 8 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_8TEAMS, "FS - Brackets - Bracket 2 - Title", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_8TEAMS, "Bracket 3 - 8 Teams", toggle)
    obs.toggle_source_visibility(config.FSS_BRACKETS_3_8TEAMS, "FS - Brackets - Bracket 3 - Title", toggle)

def show_ind_bracket(brackets, toggle_all, input_num_brackets=6, input_num_teams=6):

    global current_num_brackets
    global current_num_teams

    obs.set_scene(config.FULL_SCREEN_STATS)
    
    try:
        current_num_brackets
    except NameError:
        current_num_brackets = input_num_brackets

    try:
        current_num_teams
    except NameError:
        current_num_teams = input_num_teams

    bracketcount = 1
    fss_scene = config.FSS_BRACKETS_3_8TEAMS

    num_brackets = len(brackets)

    if num_brackets <=6:
        for bracket in brackets:
            teams = bracket['teams']

            if(len(teams) == 6):
                if num_brackets == 1:
                    fss_scene = config.FSS_BRACKETS_1_6TEAMS
                elif num_brackets == 2:
                    fss_scene = config.FSS_BRACKETS_2_6TEAMS
                else:
                    fss_scene = config.FSS_BRACKETS_3_6TEAMS
            elif(len(teams) == 8):
                if num_brackets == 1:
                    fss_scene = config.FSS_BRACKETS_1_8TEAMS
                elif num_brackets == 2:
                    fss_scene = config.FSS_BRACKETS_2_8TEAMS
                else:
                    fss_scene = config.FSS_BRACKETS_3_8TEAMS
            elif(len(teams) == 7):
                if num_brackets == 1:
                    fss_scene = config.FSS_BRACKETS_1_7TEAMS
                elif num_brackets == 2:
                    fss_scene = config.FSS_BRACKETS_2_7TEAMS
                else:
                    fss_scene = config.FSS_BRACKETS_3_7TEAMS
            elif(len(teams) == 5):
                if num_brackets == 1:
                    fss_scene = config.FSS_BRACKETS_1_5TEAMS
                elif num_brackets == 2:
                    fss_scene = config.FSS_BRACKETS_2_5TEAMS
                else:
                    fss_scene = config.FSS_BRACKETS_3_5TEAMS
            else:
                if num_brackets == 1:
                    fss_scene = config.FSS_BRACKETS_1_4TEAMS
                elif num_brackets == 2:
                    fss_scene = config.FSS_BRACKETS_2_4TEAMS
                elif num_brackets == 3:
                    fss_scene = config.FSS_BRACKETS_3_4TEAMS
                elif num_brackets == 4:
                    fss_scene = config.FSS_BRACKETS_4_4TEAMS
                elif num_brackets == 5:
                    fss_scene = config.FSS_BRACKETS_5_4TEAMS
                else:
                    fss_scene = config.FSS_BRACKETS_6_4TEAMS

            if (len(teams) != current_num_teams) or (num_brackets != current_num_brackets):
                hide_all_overlays()
                config.time.sleep(config.SLEEP_TIME)
                current_num_brackets = num_brackets
                current_num_teams = len(teams)
               
            toggle_brackets_visibility(False)
            obs.toggle_source_visibility(config.FULL_SCREEN_STATS, fss_scene, True)
            teamcount = 1

            path = "./Text Files/Big Screen/Brackets/Bracket " +str(bracketcount) +"/"
            with open(path + "Bracket " +str(bracketcount) +" Name.txt", 'w') as src:
                src.write(bracket['bracket'])
            

            for team in teams:
                with open(path + "Team " +str(teamcount) +" Name.txt", 'w') as src:
                    src.write(team['team'])
                with open(path + "Team " +str(teamcount) +" City.txt", 'w') as src:
                    src.write(team['city'])
                
                teamcount+=1
            
            teamcount = 1
            bracketcount += 1
        
        config.time.sleep(config.SLEEP_TIME)
        toggle_brackets_visibility(True)
        bracketcount = 1

def loop_brackets(phase):
    
    global current_num_brackets
    global current_num_teams

    current_num_brackets = 0
    current_num_teams = 0

    scene_title = "./Text Files/Big Screen/Title.txt"

    obs.set_scene(config.FULL_SCREEN_STATS)
    config.time.sleep(config.SLEEP_TIME)
    hide_all_overlays()

    if phase == "Prelims":
        with open(scene_title, 'w') as file:
            file.write("Preliminary Brackets")
    elif phase == "Playoffs":
        with open(scene_title, 'w') as file:
            file.write("Playoff Brackets")
    elif phase == "Superplayoffs":
        with open(scene_title, 'w') as file:
            file.write("Superplayoff Brackets")
    else:
        with open(scene_title, 'w') as file:
            file.write("Finals")

    brackets = data.get_brackets_with_teams(phase)
    bracketcount = 1
    active_brackets = []
    total_count = 1

    for bracket in brackets:
       
        team_len = len(bracket['teams'])
        active_brackets.append(bracket)

        if (bracketcount == 3 and team_len != 4) or (bracketcount == 2 and total_count == 14 and team_len != 4) or (bracketcount == 5 and team_len == 4):
            show_ind_bracket(active_brackets, False, current_num_brackets, current_num_teams)
            config.time.sleep(config.SHOW_TIME * 3)
            toggle_brackets_visibility(False)
            bracketcount = 1
            config.time.sleep(config.SLEEP_TIME)
            active_brackets.clear()
        else:
            bracketcount+=1
        total_count+=1

    hide_all_overlays()
    config.time.sleep(config.SLEEP_TIME)

#END BRACKET#
#BEGIN INDIVIDUAL#

def toggle_ind_visibility(toggle):
    for indNum in range(1,11):
        obs.toggle_source_visibility(config.FSS_INDIVIDUAL, "FS - Individual - P" +str(indNum) +" - Rank - Text", toggle)
        obs.toggle_source_visibility(config.FSS_INDIVIDUAL, "FS - Individual - P" +str(indNum) +" - PPG - Text", toggle)
        obs.toggle_source_visibility(config.FSS_INDIVIDUAL, "FS - Individual - P" +str(indNum), toggle)

def show_individual_ranking(players):
    playercount = 1

    for player in players:
        path = "./Text Files/Big Screen/Individual Standings/Player " +str(playercount) +"/"

        rank_file= path + "Rank.txt"
        name_file= path + "Name.txt"
        grade_file= path + "Grade.txt"
        team_file= path + "Team.txt"
        city_file= path + "City.txt"
        stats_file= path + "Stats.txt"
        ppg_file= path + "PPG.txt"

        with open(rank_file, 'w') as file:
            file.write(str(player['rank']))
        with open(name_file, 'w') as file:
            file.write(str(player['name']))
        with open(grade_file, 'w') as file:
            if player['grade']==12:
                file.write("Senior")
            elif player['grade'] == 11:
                file.write("Junior")
            elif player['grade'] == 10:
                file.write("Sophomore")
            elif player['grade'] == 9:
                file.write("Freshman")
            else:
                file.write(str(player['grade']) +"th Grade")
        with open(team_file, 'w') as file:
            file.write(str(player['team']))
        with open(city_file, 'w') as file:
            file.write(str(player['city']))
        with open(stats_file, 'w') as file:
            file.write(str(player['powers']) +" powers (20's)\n" +str(player['tossups']) +" tossups (10's)\n" +str(player['tuh']) + " tossups heard")
        with open(ppg_file, 'w') as file:
            file.write(str(player['ppg']) + " PPG")

        playercount +=1
    
    config.time.sleep(config.SLEEP_TIME)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, config.FSS_INDIVIDUAL, True)

def loop_individual():
    scene_title = "./Text Files/Big Screen/Title.txt"

    obs.set_scene(config.FULL_SCREEN_STATS)
    hide_all_overlays()

    with open(scene_title, 'w') as file:
        file.write("Individual Standings")

    players = data.get_players()
    playercount = 1

    act_players = []

    for player in players:

        act_players.append(player)
    
        if playercount == 10 or player['ppg'] == 0:
            show_individual_ranking(act_players)
            toggle_ind_visibility(True)
            config.time.sleep(config.SHOW_TIME * 5)
            toggle_ind_visibility(False)

            if(player['ppg'] == 0):
                break
            playercount = 1
            act_players.clear()
        else:
            playercount+=1
            

    hide_all_overlays()
    config.time.sleep(config.SLEEP_TIME)

#END INDIVIDUAL#
#BEGIN RESULTS#

def loop_round_matches(round):
    scene_title = "./Text Files/Big Screen/Title.txt"

    obs.set_scene(config.FULL_SCREEN_STATS)
    hide_all_overlays()

    matchups = data.get_results(round)
    len_match = len(matchups)
    match_limit = 1
    scene_choice = ""

    if(round >= 11 and round <=16):
        match_limit = 4
        scene_choice = config.FSS_RESULTS_4
    elif(round <= 10 and isinstance(round, int)):
        match_limit = 3
        scene_choice = config.FSS_RESULTS_3
    elif(len_match % 4 == 0):
        match_limit = 4
        scene_choice = config.FSS_RESULTS_4
    elif(len_match % 3 == 0):
        match_limit = 3
        scene_choice = config.FSS_RESULTS_3
    elif (len_match % 2 == 0):
        match_limit = 2
        scene_choice = config.FSS_RESULTS_2
    else:
        scene_choice = config.FSS_RESULTS_1

    match_count = 1
    pp_array = []
    active_matches = []

    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, scene_choice, True)

    for matchup in matchups:

        active_matches.append(matchup)

        if match_count == match_limit:
            
            loop_ind_results(active_matches)
            active_matches.clear()

            j=1
            config.time.sleep(config.SHOW_TIME*match_limit)

            while j <= match_limit:
                obs.toggle_source_visibility(scene_choice, "FS - Results - Match " +str(j) + " - Text", False)
                obs.toggle_source_visibility(scene_choice, "FS - Results - Match " +str(j) + " - PP", False)

                j+=1 
            pp_array.clear()
            match_count = 1
        else:
            match_count+=1

    hide_all_overlays()

def loop_ind_results(results):
    scene_title = "./Text Files/Big Screen/Title.txt"

    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - 1 Match", False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - 2 Matches", False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - 3 Matches", False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Results - 4 Matches", False)

    obs.set_scene(config.FULL_SCREEN_STATS)

    phase = ""
    round = results[0]['round']

    with open(scene_title, 'w') as file:
        if str(round).find('.') != -1:
            phase = "Tiebreakers"
        elif int(round) >= 17:
            phase = "Final Rounds"
        else:
            phase = "Round " +str(round) +" Results"
        file.write(phase)

    match_limit = 1
    scene_choice = ""
    len_match = len(results)

    if(len_match % 4 == 0):
        match_limit = 4
        scene_choice = config.FSS_RESULTS_4
    elif(len_match % 3 == 0):
        match_limit = 3
        scene_choice = config.FSS_RESULTS_3
    elif (len_match % 2 == 0):
        match_limit = 2
        scene_choice = config.FSS_RESULTS_2
    else:
        scene_choice = config.FSS_RESULTS_1

    match_count = 1
    pp_array = []

    for matchup in results:
        info_file = "./Text Files/Big Screen/Results/Match " +str(match_count) +"/Info.txt"
        status_file = "./Text Files/Big Screen/Results/Match " +str(match_count) +"/Status.txt"
        team1_file = "./Text Files/Big Screen/Results/Match " +str(match_count) +"/Team 1.txt"
        team1city_file = "./Text Files/Big Screen/Results/Match " +str(match_count) +"/Team 1 City.txt"
        team1score_file = "./Text Files/Big Screen/Results/Match " +str(match_count) +"/Team 1 Score.txt"
        team2_file = "./Text Files/Big Screen/Results/Match " +str(match_count) +"/Team 2.txt"
        team2city_file = "./Text Files/Big Screen/Results/Match " +str(match_count) +"/Team 2 City.txt"
        team2score_file = "./Text Files/Big Screen/Results/Match " +str(match_count) +"/Team 2 Score.txt"

        pp_array.append(matchup['pp'])

        with open(info_file, 'w') as file:
            if phase == "Tiebreakers":
                file.write("Tiebreakers - " +matchup['bracket'])
            else:
                file.write("Round " +str(matchup['round']) +" - " +matchup['bracket'])
        with open(team1_file, 'w') as file:
            file.write(matchup['team1'])
        with open(team1city_file, 'w') as file:
            file.write(matchup['team1_city'])
        with open(team1score_file, 'w') as file:
            file.write(str(matchup['team1_score']))
        with open(team2_file, 'w') as file:
            file.write(matchup['team2'])
        with open(team2city_file, 'w') as file:
            file.write(matchup['team2_city'])
        with open(team2score_file, 'w') as file:
            file.write(str(matchup['team2_score']))
        with open(status_file, 'w') as file:
            txt2write = ""

            arr = matchup['status'].split(" ")

            if arr[0] == "Tossup":
                text2write = arr[0] + "\n" +arr[1]
            elif arr[0] == "Bonus":
                 text2write = arr[0] + "\n" +arr[1]
            elif arr[0] == "Final":
                if len(arr) == 1:
                    txt2write = "Final"
                elif len(arr) == 2:
                    txt2write = "Final\n(OT)"
                else:
                    txt2write = "Final\n(10 TU)"
            else:
                txt2write = matchup['status']

            file.write(txt2write)

        if match_count == match_limit:
            config.time.sleep(config.SLEEP_TIME)
            j = 1

            obs.toggle_source_visibility(config.FULL_SCREEN_STATS, scene_choice, True)

            while j <= match_limit:
                print(scene_choice)
                obs.toggle_source_visibility(scene_choice, "FS - Results - Match " +str(j) + " - Text", True)
                obs.toggle_source_visibility(scene_choice, "FS - Results - Match " +str(j) + " - PP", pp_array[j-1])

                j+=1
        else:
            match_count += 1

#END RESULTS#
#BEGIN MATCHUPS#

def show_ind_matchup(matchups, phase):
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - 1 Match", False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - 2 Matches", False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - 3 Matches", False)
    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, "Full Screen - Matchups - 4 Matches", False)
    
    scene_choice = ""
    match_limit = 1
    len_match = len(matchups)

    if(len_match % 4 == 0):
        match_limit = 4
        scene_choice = config.FSS_MATCHUPS_4
    elif(len_match % 3 == 0):
        match_limit = 3
        scene_choice = config.FSS_MATCHUPS_3
    elif (len_match % 2 == 0):
        match_limit = 2
        scene_choice = config.FSS_MATCHUPS_2
    else:
        scene_choice = config.FSS_MATCHUPS_1 

    match_count = 1

    for matchup in matchups:

        path = "./Text Files/Big Screen/Matchups/"        
        info_file = path + "Match " +str(match_count) +"/Info.txt"
        team1_file = path + "Match " +str(match_count) +"/Team 1.txt"
        team1city_file = path + "Match " +str(match_count) +"/Team 1 City.txt"
        team2_file = path + "Match " +str(match_count) +"/Team 2.txt"
        team2city_file = path + "Match " +str(match_count) +"/Team 2 City.txt"

        with open(info_file, 'w') as file:
            if phase == "Tiebreakers":
                file.write("Tiebreakers - " +matchup['bracket'])
            else:
                file.write("Round " +str(matchup['round']) +" - " +matchup['bracket'])
        with open(team1_file, 'w') as file:
            file.write(matchup['team1'])
        with open(team1city_file, 'w') as file:
            file.write(matchup['team1_city'])
        with open(team2_file, 'w') as file:
            file.write(matchup['team2'])
        with open(team2city_file, 'w') as file:
            file.write(matchup['team2_city'])

        if match_count == match_limit:
            
            config.time.sleep(config.SLEEP_TIME)
            j = 1

            while j <= match_limit:
                obs.toggle_source_visibility(config.FULL_SCREEN_STATS, scene_choice, True)
                obs.toggle_source_visibility(scene_choice, "FS - Matchups - Match " +str(j), True)

                j+=1
        else:
            match_count +=1

def loop_matchups(phase):
    scene_title = "./Text Files/Big Screen/Title.txt"

    obs.set_scene(config.FULL_SCREEN_STATS)
    hide_all_overlays()

    with open(scene_title, 'w') as file:
        if phase == "Prelims":
            round = 1
        elif phase == "Playoffs":
            round = 6
        elif phase == "Superplayoffs":
            round = 11
        else:
            round = 1

        file.write("Round " + str(round) + " Matchups ")

    matchups = data.get_matchups(round)
    len_match = len(matchups)
    match_limit = 1
    scene_choice = ""

    if(round >= 11 and round <=16):
        match_limit = 4
        scene_choice = config.FSS_MATCHUPS_4
    elif(round <= 10 and isinstance(round, int)):
        match_limit = 3
        scene_choice = config.FSS_MATCHUPS_3
    elif(len_match % 4 == 0):
        match_limit = 4
        scene_choice = config.FSS_MATCHUPS_4
    elif(len_match % 3 == 0):
        match_limit = 3
        scene_choice = config.FSS_MATCHUPS_3
    elif (len_match % 2 == 0):
        match_limit = 2
        scene_choice = config.FSS_MATCHUPS_2
    else:
        scene_choice = config.FSS_MATCHUPS_1

    match_count = 1
    active_matchups = []

    for matchup in matchups:

        active_matchups.append(matchup)

        if match_count == match_limit:

            show_ind_matchup(active_matchups, phase)
            active_matchups.clear()
            
            j=1
            config.time.sleep(config.SHOW_TIME*match_limit)

            while j <= match_limit:
                obs.toggle_source_visibility(scene_choice, "FS - Matchups - Match " +str(j), False)
                j+=1
                
            match_count = 1
        else:
            match_count+=1

    hide_all_overlays()

#END MATCHUPS#
#BEGIN STANDINGS#

def show_ind_standings(phase, bracket):
    scene_title = "./Text Files/Big Screen/Standings/Title.txt"

    hide_all_overlays()

    scene_choice = config.STANDINGS_6
    tot_teams = 6

    if phase == "Superplayoffs":
        tot_teams = len(bracket['teams'])

        if tot_teams == 8:
            scene_choice = config.STANDINGS_8
        else:
            scene_choice = config.STANDINGS_4
        
    elif phase == "Playoffs":
        scene_choice = config.STANDINGS_7
        tot_teams = 7

    obs.toggle_source_visibility(config.FULL_SCREEN_STATS, scene_choice, True)

    team_count = 1

    with open(scene_title, 'w') as dest:
        dest.write(bracket['name'])
        
    for school in bracket['teams']:

        city_file = "./Text Files/Big Screen/Standings/Team " +str(team_count) +"/City.txt"
        ppb_file = "./Text Files/Big Screen/Standings/Team " +str(team_count) +"/PPB.txt"
        ppg_file = "./Text Files/Big Screen/Standings/Team " +str(team_count) +"/PPG.txt"
        rank_file = "./Text Files/Big Screen/Standings/Team " +str(team_count) +"/Rank.txt"
        record_file = "./Text Files/Big Screen/Standings/Team " +str(team_count) +"/Record.txt"
        team_file =  "./Text Files/Big Screen/Standings/Team " +str(team_count) +"/Team.txt"

        team_count+=1

        with open(rank_file, 'w') as dest:
            dest.write(str(school['rank']))
        with open(team_file, 'w') as dest:
            dest.write(school['team'])
        with open(city_file, 'w') as dest:
            dest.write(school['city'])
        with open(record_file, 'w') as dest:
            dest.write(school['record'])
        with open(ppg_file, 'w') as dest:
            dest.write(str(school['ppg']))
        with open(ppb_file, 'w') as dest:
            dest.write(str(school['ppb']))
    
    config.time.sleep(config.SLEEP_TIME)
    team_count = 1

    obs.toggle_source_visibility(scene_choice, "FS - Standings - Title", True)

    for school in bracket['teams']:
        obs.toggle_source_visibility(scene_choice, "FS - Standings - Team " + str(team_count), True)
        obs.toggle_source_visibility(scene_choice, "FS - Standings - Team " + str(team_count) +" - Next Phase Flag", school['adv_flag'])
        obs.toggle_source_visibility(scene_choice, "FS - Standings - Team " + str(team_count) +" - Tiebreaks Flag", school['tb_flag'])
        obs.toggle_source_visibility(scene_choice, "FS - Standings - Team " + str(team_count) +" - PP Flag", school['pp_flag'])

        team_count +=1
        
def loop_standings(phase):
    scene_title = "./Text Files/Big Screen/Title.txt"

    obs.set_scene(config.FULL_SCREEN_STATS)
    hide_all_overlays()
    tot_teams = 6

    scene_choice = config.STANDINGS_6
    tot_teams = 6
    counter = 0

    if phase == "Superplayoffs":
        scene_choice = config.STANDINGS_8
        tot_teams = 8
    elif phase == "Playoffs":
        scene_choice = config.STANDINGS_7
        tot_teams = 7

    with open(scene_title, 'w') as file:
        file.write(phase +" Standings")

    standings = data.get_standings(phase)

    config.time.sleep(config.SLEEP_TIME)

    for bracket in standings:

        team_count = 1
        counter+=1

        if counter == 4 and phase == "Superplayoffs":
            hide_all_overlays()
            config.time.sleep(config.SLEEP_TIME)
            scene_choice = config.STANDINGS_4
            tot_teams = 4

        show_ind_standings(phase, bracket)
        config.time.sleep(config.SHOW_TIME*tot_teams/2)

        obs.toggle_source_visibility(scene_choice, "FS - Standings - Title", False)

        for school in bracket['teams']:
            obs.toggle_source_visibility(scene_choice, "FS - Standings - Team " + str(team_count), False)
            obs.toggle_source_visibility(scene_choice, "FS - Standings - Team " + str(team_count) +" - Next Phase Flag", False)
            obs.toggle_source_visibility(scene_choice, "FS - Standings - Team " + str(team_count) +" - Tiebreaks Flag", False)
            obs.toggle_source_visibility(scene_choice, "FS - Standings - Team " + str(team_count) +" - PP Flag", False)

            team_count +=1

        team_count = 1

    hide_all_overlays()

#END STANDINGS#
#BEGIN QUESTIONS#

def get_question(round_number, question_number, is_TU):
    path = "./Data/Questions/"

    if round_number < 10:
        path = path + "Round 0" + str(round_number) +".json"
    else:
        path = path + "Round " + str(round_number) +".json"

    with open(path, 'r') as file:
        data = config.json.load(file)

    question = None

    if is_TU:
        question = data["tossups"][question_number-1]
    else:
        question = data["bonuses"][question_number-1]

    return question

def set_question(question, question_number, round_number, is_TU):
    path = "./Text Files/Big Screen/Questions/"

    if is_TU:
        with open(path + "Header.txt", 'w') as file:
            file.write("Round " + str(round_number) + " - " + "Tossup " +str(question_number))
        with open(path + "Tossup.txt", 'w') as file:
            tossup_text = question['question']
            file.write(clean_text(tossup_text))
        with open(path + "Tossup_Answer.txt", 'w') as file:
            ans_text = question['answer']
            file.write(clean_text(ans_text))
    else:
        with open(path + "Header.txt", 'w') as file:
            file.write("Round " + str(round_number) + " - " + "Bonus " +str(question_number))
        with open(path + "Bonus.txt", 'w') as file:
            full_text = question['leadin'] + "\n\n\n"
            for i in range (0, 3):
                full_text = full_text + question['parts'][i] + "\n"
                full_text = full_text + "Answer: " + question['answers'][i] + "\n\n\n"

            file.write(clean_text(full_text))

def load_question(round_number, question_number, is_TU):
    obs.toggle_source_visibility("Question Scene", "Question - Tossup", False)
    obs.toggle_source_visibility("Question Scene", "Question - Bonus", False)
    obs.toggle_source_visibility("Question Scene", "Question - Header", False)
    config.time.sleep(config.SLEEP_TIME/2)
    set_question(get_question(round_number, question_number, is_TU),question_number, round_number, is_TU)
    config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility("Question Scene", "Question - Header", True)
    if is_TU:
        obs.toggle_source_visibility("Question Scene", "Question - Tossup", True)
    else:
        obs.toggle_source_visibility("Question Scene", "Question - Bonus", True)

def remove_diacritics(text):
    return ''.join(
        c for c in config.unicodedata.normalize('NFKD', text)
        if not config.unicodedata.combining(c)
    )

def clean_text(text):
    text = text.replace('\u201C', '"').replace('\u201D','"').replace('\u2019',"'")
    text = text.replace('<b>','').replace('</b>','').replace('<i>','').replace('</i>','').replace('<u>','').replace('</u>','')
    text = text.replace('<em>','').replace('</em>','')
    text = config.re.sub(r'\s*\([^)]*\)', '', text)
    text = remove_diacritics(text)
    return text

#END QUESTIONS#


if __name__ == "__main__":
    config.init()

    load_question(10, 4, False)
    '''
    loop_brackets("Prelims")
    loop_brackets("Playoffs")
    loop_brackets("Superplayoffs")
    
    loop_individual()
    
    loop_standings("Prelims")
    loop_standings("Playoffs")
    loop_standings("Superplayoffs")
    
    loop_matchups("Prelims")
    loop_matchups("Playoffs")
    loop_matchups("Superplayoffs")
    
    i = 1
    while i <= 1:
        loop_round_matches(i)
        i+=1
    
    loop_round_matches(5.1)
    loop_round_matches(5.2)

    i = 6
    while i <= 10:
        loop_round_matches(i)
        i+=1
    loop_round_matches(10.1)
    loop_round_matches(10.2)

    i = 11
    while i <= 18:
        loop_round_matches(i)
        i+=1
    
    '''