import json

def getJson():
    aa = '{"intent": { "name": "good_news_by_month", "slots": { "AMAZON.Month": { "name": "AMAZON.Month", "value": "January"}}}}'
    print (aa)
    print(json.load('{"intent": { "name": "good_news_by_month", "slots": { "AMAZON.Month": { "name": "AMAZON.Month", "value": "January"}}}}'))

getJson()
