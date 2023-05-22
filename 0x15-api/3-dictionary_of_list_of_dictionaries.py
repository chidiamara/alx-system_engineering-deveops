#!/usr/bin/python3
""" a Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
import json
import requests
import sys


if __name__ == '__main__':
    data = {}
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    response2 = requests.get(todos_url)
    for item in response2.json():
        if str(item.get('userId')) not in data:
            data[str(item.get('userId'))] = []
        id_url = 'https://jsonplaceholder.typicode.com/users?id='\
            + str(item.get('userId'))
        response1 = requests.get(id_url)
        response1 = response1.json()
        username = response1[0]['username']
        d = {}
        d['username'] = username
        d['task'] = item.get('title')
        d['completed'] = item.get('completed')
        data[str(item.get('userId'))].append(d)

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        json.dump(data, f)
