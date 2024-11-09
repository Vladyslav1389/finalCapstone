
# Task Manager

This Task Management System is a Python-based application that allows users to manage tasks efficiently. It includes functionalities for user registration, task creation, task overview reporting, and user-specific task management. The system supports different user roles, with the admin user having additional capabilities like generating and displaying statistics.

## Features
User Authentication: Secure login system with username and password.

User Registration: Admin can register new users.

Task Management: Users can add tasks, view all tasks, and view tasks assigned to them.

Reporting: Generate and view task and user overview reports (admin only).

Input Validation: Ensures clean and valid user inputs.

File Storage: User and task data is stored in text files for persistence.

## File Structure
main.py: The main script containing all functionalities.

user.txt: Stores user data (username and password).

tasks.txt: Stores task data.

task_overview.txt: Stores task overview report.

user_overview.txt: Stores user overview report.

## The table of content

1. Installation section.
2. Usage section.
3. Section for credits.
## Installation section
Prerequisites
Python 3.x

Basic knowledge of Python and command line interface

## Installation
#### Clone the repository:
    git clone https://github.com/Vladyslav1389/finalCapstone.git
    cd finalCapstone
### #Run the application:
    task-manager.py

## Usage section

***
### Options that you can do:
    
   1. Login

   ![First loggin](https://github.com/Vladyslav1389/finalCapstone/blob/master/Images/First%20Login.png)
  
  Note: For the first time, the default credentials you should use are: Username-admin, Password-password.

   2. Adding a new user
   ![Adding new user](https://github.com/Vladyslav1389/finalCapstone/blob/master/Images/Adding%20new%20user.png)

   3. Adding a task
   ![Adding a new task](https://github.com/Vladyslav1389/finalCapstone/blob/master/Images/Adding%20a%20task.png)

   4. Viewing all tasks
   ![View all tasks](https://github.com/Vladyslav1389/finalCapstone/blob/master/Images/View%20all%20tasks.png)

   5. View the tasks that are assigned to the current user

   - Here you can either edit the task or mark it as completed.

   * Marking a task as completed.     
   ![Marking task as complete](https://github.com/Vladyslav1389/finalCapstone/blob/master/Images/Mark%20as%20completed.png)
   
   * Editing the person assigned to this task or due date.
   ![Changing the pearson](https://github.com/Vladyslav1389/finalCapstone/blob/master/Images/Editing%20the%20name%20of%20the%20user%20the%20task%20is%20assigned%20to.png)

   ![Changing due date](https://github.com/Vladyslav1389/finalCapstone/blob/master/Images/Editing%20the%20due%20date%20of%20the%20task.png)

   6. Generating a report that will be saved into two ".txt" files
   ![Generating a report](https://github.com/Vladyslav1389/finalCapstone/blob/master/Images/Generating%20the%20report.png)

   7. Displaying a report to the terminal.
   ![Displaying a report](https://github.com/Vladyslav1389/finalCapstone/blob/master/Images/Displaying%20the%20report.png)
***
## Section for credits

The whole project was written by [Vladyslav Shcherbak](https://github.com/Vladyslav1389 "https://github.com/Vladyslav1389")
