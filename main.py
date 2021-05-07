import os
from subprocess import Popen, PIPE
import requests
import pprint
from bs4 import BeautifulSoup
import time
from pypresence import Presence
import threading
import asyncio
mode = input('web/discord : ')


def get_url():
    cmd = "/usr/bin/osascript -e 'tell application \"Safari\"' -e 'get URL of every tab of every window' -e 'end tell'" # this works on macos only!
    pipe = Popen(cmd, shell=True, stdout=PIPE).stdout
    urls = pipe.readlines()
    return urls



def main():
    api_key = os.getenv('API_KEY')
    base_api_url = f'https://www.googleapis.com/youtube/v3/videos?id=%s&key={api_key}&part=snippet'
    base_url = 'https://www.youtube.com/watch?v='

    currently_playing = ''
    while 1:
        current_urls = get_url()
        current_urls = current_urls[0].decode().split(',')
        for url in current_urls:
            if 'music.youtube.com' in url:
                if url != currently_playing:
                    try:
                        print(url)
                        url_code = url.split('v=')[1].split('&')[0]
                    except Exception as e:
                        print(e)
                        continue

                    url_to_get = base_api_url % url_code
                    r = requests.get(url_to_get)
                    resp = r.json()
                    vid_title = resp['items'][0]['snippet']['title']
                    vid_author = resp['items'][0]['snippet']['channelTitle']
                    currently_playing = url
                    if vid_author.endswith('- Topic'):
                        vid_author = vid_author[:-7]
                    print(f'{vid_title} - {vid_author}')
                    if mode == 'web':
                        data = {'track': f'{vid_title} - {vid_author}'}
                        requests.post('http://127.0.0.1:8000/currently_playing', data=data)
                    else:
                        with open('tmp.txt', 'w') as f:
                            f.write(f'{vid_title} - {vid_author}')
                    time.sleep(5)
                else:
                    print('Track not changed')
                    time.sleep(5)

            

    
main()