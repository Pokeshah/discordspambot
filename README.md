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

## Troubleshooting

### It was fast but slowed down/It didn't send the specified amount of messages

Discord's servers are programmed to return the error message `429 Too Many Requests`. On the Discord client this can be seen as the `Woah There. Way too Spicy. You're sending messages way too quickly`  popup. As of now, the servers have no way of distinguishing between a legitimate discord message and one sent with this program. As a result, this is the quickest way to send messages(technically you can modify this library to use threading to send multiple messages at once, but that would just result in a 429 earlier).

I decided that it would be a bad idea to implement 429 detection, since discord's severs behave in a really weird way. Instead, if we get a 429 that message will not be sent and we will not attempt to send it again. This helps in dealing with 429s.

### Doesn't work

You most likely configured it incorrectly, or Discord has changed its server code, rendering this code obsolete. Please open an issue so that we can discuss it.

## WARNINGS

THIS IS AGAINST DISCORD TERMS OF SERVICE. USE AT YOUR OWN RISK.
