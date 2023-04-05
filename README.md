# DiscordSpamBot

A Discord bot that will spam any channel on your behalf.

## How to Use

Clone this repository and open `main.py` in your favorite text editor. Then, replace `{Discord Token}` with your discord token and `{Discord Username}` with your discord username (ex. wumpus#0000). Then, using any Python interpreter, run the program.

## How to Spam

Open Discord with the same account from which you obtained the token. Then go to any channel on any server (or dms) and send a message in the format shown below.

|!spam|times|delay |
|--|--|--|
|calls spam|# of messages to send|delay between messages(in seconds)|

### Example

`!spam 4 1 abcd` This will spam abcd four times, with a one-second interval between messages. All of these messages WILL be sent from your account on your internet.

#### Multiple Spaces
You can have as many spaces as you want after the `!spam `

`!spam a          3 1` will work the same as `!spam a 3 1`

#### New Lines
This code supports new lines. You can use
```
!spam a
b 3 1
```

and it will send
```
a
b
```

You can also say `!spam a\nb 3 1` and it will the same thing (\n and a new line are interchangable)

## Troubleshooting

### Got a 429

Discord's servers are programmed to return the error message `429 Too Many Requests`. On the Discord client this can be seen as the `Woah There. Way too Spicy. You're sending messages way too quickly` popup. As of now, the servers have no way of distinguishing between a legitimate discord message and one sent with this program. As a result, this is the quickest way to send messages(technically you can modify this library to use threading to send multiple messages at once, but that would just result in a 429 earlier).

If it suddenly posts a message `got a 429 taking a break` it will wait for 10 seconds before sending another message. Although this sound counter intuitive it will post more messages in a shorter amount of time than the alternative.

### Doesn't work

You most likely configured it incorrectly, or Discord has changed its server code, rendering this code obsolete. Please open an issue so that we can discuss it.

## WARNINGS

**THIS IS AGAINST DISCORD TERMS OF SERVICE. USE AT YOUR OWN RISK.**
