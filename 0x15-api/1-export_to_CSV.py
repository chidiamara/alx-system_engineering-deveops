#!/usr/bin/python3
""" a Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
import csv
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    response1 = requests.get(url)
    if response1.status_code == 200:
        USERNAME = response1.json().get("username")
        url2 = 'https://jsonplaceholder.typicode.com/todos'
        response2 = requests.get(url2)
        filename = USER_ID + '.csv'
        with open(filename, 'w') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
            for item in response2.json():
                if item.get("userId") == int(USER_ID):
                    line = [item.get("userId"),
                            USERNAME,
                            str(item.get("completed")),
                            item.get('title')]
                    wr.writerow(line)
