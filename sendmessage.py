import json
import requests
import string
import random
import time

# SET RAIDMODE ON OR OFF

RAIDMODE = True


def retMode():
    if RAIDMODE:
        return "ON"
    else:
        return "OFF"


print("DISCORD MESSAGE SENDER v1.0")
print("RAIDMODE IS: " + retMode() + "\n")

authToken = input("ENTER DISCORD AUTHORIZATION TOKEN: ")
if not authToken:
    print("SERVER: NO TOKEN: UNAUTHORIZED")
    exit(-1)

message = input("TYPE MESSAGE: ")
# tts = input("TTS? (true OR false): ")


def id_generator(size=17, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def genBody(message, tts):
    body = {
        "content": message,
        "nonce": id_generator(17, "1234567890"),
        "tts": tts
    }
    return body


headers_ = {
    "accept": "*/*",
    "accept-language": "en-US",
    "authorization": str(authToken),
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
}

url_base = 'https://discord.com/api/v9/channels/'
url_id = input("CHANNEL ID: ")
url = "".join(url_base + url_id + "/messages")
print(url)

# Use the 'headers' parameter to set the HTTPS headers:
# bodyjson = json.dumps(genBody())

# print(bodyjson) -- DEBUG

def sendMessage():
    bodyjson = json.dumps(genBody(message, "false"))
    res = requests.post(url, data=bodyjson, headers=headers_)
    resjson = json.loads(res.text)

    try:
        print("SERVER: " + resjson["message"])
        try:
            print(" - RETRY AFTER: " + str(resjson["retry_after"]) + "s\n")
        except KeyError:
            pass
    except KeyError:
        print("Sent!\n")
        print("Message Sent: ")
        print(resjson["content"] + "\n")
        print("Sent as: ")
        print(resjson["author"]["username"] + "#" + resjson["author"]["discriminator"] + "\n")


    # print(resjson) -- DEBUG
    time.sleep(0.05)

while RAIDMODE:
    sendMessage()

sendMessage()
