import datetime
from datetime import date

bday = date(2018, 3, 31)
dates = ['2017-12-25', '2018-01-01', '2018-01-15', '2018-02-19', '2018-03-31']

def convert_to_date():
    lst = [];
    for x in dates:
        tempdt = datetime.datetime.strptime(x, '%Y-%m-%d').date()
        lst.append(tempdt)
    return lst

def sorted_list_greater_than_date(day):
    lst = convert_to_date()
    temp = sorted(x for x in lst if x >= day)
    return temp

def dateToString(lst):
    return ' and '.join([x.strftime('%m/%d/%Y') for x in lst])

def get_date_by_year(year):
    lst = convert_to_date()
    temp = sorted(x for x in lst if x.year == year)
    return temp

def get_date_by_year_month(year, month):
    lst = convert_to_date()
    temp = sorted(x for x in lst if x.year == year and x.month == month)
    print(temp)
    return temp

def lambda_handler(event, context):
    if event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    else:
        return "invalid request"

def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == "good_news":
        return conversation("test", "this is what alexa will speak")
    elif intent_name == "good_news_by_month":
        return conversation("test", "in the month of " + dateToString(get_date_by_year_month(2018,3)))
    elif intent_name == "devicecode":
        return "not yet implemented."
    else:
        return "return from else"

def OutputSpeech(alexa_response):
    message = {}
    message['type'] = "PlainText"
    message['text'] = alexa_response
    return message

def card(title, alexa_response):
    message = {}
    message['type'] = "Simple"
    message['title'] = title
    message['content'] = alexa_response
    return message

def conversation(title, alexa_response):
    response = {}
    response['outputSpeech'] = OutputSpeech(alexa_response)
    response['card'] = card(title, alexa_response)
    response['shouldEndSession'] = True

    outer = {}
    outer['version'] = '1.0'
    outer['response'] = response
    return outer




def aa():

    month_name = "jul"
    print(datetime.datetime.strptime(month_name, '%b').month)

    slots = {}
    slots['name']='AMAZON.Month'
    slots['value'] = 'January'

    temp = {}
    temp['AMAZON.Month'] = slots

    temp2 = {}
    temp2['name']='good_news_by_month'
    temp2['slots'] = temp

    outer = {}
    outer['intent'] = temp2

    print(on_intent(outer,'aa'))
    print(outer)

aa()
