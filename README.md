# Manual-API-CRUD-Operation
Manual Student API CRUD Operation 

# How to Set Up and Run the Django Project

# 1 First, check if Python is installed on your system.
Open Command Prompt and type:
python
If Python opens the interactive shell, it means it's installed. Type exit() to exit the shell.

# 2 Create a new folder for your project and open Command Prompt inside that folder.
(You can do this by typing cmd in the folder path bar in File Explorer.)

# 3 Create a virtual environment for the project:
python -m venv foldername

python -m venv myenv (for better understanding keep myenv)

# 4 Activate the virtual environment:
myenv\Scripts\activate (for Windows)
or
source myenv/bin/activate (for macOS/Linux)

# 5 Install Django:
pip install django

# 6 To check if Django is installed successfully, use any of these commands:
pip list
or
pip freeze

# 7 Create a new Django project:
django-admin startproject projectname
django-admin startproject myproject
(You can change myproject to any name you prefer.for better understanding i have kept myproject )

# 8 Navigate into the project folder:
cd shopsphere

# 9 Run the development server:
python manage.py runserver
