#!/usr/bin/python3

"""
Queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves the titles of all hot
    articles from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): A list to store the titles of hot
        articles (default is an empty list).
        after (str, optional): The 'after' parameter to fetch the next set
        of articles (default is None).

    Returns:
        list: A list of titles of all hot articles.

    Raises:
        None

    Example Usage:
        >>> titles = recurse('python')
        >>> for title in titles:
        ...     print(title)

    """
    if not isinstance(subreddit, str) or subreddit is None:
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
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
