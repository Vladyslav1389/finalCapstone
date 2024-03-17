"""
It is a task manager that allows to add users, add tasks, modify tasks( change
the person to whom the task is assigned, change the due date, and mark a task
as completed). Track all tasks and track tasks that are assigned to each
person. It also allows the admin to generate, display and write reports into
a file. 
"""


import os
from datetime import datetime, date


##===========================================================================
def display_menu(curr_user: str) -> str:
    """
    The function `display_menu` presents a menu of options based on the current
    user, allowing them to select various actions.
    
    :param curr_user: The user that logged in.
    :type curr_user: str
    :return: Display menu options based on the user type. If the current user
        is 'admin', the menu includes additional options such as 'gr - Generate
        report' and 'ds - Display statistics'. If the current user is not
        'admin', the menu does not include these additional options. The
        function returns the selected menu option as a lowercase string.
    :rtype: str
    """
    # Checking if the current user is 'admin'. If the current user is 'admin',
    # it will display a menu with additional options: generating a report and
    # displaying statistics.
    if curr_user == 'admin':
        menu = input_validation('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate report
ds - Display statistics
e - Exit
: ''').lower()
        return menu

    else:
        menu = input_validation('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
        return menu


##===========================================================================
def reg_user(username_password: dict) -> None:
    """
    The function `reg_user` registers a new user by prompting for a username 
    and password, validating the inputs, and storing the user data in a file.
    If the username already exists, the function will recursively call itself
    until a unique username is provided.
    
    :param username_password: is a dictionary that stores usernames as keys and
    passwords as values.
    :type username_password: dict
    :return: None
    """
    # Check if the new username already exists, it will recursively prompt the
    # user to input another username.
    new_username = input_validation("New Username: ")
    if new_username in username_password.keys():
        print("The user with this name already exists. Please could you"
              " input another user name")
        return reg_user(username_password)

    while True:
        # Request input of a new password.
        new_password = input_validation("New Password: ")

        # Request input of password confirmation.
        confirm_password = input_validation("Confirm Password: ")

        # Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password

            with open(path_user_txt, "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
            break
        # Otherwise you present a relevant message.
        else:
            print("Passwords do no match. Please retry.")


##===========================================================================
def add_task(task_list: list, username_password: dict) -> None:
    '''Allow a user to add a new task to task.txt file
    Prompt a user for the following: 
        - A username of the person to whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - The due date of the task.

    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :param username_password: Dictionary that stores usernames as keys and
        passwords as values.
    :type username_password: dict
    :return: None
    '''

    # Check if the input user exists by recursively prompting the user for
    # valid input.
    task_username = input_validation("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return add_task(task_list, username_password)

    # Ask the user for necessary inputs.
    task_title = input_validation("Title of Task: ")
    task_description = input_validation("Description of Task: ")
    due_date_time = date_validation()

    # Creates a new task adding all inputed early data as a dictionary.
    new_task = {
        'task_ID': str(len(task_list) + 1),
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Adds the new task to task_list and writes it to the file.
    task_list.append(new_task)
    write_tasks_to_file(task_list, path_tasks_txt)

    print("Task successfully added.")
    print('-'*79)


##===========================================================================
def view_all_tasks(task_list: list) -> None:
    """
    Displays all tasks in a user-friendly way.

    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :return: None
    """

    # Iterates through all tasks list and puts all information to the disp_str
    # variable in a user-friendly way to print it in the terminal.
    for t in task_list:
        disp_str = f"Task ID: \t {t['task_ID']}\n"
        disp_str += f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += (f"Date Assigned: \t "
                     f"{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n")
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Complete? \t {"Yes" if t['completed'] is True else "No"}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


##===========================================================================
def view_user_task(task_list: list, curr_user: str) -> None:
    """
    Displays tasks assigned to a specific user.

    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :param curr_user: Username of the user whose tasks need to be displayed.
    :type curr_user: str
    :return: None
    """

    print(f"All the tasks that have been assigned to {curr_user}:\n")

    # List to store tasks ID assigned to the current user.
    user_tasks = []

    # Iterate through task_list and display tasks assigned to the specific user
    # in a user-friendly way.
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task ID: \t {t['task_ID']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += (f"Date Assigned: "
                         f"\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n")
            disp_str += (f"Due Date: "
                         f"\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n")
            disp_str += (f"Task Complete? "
                         f" \t{"Yes" if t['completed'] is True else "No"}\n")
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)

            # Add to the list each task ID assigned to the current user.
            user_tasks.append(t['task_ID'])

    # Asks users to decide whether to choose a particular task to edit or
    # return to the main menu.
    user_task_choice = ''
    while user_task_choice != '-1':
        print('-'*79)
        message_task_choice = ("Please enter either: \n"
                               "a specific task (by entering Task ID number)\n"
                               "‘-1’ to return to the main menu\n: ")
        user_task_choice = input_validation(message_task_choice)
        print('-'*79)

        # Checks if user task choice is assigned to the user, if so asks to
        # choose either mark the task as complete or edit it.
        if user_task_choice in user_tasks:
            message_mark_or_edit = ("Please enter:\n"
            "'m' - if you would like to mark the task as complete\n"
            "'e' - if you would like to edit the task\n: ")
            mark_or_edit_choice = input_validation(message_mark_or_edit)
            print('-'*79)

            # If a user chooses to mark the task as complete change the value
            # of the 'completed' key value to True, rewrite it to the task.txt
            # file, and change the user_task_choice to '-1' to break the while
            # loop.
            if mark_or_edit_choice == 'm':
                task_list[int(user_task_choice) - 1]['completed'] = True
                user_task_choice = '-1'
                write_tasks_to_file(task_list, path_tasks_txt)

            # If a user chooses to edit the task call a function that allows
            # the user to change the due date or username of the person to whom
            # the task is assigned.
            if mark_or_edit_choice == 'e':
                edit_task(user_task_choice, task_list, username_password)
        else:
            print("You entered task that do not assigned to particular user.")


##===========================================================================
def task_overview_report(task_list: list) -> str:
    """
    Generates a task overview report based on the calculated statistics
    including the total number of tasks, completed tasks, uncompleted
    tasks, uncompleted overdue tasks, percentages of incomplete tasks, and
    overdue tasks are also computed.

    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :return: A formatted string containing the task overview report.
    :rtype: str
    """

    # If the task_list is empty, it informs the user that no tasks are
    # available to avoid zero division.
    if len(task_list) == 0:
        return print("Sorry, but you do not have any tasks yet")

    # The function calculates various task statistics based on the provided
    # task_list.
    total_num_tasks = len(task_list)
    completed_tasks = completed_task(task_list)
    uncompleted_tasks = uncompleted_task(task_list)
    uncompleted_overdue = uncompleted_overdue_tasks(task_list)
    percent_uncompleted_tasks = round((uncompleted_tasks * 100) / total_num_tasks)
    percent_overdue_tasks = round((overdue(uncompleted_overdue) * 100)
                                   / uncompleted_tasks)

    # Writes all calculated statistics to task_overview.txt file in a
    # user-friendly way.
    with open(path_task_overview_txt, 'w') as task_overview_file:
        content = f"The total number of tasks is:~`{total_num_tasks}\n"
        content += f"The total number of completed tasks is:~`{completed_tasks}\n"
        content += (f"The total number of uncompleted tasks"
                    f" is:~`{uncompleted_tasks}\n")
        content += (f"The total number of uncompleted and overdue tasks"
                    f" is:~`{len(uncompleted_overdue)}\n")
        content += (f"The percentage of tasks that are incomplete:~`"
                    f"{percent_uncompleted_tasks}%\n")
        content += (f"The percentage of tasks that are overdue"
                    f" is:~`{percent_overdue_tasks}%")

        # The align_to_left function is used to format the content for
        # readability.
        edited_data = align_to_left(content)

        task_overview_file.write(edited_data)
    return edited_data


##===========================================================================
def user_overview_report(task_list: list, username_password: dict) -> str:
    """
    Generates an overview report for registered users based on tasks. 
    The report includes the total number of registered users and the total
    number of tasks. For each user, it computes the percentage of tasks 
    completed, uncompleted, and uncompleted overdue tasks.

    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :param username_password: Dictionary that stores usernames as keys and
        passwords as values.
    :type username_password: dict
    :return: A formatted string containing the task overview report for each
        user.
    :rtype: str
    """

    # Creates a dictionary with users as keys and their corresponding tasks as
    # values.
    user_task = total_amount_of_user_task(task_list, username_password)

    # Determines how many users are registered in the program.
    total_users_num = len([user for user in username_password.keys()])

    # Determines how many tasks are registered in the program.
    total_num_tasks = len(task_list)

    # Creates a list of users to make it easier to iterate through it in the
    # future.
    users_list = [user for user in user_task.keys()]

    # Writes all calculated statistics to user_overview.txt file in a
    # user-friendly way.
    with open(path_user_overview_txt, 'w') as task_overview_file:
        content = f"The total number of registered users is:~`{total_users_num}\n"
        content += f"The total number of tasks is:~`{total_num_tasks}\n"

        # Iterates through each user
        for user in users_list:

            # Calculates the percentage of tasks that are assigned to the
            # particular user.
            percent_of_tasks = round((len(user_task[user]) * 100)
                                      / total_num_tasks)

            # Initializes a counter to count how many tasks the particular
            # user has completed.
            completed = 0
            for task in user_task[user]:
                if task['completed']:
                    completed += 1

            # Checks the number of user tasks to avoid zero division, and
            # displays that the particular user does not have any tasks.
            if len(user_task[user]) == 0:
                content += f"\nUser '{user}' does not have a task.\n"
                continue

            # # Calculate task-related statistics for each user
            percent_of_completed = round(completed * 100 / len(user_task[user]))
            uncompleted = len(user_task[user]) - completed
            percent_of_uncompleted = round(uncompleted * 100 / len(user_task[user]))
            percent_uncompleted_overdue_tasks = round(len
                (uncompleted_overdue_tasks(user_task[user])) * 100 / uncompleted)

            content += f"\n\t{user}\n"
            content += (f"The total number of assigned tasks to the"
                        f" user:~`{len(user_task[user])}\n")
            content += (f"The percentage of the total number of tasks that have"
                        f" been assigned to the user:~`{percent_of_tasks}%\n")
            content += (f"The percentage of the tasks assigned to the user"
                        f" that have been completed:~`{percent_of_completed}%\n")
            content += (f"The percentage of the tasks assigned to the user that"
                        f" must still be completed:~`{percent_of_uncompleted}%\n")
            content += (f"The percentage of the tasks assigned to the user that"
                        f" have not yet been completed and are "
                        f"overdue:~`{percent_uncompleted_overdue_tasks}%\n")

        # The align_to_left function is used to format the content for
        # readability.
        edited_data = align_to_left(content)

        task_overview_file.write(edited_data)
    return edited_data


##===========================================================================
def total_amount_of_user_task(task_list: list, username_password: dict) -> dict:
    """
    Creates a dictionary with users as keys and their corresponding tasks as
    values by iterating through username_password dictionary and assigning only
    particular user's tasks as a list of nested tasks dictionaries.

    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :param username_password: Dictionary that stores usernames as keys and
        passwords as values.
    :type username_password: dict
    :return: A dictionary where keys are usernames and values are lists of
        tasks assigned to each user.
    :rtype: dict
    """

    # Initialize an empty dictionary to store user-task associations.
    dict_users_with_their_tasks = {}

    for user in username_password.keys():

        # Initialize an empty list for tasks related to a specific user.
        list__of_particular_user_task = []
        for task in task_list:
            if user == task['username']:

                # Append the task to the user's list.
                list__of_particular_user_task.append(task)

                # Store the user's tasks in the dictionary.
            dict_users_with_their_tasks[user] = list__of_particular_user_task
    return dict_users_with_their_tasks


##===========================================================================
def align_to_left(content: str) -> str:
    """
    Aligns the lines of input content to the left by adding indentation as
    underscores.

    :param content: The input content with lines separated by newline characters.
    :type content: str
    :return: The aligned content with added indentation to the left.
    :rtype: str
    """

    # Split the content into individual lines. Find the length of the longest
    # line. Initialize an empty string to store the aligned content.
    splited = content.split('\n')
    max_len = len(max(splited, key=len))
    aligned_content = ''

    # Iterates through lines. Calculate the indentation needed for each line.
    # Replace special characters with indentation.
    for line in splited:
        indentation = '_'*((max_len - len(line)) + 3)
        line = line.replace('~`', indentation)
        aligned_content += line + "\n"
    return aligned_content


##===========================================================================
def date_validation() -> str:
    """
    Checks if the input date is in the proper format and later than the current
    date.

    :return: Date in format (YYYY-MM-DD)
    :rtype: str
    """
    # Checks if the input date is in the proper format.
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Checks if the input date is later than the current date.
    if due_date_time >= curr_date:
        return due_date_time.date()
    else:
        print("The due date cannot be before the current date.")
        return date_validation()


##===========================================================================
def input_validation(message: str) -> str:
    """
    Removes spaces at the beginning and end of input and also checks for empty
    input recursively prompting a user for valid input.

    :param message: Massage that will display to a user.
    :type message: str
    :return: Validated user input.
    :rtype: str
    """
    # Removes spaces at the beginning and end of input
    user_input = input(message).strip()

    # Checks for empty input recursively prompting a user for valid input
    if user_input == "":
        print("Sorry, but you inputed nothing.")
        return input_validation(message)
    else:
        return user_input


##===========================================================================
def overdue(uncompleted_overdue:list) -> int:
    """
    Calculates the number of uncompleted tasks that are overdue.

    :param uncompleted_overdue: List of task dictionaries representing
        uncompleted tasks.
    :type uncompleted_overdue: list
    :return: The count of overdue tasks.
    :rtype: int
    """

    counter = 0 # Initialize a counter for overdue tasks.

    # Check if the task's due date is earlier than or equal to the current
    # date.
    for task in uncompleted_overdue:
        if task['due_date'] <= curr_date:
            counter += 1
    return counter


##===========================================================================
def completed_task(task_list: list) -> int:
    """
    Calculates the total number of completed tasks.

   :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :return: The count of completed tasks.
    :rtype: int
    """

    completed = 0
    for task in task_list:
        if task['completed']:
            completed += 1
    return completed


##===========================================================================
def uncompleted_task(task_list: list) -> int:
    """
    Calculates the total number of uncompleted tasks.

    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :return: The count of uncompleted tasks.
    :rtype: int
    """

    uncompleted = 0
    for task in task_list:
        if task['completed'] != True:
            uncompleted += 1
    return uncompleted


##===========================================================================
def uncompleted_overdue_tasks(task_list: list) -> list:
    """
    AI is creating summary for uncompleted_overdue_tasks

    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :return: A filtered list of uncompleted tasks that are overdue.
    :rtype: list
    """

    # Iterates through each task in the input list, checks if the task is
    # uncompleted and its due date has passed, and adds it to the
    # uncompleted_overdue_list.
    uncompleted_overdue_list =[]
    for task in task_list:
        if task['completed'] == False and task['due_date'] <= curr_date:
            uncompleted_overdue_list.append(task)
    return uncompleted_overdue_list


##===========================================================================
def edit_task(username_password: dict, user_task_choice: str,
              task_list: list) -> None:
    """
    Allows the user to edit either the username of the person to whom the task
    is assigned or the due date of the task.

    :param username_password: Dictionary that stores usernames as keys and
        passwords as values.
    :type username_password: dict
    :param user_task_choice: User choice of a specific task (by entering Task
        ID number).
    :type user_task_choice: str
    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :return: None
    """

    # Checks if the selected task is not completed and asks for the user's
    # choice.
    if task_list[int(user_task_choice) - 1]['completed'] == False:
        display_choices = ("Please enter:\n"
                           "'n' if you want to change the username of the
                           " person to whom the task is assigned\n"
                           "'d' if you want to change the due date of the
                           " task\n any other button to choose another task: ")
        edit_task_choice = input_validation(display_choices)

        if edit_task_choice == 'n':
            change_username(username_password, user_task_choice, task_list)

        # Checks, assigns, and writes to the tasks.txt file the new due date.
        if edit_task_choice == 'd':
            task_list[int(user_task_choice) - 1]['due_date'] = date_validation()
            write_tasks_to_file(task_list, path_tasks_txt)
    else:
        print("This task is already completed.")


##===========================================================================
def change_username(username_password: dict, user_task_choice: str,
                    task_list: list) -> None:
    """
    Changes the assigned username for a specific task and checks if the
    username exists.

    :param username_password: Dictionary that stores usernames as keys and
        passwords as values.
    :type username_password: dict
    :param user_task_choice: User choice of a specific task (by entering Task
        ID number).
    :type user_task_choice: str
    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :return: None
    """

    # Displays all usernames to whom it is possible to assign the task.
    print('-'*79)
    print(f"All usernames of people: ", end='')
    print(', '.join(username_password.keys()))

    # Changes the assigned username for a specific task.
    while True:
        message = ("Please enter the name of the person to whom you want to"
        " assign the task to: ")
        new_assigned_user = input_validation(message)

        # Checks if the username exists and write it to the tasks.txt.
        if new_assigned_user in username_password.keys():
            task_list[int(user_task_choice) - 1]['username'] = new_assigned_user
            write_tasks_to_file(task_list, path_tasks_txt)
            break
        else:
            print("Unexist person or incorrect person name!")


##===========================================================================
def write_tasks_to_file(task_list: list) -> None:
    """
    Writes the task list in a text file in a specific format.

    :param task_list: List of dictionaries containing all tasks.
    :type task_list: list
    :return: None
    """

    with open(path_tasks_txt, "w") as task_file:

        # For each task in the task list creates nested task lists with all
        # attributes.
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['task_ID'],
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]

            # Joins attributes with semicolons and appends all lists to one
            # big list.
            task_list_to_write.append(";".join(str_attrs))

        # Write the formatted task strings to the file separates each list by
        # a new line character.
        task_file.write("\n".join(task_list_to_write))


##===========================================================================
curr_date = datetime.now()
DATETIME_STRING_FORMAT = "%Y-%m-%d"
path_user_txt = "user.txt"
path_tasks_txt = "tasks.txt"
path_task_overview_txt = "task_overview.txt"
path_user_overview_txt = "user_overview.txt"


def main():
    # Create tasks.txt if it doesn't exist
    if not os.path.exists(path_tasks_txt):
        with open(path_tasks_txt, "w") as default_file:
            pass

    # Reads from task.txt file data and stores it as a list.
    with open(path_tasks_txt, 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    # Loads task data from a text file and returns a list of dictionaries.
    task_list = []
    for task_ID, t_str in enumerate(task_data, 1):
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['task_ID'] = str(task_ID)
        curr_t['username'] = task_components[1]
        curr_t['title'] = task_components[2]
        curr_t['description'] = task_components[3]
        curr_t['due_date'] = (datetime.strptime(task_components[4],
                                                DATETIME_STRING_FORMAT))
        curr_t['assigned_date'] = (datetime.strptime(task_components[5], 
                                                    DATETIME_STRING_FORMAT))
        curr_t['completed'] = True if task_components[6] == "Yes" else False

        task_list.append(curr_t)



    #====Login Section====
    '''This code reads usernames and password from the user.txt file to 
        allow a user to login.
    '''
    # If no user.txt file, write one with a default account
    if not os.path.exists(path_user_txt):
        with open(path_user_txt, "w") as default_file:
            default_file.write("admin;password")

    # Read in user_data
    with open(path_user_txt, 'r') as user_file:
        user_data = user_file.read().split("\n")

    # Convert to a dictionary
    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    # ensures that the user continues to be prompted for login credentials
    # until they successfully log in.
    logged_in = False
    while not logged_in:

        print("LOGIN")

        # The curr_user and curr_pass variables store the username and
        # password entered by the user.
        curr_user = input("Username: ")
        curr_pass = input("Password: ")

        # Checks if the user exists and passwords are matches.
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print('-'*79)
            print("Login Successful!")
            logged_in = True


    while True:

        # Presents the menu to the user and validate user's input
        print()
        print('='*79)
        menu = display_menu(curr_user)
        print('='*79)

    #=== If the user chooses to register a user ==============================
        if menu == 'r':
            reg_user(username_password)

    #=== If the user chooses to add a task ===================================
        elif menu == 'a':
            add_task(task_list, username_password)

    #=== If the user chooses to view all tasks ===============================
        elif menu == 'va':
            view_all_tasks(task_list)

    #=== To view all the tasks that have been assigned to them ===============
        elif menu == 'vm':
            view_user_task(task_list, curr_user)

    #=== Generates reports and write it to text files ========================
        elif menu == 'gr' and curr_user == 'admin':
            task_overview_report(task_list)
            user_overview_report(task_list, username_password)
            print("The reports were generated successfully.")

    # Displays reports to the terminal and writes them to the file ===========
        elif menu == 'ds' and curr_user == 'admin':
            print(task_overview_report(task_list))
            print(user_overview_report(task_list, username_password))
            print("The reports were generated successfully.")

    # Exit the program =======================================================
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

    # Prints if a user made a wrong choice====================================``
        else:
            print("You have made a wrong choice, Please Try again")


if __name__ == "__main__":
    main()