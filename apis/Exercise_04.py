'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
url = "http://demo.codingnomads.co:8080/tasks_api/users"

#Update user
data = {
    "id" : 002
    "first_name" : "Marie",
    "last_name" : "Nakitende",
    "email" : "nakimarie@gmail.com",
    
}
response_put = requests.put(url, json=data)

#get user information
user_id = 002
url_get = f"http://demo.codingnomads.co:8080/tasks_api/users{user_id}"
response_get = requests.get(url_get)
user_data = response_get.json()
print("User details:")
print(user_data)
