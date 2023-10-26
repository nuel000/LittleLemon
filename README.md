# LittleLemon

## Setting up the Project

- step 1: Activate the virtual enviroment from the root folder (containing the "Scripts" folder) using `source Scripts/actiavte` (ensure to use Gitbash terminal not Powershell).
- step 2: Run the server with the command `python manage.py runserver` and visit the endpoints below
  
Examples of endpoints to test

1. http://127.0.0.1:8000/restaurant/menu/ using GET Method - To get the list of menu items
2. http://127.0.0.1:8000/restaurant/menu/ using POST Method and Filling Form encoded URL with the data to post - To post a menu item to the database
3. http://127.0.0.1:8000/auth/users/ using the POST method - For user registration ensure to specify username, email and password in the form-encoded URL

# Steps for unit testing
1. navigate the the root folder containing the `manage.py` file.
2. run the code `python manage.py test tests.test-model` for testing model
3. run the code `python manage.py test tests.test-views` for testing views
