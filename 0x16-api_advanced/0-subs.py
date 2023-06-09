#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or
        0 if the subreddit does not exist or an error occurs.

    Raises:
        None

    Example Usage:
        >>> number_of_subscribers('python')
        8000000

    """
    user = {"User-Agent": "Scoot"}
    req = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers=user)
    if req.status_code != requests.codes.OK:
        return 0

    else:
        return req.json().get("data").get("subscribers")
