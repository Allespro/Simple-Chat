#!/usr/bin/env python3
from bottle import route, request, run, template # $ pip install bottle

temperature = None
online = []
offline = ''
messages = {}
mess_to = ''
message = ''
to_user = ''
from_user = ''

@route('/')
def index():
    global temperature
    global online
    global offline
    global messages
    global mess_to
    if(request.query.online and online != ''):
    	online.append(request.query.online or online)

    if(request.query.offline or offline != ''):
    	online.remove(request.query.offline or offline)

    if(request.query.message or request.query.to_user or request.query.from_user != ''): #and request.query.to_user != '' and request.query.from_user != ''):
    	message = request.query.message
    	to_user = request.query.to_user
    	from_user = request.query.from_user
    	messages[to_user] = from_user + ": " + message
    	print(messages)
    	
    if(request.query.mess_to or mess_to != ''):
    	mess_to = request.query.mess_to or mess_to
    	return template('{{messages}}',
                    messages=messages[mess_to])



    #temperature = request.query.temperature or temperature
    #return template('<b>Temperature: {{temperature}}</b>',
    #                temperature=temperature)

if __name__ == '__main__':
	run(host='localhost', port=8000)