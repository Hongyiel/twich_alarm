# checks whether a twitch.tv userstream is live
import requests

URL = 'https://api.twitch.tv/helix/streams?user_login=woowakgood'
authURL = 'https://id.twitch.tv/oauth2/token'

# This could be change
Client_ID = '1cfajfk4cpnfo6nql6fw7nqdgwrbym'
Secret  = 'dyua0rlbefuqceogqraa7wh1t4u7gn'

getInfo = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }

def Check():
    callInfo = requests.post(url=authURL, params=getInfo)
    access_token = callInfo.json()['access_token']

    head = {
    'Client-ID' : Client_ID,
    'Authorization' :  "Bearer " + access_token
    }

    checkRequest = requests.get(URL, headers = head).json()['data']

    if checkRequest:
        checkRequest = checkRequest[0]
        if checkRequest['type'] == 'live':
            return True
        else:
            return False
    else:
        return False

print(Check())
