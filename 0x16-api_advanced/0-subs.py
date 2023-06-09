#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if an error occurs.

    Raises:
        None

    Example Usage:
        >>> number_of_subscribers('python')
        8000000

    """
    import requests
    if not isinstance(subreddit, str) or subreddit is None:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    response = requests.get(url, headers=headers)

    try:
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0
