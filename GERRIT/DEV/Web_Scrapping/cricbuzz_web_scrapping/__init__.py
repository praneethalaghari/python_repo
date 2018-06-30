from bs4 import BeautifulSoup
import requests

base_url = "http://www.cricbuzz.com/live-cricket-scorecard/19956/ind-vs-afg-only-test-afghanistan-tour-of-india-2018"
webpage_response = requests.get(base_url)

webpage_content = BeautifulSoup(webpage_response.text, "html.parser")

'''Below commented lines are to copy the single line inspect source code t
 prettified source code just for better readability'''
# with open('cricbuzz_prettified','w+') as source_code:
#  cool = webpage_content.prettify()

#   for line in cool:
#    if(ord(line)<127):
#        source_code.write(line)

matches_today = []

todays_matches = webpage_content.find_all(class_='cb-mtch-all')
for today_match in todays_matches:
    to_ma = today_match.find(class_='cb-mm-mtch-tm')
    for tm in to_ma:
        matches_today.append(tm)

#print("Matches today are :", matches_today)

title = webpage_content.find_all('title')
for titl in title:
    print(titl.text)

todays_match_result = webpage_content.find(class_='cb-col cb-scrcrd-status cb-col-100 cb-text-complete')
#print("Match Result :", todays_match_result.text)


##################################### FIRST INNINGS (BATSMAN STATS) ######################################################

name_of_batsman_1st_inn = []
score_of_batsman_1st_inn = []
balls_of_batsman_1st_inn = []
fours_of_batsman_1st_inn = []
sixes_of_batsman_1st_inn = []
strike_rate_of_batsman_1st_inn = []


batsmen_tmp = webpage_content.find_all('div', {"id": "innings_1"})
for spd in batsmen_tmp:
    batsmen = spd.find_all(class_="cb-col cb-col-100 cb-scrd-itms")
    for itr_batsmen in batsmen:
        i = 0
        for ita in itr_batsmen.find_all('a',href=True):
            name_of_batsman_1st_inn.append(ita.text)
        batsmen_score = itr_batsmen.find_all(class_='cb-col cb-col-8 text-right text-bold')
        for items in batsmen_score:
            score_of_batsman_1st_inn.append(items.text)
        batsmen_data = itr_batsmen.find_all(class_='cb-col cb-col-8 text-right')
        for items in batsmen_data:
            #data_of_batsman_1st_inn.append(items.text)
            if i%4 == 0:
                balls_of_batsman_1st_inn.append(items.text)
            elif i%4 ==1:
                fours_of_batsman_1st_inn.append(items.text)
            elif i%4 ==2:
                sixes_of_batsman_1st_inn.append(items.text)
            elif i%4 ==3:
                strike_rate_of_batsman_1st_inn.append(items.text)
            i += 1

'''
print(name_of_batsman_1st_inn)
print(score_of_batsman_1st_inn)
print(balls_of_batsman_1st_inn)
print(fours_of_batsman_1st_inn)
print(sixes_of_batsman_1st_inn)
print(strike_rate_of_batsman_1st_inn)
'''

first_inn_scorecard = {}

for i,j,k,l,m,n in zip(name_of_batsman_1st_inn,score_of_batsman_1st_inn,balls_of_batsman_1st_inn,fours_of_batsman_1st_inn,sixes_of_batsman_1st_inn,strike_rate_of_batsman_1st_inn):
    first_inn_scorecard[i] = [j,k,l,m,n]


'''
bowler = webpage_content.find_all('div', id="innings_1", class_='cb-col cb-col-100 cb-scrd-itms')
for itr_bowler in bowler:
    bwlr = itr_bowler.find('a')
    print(bwlr.text)
    bowler_data = itr_bowler.find_all(class_='cb-col cb-col-8 text-right')
    for items in bowler_data:
        print(items)
'''


##################################### SECOND INNINGS (BATSMAN STATS)######################################################


name_of_batsman_2nd_inn = []
score_of_batsman_2nd_inn = []
balls_of_batsman_2nd_inn = []
fours_of_batsman_2nd_inn = []
sixes_of_batsman_2nd_inn = []
strike_rate_of_batsman_2nd_inn = []

batsmen_tmp = webpage_content.find_all('div', {"id": "innings_2"})
for spd in batsmen_tmp:
    batsmen = spd.find_all(class_="cb-col cb-col-100 cb-scrd-itms")
    for itr_batsmen in batsmen:
        i = 0
        for ita in itr_batsmen.find_all('a',href=True):
            name_of_batsman_2nd_inn.append(ita.text)
        batsmen_score = itr_batsmen.find_all(class_='cb-col cb-col-8 text-right text-bold')
        for items in batsmen_score:
            score_of_batsman_2nd_inn.append(items.text)
        batsmen_data = itr_batsmen.find_all(class_='cb-col cb-col-8 text-right')
        for items in batsmen_data:
            #data_of_batsman_2nd_inn.append(items.text)
            if i%4 == 0:
                balls_of_batsman_2nd_inn.append(items.text)
            elif i%4 ==1:
                fours_of_batsman_2nd_inn.append(items.text)
            elif i%4 ==2:
                sixes_of_batsman_2nd_inn.append(items.text)
            elif i%4 ==3:
                strike_rate_of_batsman_2nd_inn.append(items.text)
            i += 1
'''
print(name_of_batsman_2nd_inn)
print(score_of_batsman_2nd_inn)
print(balls_of_batsman_2nd_inn)
print(fours_of_batsman_2nd_inn)
print(sixes_of_batsman_2nd_inn)
print(strike_rate_of_batsman_2nd_inn)
'''

#for i,j,k,l,m,n in zip(name_of_batsman_2nd_inn,score_of_batsman_2nd_inn,balls_of_batsman_2nd_inn,fours_of_batsman_2nd_inn,sixes_of_batsman_2nd_inn,strike_rate_of_batsman_2nd_inn):
#    print(i,j,k,l,m,n)


##################################### FIRST INNINGS (BOWLER STATS)######################################################

name_of_bowler_1st_inn = []
overs_of_bowler_1st_inn = []
maidens_of_bowler_1st_inn = []
runs_of_bowler_1st_inn = []
wickets_of_bowler_1st_inn = []
no_balls_of_bowler_1st_inn = []
wides_of_bowler_1st_inn = []
economy_of_bowler_1st_inn = []

bowler_tmp = webpage_content.find_all('div',{'id':'innings_1'})
for bowl in bowler_tmp:
    bowler = bowl.find_all(class_='cb-col cb-col-100 cb-ltst-wgt-hdr')
    for itr in bowler:
        bowler_1 = itr.find_all(class_='cb-col cb-col-100 cb-scrd-itms ')
        for itr_1 in bowler_1:
            i = 0
            j = 0
            bowler_2 = itr_1.find_all(class_='cb-text-link')
            for itr_2 in bowler_2:
                name_of_bowler_1st_inn.append(itr_2.text)
            bowler_2 = itr_1.find_all(class_='cb-col cb-col-8 text-right')
            for itr_2 in bowler_2:
                if i%4 == 0:
                    overs_of_bowler_1st_inn.append(itr_2.text)
                elif i%4 == 1:
                    maidens_of_bowler_1st_inn.append(itr_2.text)
                elif i%4 == 2:
                    no_balls_of_bowler_1st_inn.append(itr_2.text)
                elif i%4 == 3:
                    wides_of_bowler_1st_inn.append(itr_2.text)
                i += 1
            bowler_2 = itr_1.find_all(class_='cb-col cb-col-10 text-right')
            for itr_2 in bowler_2:
                if j % 2 == 0:
                    runs_of_bowler_1st_inn.append(itr_2.text)
                elif j % 2 == 1:
                    economy_of_bowler_1st_inn.append(itr_2.text)
                j += 1
            bowler_3 = itr_1.find(class_='cb-col cb-col-8 text-right text-bold')
            wickets_of_bowler_1st_inn.append(bowler_3.text)

'''
print(name_of_bowler_1st_inn)
print(overs_of_bowler_1st_inn)
print(maidens_of_bowler_1st_inn)
print(no_balls_of_bowler_1st_inn)
print(wides_of_bowler_1st_inn)
print(runs_of_bowler_1st_inn)
print(economy_of_bowler_1st_inn)
print(wickets_of_bowler_1st_inn)
'''

#for i,j,k,l,m,n,o,p in zip(name_of_bowler_1st_inn,overs_of_bowler_1st_inn,maidens_of_bowler_1st_inn,runs_of_bowler_1st_inn,wickets_of_bowler_1st_inn,no_balls_of_bowler_1st_inn,wides_of_bowler_1st_inn,economy_of_bowler_1st_inn):
#    print(i,j,k,l,m,n,o,p)


##################################### SECOND INNINGS (BOWLER STATS) ######################################################

name_of_bowler_2nd_inn = []
overs_of_bowler_2nd_inn = []
maidens_of_bowler_2nd_inn = []
runs_of_bowler_2nd_inn = []
wickets_of_bowler_2nd_inn = []
no_balls_of_bowler_2nd_inn = []
wides_of_bowler_2nd_inn = []
economy_of_bowler_2nd_inn = []

bowler_tmp = webpage_content.find_all('div',{'id':'innings_2'})
for bowl in bowler_tmp:
    bowler = bowl.find_all(class_='cb-col cb-col-100 cb-ltst-wgt-hdr')
    for itr in bowler:
        bowler_1 = itr.find_all(class_='cb-col cb-col-100 cb-scrd-itms ')
        for itr_1 in bowler_1:
            i = 0
            j = 0
            bowler_2 = itr_1.find_all(class_='cb-text-link')
            for itr_2 in bowler_2:
                name_of_bowler_2nd_inn.append(itr_2.text)
            bowler_2 = itr_1.find_all(class_='cb-col cb-col-8 text-right')
            for itr_2 in bowler_2:
                if i%4 == 0:
                    overs_of_bowler_2nd_inn.append(itr_2.text)
                elif i%4 == 1:
                    maidens_of_bowler_2nd_inn.append(itr_2.text)
                elif i%4 == 2:
                    no_balls_of_bowler_2nd_inn.append(itr_2.text)
                elif i%4 == 3:
                    wides_of_bowler_2nd_inn.append(itr_2.text)
                i += 1
            bowler_2 = itr_1.find_all(class_='cb-col cb-col-10 text-right')
            for itr_2 in bowler_2:
                if j % 2 == 0:
                    runs_of_bowler_2nd_inn.append(itr_2.text)
                elif j % 2 == 1:
                    economy_of_bowler_2nd_inn.append(itr_2.text)
                j += 1
            bowler_3 = itr_1.find(class_='cb-col cb-col-8 text-right text-bold')
            wickets_of_bowler_2nd_inn.append(bowler_3.text)

'''
print(name_of_bowler_2nd_inn)
print(overs_of_bowler_2nd_inn)
print(maidens_of_bowler_2nd_inn)
print(no_balls_of_bowler_2nd_inn)
print(wides_of_bowler_2nd_inn)
print(runs_of_bowler_2nd_inn)
print(economy_of_bowler_2nd_inn)
print(wickets_of_bowler_2nd_inn)
'''

#for i,j,k,l,m,n,o,p in zip(name_of_bowler_2nd_inn,overs_of_bowler_2nd_inn,maidens_of_bowler_2nd_inn,runs_of_bowler_2nd_inn,wickets_of_bowler_2nd_inn,no_balls_of_bowler_2nd_inn,wides_of_bowler_2nd_inn,economy_of_bowler_2nd_inn):
#    print(i,j,k,l,m,n,o,p)