#!/usr/bin/env python3
from bottle import route, request, run, template # $ pip install bottle
import os
from collections import deque

temperature = None
online = []
offline = ''
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
	# Пользователь онлайн
	if(request.query.online and online != ''):
		online.append(request.query.online or online)
		room_location = "./history_rooms/" + request.query.room
		file = open(room_location, "a")
		file.write("SYSTEM MESSAGE: User " + request.query.online + " signed in!\n")
		file.close()

	# Пользователь оффлайн
	if(request.query.offline or offline != ''):
		online.remove(request.query.offline or offline)
		room_location = "./history_rooms/" + request.query.room
		file = open(room_location, "a")
		file.write("SYSTEM MESSAGE: User " + request.query.offline + " signed off!\n")
		file.close()

	# Принятие сообщения от пользователя
	if(request.query.action == 'send'): #and request.query.to_user != '' and request.query.from_user != ''):
		message = request.query.message
		room = request.query.room
		from_user = request.query.from_user
		tofile = from_user + ": " + message + "\n"
		room_location = "./history_rooms/" + request.query.room
		file = open(room_location, "a")
		file.write(tofile)
		file.close()
		#print(messages)
		
	# чтение сообщений пользователем
	if(request.query.action == 'read'):
		messages = ''
		room = request.query.room
		with open("history_rooms/" + room) as f:
			for row in deque(f, 30):
				messages += row.strip() + "\n"
		#with open("history_rooms/" + room) as f:
		#	messages = list(deque(f, 30))
		return template('{{messages}}',
					messages=messages)



	#temperature = request.query.temperature or temperature
	#return template('<b>Temperature: {{temperature}}</b>',
	#				temperature=temperature)

if __name__ == '__main__':
	run(host='localhost', port=8000)