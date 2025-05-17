import config

#https://cornerstone-scheduler-fvd6c3agbccxd7f5.eastus2-01.azurewebsites.net/dashboard
#username = beta2
#password = 23N3U2pT

def getTournament(tournamentID):
    try:
        send_url = config.cornerstone_url + "tournament/" +str(tournamentID)
        headers = {"X-API-Key": config.cornerstone_api_key}

        response = config.requests.get(url=send_url, headers=headers)
        json_data = response.json()

        if json_data == []:
            return -1
        return json_data

    except Exception as e:
        print(f"Error {e}")

def getTeams(tournamentID):
    try:
        send_url = config.cornerstone_url + "teams/" +str(tournamentID)
        headers = {"X-API-Key": config.cornerstone_api_key}

        response = config.requests.get(url=send_url, headers=headers)
        json_data = response.json()
        return json_data

    except Exception as e:
        print(f"Error {e}")
        return -1

def getPools(tournamentID):
    try:
        send_url = config.cornerstone_url + "pools/" +str(tournamentID)
        headers = {"X-API-Key": config.cornerstone_api_key}

        response = config.requests.get(url=send_url, headers=headers)
        json_data = response.json()
        return json_data

    except Exception as e:
        print(f"Error {e}")
        return -1

def getRooms(tournamentID):
    try:
        send_url = config.cornerstone_url + "rooms/" +str(tournamentID)
        headers = {"X-API-Key": config.cornerstone_api_key}

        response = config.requests.get(url=send_url, headers=headers)
        json_data = response.json()
        return json_data

    except Exception as e:
        print(f"Error {e}")
        return -1

def getTeamSchedules(tournamentID):
    try:
        send_url = config.cornerstone_url + "team_schedules/" +str(tournamentID)
        headers = {"X-API-Key": config.cornerstone_api_key}

        response = config.requests.get(url=send_url, headers=headers)
        json_data = response.json()
        return json_data

    except Exception as e:
        print(f"Error {e}")
        return -1

def getRoomSchedules(tournamentID):
    try:
        send_url = config.cornerstone_url + "room_schedules/" +str(tournamentID)
        headers = {"X-API-Key": config.cornerstone_api_key}

        response = config.requests.get(url=send_url, headers=headers)
        json_data = response.json()
        return json_data

    except Exception as e:
        print(f"Error {e}")
        return -1

def get_no_bracket_numbers():
    prelims = 0
    playoffs = 0
    superplayoffs = 0

    teams = getTeams(config.cornerstone_tournamentID)

    for team in teams:
        if team['prelim_pool'] == None:
            prelims += 1
        if team['playoff_pool'] == None:
            playoffs +=1
        if team['superplayoff_pool'] == None:
            superplayoffs += 1

    ret = {
        'Prelims':prelims,
        'Playoffs':playoffs,
        'Superplayoffs':superplayoffs
    }

    return ret

def ping():
    if getTournament(config.cornerstone_tournamentID) == -1:
        return False
    return True

if __name__ == "__main__":
    print(getTournament(config.cornerstone_tournamentID))
    print(getTeams(config.cornerstone_tournamentID))
    print(getPools(config.cornerstone_tournamentID))
    print(getRooms(config.cornerstone_tournamentID))
    print(getTeamSchedules(config.cornerstone_tournamentID))
    print(getRoomSchedules(config.cornerstone_tournamentID))

    #print(get_no_bracket_numbers())