import requests

api_key = 'xxx'

channelName = input('Channel Name: ')

channelInfosByName = requests.get(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={channelName}&key={api_key}')

jsonChannelData = channelInfosByName.json()

try:
    subscriberCount = jsonChannelData['items'][0]['statistics']['subscriberCount']
    print("Channel has {:,} subs!".format(int(subscriberCount)))
except:
    print('Channel is not found!')

