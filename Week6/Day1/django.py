#Why do we use a virtual environment?
#A virtual environment is used to create an isolated environment for Python projects. 
# This allows you to manage dependencies and packages specific to a project without affecting the global Python installation or other projects. 
# It helps avoid version conflicts and ensures that your project has the exact versions of libraries it needs to run correctly. 
# It also makes it easier to share your project with others, as they can set up the same environment using a requirements file.
# It also allows for better organization and management of project dependencies, making it easier to maintain and update your codebase over time.

#Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. 
# It follows the model-template-views (MTV) architectural pattern and provides a robust set of tools for building web applications quickly and efficiently.  

# Django includes features such as an ORM (Object-Relational Mapping) for database interactions, a built-in admin interface, authentication mechanisms, and support for URL routing, making it a popular choice for web development.

#How to install Django in a virtual environment:
#1. Create a virtual environment:
#   python -m venv myenv
#2. Activate the virtual environment:
#   source myenv/bin/activate 
#   On Windows: myenv\Scripts\activate
#3. Install Django:
#   pip install django

#How to create a Django project:
#1. Create a new Django project:
#   django-admin startproject myproject
#2. Navigate to the project directory:
#   cd myproject
#3. Run the development server: 
#   python manage.py runserver

#How to create a Django app:
#1. Create a new Django app:
#   python manage.py startapp myapp

#How do we deactivate a virtual environment?
#To deactivate a virtual environment, you can simply run the command: deactivate    

#How to check the installed packages in a virtual environment?
#To check the installed packages in a virtual environment, you can use the command: pip list    

#How to create a requirements.txt file?
#To create a requirements.txt file, you can use the command: pip freeze > requirements.txt  

#How to install packages from a requirements.txt file?
#To install packages from a requirements.txt file, you can use the command: pip install -r requirements.txt 

#How to check the version of python and pip in a virtual environment?
#To check the version of Python in a virtual environment, you can use the command: python --version
#To check the version of pip in a virtual environment, you can use the command: pip --version

#How to check the version of Django in a virtual environment?
#To check the version of Django in a virtual environment, you can use the command: python -m django --version

#What is a model in Django?
#In Django, a model is a Python class that represents a database table. 
# It defines the structure of the data, including the fields and their types, as well as any relationships between different models. 
# Models are used to interact with the database, allowing you to create, read, update, and delete records in a structured way. 
# Each model class is typically associated with a specific table in the database, and Django's ORM (Object-Relational Mapping) handles the translation between the model and the underlying database schema.

#Example of a simple model usage in realworld:
#Let's say we are building a blog application. We can create a model called "Post"  
# that represents a blog post in our application. The model might look like this:
from django.db import models    

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

#MVT stands for Model-View-Template, which is the architectural pattern used in Django applications.
#1. Model: The model represents the data structure and handles the interaction with the database. It defines the fields and behaviors of the data you want to store. In Django, models are defined as Python classes that inherit from django.db.models.Model.
#2. View: The view is responsible for processing user requests, retrieving data from the model, and returning the appropriate response. Views contain the logic for handling user interactions and determining what data to display. In Django, views are typically defined as Python functions or classes that take a request object and return a response object.

#How to create a view in Django:
#To create a view in Django, you can define a function or class in the views.py file of your app. Here's an example of a simple function-based view:
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, World!")

#How can i see my view through the terminal?
#To see your view through the terminal, you can run the Django development server using the command: python manage.py runserver.
#Once the server is running, you can open a web browser and navigate to the URL that maps to your view. For example, if your view is mapped to the root URL ("/"), you can access it by going to http://127.0.0.1:8000/

#How to map a view to a URL in Django:
#To map a view to a URL in Django, you need to define a URL pattern in the urls.py file of your app. Here's an example of how to map the my_view function to a URL:
from django.urls import path

#Which command do we use to create a view file in Django project directory through terminal?
#In Django, you don't need to create a view file through the terminal. The views.py file is automatically created when you create a new app using the command: python manage.py startapp myapp. You can then define your views in the views.py file of your app.
#Command to create a view file in Django project directory through terminal is: python manage.py startapp myapp



#3. Template: The template is responsible for rendering the user interface and presenting the data to the user. Templates are HTML files that can include dynamic content using Django's template language. They allow you to separate the presentation layer from the business logic, making it easier to maintain and update the user interface.
