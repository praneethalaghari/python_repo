from pycricbuzz import Cricbuzz
import json
import time
from win10toast import ToastNotifier 

c = Cricbuzz()


print(help(Cricbuzz))

#print(json.dumps(c.matches(),indent = 4))



match_id_list = []

for i in c.matches():
    match_id_list.append(i['id'])
    
    match_info = c.matchinfo(i['id'])
    Team_A = match_info['team1']['name']
    Team_B = match_info['team2']['name']
 
    print(i['id'] + '\t' + ' --- ' + '\t' + Team_A + ' vs ' + Team_B + '\t' + ' --- ' + '\t' + i['srs'])



def is_ball_bowled(overs):

    over_count,ball_count = str(overs).split('.') 
   

    live_score_update = c.livescore(match_id)

    live_overs = float(live_score_update['batting']['score'][0]['overs'])
    live_score = live_score_update['batting']['score'][0]['runs']
    live_over_count,live_ball_count = str(live_overs).split('.')


    if over_count != live_over_count or ball_count != live_ball_count:
        return True,live_overs,live_score
    else:
        return None,None,None


while(True): 


    match_id = input("ENTER MATCH ID :")


    if match_id in match_id_list:
        livescore = c.livescore(match_id)
        if livescore:
            overs = float(livescore['batting']['score'][0]['overs'])
            while(True):
                ball_bowled,live_overs,live_score = is_ball_bowled(overs)
                if(ball_bowled):
                    toaster = ToastNotifier()
                    toaster.show_toast("SCORE UPDATE",str(live_overs)+'-'+str(live_score))

                    print(str(live_overs) + '-' + str(live_score))
                    overs = live_overs

        else:
            print("Stay tuned.. Match is yet to begin!!!")
        break
    else:
        print("Please enter correct Id")


