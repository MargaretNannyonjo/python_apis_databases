'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests
url = "http://demo.codingnomads.co:8080/tasks_api/users"

#create user
data = {
    "id" : 002
    "first_name" : "Maggie",
    "last_name" : "Nannyonjo",
    "email" : "nannyonjoleon@gmail.com",
}
response_post = requests.post(url, json=data)

#get user information
user_id = 002
url_get = f"http://demo.codingnomads.co:8080/tasks_api/users{user_id}"
response_get = requests.get(url_get)
user_data = response_get.json()
print("User details:")
print(user_data)
