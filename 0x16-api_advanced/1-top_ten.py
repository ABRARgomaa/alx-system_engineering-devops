#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    try:
        response = requests.get(url, headers=user)
        response.raise_for_status()  # Raises exception for 4xx or 5xx status codes
        data = response.json()
        for post in data.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"KeyError: {e}, Response: {data}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py subreddit_name")
    else:
        top_ten(argv[1])
