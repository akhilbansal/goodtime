import aa
import alexa_response

def lambda_handler(event, context):
    if event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    else:
        return "no match"


def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == "good_news":
        aa.get_date_by_year(2018)
        return alexa_response.conversation("test", "this is what alexa will speak")
    elif intent_name == "devicecode":
        return "not yet implemented."
    else:
        return "return from else"

def good_news_by_month(month):
    print (month)