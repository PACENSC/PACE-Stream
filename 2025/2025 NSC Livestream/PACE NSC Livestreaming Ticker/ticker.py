import config
import obs
import data

#Function to loop through scroll ticker lines:
def ticker_loop_start():
    try:
        line_count = 1
        source_path="./Text Files/Scroll Bar/Scores.txt"
        dest_path="./Text Files/Scroll Bar/Active Text.txt"
        with open(source_path, 'r') as file:
            lines = file.readlines()

            line_count = len(lines)
            #print(f"Number of lines: {line_count}")
        
        line_num = 1

        while line_count > 0:
            if(line_num > line_count):
                    line_num = 1

            display_line = config.linecache.getline(source_path,line_num).strip()

            config.time.sleep(config.SHOW_TIME)

            with open(dest_path, 'w') as file:
                file.write(display_line)

            obs.toggle_source_visibility(config.OVERLAY, config.SCORE_TICKER, False)

            config.time.sleep(config.SLEEP_TIME)

            obs.toggle_source_visibility(config.OVERLAY, config.SCORE_TICKER, True)

            line_num+=1
            with open(source_path, 'r') as file:
                lines = file.readlines()

                line_count = len(lines)
                #print(f"Number of lines: {line_count}")

    except Exception as e:
        print(f"Failed to connect or perform actions: {e}")

def hide_all_overlays():
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_BRACKETS, False)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_INDIVIDUAL, False)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_MATCHUPS, False)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_RESULTS, False)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_STANDINGS, False)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.PHASE_OF_TICKER, False)
    config.time.sleep(config.SLEEP_TIME)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.PHASE_OF_TICKER, False)

def loop_brackets(phase):

    file_path="./Text Files/Scroll Bar/Brackets/"+phase+"/"
    phase_of_ticker="./Text Files/Scroll Bar/Phase of Ticker.txt"
    active_city="./Text Files/Scroll Bar/Brackets/Active City.txt"
    active_team="./Text Files/Scroll Bar/Brackets/Active Team.txt"
    active_bracket="./Text Files/Scroll Bar/Brackets/Bracket Name.txt"

    hide_all_overlays()

    if phase=="Prelims":
        with open(phase_of_ticker, 'w') as file:
                file.write("Preliminary Brackets")
    elif phase=="Playoffs":
        with open(phase_of_ticker, 'w') as file:
                file.write("Playoff Brackets")
    elif phase=="Superplayoffs":
        with open(phase_of_ticker, 'w') as file:
                file.write("Superplayoff Brackets")

    config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.PHASE_OF_TICKER, True)    

    obs.toggle_source_visibility(config.BOS_BRACKETS, config.BRACKETS_CITY_NAME, False)
    obs.toggle_source_visibility(config.BOS_BRACKETS, config.BRACKETS_TEAM_NAME, False)
    obs.toggle_source_visibility(config.BOS_BRACKETS, config.BRACKETS_NAME, False)

    config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_BRACKETS, True)

    brackets = data.get_brackets_with_teams(phase)

    for bracket in brackets:

        with open(file_path + bracket['bracket'] + '.txt', 'r') as file:
            lines = file.readlines()
            display_bracket = bracket['bracket']

            with open(active_bracket, 'w') as bracket_file:
                bracket_file.write(display_bracket)

            config.time.sleep(config.SLEEP_TIME)
            obs.toggle_source_visibility(config.BOS_BRACKETS, config.BRACKETS_NAME, True)

            teams=data.get_teams_in_bracket(phase, display_bracket)

            for line in teams:
                high_school = line['team']
                city = line['city']

                with open(active_team, 'w') as team_file:
                    team_file.write(high_school)
                
                with open(active_city, 'w') as city_file:
                    city_file.write(city)
                
                config.time.sleep(config.SLEEP_TIME)
                
                obs.toggle_source_visibility(config.BOS_BRACKETS, config.BRACKETS_CITY_NAME, True)
                obs.toggle_source_visibility(config.BOS_BRACKETS, config.BRACKETS_TEAM_NAME, True)

                config.time.sleep(config.SHOW_TIME)
                
                obs.toggle_source_visibility(config.BOS_BRACKETS, config.BRACKETS_CITY_NAME, False)
                obs.toggle_source_visibility(config.BOS_BRACKETS, config.BRACKETS_TEAM_NAME, False)

        config.time.sleep(config.SLEEP_TIME)
        obs.toggle_source_visibility(config.BOS_BRACKETS, config.BRACKETS_NAME, False)
    config.time.sleep(config.SLEEP_TIME)
    hide_all_overlays()

def loop_standings(phase):
    phase_of_ticker="./Text Files/Scroll Bar/Phase of Ticker.txt"
    rank_file = "./Text Files/Scroll Bar/Standings/Active Rank.txt"
    bracket_file = "./Text Files/Scroll Bar/Standings/Active Bracket.txt"
    ppb_file = "./Text Files/Scroll Bar/Standings/Active PPB.txt"
    team_file = "./Text Files/Scroll Bar/Standings/Active Team.txt"
    city_file = "./Text Files/Scroll Bar/Standings/Active City.txt"
    ppg_file = "./Text Files/Scroll Bar/Standings/Active PPG.txt"
    record_file = "./Text Files/Scroll Bar/Standings/Active Record.txt"

    hide_all_overlays()

    with open(phase_of_ticker, 'w') as file:
        file.write(phase +" Standings")

    standings = data.get_standings(phase)

    config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.PHASE_OF_TICKER, True)
    #config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_BRACKET, False)
    obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_RANK, False)
    obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_TEAM, False)
    obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_CITY, False)
    obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_RECORD, False)
    obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_PPB, False)
    obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_PPG, False)

    config.time.sleep(config.SLEEP_TIME)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_STANDINGS, True)

    for bracket in standings:
        with open(bracket_file, 'w') as dest:
            dest.write(bracket['name'])

        config.time.sleep(config.SLEEP_TIME)
        obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_BRACKET, True)

        for school in bracket['teams']:
            rank = int(school['rank'])
            team = str(school['team'])
            record = str(school['record'])
            ppg = float(school['ppg'])
            ppb = float(school['ppb'])
            city = school['city']

            with open(rank_file, 'w') as dest:
                dest.write(str(rank) + ".")
            with open(team_file, 'w') as dest:
                dest.write(team)
            with open(city_file, 'w') as dest:
                dest.write(city)
            with open(record_file, 'w') as dest:
                dest.write(record)
            with open(ppg_file, 'w') as dest:
                dest.write(str(ppg) + " PPG")
            with open(ppb_file, 'w') as dest:
                dest.write(str(ppb) + " PPB")

            config.time.sleep(config.SLEEP_TIME)

            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_RANK, True)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_TEAM, True)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_CITY, True)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_RECORD, True)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_PPB, True)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_PPG, True)

            config.time.sleep(config.SHOW_TIME + 2)

            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_RANK, False)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_TEAM, False)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_CITY, False)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_RECORD, False)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_PPB, False)
            obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_PPG, False)

        config.time.sleep(config.SLEEP_TIME)
        obs.toggle_source_visibility(config.BOS_STANDINGS, config.STANDINGS_BRACKET, False)
        config.time.sleep(config.SLEEP_TIME)

    hide_all_overlays()
    config.time.sleep(config.SLEEP_TIME)

def loop_results(round):
     
    phase_of_ticker="./Text Files/Scroll Bar/Phase of Ticker.txt"
    results_file_pre="./Text Files/Scroll Bar/Results/Rounds/Round " +str(round) +".txt"
    results_file_post="./Text Files/Scroll Bar/Results/Active/Active Results.txt"
    team1_file = "./Text Files/Scroll Bar/Results/Active/Active Team 1.txt"
    team1_city_file = "./Text Files/Scroll Bar/Results/Active/Active Team 1 City.txt"
    team1_score_file = "./Text Files/Scroll Bar/Results/Active/Active Team 1 Score.txt"
    team2_file = "./Text Files/Scroll Bar/Results/Active/Active Team 2.txt"
    team2_city_file = "./Text Files/Scroll Bar/Results/Active/Active Team 2 City.txt"
    team2_score_file = "./Text Files/Scroll Bar/Results/Active/Active Team 2 Score.txt"
    results_file = "./Text Files/Scroll Bar/Results/Active/Status.txt"
    bracket_file="./Text Files/Scroll Bar/Results/Active/Active Bracket.txt"

    phase = ""

    hide_all_overlays()

    with open(phase_of_ticker, 'w') as file:
        if str(round).find('.') != -1:
            phase = "Tiebreakers"
        elif int(round) >= 17:
            phase = "Final Rounds"
        else:
            phase = "Round " +str(round) +" Results"
        file.write(phase)

    with open(results_file_pre, 'r') as src, open(results_file_post, 'w') as dest:
        dest.write(src.read())

    matchups = data.get_results(round)

    config.time.sleep(config.SLEEP_TIME)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.PHASE_OF_TICKER, True)
    config.time.sleep(1)

    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_BRACKET, False)
    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM1, False)
    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM1_CITY, False)
    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM1_SCORE, False)
    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2, False)
    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2_CITY, False)
    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2_SCORE, False)
    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2_CITY, False)
    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_STATUS, False)
    obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_PROTEST_PENDING, False)
    config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_RESULTS, True)

    i = 0

    for matchup in matchups:
        
        with open(bracket_file, 'w') as file:
            file.write(matchup['bracket'])
        with open(team1_file, 'w') as file:
            file.write(matchup['team1'])
        with open(team1_city_file, 'w') as file:
            file.write(matchup['team1_city'])
        with open(team1_score_file, 'w') as file:
            file.write(str(matchup['team1_score']))
        with open(team2_file, 'w') as file:
            file.write(matchup['team2'])
        with open(team2_city_file, 'w') as file:
            file.write(matchup['team2_city'])
        with open(team2_score_file, 'w') as file:
            file.write(str(matchup['team2_score']))
        with open(results_file, 'w') as file:
            file.write(matchup['status'])

        config.time.sleep(config.SLEEP_TIME)

        next_bracket = ""

        if(i < len(matchups)-1):
            next_bracket = matchups[i+1]['bracket']

        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_BRACKET, True)
        config.time.sleep(config.SLEEP_TIME)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM1, True)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM1_CITY, True)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM1_SCORE, True)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2, True)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2_CITY, True)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2_SCORE, True)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2_CITY, True)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_STATUS, True)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_PROTEST_PENDING, matchup['pp'])

        config.time.sleep(config.SHOW_TIME + 2)
        i+=1

        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM1, False)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM1_CITY, False)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM1_SCORE, False)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2, False)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2_CITY, False)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2_SCORE, False)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_TEAM2_CITY, False)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_STATUS, False)
        obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_PROTEST_PENDING, False)

        if(matchup['bracket'] != next_bracket):
            config.time.sleep(config.SLEEP_TIME)
            obs.toggle_source_visibility(config.BOS_RESULTS, config.RESULTS_BRACKET, False)
            config.time.sleep(config.SLEEP_TIME)
    config.time.sleep(config.SLEEP_TIME)
    hide_all_overlays()
        
def loop_individual():
    phase_of_ticker="./Text Files/Scroll Bar/Phase of Ticker.txt"
    
    rank_file = "./Text Files/Scroll Bar/Individual Standings/Active/Active Rank.txt"
    player_file = "./Text Files/Scroll Bar/Individual Standings/Active/Active Name.txt"
    grade_file = "./Text Files/Scroll Bar/Individual Standings/Active/Active Year.txt"
    school_file = "./Text Files/Scroll Bar/Individual Standings/Active/Active School.txt"
    city_file = "./Text Files/Scroll Bar/Individual Standings/Active/Active City.txt"
    stats_file = "./Text Files/Scroll Bar/Individual Standings/Active/Active Stats.txt"
    powers_file = "./Text Files/Scroll Bar/Individual Standings/Active/Active Powers.txt"
    tossups_file = "./Text Files/Scroll Bar/Individual Standings/Active/Active Tossups.txt"
    tuh_file = "./Text Files/Scroll Bar/Individual Standings/Active/Active TUH.txt"

    hide_all_overlays()
    
    with open(phase_of_ticker, 'w') as file:
        file.write("Individual Standings")
    
    config.time.sleep(config.SLEEP_TIME)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.PHASE_OF_TICKER, True)
    config.time.sleep(1)

    obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_RANK, False)
    obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_PLAYER, False)
    obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_GRADE, False)
    obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_SCHOOL, False)
    obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_CITY, False)
    obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_STATS, False)
    obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_POWERS, False)
    obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_TOSSUPS, False)
    obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_TUH, False)

    config.time.sleep(config.SLEEP_TIME)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_INDIVIDUAL, True)
    config.time.sleep(config.SLEEP_TIME)

    players = data.get_players()

    for player in players:
        

        with open(rank_file, 'w') as file:
            file.write(str(player['rank']) +".")
        with open(player_file, 'w') as file:
            file.write(player['name'])
        with open(grade_file, 'w') as file:
            if player['grade']==12 or player['grade'] == "Senior":
                file.write("Senior")
            elif player['grade'] == 11 or player['grade'] == "Junior":
                file.write("Junior")
            elif player['grade'] == 10 or player['grade'] == "Sophomore":
                file.write("Sophomore")
            elif player['grade'] == 9 or player['grade'] == "Freshman":
                file.write("Freshman")
            else:
                file.write(str(player['grade']) +"th Grade")
        with open(school_file, 'w') as file:
            file.write(player['team'])
        with open(city_file, 'w') as file:
            file.write(player['city'])
        with open(stats_file, 'w') as file:
            file.write(player['stats'])
        with open(powers_file, 'w') as file:
             file.write(str(player['powers']) + " powers (20's)")
        with open(tossups_file, 'w') as file:
             file.write(str(player['tossups']) + " tossups (10's)")
        with open(tuh_file, 'w') as file:
             file.write(str(player['tuh']) + " tossups heard")
                   
        config.time.sleep(config.SLEEP_TIME)

        if(player['ppg'] <=0):
            break

        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_RANK, True)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_PLAYER, True)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_GRADE, True)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_SCHOOL, True)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_CITY, True)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_STATS, True)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_POWERS, True)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_TOSSUPS, True)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_TUH, True)

        config.time.sleep(config.SHOW_TIME * 2)
        
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_RANK, False)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_PLAYER, False)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_GRADE, False)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_SCHOOL, False)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_CITY, False)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_STATS, False)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_POWERS, False)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_TOSSUPS, False)
        obs.toggle_source_visibility(config.BOS_INDIVIDUAL, config.INDIVIDUAL_TUH, False)

    config.time.sleep(config.SLEEP_TIME)         
    hide_all_overlays() 
 
def loop_matchups(phase):

    phase_of_ticker="./Text Files/Scroll Bar/Phase of Ticker.txt"
    round_matchups = "./Text Files/Scroll Bar/Matchups/"
    team1_file="./Text Files/Scroll Bar/Matchups/Active Team 1.txt"
    team1_city_file="./Text Files/Scroll Bar/Matchups/Active Team 1 City.txt"
    team2_file="./Text Files/Scroll Bar/Matchups/Active Team 2.txt"
    team2_city_file="./Text Files/Scroll Bar/Matchups/Active Team 2 City.txt"
    active_bracket="./Text Files/Scroll Bar/Brackets/Bracket Name.txt"
    name=""
    roundNo = 0
    bracket_toggle = True

    #obs.move_source_X(config.OVERLAY, config.BRACKETS_NAME, 600)
    hide_all_overlays()

    if phase=="Prelims":
        with open(phase_of_ticker, 'w') as file:
                name="Round 1 Matchups"
                file.write(name)
                roundNo = 1
    elif phase=="Playoffs":
        with open(phase_of_ticker, 'w') as file:
                name="Round 6 Matchups"
                file.write(name)
                roundNo = 6
    elif phase=="Superplayoffs":
        with open(phase_of_ticker, 'w') as file:
                name="Round 11 Matchups"
                file.write(name)
                roundNo = 11

    lines = []

    with open(round_matchups + name + ".txt", 'r') as file:
            lines = file.readlines()

    config.time.sleep(config.SLEEP_TIME)
    matchups = data.get_matchups(roundNo)

    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.PHASE_OF_TICKER, True)
    config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_DASH, False)
    obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_1, False)
    obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_1_CITY, False)
    obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_2, False)
    obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_2_CITY, False)
    obs.toggle_source_visibility(config.BOS_MATCHUPS, config.BRACKETS_NAME, False)
    config.time.sleep(config.SLEEP_TIME)

    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_MATCHUPS, True)
    

    i = 0

    for matchup in matchups:
        team1 = matchup['team1']
        team2 = matchup['team2']

        team1_city = matchup['team1_city']
        team2_city = matchup['team2_city'] 

        with open(team1_file, 'w') as file:
            file.write(team1)
        with open(team1_city_file, 'w') as file:
             file.write(team1_city)
        with open(team2_file, 'w') as file:
            file.write(team2)
        with open(team2_city_file, 'w') as file:
             file.write(team2_city)
        with open(active_bracket, 'w') as bracket_file:
                bracket_file.write(matchup['bracket'])

        config.time.sleep(config.SLEEP_TIME)

        if bracket_toggle:
            obs.toggle_source_visibility(config.BOS_MATCHUPS, config.BRACKETS_NAME, True)
            config.time.sleep(config.SLEEP_TIME)
            bracket_toggle = False
        
        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_DASH, True)
        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_1, True)
        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_1_CITY, True)
        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_2, True)
        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_2_CITY, True)
        
        config.time.sleep(config.SHOW_TIME + 2)

        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_DASH, False)
        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_1, False)
        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_1_CITY, False)
        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_2, False)
        obs.toggle_source_visibility(config.BOS_MATCHUPS, config.MATCHUPS_TEAM_2_CITY, False)

        hide = False 

        if i+1 == len(matchups):
            hide = True

        if(hide or matchup['bracket'] != matchups[i+1]['bracket']):
            config.time.sleep(config.SLEEP_TIME)
            obs.toggle_source_visibility(config.BOS_MATCHUPS, config.BRACKETS_NAME, False)
            bracket_toggle = True

        if hide:
            break

        i+=1
    config.time.sleep(config.SLEEP_TIME)
    hide_all_overlays()

def loop_ticker():
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_MATCHUPS, False)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_BRACKETS, False)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_INDIVIDUAL, False)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_STANDINGS, False)
    obs.toggle_source_visibility(config.BOTTOM_OF_SCREEN, config.BOS_RESULTS, False)

    results_path="./Text Files/Scroll Bar/Results/Rounds/"

    try:
        old_phase = config.current_phase
        arrayNum=0
        current_round = 1

        while True:
            new_phase = config.current_phase

            if(new_phase != old_phase):
                print("Change configs")
                old_phase=config.current_phase
                arrayNum=0

                if(new_phase == config.TOURNAMENT_PHASE.BEFORE_PRELIMS or new_phase == config.TOURNAMENT_PHASE.PRELIMS or new_phase == config.TOURNAMENT_PHASE.POST_PRELIMS):
                    current_round == 1
                if(new_phase == config.TOURNAMENT_PHASE.PRE_PLAYOFFS or new_phase == config.TOURNAMENT_PHASE.PLAYOFFS or new_phase == config.TOURNAMENT_PHASE.POST_PLAYOFFS_D1):
                    current_round = 6
                else:
                    current_round = 11
            else:
                print("Keep Looping")
                arrayLen = 0
                if(new_phase == config.TOURNAMENT_PHASE.BEFORE_PRELIMS):
                    #Before Prelims Ticker and during Round 1
                    arrayLen = len(config.ticker_phases_before_prelims)

                    if config.ticker_phases_before_prelims[arrayNum] == "Brackets":
                        loop_brackets("Prelims")
                    elif config.ticker_phases_before_prelims[arrayNum] == "Matchups":
                        loop_matchups("Prelims")

                    arrayNum += 1
                elif(new_phase == config.TOURNAMENT_PHASE.PRELIMS):
                    #Prelims Ticker
                    arrayLen = len(config.ticker_phases_prelims)
                    if config.ticker_phases_prelims[arrayNum] == "Results":
                        if config.os.path.exists(results_path + "Round " + str(current_round) +".txt"):
                            loop_results(current_round)

                            if current_round == 5.2:
                                current_round = 1
                                arrayNum+=1
                            elif current_round == 5.1:
                                current_round = 5.2
                            elif current_round == 5:
                                current_round = 5.1
                            else:
                                current_round+=1
                        else:
                            current_round = config.start_round
                            arrayNum+=1

                    elif config.ticker_phases_prelims[arrayNum] == "Standings":
                        if config.os.path.exists(results_path + "Round 2.txt"):
                            loop_standings("Prelims")
                        arrayNum+=1
                    elif config.ticker_phases_prelims[arrayNum] == "Individual Standings":
                        if config.os.path.exists("./Text Files/Scroll Bar/Individual Standings/Individual Standings.txt"):
                            loop_individual()
                        arrayNum+=1
                    
                elif(new_phase == config.TOURNAMENT_PHASE.POST_PRELIMS):
                    #Post-Prelim Ticker
                    if config.ticker_phases_post_prelims[arrayNum] == "Results":
                        if config.os.path.exists(results_path + "Round " + str(current_round) +".txt"):
                            loop_results(current_round)

                            if current_round == 5.2:
                                current_round = 1
                                arrayNum+=1
                            elif current_round == 5.1:
                                current_round = 5.2
                            elif current_round == 5:
                                current_round = 5.1
                            else:
                                current_round+=1
                        else:
                            current_round = config.start_round
                            arrayNum+=1

                    elif config.ticker_phases_post_prelims[arrayNum] == "Standings":
                        if config.os.path.exists(results_path + "Round 2.txt"):
                            loop_standings("Prelims")
                        arrayNum+=1
                    elif config.ticker_phases_post_prelims[arrayNum] == "Individual Standings":
                        if config.os.path.exists("./Text Files/Scroll Bar/Individual Standings/Individual Standings.txt"):
                            loop_individual()
                        arrayNum+=1
                    arrayLen = len(config.ticker_phases_post_prelims)
                elif(new_phase == config.TOURNAMENT_PHASE.PRE_PLAYOFFS):
                    #Pre-playoff Ticker
                    arrayLen = len(config.ticker_phases_pre_playoffs)

                    if config.ticker_phases_pre_playoffs[arrayNum] == "Individual Standings":
                        if config.os.path.exists("./Text Files/Scroll Bar/Individual Standings/Individual Standings.txt"):
                            loop_individual()
                    if config.ticker_phases_pre_playoffs[arrayNum] == "Brackets":
                        loop_brackets("Playoffs")
                    elif config.ticker_phases_pre_playoffs[arrayNum] == "Matchups":
                        loop_matchups("Playoffs")
                    arrayNum+=1

                elif(new_phase == config.TOURNAMENT_PHASE.PLAYOFFS):
                    #Playoff Ticker
                    arrayLen = len(config.ticker_phases_playoffs)

                    if config.ticker_phases_playoffs[arrayNum] == "Results":
                        if config.os.path.exists(results_path + "Round " + str(current_round) +".txt"):
                            loop_results(current_round)

                            if current_round == 12.2:
                                current_round = 6
                                arrayNum+=1
                            elif current_round == 12.1:
                                current_round = 12.2
                            elif current_round == 12:
                                current_round = 12.1
                            else:
                                current_round+=1
                        else:
                            current_round = config.start_round
                            arrayNum+=1

                    elif config.ticker_phases_playoffs[arrayNum] == "Standings":
                        if config.os.path.exists(results_path + "Round 2.txt"):
                            loop_standings("Prelims")
                        arrayNum+=1
                elif(new_phase == config.TOURNAMENT_PHASE.POST_PLAYOFFS_D1):
                    #Post-Playoffs Ticker
                    arrayLen = len(config.ticker_phases_post_playoffs)

                    if config.ticker_phases_post_playoffs[arrayNum] == "Results":
                        if config.os.path.exists(results_path + "Round " + str(current_round) +".txt"):
                            loop_results(current_round)

                            if current_round == 12.2:
                                current_round = 6
                                arrayNum+=1
                            elif current_round == 12.1:
                                current_round = 12.2
                            elif current_round == 12:
                                current_round = 12.1
                            else:
                                current_round+=1
                        else:
                            current_round = config.start_round
                            arrayNum+=1

                    elif config.ticker_phases_post_playoffs[arrayNum] == "Standings":
                        if config.os.path.exists(results_path + "Round 7.txt"):
                            loop_standings("Prelims")
                        arrayNum+=1
                elif(new_phase == config.TOURNAMENT_PHASE.PRE_SUPERPLAYOFFS_D2):
                    #Pre-Superplayoffs Ticker
                    arrayLen = len(config.ticker_phases_pre_superplayoffs)

                    if config.ticker_phases_pre_superplayoffs[arrayNum] == "Brackets":
                        loop_brackets("Superplayoffs")
                    elif config.ticker_phases_pre_superplayoffs[arrayNum] == "Matchups":
                        loop_matchups("Superplayoffs")
                else:
                    #D2 Ticker
                    arrayLen = len(config.ticker_phases_rest_of_day)

                    if config.ticker_phases_rest_of_day[arrayNum] == "Results":
                        if config.os.path.exists(results_path + "Round " + str(current_round) +".txt"):
                            loop_results(current_round)

                            if current_round == 20:
                                current_round = 11
                                arrayNum+=1
                            else:
                                current_round+=1
                        else:
                            current_round = config.start_round
                            arrayNum+=1

                    elif config.ticker_phases_rest_of_day[arrayNum] == "Standings":
                        if config.os.path.exists(results_path + "Round 12.txt"):
                            loop_standings("Prelims")
                        arrayNum+=1
                if(arrayNum == arrayLen):
                    arrayNum = 0
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    config.init()
    '''
    
    loop_brackets("Prelims")
    loop_brackets("Playoffs")
    loop_brackets("Superplayoffs")
    
    loop_standings("Prelims")
    loop_standings("Playoffs")
    loop_standings("Superplayoffs")
    
    loop_matchups("Prelims")
    loop_matchups("Playoffs")
    loop_matchups("Superplayoffs")
    '''
    loop_individual()
    
    i = 1
    while i <= 5:
        loop_results(i)
        i+=1
    
    loop_results(5.1)
    loop_results(5.2)

    i = 6
    while i <= 10:
        loop_results(i)
        i+=1
    loop_results(10.1)
    loop_results(10.2)

    i = 11
    while i <= 18:
        loop_results(i)
        i+=1
    