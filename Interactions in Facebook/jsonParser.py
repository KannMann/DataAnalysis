
import json
import pandas as pd
from datetime import datetime
from datetime import date


# COUNT OF FACEBOOK LIKES
with open('posts_and_comments.json') as jsonFile:
    jsonObject = json.load(jsonFile)

relevantAction = jsonObject['reactions']
relevantDict = {}
for item in relevantAction:
    actionDate = date.fromtimestamp(item['timestamp'])
    actionTaken = item['data'][0]['reaction']['reaction']
    relevantDict[actionDate] = actionTaken

relevantDf = pd.DataFrame.from_dict(relevantDict, orient = 'index', columns=['Action'])
relevantDf.reset_index(inplace=True)
relevantDf.rename({"index": "Datetime"}, axis='columns', inplace=True)
table = pd.pivot_table(relevantDf, index = ['Datetime'], columns='Action', aggfunc=len, fill_value=0)
table.reset_index(inplace=True)
table.to_csv('likeOutput.csv')


# COUNT OF INSTAGRAM LIKES
with open('likes_insta.json') as jsonFileInsta:
    jsonObjInsta = json.load(jsonFileInsta)

relevantActionInsta = jsonObjInsta['media_likes']
dateList = []
for item in relevantActionInsta:
    dateList.append(pd.to_datetime(item[0]))

dateList = pd.DataFrame(dateList, columns=['Datetime'])
cleanDates = dateList['Datetime'].dt.date
cleanDates.to_csv('likeOutputInsta.csv', header = True)