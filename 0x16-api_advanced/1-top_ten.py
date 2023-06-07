#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    if not isinstance(subreddit, str) or subreddit is None:
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    response = requests.get(url, headers=headers)
    data = response.json().get('data')
    if response.status_code == 200:
        if 'children' in data:
            for post in data.get('children'):
                print(post.get('data').get('title'))
    else:
        print("None")
