# logging - https://www.youtube.com/watch?v=dR9n1zmw-Go
# send - https://www.youtube.com/watch?v=DArlLAq56Mo
# code from source above modified everything else by me

import requests
import json
import websocket
import threading
import time

ws = websocket.WebSocket()

token = "{Discord Token}"
username = "{Discord Username}"

lastusermessage = ""


def send_json_request(ws, request):
	ws.send(json.dumps(request))

def recieve_json_response(ws):
	response = ws.recv()
	if response:
		return json.loads(response)	

def heartbeat(interval, ws):
	print('Monitoring Started')
	while True:
		time.sleep(interval)
		heartbeatJSON = {
			'op': 1,
			'd': 'null'
		}
		send_json_request(ws, heartbeatJSON)


def send(message, auth, channelid):
	payload = {
    	'content': message
	}
	
	header = {
		'authorization': auth
	}
	r = requests.post(
		f'https://discord.com/api/v9/channels/{channelid}/messages',
		data=payload,
		headers=header)
 
ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
event = recieve_json_response(ws)

heartbeat_interval = event['d']['heartbeat_interval'] / 1000

threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

payload = {
	'op': 2,
	"d": {
		"token": token,
		"properties": {
			"$os": "windows",
			"$browser": "chrome",
			"$device": "pc",
		}
	}
}

send_json_request(ws, payload)


def do_stuff(author, channelid, message, lastmessage):
	if author == username and message[0:5].lower() == "!spam":
		split = message[6:].split()
		if len(split) == 3:
			data = list(split[0]) + list(map(int, split[1:]))
			if lastmessage != message:
				for x in range(data[1]):
					send(message=data[0], auth=token, channelid=channelid)
					time.sleep(data[2])
		else:
			send(message="input not formatted correctly", auth=token, channelid=channelid)
	return message


while True:
	try:
		event = recieve_json_response(ws)
		# print(f"{event['d']['author']['username']}#{event['d']['author']['discriminator']}: {event['d']['content']}")
		# print(f"ChannelID - {event['d']['channel_id']}")
		lastusermessage = do_stuff(
			author=event['d']['author']['username']+"#"+event['d']['author']['discriminator'],
			channelid=event['d']['channel_id'],
			message=event['d']['content'],
			lastmessage=lastusermessage
		)
	except KeyboardInterrupt:
		break
	except:
		pass
