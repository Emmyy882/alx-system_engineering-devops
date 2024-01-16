#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.'''
import requests


def number_of_subscribers(subreddit):
    '''Retrieves the number of subscribers in a given subreddit.'''
    BASE_URL = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0)',
            'Geecko/20100101, Firefox/119.0'
        ])
    }
    params = {
            "limit": 10
            }
    response = requests.get(BASE_URL,
                            headers=api_headers,
                            params=params,
                            allow_redirects=False
                            )
    if response.status_code == 200:
        for post in response.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
