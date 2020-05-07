#!/usr/bin/python3
'''point 2 posts'''


hot_list = []
final = []
count = 0


def recurse(subreddit):
    '''return total titles lists'''

    import json
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
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
    ag1 = agChrome
    ag2 = agMac
    ag3 = agLinux
    ag4 = agIosIphone
    ag5 = agIpad
    ag6 = agIpod
    ag7 = agAndroid
    ag8 = agAndroidSamsung
    ag9 = agLg
    headers_concat = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\
'.format(ag1, s, ag2, s, ag3, s, ag4, s, ag5, s, ag6, s, ag7, s, ag8, s, ag9)
    headers = {"User-Agent": headers_concat}
    red = requests.get(url, headers=headers)
    if red:
        reddit = red.json()
        final = recurse2(reddit, hot_list, count)
        print(final)
        return final
    else:
        return None


def recurse2(reddit, hot_list, count):
    '''recursion 2 for adding title of the json data'''
    try:
        title = ''
        if reddit.get('data').get('children')[count].get('data\
').get('title'):
            title = reddit.get('data').get('children')[count].get('data\
').get('title')
            hot_list.append(title)
            count += 1
            recurse2(reddit, hot_list, count)
        else:
            return hot_list
    except:
        return hot_list
    finally:
        return hot_list
