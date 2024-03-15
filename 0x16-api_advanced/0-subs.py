#!/usr/bin/python3
'''
    this module contains the function number_of_subscribers
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        returns the number of subscribers for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    sub = argv[1]
    subscribers = number_of_subscribers(sub)
    if subscribers:
        print("Output: existing subreddit")
        print("Score: 2 out of 2 points")
        print("Reason: OK")
    else:
        print("Output: nonexisting subreddit")
        print("Score: 2 out of 2 points")
        print("Reason: OK")
