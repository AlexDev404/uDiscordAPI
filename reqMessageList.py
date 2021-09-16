# REQUESTS THE LATEST MESSAGE IN A DISCORD CHANNEL

import json
import requests
import time


print("DISCORD MESSAGE SENDER v1.0")

authToken = input("ENTER DISCORD AUTHORIZATION TOKEN: ")
if not authToken:
    print("SERVER: NO TOKEN: UNAUTHORIZED")
    exit(-1)

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
url = "".join(url_base + url_id + "/messages?limit=1")
print(url)


# Use the 'headers' parameter to set the HTTPS headers:
# bodyjson = json.dumps(genBody())

# print(bodyjson) -- DEBUG


def reqMessage():
    res = requests.get(url, data=None, headers=headers_)
    uresjson = json.loads(res.text)
    resjson = json.dumps(uresjson, indent=3)

    try:
        print("SERVER: " + resjson["message"])
        try:
            print(" - RETRY AFTER: " + str(resjson["retry_after"]) + "s\n")
        except KeyError:
            pass
        except TypeError:
            pass
    except TypeError:
        x = 0
        while x < len(uresjson):
            print(uresjson[x]["content"])
            x = x + 1
    except KeyError:
        print(uresjson[0]["content"])


reqMessage()
