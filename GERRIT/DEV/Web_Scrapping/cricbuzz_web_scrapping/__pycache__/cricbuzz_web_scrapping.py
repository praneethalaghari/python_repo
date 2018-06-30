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

print("Matches today are :", matches_today)

title = webpage_content.find_all('title')
for titl in title:
    print(titl.text)

todays_match_result = webpage_content.find(class_='cb-col cb-scrcrd-status cb-col-100 cb-text-complete')
print("Match Result :", todays_match_result.text)


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

print(name_of_batsman_1st_inn)
print(score_of_batsman_1st_inn)
print(balls_of_batsman_1st_inn)
print(fours_of_batsman_1st_inn)
print(sixes_of_batsman_1st_inn)
print(strike_rate_of_batsman_1st_inn)


#for i,j,k,l,m,n in zip(name_of_batsman_1st_inn,score_of_batsman_1st_inn,balls_of_batsman_1st_inn,fours_of_batsman_1st_inn,sixes_of_batsman_1st_inn,strike_rate_of_batsman_1st_inn):
#    print(i,j,k,l,m,n)

'''
bowler = webpage_content.find_all('div', id="innings_1", class_='cb-col cb-col-100 cb-scrd-itms')
for itr_bowler in bowler:
    bwlr = itr_bowler.find('a')
    print(bwlr.text)
    bowler_data = itr_bowler.find_all(class_='cb-col cb-col-8 text-right')
    for items in bowler_data:
        print(items)
'''

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
                print('hit')
                balls_of_batsman_2nd_inn.append(items.text)
            elif i%4 ==1:
                fours_of_batsman_2nd_inn.append(items.text)
            elif i%4 ==2:
                sixes_of_batsman_2nd_inn.append(items.text)
            elif i%4 ==3:
                strike_rate_of_batsman_2nd_inn.append(items.text)
            i += 1

print(name_of_batsman_2nd_inn)
print(score_of_batsman_2nd_inn)
print(balls_of_batsman_2nd_inn)
print(fours_of_batsman_2nd_inn)
print(sixes_of_batsman_2nd_inn)
print(strike_rate_of_batsman_2nd_inn)


#for i,j,k,l,m,n in zip(name_of_batsman_2nd_inn,score_of_batsman_2nd_inn,balls_of_batsman_2nd_inn,fours_of_batsman_2nd_inn,sixes_of_batsman_2nd_inn,strike_rate_of_batsman_2nd_inn):
#    print(i,j,k,l,m,n)


