import random
import replies
from time import sleep
from telethon import TelegramClient, events

# Log in data
api_id = 0
api_hash = ''
phone_number = ''
session_name = "pythonSession"
friends_phone_number = ""

# Create a new Telegram client
client = TelegramClient(session_name, api_id, api_hash)


def randomChoiceDel(container):
    element = random.choice(container)
    container.remove(element)
    return element


def mirrorFun(input_str):
    # setup
    output_str = ''

    for i in range(len(input_str)):
        if i % 2 == 0:
            output_str += input_str[i].lower()
        else:
            output_str += input_str[i].upper()

    for i in range(random.randint(0, 10)):
        output_str += " "
        output_str += random.choice(replies.emojis)

    return output_str


def textEmojiMirrorLink(input_str):
    key = random.random()

    if key < 0.4:
        return randomChoiceDel(replies.texts)

    if key < 0.8:
        return randomChoiceDel(replies.links)

    if key < 0.9:
        return random.choice(replies.emojis)

    if key < 1:
        return mirrorFun(input_str)

    return "pass"


# define an event handler for incoming messages
@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    # waiting for a moment
    sleep(random.randint(0, 2))

    # generating key
    key = random.random()

    # 70%
    if key < 0.8:
        await event.respond(textEmojiMirrorLink(str(event.message.message)))
        return

    # 20%
    if key < 1:
        video_path = 'C:/Users/Sant Antonio/Desktop/Projects/telegaBot/' + randomChoiceDel(replies.videos)
        await client.send_file(friends_phone_number, video_path)
        return

    # 10%
    if key < 1:
        return


# starting and never ending setup
client.start()
client.run_until_disconnected()
