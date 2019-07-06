import requests
#import threading

username = ""
server_host='https://20765ef8.ngrok.io'#'http://127.0.0.1:8000'

def readmess():
	payload = {'mess_to': username}
	r = requests.get(server_host, params=payload)
	if ("DOCTYPE HTML PUBLIC" in r.text):
		print("No messages")
	else:
		print(r.text)

def sendmess():
	text = input("Input message: ")
	chatname = input("Send to: ")
	payload = {'message': text, 'to_user': chatname, 'from_user': username} 
	r = requests.get(server_host, params=payload)
	print(r.url)

def user_login():
	global username
	username = input("Input your name: ")
	payload = {'online': username} 
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
	payload = {'offline': username}
	r = requests.get(server_host, params=payload)
	exit("Good buy!")

if __name__ == '__main__':
	user_login()
	while True:
		user_loop()
