import config
import cornerstone

#Get Data for ticker and full screen stats

def get_bracket_list(phase):
    brackets_src_path="./Text Files/Scroll Bar/Brackets/"+phase+"/"

    brackets = sorted([file for file in config.os.listdir(brackets_src_path) if file.endswith(".txt")])
    brackets = [bracket.removesuffix(".txt") for bracket in brackets]

    if phase == "Superplayoffs":
        brackets = sorted(brackets, key=custom_sort)
    return brackets

def custom_sort(item):
    if item == "Championship":
        return (0, 0)  # Place "Championship" first
    else:
        start, _ = map(int, item.split('-'))
        return (1, start)  # Sort numerically based on the start of the range

def get_brackets_with_teams(phase):
    path = "./Data/Brackets/" + phase + ".json"
    
    if config.os.path.exists(path):
        brackets = None
        with open(path, 'r') as f:
            brackets = config.json.load(f)
        
        return brackets
    
    
    if config.LIVE and cornerstone.ping():
        if cornerstone.get_no_bracket_numbers()[phase] > 0:
            return {}

        phase_key = ""
        brackets = {}

        if phase == "Prelims":
            phase_key = 'prelim_pool'
        elif phase == "Playoffs":
            phase_key = 'playoff_pool'
        elif phase == "Superplayoffs":
            phase_key = 'superplayoff_pool'

        team_list = cornerstone.getTeams(config.cornerstone_tournamentID)

        for entry in team_list:
            team = entry['name']
            pool = entry[phase_key]
            city = get_city(team)

            if pool not in brackets:
                brackets[pool] = []

            brackets[pool].append({'team': team, 'city': city})

        result = [{"bracket": pool, "teams": sorted(participants, key=lambda x: x["team"])} for pool, participants in sorted(brackets.items())]

        return result
    else:
        brackets = get_bracket_list(phase)

        ret_list = []

        for bracket in brackets:
            teams = get_teams_in_bracket(phase, bracket)
            
            temp = {
                'bracket': bracket,
                'teams': teams
            }
            
            ret_list.append(temp)

        return ret_list

def get_teams_in_bracket(phase, bracket):

    brackets_src_path="./Text Files/Scroll Bar/Brackets/"+phase+"/"+bracket+".txt"

    ret = []
    lines = []

    if config.os.path.isfile(brackets_src_path):
            if brackets_src_path.endswith(".txt"):
                with open(brackets_src_path, 'r') as src:
                    lines = src.readlines()

    for team in lines:
        high_school = None
        city = None

        if(phase == "Prelims"):
            high_school, city = team.split(" (")
            city = city.strip().rstrip(")")
        else:
            high_school = team.strip()
            city = get_city(high_school)

        li = {'team':high_school, 'city':city}
        ret.append(li)
    return ret

def get_city(team):
    city = ""
    brackets_folder = "./Text Files/Scroll Bar/Brackets/Prelims" 

    for filename in config.os.listdir(brackets_folder):
        # Get the full file path
        file_path = config.os.path.join(brackets_folder, filename)

        # Check if it's a file (not a directory)
        if config.os.path.isfile(file_path):
            if filename.endswith(".txt"):
                with open(file_path, 'r') as src:
                    for line in src:
                        team_name = line.split(" (")[0]  # Everything before " ("
                        city_name = line.split(" (")[1].strip().rstrip(")")

                        if(team == team_name):
                            return city_name
                            break

    return city

def get_players():
    results_file_pre="./Text Files/Scroll Bar/Individual Standings/Individual Standings.txt"
    results_file_post="./Text Files/Scroll Bar/Individual Standings/Active/Active Standings.txt"
    lines = []
    ret = []
    i = 1

    if config.LIVE:
        orig_players = config.harry.get_individual_scoring()
        current_rank = 1
        

        for orig_player in orig_players:            
            
            city = get_city(orig_player["team"])

            player = {
                'rank':current_rank,
                'name':orig_player["name"],
                'grade':orig_player["grade"],
                'team':orig_player["team"],
                'city':city,
                'ppg':orig_player["ppg"],
                'tuh':orig_player["tuh"],
                'powers':orig_player["powers"],
                'tossups':orig_player["tus"],
                'stats':str(orig_player["ppg"]) + " PPG"
            }

            current_rank+=1

            ret.append(player)
    else:
        with open(results_file_pre, 'r') as src:
            #while i <= 30:
            lines.append(src.read())
            i+=1
        
        lines = lines[0].split('\n')[:30]

        with open(results_file_post, 'w') as dest:
            dest.writelines(lines)

        for line in lines:
            parts = line.strip().split('\t')  # Splits based on tabs
                
            # Initialize variables to store the name, grade, team, PPG, etc.
            name_parts = []
            grade = None
            team = None
            ppg = None
            tossups = None
            powers = None
            tuh = None
                
            # The first item in the line is always the rank
            rank = int(parts[0])

            for i, part in enumerate(parts[1:], 1):
                if part.isdigit():
                    grade = int(part)
                    name_parts = parts[1:i]
                    team = parts[i + 1]
                    
                    ppg = float(parts[-1])
                    tuh = int(parts[-3])
                    tossups = int(parts[-4])
                    powers = int(parts[-5])
                    break

            # Join the name parts (in case the name has 2 or 3 words)
            name = " ".join(name_parts)

            city = get_city(team) 
            stats=str(ppg) + " PPG"

            player = {
                'rank':rank,
                'name':name,
                'grade':grade,
                'team':team,
                'city':city,
                'ppg':ppg,
                'tuh':tuh,
                'powers':powers,
                'tossups':tossups,
                'stats':stats
            }

            ret.append(player)
    return ret

def get_results(round):
    lines = []
    round_file="./Text Files/Scroll Bar/Results/Rounds/Round " +str(round) +".txt"

    with open(round_file, 'r') as file:
        lines = file.readlines()

    lines = sorted(lines)

    matches = []

    for matchup in lines:
        bracket, rest = matchup.split(":", 1)
        rest = rest.strip()

        protest_pending = False

        # Extract the teams and scores
        if rest.strip().endswith("PP"):
            rest = rest.removesuffix("PP").strip()
            protest_pending = True
        else:
            rest.strip()
            protest_pending = False

        team1, team2_section = rest.split("vs.", 1)
        team1 = team1.strip()
        team1_city = get_city(team1)

        team2_left, rest = team2_section.split("-")
        team2 = team2_left.split(" ")[:-1]
        team2 = ' '.join(team2).strip()
        team2_city = get_city(team2)
        team1_score = team2_left.split(" ")[-1]

        team2_score, status = rest.split(" ", 1)

        match = {
            'round':round,
            'bracket':bracket.strip(),
            'pp':protest_pending,
            'team1':team1,
            'team1_city':team1_city,
            'team1_score':team1_score,
            'team2':team2,
            'team2_city':team2_city,
            'team2_score':team2_score,
            'status':status
        }

        matches.append(match)

    return matches

def get_standings(phase):
    phase_files="./Text Files/Scroll Bar/Standings/" + phase + "/"

    files = sorted([file for file in config.os.listdir(phase_files) if file.endswith('.txt') and config.os.path.isfile(config.os.path.join(phase_files, file))])

    standings = []

    for file in files:

        lines = []

        bracket_file = "./Text Files/Scroll Bar/Standings/" + phase + "/" +file

        with open(bracket_file, 'r') as dest:
            lines = dest.readlines()

        bracket_name = str(file).removesuffix('.txt')

        teams = []

        for item in lines:
            parts = item.strip().removesuffix('\n').split('\t')

            rank = int(parts[0])
            team = str(parts[1])
            record = str(parts[4] + "-" + parts[5])
            ppg = float(parts[7])
            ppb = float(parts[-1])
            city = get_city(team)

            team = {
                'rank':rank,
                'team':team,
                'city':city,
                'record':record,
                'ppg':ppg,
                'ppb':ppb,
                'tb_flag':False,
                'pp_flag':False,
                'adv_flag':False
            }

            teams.append(team)

        bracket = {
            'name':bracket_name,
            'teams':teams
        }

        standings.append(bracket)
    
    if phase == "Superplayoffs":
        desired_order = ['Championship', '9-16', '17-24', '25-28', '29-32', '33-36', '37-40', '41-44', '45-48',
                         '49-52', '53-56', '57-60', '61-64', '65-68', '69-72', '73-76', '77-80', '81-84']
        
        standings.sort(key=lambda bracket: desired_order.index(bracket['name']))

    return standings

def get_matchups(round):
    path = "./Data/Matchups/"

    if config.os.path.exists(path + "Round " +str(round) + ".json"):
        loaded_dict = None
        with open(path + "Round " +str(round) + ".json", 'r') as f:
            loaded_dict = config.json.load(f)
        
        return loaded_dict

    if config.LIVE and cornerstone.ping():
        phase = "Prelims"

        if round >= 11:
            phase == "Superplayoffs"
        elif round >= 6:
            phase == "Playoffs"


        if cornerstone.get_no_bracket_numbers()[phase] > 0:
            return {}
        
        initial_schedules = cornerstone.getTeamSchedules(config.cornerstone_tournamentID)

        if initial_schedules == []:
            return {}
        
        round_schedules = []
        brackets = get_brackets_with_teams(phase)

        for matchup in initial_schedules:
            item = {}

            if matchup['round'] == round:
                team1 = matchup['team_name']
                team2 = matchup['opponent']
                city1 = get_city(team1)
                city2 = get_city(team2)
                bracket = ""

                found = False
                for bracket in brackets:
                    for team in bracket['teams']:
                        if team['team'] == team1:
                            bracket = bracket['bracket']
                            found = True
                            break
                    if found:
                        break

                item = {
                    'round':round,
                    'team1':team1,
                    'team2':team2,
                    'team1_city':city1,
                    'team2_city':city2,
                    'bracket':bracket
                }

                round_schedules.append(item)
            
        
        round_schedules = sorted(round_schedules, key=lambda x: x['bracket'])

        seen = set()
        deduplicated_data = []

        for match in round_schedules:
            team_pair = frozenset([match["team1"], match["team2"]])  # Order-independent key
            if team_pair not in seen:
                seen.add(team_pair)
                deduplicated_data.append(match)  # Preserve the first occurrence

        return deduplicated_data
    else:
        results = get_results(round)

        matchups = []

        for result in results:
            matchup = {
                'round':round,
                'team1':result['team1'],
                'team2':result['team2'],
                'team1_city':result['team1_city'],
                'team2_city':result['team2_city'],
                'bracket':result['bracket']
            }

            matchups.append(matchup)

        return matchups

def get_matchups_all():
    path = "./Data/Matchups/"
    for i in range(1, 17):
        if not config.os.path.exists(path + "Round " +str(i) + ".json"):
            round_matchups = get_matchups(i)

            if not round_matchups == []:
                with open(path + "Round " +str(i) + ".json", 'w') as f:
                    config.json.dump(round_matchups, f)

def get_brackets_all():
    phases = ["Prelims", "Playoffs", "Superplayoffs"]
    path = "./Data/Brackets/"

    for phase in phases:
        if not config.os.path.exists(path + phase +".json"):
            brackets = get_brackets_with_teams(phase)

            if not brackets == []:
                with open(path + phase +".json", 'w') as f:
                    config.json.dump(brackets, f)

if __name__ == "__main__":
    config.init()
    #print(get_matches(1))
    #print(get_brackets_with_teams("Preli"))
    #get_brackets_all()
    #get_matchups_all()
    #print(get_results(1))
    #print(get_bracket_list("Playoffs"))
    print(get_brackets_with_teams("Superplayoffs"))
    #print(get_players())