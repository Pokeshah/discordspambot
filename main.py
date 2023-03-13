# logging - https://www.youtube.com/watch?v=dR9n1zmw-Go
# send - https://www.youtube.com/watch?v=DArlLAq56Mo
# code from source above slightly modified
# everything else by me

import requests
import json
import websocket
import threading
import time
import math

ws = websocket.WebSocket()

token = '' # replace with your discord token
username = "" # replace with discord username in username#discriminator format(ex. wumpus#0001) IT HAS TO BE EXACTLY LIKE YOUR USERNAME OTHERWISE IT WON'T WORK


def send_json_request(ws, request):
	ws.send(json.dumps(request))

def recieve_json_response(ws):
	response = ws.recv()
	if response:
		return json.loads(response)	

def heartbeat(interval, ws):
	print('Monitoring Started') # prints when its started monitering
	while True:
		time.sleep(interval)
		heartbeatJSON = {
			'op': 1,
			'd': 'null'
		}
		send_json_request(ws, heartbeatJSON)


def send(message, auth, channel):
	r = requests.post(
        url=f"https://discord.com/api/v9/channels/{channel}/messages",
        data={'content': message},
        headers=({'authorization': auth})
    )
	# print(r.status_code) # uncomment if you want to see the status code after sending the message
	if r.status_code == 429:
		time.sleep(10)
		r = requests.post(
            url=f"https://discord.com/api/v9/channels/{channel}/messages",
            data={'content': 'got a 429 taking a break'},
            headers=({'authorization': auth})
        )
		
 
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


def processResponse(author, channelid, message):
	if author == username and message[0:5].lower() == "!spam": # check if message starts with !spam and it came from the username specified in the username variable
		split = message[6:].split(" ") # split into array
		split = list(filter(None, split)) # remove multiple spaces
		split[0] = split[0].replace("\\n", "\n") # if the message has a \\n replace with \n(discord converts any user typed \n to \\n)
		# print(split) # uncomment if you want to see what the code is processing
		if len(split) == 3: # if array is in the correct form
			data = list(map(float, split[1:])) # convert last 2 items of array to float(the amount of messages to send and the time between each message)
			data.append(split[0]) # add the floats to the end of the array
			data[0] = int(math.ceil((data[0]))) # round the amount of messages to send up to the nearest whole number
			for x in range(data[0]): # loop to send x amount of messages
					send(message=data[2], auth=token, channel=channelid) # send message
					time.sleep(data[1]) # wait x amount of seconds
		else:
			send(message="input not formatted correctly", auth=token, channel=channelid) # if input not formatted correctly send this message

while True:
	try:
		event = recieve_json_response(ws)
		# uncomment these if you want to see the messages recieved
		# print(f"{event['d']['author']['username']}#{event['d']['author']['discriminator']}: {event['d']['content']}")
		# print(f"ChannelID - {event['d']['channel_id']}")
		processResponse(
			author=event['d']['author']['username']+"#"+event['d']['author']['discriminator'],
			channelid=event['d']['channel_id'],
			message=event['d']['content']
		)
	except KeyboardInterrupt:
		break
	except:
		pass
