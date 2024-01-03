'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
import requests
url = "http://demo.codingnomads.co:8080/tasks_api/users"

#delete user
user_id = 002
url_delete = f"http://demo.codingnomads.co:8080/tasks_api/users{user_id}"
response_delete = requests.delete(url_delete)

#get user information
url_get = f"http://demo.codingnomads.co:8080/tasks_api/users{user_id}"
response_get = requests.get(url_get)

print(status_code)
