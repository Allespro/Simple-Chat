import requests
#import threading

username = ""
room = ""
server_host='http://127.0.0.1:8000'

def readmess():
	global room
	payload = {'room': room, 'action': 'read'}
	r = requests.get(server_host, params=payload)
	if ("DOCTYPE HTML PUBLIC" in r.text):
		print("No messages")
	else:
		output = r.text
		print(output)

def sendmess():
	text = input("Input message: ")
	payload = {'message': text, 'room': room, 'from_user': username, 'action': 'send'} 
	r = requests.get(server_host, params=payload)
	print(r.url)

def user_login():
	global username
	global room
	username = input("Input your name: ")
	room = input("Input room name: ")
	payload = {'online': username, 'room': room} 
	r = requests.get(server_host, params=payload) 

def user_loop():
	print("[1] - write message\n[2] - read messages\n[3] - exit")
	loop_ch = int(input("~> "))
	if(loop_ch == 1):
		sendmess()
	elif(loop_ch == 2):
		readmess()
	elif(loop_ch == 3):
		chat_exit()
	else:
		print("ERROR INPUT")


def chat_exit():
	global room
	payload = {'offline': username, 'room': room}
	r = requests.get(server_host, params=payload)
	exit("Good buy!")

if __name__ == '__main__':
	user_login()
	while True:
		user_loop()
