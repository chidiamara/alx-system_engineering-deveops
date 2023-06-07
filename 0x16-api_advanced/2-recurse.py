#!/usr/bin/python3

"""
Queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles"""
    import requests

    if not isinstance(subreddit, str) or subreddit is None:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        if after is None:
            return hot_list
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    else:
        return None
