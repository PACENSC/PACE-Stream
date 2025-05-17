import config
import obs
import data

def hide_all_overlays():
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_BRACKETS_4_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_BRACKETS_5_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_BRACKETS_6_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_BRACKETS_7_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_BRACKETS_8_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_STANDINGS_4_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_STANDINGS_5_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_STANDINGS_6_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_STANDINGS_7_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_STANDINGS_8_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_INDIVIDUAL, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_RESULTS_1, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_RESULTS_2, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_RESULTS_3, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_RESULTS_4, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_MATCHUPS_1, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_MATCHUPS_2, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_MATCHUPS_3, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_MATCHUPS_4, False)

    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_BRACKETS_4_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_BRACKETS_5_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_BRACKETS_6_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_BRACKETS_7_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_BRACKETS_8_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_STANDINGS_4_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_STANDINGS_5_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_STANDINGS_6_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_STANDINGS_7_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_STANDINGS_8_TEAMS, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_INDIVIDUAL, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_RESULTS_1, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_RESULTS_2, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_RESULTS_3, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_RESULTS_4, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_MATCHUPS_1, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_MATCHUPS_2, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_MATCHUPS_3, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_MATCHUPS_4, False)

### ---BEGIN BRACKET--- ###

def loop_brackets(phase, side):
    scene_title = "./Text Files/Big Screen/Title.txt"
    sceneLen=0
    counter = 0

    obs.set_scene(config.SIDESHOT)
    hide_all_overlays()

    if phase == "Prelims":
        with open(scene_title, 'w') as file:
            file.write("Preliminary Brackets")
        sceneLen=6
    elif phase == "Playoffs":
        with open(scene_title, 'w') as file:
            file.write("Playoff Brackets")
        sceneLen=7
    elif phase == "Superplayoffs":
        with open(scene_title, 'w') as file:
            file.write("Superplayoff Brackets")
        sceneLen=8
    else:
        with open(scene_title, 'w') as file:
            file.write("Finals")
        sceneLen=1

    brackets = data.get_brackets_with_teams(phase)

    for bracket in brackets:
        counter+=1
        show_individual_bracket(bracket, side)
        config.time.sleep(config.SHOW_TIME*2)
        if counter == 3 and sceneLen == 8:
            sceneLen = 4
            if side == config.SIDE.LEFT:
                hide_all_overlays()
                config.time.sleep(config.SLEEP_TIME * 2)
                obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_BRACKETS_4_TEAMS, True)
            else:
                hide_all_overlays()
                config.time.sleep(config.SLEEP_TIME * 2)
                obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_BRACKETS_4_TEAMS, True)

    scene = config.SSS_BRACKETS_6_TEAMS
    if sceneLen == 8:
        scene = config.SSS_BRACKETS_8_TEAMS
    elif sceneLen == 7:
        scene = config.SSS_BRACKETS_7_TEAMS
    elif sceneLen == 4:
        scene = config.SSS_BRACKETS_4_TEAMS

    obs.toggle_source_visibility(scene, "SS - Brackets - Title - Text", False)
    obs.toggle_source_visibility(scene, "SS - Brackets - "+ str(sceneLen) +" Teams", False)

    hide_all_overlays()

def show_individual_bracket(bracket, side):
    teams = bracket['teams']
    scene = ""
    dir_scene = ""
    sceneLen = len(teams)
    
    if(sceneLen == 4):
        if side == config.SIDE.LEFT:
            dir_scene = config.LEFT_SSS_BRACKETS_4_TEAMS
        else:
            dir_scene = config.RIGHT_SSS_BRACKETS_4_TEAMS

        scene = config.SSS_BRACKETS_4_TEAMS
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene, True)
    elif(sceneLen == 5):
        if side == config.SIDE.LEFT:
            dir_scene = config.LEFT_SSS_BRACKETS_5_TEAMS
        else:
            dir_scene = config.RIGHT_SSS_BRACKETS_5_TEAMS

        scene = config.SSS_BRACKETS_5_TEAMS
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene, True)
    elif(sceneLen == 6):
        if side == config.SIDE.LEFT:
            dir_scene = config.LEFT_SSS_BRACKETS_6_TEAMS
        else:
            dir_scene = config.RIGHT_SSS_BRACKETS_6_TEAMS

        scene = config.SSS_BRACKETS_6_TEAMS
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene, True)
    elif(sceneLen == 7):
        if side == config.SIDE.LEFT:
            dir_scene = config.LEFT_SSS_BRACKETS_7_TEAMS
        else:
            dir_scene = config.RIGHT_SSS_BRACKETS_7_TEAMS

        scene = config.SSS_BRACKETS_7_TEAMS
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene, True)
    else:
        if side == config.SIDE.LEFT:
            dir_scene = config.LEFT_SSS_BRACKETS_8_TEAMS
        else:
            dir_scene = config.RIGHT_SSS_BRACKETS_8_TEAMS
        scene = config.SSS_BRACKETS_8_TEAMS
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene, True)

    teamcount = 1

    obs.toggle_source_visibility(scene, "SS - Brackets - Title - Text", False)
    obs.toggle_source_visibility(scene, "SS - Brackets - " +str(sceneLen) + " Teams", False)

    path = "./Text Files/Side Screen/Brackets/"
    with open(path + "Bracket.txt", 'w') as src:
        src.write(bracket['bracket'])                
            

    for team in teams:
        with open(path + "Team " +str(teamcount) +"/Name.txt", 'w') as src:
            src.write(team['team'])
        with open(path + "Team " +str(teamcount) +"/City.txt", 'w') as src:
            src.write(team['city'])
            
        teamcount+=1

    config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility(scene, "SS - Brackets - Title - Text", True)
    obs.toggle_source_visibility(scene, "SS - Brackets - " +str(sceneLen) + " Teams", True)

### ---END BRACKET--- ###
### ---BEGIN STANDINGS--- ###

def loop_standings(phase, side):
    obs.set_scene(config.SIDESHOT)
    hide_all_overlays()

    dir_scene_choice = ""
    counter = 0

    if side == config.SIDE.LEFT:
        dir_scene_choice = config.LEFT_SSS_STANDINGS_6_TEAMS
    else:
        dir_scene_choice = config.RIGHT_SSS_STANDINGS_6_TEAMS
    scene_choice = config.SSS_STANDINGS_6_TEAMS
    
    tot_teams = 6

    if phase == "Superplayoffs":
        if side == config.SIDE.LEFT:
            dir_scene_choice = config.LEFT_SSS_STANDINGS_8_TEAMS
        else:
            dir_scene_choice = config.RIGHT_SSS_STANDINGS_8_TEAMS
        scene_choice = config.SSS_STANDINGS_8_TEAMS
        tot_teams = 8
    elif phase == "Playoffs":
        if side == config.SIDE.LEFT:
            dir_scene_choice = config.LEFT_SSS_STANDINGS_7_TEAMS
        else:
            dir_scene_choice = config.RIGHT_SSS_STANDINGS_7_TEAMS
        scene_choice = config.SSS_STANDINGS_7_TEAMS
        tot_teams = 7

    standings = data.get_standings(phase)

    for bracket in standings:
        counter +=1

        if phase == "Superplayoffs" and counter == 4:
            if side == config.SIDE.LEFT:
                dir_scene_choice = config.LEFT_SSS_STANDINGS_4_TEAMS
            else:
                dir_scene_choice = config.RIGHT_SSS_STANDINGS_4_TEAMS
            scene_choice = config.SSS_STANDINGS_4_TEAMS
            tot_teams = 4

            hide_all_overlays()

        show_individual_standings(bracket, scene_choice, dir_scene_choice)
        config.time.sleep(config.SHOW_TIME*tot_teams/2)

        team_count = 1

        for school in bracket['teams']:
            obs.toggle_source_visibility(scene_choice, "SS - Standings - Team " + str(team_count), False)
            team_count +=1

        team_count = 1
        obs.toggle_source_visibility(scene_choice, "SS - Standings - Title - Text", False)

    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene_choice, False)

def show_individual_standings(bracket, scene_choice, dir_scene_choice):

    path = "./Text Files/Side Screen/Standings/"

    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene_choice, True)
    config.time.sleep(config.SLEEP_TIME)

    with open(path + "Bracket.txt", 'w') as file:
        file.write(bracket['name'])

    team_count = 1

    for school in bracket['teams']:
        city_file = path + "/Team " +str(team_count) +"/City.txt"
        ppg_file = path + "/Team " +str(team_count) +"/PPG.txt"
        record_file = path + "/Team " +str(team_count) +"/Record.txt"
        team_file =  path + "/Team " +str(team_count) +"/Name.txt"

        team_count+=1

        with open(team_file, 'w') as dest:
            dest.write(school['team'])
        with open(city_file, 'w') as dest:
            dest.write(school['city'])
        with open(record_file, 'w') as dest:
            dest.write(school['record'])
        with open(ppg_file, 'w') as dest:
            dest.write(str(school['ppg']) + " PPG")

    team_count = 1
    config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility(scene_choice, "SS - Standings - Title - Text", True)

    for school in bracket['teams']:
        obs.toggle_source_visibility(scene_choice, "SS - Standings - Team " + str(team_count), True)
        team_count +=1

### ---RND STANDINGS--- ###
### ---BEGIN INDIVIDUAL--- ###

def show_individual_page(players):
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 1", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 2", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 3", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 4", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 5", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 6", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Header", True)
    
    playercount = 1
    path = "./Text Files/Side Screen/Individual Standings/"

    act_players = []

    for player in players:

        rank_file= path + "Player " +str(playercount) +"/Rank.txt"
        name_file= path + "Player " +str(playercount) +"/Name.txt"
        team_file= path + "Player " +str(playercount) +"/School.txt"
        ppg_file= path + "Player " +str(playercount) +"/PPG.txt"

        act_players.append(player)

        with open(rank_file, 'w') as file:
            file.write(str(player['rank']))
        with open(name_file, 'w') as file:
            file.write(str(player['name']))
        with open(team_file, 'w') as file:
            file.write(str(player['team']) + " - "+ str(player['city']))
        with open(ppg_file, 'w') as file:
            file.write(str(player['ppg']))

        if playercount == 6 or player['ppg'] == 0:
                        
            config.time.sleep(config.SLEEP_TIME)
               
            for playerNum in range(1, playercount + 1):
                obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player " +str(playerNum), True)

            if(player['ppg'] == 0):
                break
        else:
            playercount+=1

def loop_individual(side):
    obs.set_scene(config.SIDESHOT)
    hide_all_overlays()
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Header", True)

    if side == config.SIDE.LEFT:
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_INDIVIDUAL, True) 
    else:
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_INDIVIDUAL, True) 

    players = data.get_players()
    playercount = 1
    path = "./Text Files/Side Screen/Individual Standings/"

    act_players = []

    count = 0

    while count <= 4:
        show_individual_page(players[(6*count):((6*count)+6)])
        config.time.sleep(config.SHOW_TIME*3)
        count+=1

    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 1", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 2", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 3", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 4", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 5", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Player 6", False)
    obs.toggle_source_visibility(config.SSS_INDIVIDUAL, "SS - Individual - Header", False)

###---END INDIVIDUAL---###
### ---BEGIN RESULTS--- ###

def display_round_results(results, side, header, isloop):

    obs.toggle_source_visibility(config.SSS_RESULTS_1, "SS - Results - 1/2 Match(es) - Match 1", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_1, "SS - Results - Header", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_1, "SS - Results - 1 Match - Match 1 - PP Flag", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_2, "SS - Results - 1/2 Match(es) - Match 1", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_2, "SS - Results - 1/2 Match(es) - Match 2", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_2, "SS - Results - Header", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_2, "SS - Results - 2 Matches - Match 1 - PP Flag", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_2, "SS - Results - 2 Matches - Match 2 - PP Flag", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_3, "SS - Results - Header", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_3, "SS - Results - 3 Matches - Match 1", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_3, "SS - Results - 3 Matches - Match 2", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_3, "SS - Results - 3 Matches - Match 3", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_3, "SS - Results - 3 Matches - Match 1 - PP Flag", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_3, "SS - Results - 3 Matches - Match 2 - PP Flag", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_3, "SS - Results - 3 Matches - Match 3 - PP Flag", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_4, "SS - Results - Header", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_4, "SS - Results - 4 Matches - Match 1", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_4, "SS - Results - 4 Matches - Match 2", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_4, "SS - Results - 4 Matches - Match 3", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_4, "SS - Results - 4 Matches - Match 4", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_4, "SS - Results - 4 Matches - Match 1 - PP Flag", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_4, "SS - Results - 4 Matches - Match 2 - PP Flag", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_4, "SS - Results - 4 Matches - Match 3 - PP Flag", False)
    obs.toggle_source_visibility(config.SSS_RESULTS_4, "SS - Results - 4 Matches - Match 4 - PP Flag", False)

    if not isloop:
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_RESULTS_1, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_RESULTS_1, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_RESULTS_2, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_RESULTS_2, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_RESULTS_3, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_RESULTS_3, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_RESULTS_4, False)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_RESULTS_4, False)

    len_results = len(results)

    if len_results <= 4:
        match_limit = 1
        scene_choice = ""
        dir_scene_choice = ""

        if(len_results % 4 == 0):
            match_limit = 4
            scene_choice = config.SSS_RESULTS_4

            if side == config.SIDE.LEFT:
                dir_scene_choice = config.LEFT_SSS_RESULTS_4
            else:
                dir_scene_choice = config.RIGHT_SSS_RESULTS_4

        elif(len_results % 3 == 0):
            match_limit = 3
            scene_choice = config.SSS_RESULTS_3

            if side == config.SIDE.LEFT:
                dir_scene_choice = config.LEFT_SSS_RESULTS_3
            else:
                dir_scene_choice = config.RIGHT_SSS_RESULTS_3

        elif (len_results % 2 == 0):
            match_limit = 2
            scene_choice = config.SSS_RESULTS_2

            if side == config.SIDE.LEFT:
                dir_scene_choice = config.LEFT_SSS_RESULTS_2
            else:
                dir_scene_choice = config.RIGHT_SSS_RESULTS_2

        else:
            scene_choice = config.SSS_RESULTS_1

            if side == config.SIDE.LEFT:
                dir_scene_choice = config.LEFT_SSS_RESULTS_1
            else:
                dir_scene_choice = config.RIGHT_SSS_RESULTS_1

        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene_choice, True)

        match_count = 1
        pp_array = []

        for result in results:
            path = "./Text Files/Side Screen/Results/"

            info_file = path + "Header.txt"
            status_file = path + "Match " +str(match_count) +"/Status.txt"
            team1_file = path + "Match " +str(match_count) +"/Team 1 Name.txt"
            team1city_file = path + "Match " +str(match_count) +"/Team 1 City.txt"
            team1score_file = path + "Match " +str(match_count) +"/Team 1 Score.txt"
            team2_file = path + "Match " +str(match_count) +"/Team 2 Name.txt"
            team2city_file = path + "Match " +str(match_count) +"/Team 2 City.txt"
            team2score_file = path + "Match " +str(match_count) +"/Team 2 Score.txt"

            pp_array.append(result['pp'])

            with open(info_file, 'w') as file:
                if header == "":
                    file.write("Selected Results")
                else:
                    file.write(header)
            with open(team1_file, 'w') as file:
                file.write(result['team1'])
            with open(team1city_file, 'w') as file:
                file.write(result['team1_city'])
            with open(team1score_file, 'w') as file:
                file.write(str(result['team1_score']))
            with open(team2_file, 'w') as file:
                file.write(result['team2'])
            with open(team2city_file, 'w') as file:
                file.write(result['team2_city'])
            with open(team2score_file, 'w') as file:
                file.write(str(result['team2_score']))
            with open(status_file, 'w') as file:

                txt2write = ""

                arr = result['status'].split(" ")

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
                    txt2write = result['status']

                file.write(txt2write)
            
            config.time.sleep(config.SLEEP_TIME)
            j = 1

            if match_count == match_limit:
                while j <= match_limit:
                    if match_limit <= 2:
                        obs.toggle_source_visibility(scene_choice, "SS - Results - 1/2 Match(es) - Match " +str(j), True)
                        if match_limit == 1:
                            obs.toggle_source_visibility(scene_choice, "SS - Results - 1 Match - Match " +str(j) + " - PP Flag", pp_array[j-1])
                        else:
                            obs.toggle_source_visibility(scene_choice, "SS - Results - 2 Matches - Match " +str(j) + " - PP Flag", pp_array[j-1])
                    else:
                        obs.toggle_source_visibility(scene_choice, "SS - Results - " + str(match_limit) + " Matches - Match " +str(j), True)
                        obs.toggle_source_visibility(scene_choice, "SS - Results - " + str(match_limit) + " Matches - Match " +str(j) + " - PP Flag", pp_array[j-1])
                    obs.toggle_source_visibility(scene_choice, "SS - Results - Header", True)
                    j+=1
            else:
                match_count+=1

def loop_round_results(round, side):

    scene_title = "./Text Files/Side Screen/Results/Header.txt"

    obs.set_scene(config.SIDESHOT)
    hide_all_overlays()

    phase = ""

    with open(scene_title, 'w') as file:
        if str(round).find('.') != -1:
            phase = "Tiebreakers"
        elif int(round) >= 17:
            phase = "Final Rounds"
        else:
            phase = "Round " +str(round)
        file.write(phase)

    matchups = data.get_results(round)
    len_match = len(matchups)
    match_limit = 1

    if(round >= 11 and round <=16):
        match_limit = 4        
    elif(round <= 10 and isinstance(round, int)):
        match_limit = 3
    elif(len_match % 4 == 0):
        match_limit = 4
    elif(len_match % 3 == 0):
        match_limit = 3
    elif (len_match % 2 == 0):
        match_limit = 2

    match_count = 1
    match_array = []

    for matchup in matchups:
        match_array.append(matchup)

        if match_count == match_limit:
            display_round_results(match_array, side, "Round " + str(round) + " - " + matchup['bracket'], True)
            match_array = []
            config.time.sleep(config.SHOW_TIME*match_limit)
            hide_result_overlays(match_count)
            #config.time.sleep(config.SLEEP_TIME)
            match_count = 1
        else:
            match_count+=1

    hide_all_overlays()

def hide_result_overlays(len_results):
    scene_choice = ""
    match_limit = 1
    
    if(len_results % 4 == 0):
        scene_choice = config.SSS_RESULTS_4
        match_limit = 4
    elif(len_results % 3 == 0):
        scene_choice = config.SSS_RESULTS_3
        match_limit = 3
    elif (len_results % 2 == 0):
        scene_choice = config.SSS_RESULTS_2
        match_limit = 2      
    else:
        scene_choice = config.SSS_RESULTS_1

    for i in range(len_results):
        if len_results <= 2:
            obs.toggle_source_visibility(scene_choice, "SS - Results - 1/2 Match(es) - Match " +str(i+1), False)
        else:
            obs.toggle_source_visibility(scene_choice, "SS - Results - " + str(match_limit) + " Matches - Match " +str(i+1), False)
        obs.toggle_source_visibility(scene_choice, "SS - Results - Header", False)

        if len_results == 1:
            obs.toggle_source_visibility(scene_choice, "SS - Results - 1 Match - Match 1 - PP Flag" ,False)
        else:
            obs.toggle_source_visibility(scene_choice, "SS - Results - "+ str(len_results) +" Matches - Match "+str(i+1)+" - PP Flag" ,False)

### ---END RESULTS--- ###
###---BEGIN MATCHUPS---###

def display_matchups(matches, side, header):

    obs.toggle_source_visibility(config.SSS_MATCHUPS_1, "SS - Matchups - 1/2 Match(es) - Match 1", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_1, "SS - Matchups - Header", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_2, "SS - Matchups - 1/2 Match(es) - Match 1", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_2, "SS - Matchups - 1/2 Match(es) - Match 2", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_2, "SS - Matchups - Header", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_3, "SS - Matchups - Header", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_3, "SS - Matchups - 3 Matches - Match 1", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_3, "SS - Matchups - 3 Matches - Match 2", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_3, "SS - Matchups - 3 Matches - Match 3", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_4, "SS - Matchups - Header", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_4, "SS - Matchups - 4 Matches - Match 1", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_4, "SS - Matchups - 4 Matches - Match 2", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_4, "SS - Matchups - 4 Matches - Match 3", False)
    obs.toggle_source_visibility(config.SSS_MATCHUPS_4, "SS - Matchups - 4 Matches - Match 4", False)

    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_MATCHUPS_4, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_MATCHUPS_4, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_MATCHUPS_3, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_MATCHUPS_3, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_MATCHUPS_2, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_MATCHUPS_2, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.LEFT_SSS_MATCHUPS_1, False)
    obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, config.RIGHT_SSS_MATCHUPS_1, False)
    
    
    len_match = len(matches)
    
    if len_match <= 4:

        match_limit = 1
        scene_choice = ""
        dir_scene_choice = ""

        if(len_match % 4 == 0):
            match_limit = 4
            scene_choice = config.SSS_MATCHUPS_4
            
            if side == config.SIDE.LEFT:
                dir_scene_choice = config.LEFT_SSS_MATCHUPS_4
            else:
                dir_scene_choice = config.RIGHT_SSS_MATCHUPS_4
                
        elif(len_match % 3 == 0):
            match_limit = 3
            scene_choice = config.SSS_MATCHUPS_3
            
            if side == config.SIDE.LEFT:
                dir_scene_choice = config.LEFT_SSS_MATCHUPS_3
            else:
                dir_scene_choice = config.RIGHT_SSS_MATCHUPS_3
                
        elif (len_match % 2 == 0):
            match_limit = 2
            scene_choice = config.SSS_MATCHUPS_2
            
            if side == config.SIDE.LEFT:
                dir_scene_choice = config.LEFT_SSS_MATCHUPS_2
            else:
                dir_scene_choice = config.RIGHT_SSS_MATCHUPS_2         
        else:
            scene_choice = config.SSS_MATCHUPS_1
            
            if side == config.SIDE.LEFT:
                dir_scene_choice = config.LEFT_SSS_MATCHUPS_1
            else:
                dir_scene_choice = config.RIGHT_SSS_MATCHUPS_1

        
                
        match_count = 1

        for matchup in matches:
            path = "./Text Files/Side Screen/Matchups/"

            info_file = path + "Header.txt"
            team1_file = path + "Match " +str(match_count) +"/Team 1 Name.txt"
            team1city_file = path + "Match " +str(match_count) +"/Team 1 City.txt"
            team2_file = path + "Match " +str(match_count) +"/Team 2 Name.txt"
            team2city_file = path + "Match " +str(match_count) +"/Team 2 City.txt"

            with open(info_file, 'w') as file:
                if header == "":
                    file.write("Selected Matches")
                else:
                    file.write(header)
            with open(team1_file, 'w') as file:
                file.write(matchup['team1'])
            with open(team1city_file, 'w') as file:
                file.write(matchup['team1_city'])
            with open(team2_file, 'w') as file:
                file.write(matchup['team2'])
            with open(team2city_file, 'w') as file:
                file.write(matchup['team2_city'])
            
            match_count += 1

            
        config.time.sleep(config.SLEEP_TIME)
        obs.toggle_source_visibility(config.SIDE_SCREEN_STATS, dir_scene_choice, True)

        for i in range(len_match):
            if len_match <= 2:
                obs.toggle_source_visibility(scene_choice, "SS - Matchups - 1/2 Match(es) - Match " +str(i+1), True)
            else:
                obs.toggle_source_visibility(scene_choice, "SS - Matchups - " + str(match_limit) + " Matches - Match " +str(i+1), True)
        obs.toggle_source_visibility(scene_choice, "SS - Matchups - Header", True)

def hide_matchup_overlays(len_match):
    scene_choice = ""
    match_limit = 1
    
    if(len_match % 4 == 0):
        scene_choice = config.SSS_MATCHUPS_4
        match_limit = 4
    elif(len_match % 3 == 0):
        scene_choice = config.SSS_MATCHUPS_3
        match_limit = 3
    elif (len_match % 2 == 0):
        scene_choice = config.SSS_MATCHUPS_2
        match_limit = 2      
    else:
        scene_choice = config.SSS_MATCHUPS_1

    for i in range(len_match):
        if len_match <= 2:
            obs.toggle_source_visibility(scene_choice, "SS - Matchups - 1/2 Match(es) - Match " +str(i+1), False)
        else:
            obs.toggle_source_visibility(scene_choice, "SS - Matchups - " + str(match_limit) + " Matches - Match " +str(i+1), False)
        obs.toggle_source_visibility(scene_choice, "SS - Matchups - Header", False)

def loop_matchups(phase, side):
    
    obs.set_scene(config.SIDESHOT)
    hide_all_overlays()

    round = 0

    if phase == "Prelims":
        round = 1
    elif phase == "Playoffs":
        round = 6
    elif phase == "Superplayoffs":
        round = 11
    else:
        round = 1

    matchups = data.get_matchups(round)
    len_match = len(matchups)
    match_limit = 1

    if(round >= 11 and round <=16):
        match_limit = 4
    elif(round <= 10 and isinstance(round, int)):
        match_limit = 3
    elif(len_match % 4 == 0):
        match_limit = 4
    elif(len_match % 3 == 0):
        match_limit = 3
    elif (len_match % 2 == 0):
        match_limit = 2

    matches = []

    for matchup in matchups:
        matches.append(matchup)
        if len(matches) == match_limit:
            display_matchups(matches, side, "Round " + str(round) + " - " +  matchup['bracket'])
            matches = []
            config.time.sleep(config.SHOW_TIME * match_limit)
            hide_matchup_overlays(match_limit)
            config.time.sleep(config.SLEEP_TIME)

    hide_all_overlays()

###---END MATCHUPS---###

if __name__ == "__main__":
    config.init()
    
    
    loop_round_results(1, config.SIDE.LEFT)
    loop_round_results(5.1, config.SIDE.LEFT)
    loop_round_results(11, config.SIDE.LEFT)
    
    loop_individual(config.SIDE.LEFT)
    
    
    loop_standings("Prelims", config.SIDE.LEFT)
    loop_standings("Playoffs", config.SIDE.LEFT)
    loop_standings("Superplayoffs", config.SIDE.LEFT)

    
    loop_brackets("Prelims", config.SIDE.LEFT)
    loop_brackets("Playoffs", config.SIDE.LEFT)
    loop_brackets("Superplayoffs", config.SIDE.LEFT)
    
    
    loop_matchups("Prelims", config.SIDE.LEFT)
    loop_matchups("Playoffs", config.SIDE.LEFT)
    loop_matchups("Superplayoffs", config.SIDE.LEFT)

    loop_round_results(1, config.SIDE.RIGHT)
    loop_round_results(5.1, config.SIDE.RIGHT)
    loop_round_results(11, config.SIDE.RIGHT)

    loop_individual(config.SIDE.RIGHT)

    loop_standings("Prelims", config.SIDE.RIGHT)
    loop_standings("Playoffs", config.SIDE.RIGHT)
    loop_standings("Superplayoffs", config.SIDE.RIGHT)

    loop_brackets("Prelims", config.SIDE.RIGHT)
    loop_brackets("Playoffs", config.SIDE.RIGHT)
    loop_brackets("Superplayoffs", config.SIDE.RIGHT)

    loop_matchups("Prelims", config.SIDE.RIGHT)
    loop_matchups("Playoffs", config.SIDE.RIGHT)
    loop_matchups("Superplayoffs", config.SIDE.RIGHT)
    