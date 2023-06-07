#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    if not isinstance(subreddit, str) or subreddit is None:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    response = requests.get(url, headers=headers)
    try:
        return response.json().get('data').get('subscribers')

    except Exception:
        return 0
