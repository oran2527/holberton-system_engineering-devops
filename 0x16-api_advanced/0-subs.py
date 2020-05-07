#!/usr/bin/python3
'''point 0 reddit appi'''


import json
import requests
num_subs = 0


def number_of_subscribers(subreddit):
    '''return number subscribers depending topic and device you are using'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agChrome = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    agMac = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    agLinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    agIosIphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) \
AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/81.0.4044.124 \
Mobile/15E148 Safari/604.1"
    agIpad = "Mozilla/5.0 (iPad; CPU OS 13_4 like Mac OS X) \
AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/81.0.4044.124 Mobile/15E148 \
Safari/604.1"
    agIpod = "Mozilla/5.0 (iPod; CPU iPhone OS 13_4 like Mac OS X) \
AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/81.0.4044.124 Mobile/15E148 \
Safari/604.1"
    agAndroid = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"
    agAndroidSamsung = "Mozilla/5.0 (Linux; Android 10; SM-A205U) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile \
Safari/537.36"
    agLg = "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"
    s = ' '
    a1 = agChrome
    a2 = agMac
    a3 = agLinux
    a4 = agIosIphone
    a5 = agIpad
    a6 = agIpod
    a7 = AgAndroid
    a8 = AgAndroidSamsung
    a9 = agLg
    headers_concat = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\
'.format(ag1, s, ag2, s, ag3, s, ag4, s, ag5, s, ag6, s, ag7, s, ag8, s, ag9)
    headers = {"User-Agent": headers_concat}
    red = requests.get(url, headers=headers)
    if red:
        reddit = red.json()
        return reddit.get('data').get('subscribers')
    return 0
