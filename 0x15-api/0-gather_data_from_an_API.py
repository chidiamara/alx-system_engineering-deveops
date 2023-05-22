#!/usr/bin/python3
""" a Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress"""
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    get_user_url = 'https://jsonplaceholder.typicode.com/users/' + employeeId
    response1 = requests.get(get_user_url)
    employee_name = response1.json().get("name")
    get_todos_url = 'https://jsonplaceholder.typicode.com/todos'
    response2 = requests.get(get_todos_url)
    task_names = []
    tasks = 0
    completed = 0
    for item in response2.json():
        if item.get("userId") == int(employeeId):
            tasks += 1
            if item.get("completed") is True:
                completed += 1
                task_names.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          completed,
                                                          tasks))
    for i in task_names:
        print("\t {}".format(i))
