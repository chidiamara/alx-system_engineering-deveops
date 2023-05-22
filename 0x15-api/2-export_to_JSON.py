#!/usr/bin/python3
""" a Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    id_url = 'https://jsonplaceholder.typicode.com/users?id=' + employee_id
    response1 = requests.get(id_url)
    if response1.status_code == 200:
        data = {employee_id: []}
        username = response1.json()[0].get("username")
        todo_url = 'https://jsonplaceholder.typicode.com/todos'
        response2 = requests.get(todo_url)
        for item in response2.json():
            if item.get("userId") == int(employee_id):
                d = {'task': item.get('title'),
                     'completed': item.get('completed'),
                     'username': username}
                data[employee_id].append(d)
    filename = employee_id + '.json'
    with open(filename, 'w') as f:
        json.dump(data, f)
