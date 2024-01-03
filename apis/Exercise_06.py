'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
import requests

url = "http://your_api_endpoint_here.com/tasks_api" 

def create_account():
    data = {
        "first_name": input("First name: ")
        "last_name": input("Last name: ")
        "email": input("Email address: ")
    }
    print("Creating Account.....")
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Account created Successfully")
    else:
        print("Try Again")


def view_tasks(completed=None):
    params = {} if completed is None else {'completed': completed}
    print(f"Viewing {'all' if completed is None else 'completed' if completed else 'incomplete'} tasks...")
    response = requests.get(url, params=params)
    print(response.json())


def create_task():
    task = input("ADD TASK: ")
    data = {"task": task}
    response = requests.post(url, json=data)
    print("Creating a new task...")


def update_task():
    task_id = input("Enter the Task ID to update: ")
    new_task = input("Enter the updated task: ")
    data = {"task": new_task}
    url_put = f"{url}/{task_id}"
    response = requests.put(url_put, json=data)
    print("Updating an existing task...")


def delete_task():
    task_id = input("Enter the Task ID to delete: ")
    url_delete = f"{url}/{task_id}"
    response = requests.delete(url_delete)
    print("Deleting a task...")

# CLI menu
while True:
    print("\nPlease select from the following options (enter the number of the action you'd like to take):")
    print("1) Create a new account (POST)")
    print("2) View all your tasks (GET)")
    print("3) View your completed tasks (GET)")
    print("4) View only your incomplete tasks (GET)")
    print("5) Create a new task (POST)")
    print("6) Update an existing task (PATCH/PUT)")
    print("7) Delete a task (DELETE)")
    print("8) Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks(completed=True)
    elif choice == '4':
        view_tasks(completed=False)
    elif choice == '5':
        create_task()
    elif choice == '6':
        update_task()
    elif choice == '7':
        delete_task()
    elif choice == '8':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-8).")
