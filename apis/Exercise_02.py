'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests
url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(url)

user_data = response.json()
emails = [user.get("email")for user in user_data]
print("List of Emails")
print(emails)

