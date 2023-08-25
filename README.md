
# API DOCUMENTATION
![download](https://github.com/devsylva/TaskFlow-API/assets/67736638/08e112b2-6fb4-4f54-9d05-e9c003ebd5b7)

Welcome to the documentation for Dispatch Hub! This guide provides developers with the necessary information to interact with our API and integrate it into their applications.


# Overview  
TaskFlow API is a Task Management Application RESTful API. The objectives of this application is to provide users with tools and features that help them efficiently manage their tasks, improve productivity, and stay organized.

The ultimate goal of a task management application is to empower users to manage their tasks effectively, reduce stress, and enhance their overall productivity and organization.


# Tech Stack
- Language: Python 3.11.3
- Framework: Django 4.0+
- Database: Dbsqlite3
- Methodology: Test Driven Development

# Objectives

###  Task Creation and Organization
Allow users to create tasks easily and organize them based on different parameters such as due dates, priority, categories, and projects. 

###  Task Tracking and Status Updates
Enable users to track the progress of their tasks, update task statuses (e.g., to-do, in progress, completed), and get a clear overview of tasks that need attention.

###  Deadline Management:
Help users keep track of task deadlines by providing reminders, notifications, and a clear visualization of upcoming due dates.

###  Collaboration and Sharing:
Facilitate collaboration among teams by allowing users to assign tasks to colleagues, share task details, and communicate within the application.

###  Time Management:
Provide tools to estimate and track the time required to complete tasks, helping users allocate their time effectively and avoid overloading themselves.

###  Prioritization and Sorting:
Allow users to set task priorities and sort tasks based on importance, urgency, or custom criteria, aiding in making informed decisions about task order.

###  Customization:
Offer flexibility in customizing task categories, labels, tags, and views to match users' preferred workflows and organizational methods.

###  Data Visualization and Insights:
Provide visual representations of task distribution, completion rates, and productivity trends, allowing users to gain insights into their task management habits.

###  Integration with Calendars and Tools:
Integrate with users' calendars and other productivity tools to synchronize task deadlines, meetings, and events.

###  Mobile Accessibility:
Ensure the application is accessible from mobile devices, allowing users to manage tasks on the go.

###  Data Security and Privacy:
Prioritize the security and privacy of user data, implementing proper authentication, encryption, and access controls.

###  Backup and Sync:
Implement data backup and synchronization features to prevent data loss and ensure tasks are accessible from multiple devices.

# ER-Diagram
![TaskFlow (1)](https://github.com/devsylva/TaskFlow-API/assets/67736638/21e56cdc-b00f-449d-9fa4-a9accac86420)



# Getting Started
To run the API locally, follow these steps:

1. Clone the repository: 

```
git clone https://github.com/devsylva/TaskFlow-API.git
```

2. Create a virtual environment inside the project directory: 

```
python -m venv venv
```

3. Activate the virtual environment: 

```
source venv/bin/activate
```

4. Install dependecies: 

```
pip install -r requirements.txt
```

5. Change `.env.templates` in the src/taskflow direct to `.env` and setup your environment variables

6. Setup the database: 

```
python manage.py migrate
```

7. Create a superuser account: 

```
python manage.py createsuperuser
```

8. Start the development server: 

```
python manage.py runserver
```


# Running Tests
Tests are organized into different files within the app's tests directory. Here's how to run them

1. To run all the tests, use the following command:

```
python manage.py test
```

2. To run a single test file, use the following command [replacing `<app_name>` and `<test_file>` with the appropriate values]:

```
python manage.py test <app_name>.tests.<test_file>
```

# Authentication 
Authentication is required for most endpoints in the API. To authenticate, include an access token in the `Authorization` header of your request. The access token can be obtained by logging in to your account or registering a new account.

# API Authentication Endpoints 
The following endpoints are available in the API:

-   `api/user/signup/` (POST): to allow users register an account.
-   `api/user/login/` (POST): to allow users to log in into their account.
-   `api/user/login/refresh/` (POST): to allow user refresh to get their access token after it expires.
-   `api/user/confirm-email/<uidb64>/<token>/` (GET): to allow users confirm their email address.
-   `api/user/logout/` (POST): to allow users to log out of their account.
-   `api/user/change_password/` (POST): to allow users change there account password.

# API Task Operations Endpoints
The following endpoints are available in the API:

- `api/task/task_view/` (POST): allow users create tasks.
- `api/task/task_view/` (GET): getting all task owned by the logged in user in order or priority and deadline if provided.
- `api/task/task_detail/` (GET): getting a single task.
- `api/task/task_detail/` (PUT): updating a task.
- `api/task/task_detail/` (DELETE): deleting a task.
- `api/task/tag_view/` (POST): allow users create tag.
- `api/task/tag_view/` (GET): getting all tags owned by the logged in user.
- `api/task/tag_detail/` (GET): getting a single tag.
- `api/task/tag_detail/` (PUT): updating a tag.
- `api/task/tag_detail/` (DELETE): deleting a tag.
- `api/task/category_view/` (POST): allow users create category.
- `api/task/category_view/` (GET): getting all category owned by the logged in user.
- `api/task/category_detail/` (GET): getting a single category.
- `api/task/category_detail/` (PUT): updating a category.
- `api/task/category_detail/` (DELETE): deleting a category.


# Limitations
### 1. Celery Redis Tasks and Testing Environment

TaskFlow utilizes Celery for background task processing. However, running Celery tasks with a Redis broker requires specific configuration, including a dedicated environment with Redis server installed. Users who wish to leverage Celery tasks need to set up this environment, which might not be feasible in all development or testing setups.

### 2. Windows Compatibility

TaskFlow's development and testing have primarily been focused on Unix-like operating systems such as Linux and macOS. While efforts have been made to support Windows environments, there might be differences in behavior due to environment-specific factors that Windows does not provide. Users using Windows are advised to thoroughly test the app's functionality to ensure optimal performance.

### 3. External Dependencies

TaskFlow relies on various external dependencies, such as third-party libraries and services (e.g., Amazon S3 for backups). The availability and reliability of these external dependencies might affect certain features of the app. Users should be cautious of potential service disruptions or compatibility issues with these dependencies.

### 4. Scalability Considerations

While TaskFlow is designed to be scalable, the performance of the app might vary based on factors such as the size of the user base, task complexity, and the underlying hardware and infrastructure. Large-scale deployments should be carefully planned and optimized to ensure efficient task management and responsiveness.

### 5. Data Security

TaskFlow implements security measures to protect user data. However, it's essential for users to handle sensitive information with care. The app might not account for all possible security scenarios, and users should take additional measures if dealing with highly sensitive data.

### 6. Limited Offline Functionality

TaskFlow heavily relies on internet connectivity for real-time synchronization and collaboration features. Offline functionality is limited, and users should ensure a stable internet connection to fully utilize the app's capabilities.

## Conclusion

TaskFlow offers robust task management capabilities, but it's important to understand its limitations to make informed decisions about its usage. Users should consider the app's compatibility with their specific environment and requirements before adopting it for their task management needs.

# Contributing

Contributions to this project are welcome! Go through our [GUIDELINES](https://github.com/devsylva/TaskFlow-API/blob/main/CONTRIBUTING.md)


# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
