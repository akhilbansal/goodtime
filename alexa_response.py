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