import config

def get_game_file_list(roundNo):

    response = config.requests.get(config.GAMES_JSON_LINKS)
    soup = config.BeautifulSoup(response.text, 'html.parser')  

    if not isinstance(roundNo, int):
        roundNo = int(roundNo * 10)

    # Find all links and filter by names starting with '1_' and ending with '.json'
    json_files = [
        link.get('href') for link in soup.find_all('a')
        if link.get('href', '').startswith(str(roundNo) + '_') and link.get('href').endswith('.json')
    ]

    return json_files

def download_json_files(roundNo):
    file_names = get_game_file_list(roundNo)

    download_path = "./Data/Games/Raw/Round " + str(roundNo) + "/"
    config.os.makedirs(download_path, exist_ok=True)

    for file in file_names:
        url = config.GAMES_JSON_LINKS + file
        file_content = config.requests.get(url).content

        file_path = config.os.path.join(download_path, file)
        with open(file_path, 'wb') as f:
            f.write(file_content)

def get_raw_rosters():
    rosters_file = "./Data/Rosters/rosters.json"

    people = []

    if not config.os.path.exists(rosters_file):
        raw_rosters_file = "./Data/Rosters/combined.yft"
        
        with open(raw_rosters_file, 'r') as f:
            lines = f.readlines()

        json_line = config.json.loads(lines[4].strip())

        for team in json_line:

            for name,info in team['roster'].items():

                player_grade = ""

                if info['year'] == "12":
                    player_grade = "Senior"
                elif info['year'] == "11":
                    player_grade = "Junior"
                elif info['year'] == "10":
                    player_grade = "Sophomore"
                elif info['year'] == "9":
                    player_grade = "Freshman"
                elif info['year'] == "":
                    player_grade = ""
                else:
                    player_grade = str(info['year']) + "th Grade"

                new_player = {
                    'name':name,
                    'team':team['teamName'],
                    'grade':player_grade,
                    'tuh':0,
                    'powers':0,
                    'tus':0,
                    'points':0,
                    'ppg':0
                }

                people.append(new_player)

        with open(rosters_file, 'w') as f:
            config.json.dump(people, f, indent=4)
        
    else:
        with open(rosters_file, 'r') as f:
            people = config.json.load(f)
    
    return people

def get_individual_scoring():
    players = get_raw_rosters()

    for current_round in range(config.PRELIMS_START_ROUND, config.PRELIMS_END_ROUND + 1):
        download_json_files(current_round)
        file_list = get_game_file_list(current_round)

        for game in file_list:
            game_path = "./Data/Games/Raw/Round " + str(current_round) + "/" + game

            with open(game_path, 'r') as f:
                json_game = config.json.load(f)

            team1 = game.removesuffix('.json').split("_")[1].replace('-',' ')
            team2 = game.removesuffix('.json').split("_")[2].replace('-',' ')
            match_players_t1 = json_game["match_teams"][0]["match_players"]
            match_players_t2 = json_game["match_teams"][1]["match_players"]

            if len(json_game["match_questions"]) >= 20:
                for player in players:
                    team1_match = (team1 == player['team'])
                    team2_match = (team2 == player['team'])
                    
                    if team1_match:

                        for match_t1_player in match_players_t1:
                            player_match = (match_t1_player["player"]["name"] == player["name"])
                            if player_match:
                                player["tuh"] = player["tuh"] + match_t1_player["tossups_heard"]

                                for answer_type in match_t1_player["answer_counts"]:
                                    if answer_type["answer"]["value"] == 20:
                                        player["powers"] = player["powers"] + answer_type["number"]
                                        player["points"] = player["points"] + (20 * answer_type["number"])
                                    if answer_type["answer"]["value"] == 10:
                                        player["tus"] = player["tus"] + answer_type["number"]
                                        player["points"] = player["points"] + (10 * answer_type["number"])

                    if team2_match:
                        for match_t2_player in match_players_t2:
                            player_match = (match_t2_player["player"]["name"] == player["name"])
                            if player_match:
                                player["tuh"] = player["tuh"] + match_t2_player["tossups_heard"]

                                for answer_type in match_t2_player["answer_counts"]:
                                    if answer_type["answer"]["value"] == 20:
                                        player["powers"] = player["powers"] + answer_type["number"]
                                        player["points"] = player["points"] + (20 * answer_type["number"])
                                    if answer_type["answer"]["value"] == 10:
                                        player["tus"] = player["tus"] + answer_type["number"]
                                        player["points"] = player["points"] + (10 * answer_type["number"])

    
    for player in players:
        if player["tuh"] == 0:
            player["ppg"] = 0
        else:
            player["ppg"] = round(player["points"] * 20 / player["tuh"], 1)

    players = sorted(players, key=lambda x: (x['ppg'], x['tuh'], x['powers']), reverse=True)
    
    return players[:30]
                                



if __name__ == "__main__":
    test = get_individual_scoring()
    #print(test)