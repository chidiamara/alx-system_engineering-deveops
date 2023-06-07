#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None, word_dict=None):
    if not isinstance(subreddit, str) or subreddit is None:
        return None
    if not isinstance(word_list, list) or word_list is None:
        return None

    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')

        for child in children:
            title = child.get('data').get('title')
            words = title.lower().split()

            for word in word_dict:
                if word in words:
                    word_dict[word] += words.count(word)

        if after is None:
            sorted_words = sorted(word_dict.items(),
                                  key=lambda x: x[1],
                                  reverse=True)

            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")

            return

        return count_words(subreddit, word_list, after, word_dict)

    else:
        return None
