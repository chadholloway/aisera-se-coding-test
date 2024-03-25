import requests
import json
import sys

team='144'

def getTeamInfo(teamNo):
    url = "https://mlb-data.p.rapidapi.com/json/named.team_all_season.bam"

    querystring = {"season":"'2017'","all_star_sw":"'N'","sort_order":"name_asc"}

    headers = {
	    "X-RapidAPI-Key": "f473bb06e8msh39f4e09090dffeep12d875jsn44eb445b0166",
	    "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    teamjson = response.json()

    for single_item in teamjson["team_all_season"]["queryResults"]["row"]:
        id=single_item["team_id"]
        if(id==teamNo):
            teamname=single_item["mlb_org_brief"]

    return teamname

args=len(sys.argv)
if(args==1):
    print("ERROR:  you must supply a file name")
    exit(997)

filename=sys.argv[1]

outputFile = open(filename,"w")


url = "https://mlb-data.p.rapidapi.com/json/named.roster_40.bam"

querystring = {"team_id":"'144'"}

headers = {
	"X-RapidAPI-Key": "f473bb06e8msh39f4e09090dffeep12d875jsn44eb445b0166",
	"X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

jsondata=response.json()
#print(jsondata["roster_40"]["queryResults"]["row"]["name_full"])
for single_item in jsondata["roster_40"]["queryResults"]["row"]:
    player=single_item["name_full"].ljust(24)
    number=single_item["jersey_number"].rjust(2)
    outputFile.write(player + ' ' + number + '\n')
    print(player,number)


teamName=getTeamInfo(team)

print("Roster for " + teamName + " Complete")
outputFile.write("Roster for " + teamName + " Complete\n")

outputFile.close()
