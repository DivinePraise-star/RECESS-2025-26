#Import flask
from flask import Flask, render_template

#create an instance of the Flask class
#''__name__ is a special variable in Python that represents the name of the current module.
#When you create a Flask application, you typically pass __name__ as an argument to the Flask class constructor. This allows Flask to determine the root path of the application and locate resources such as templates and static files.

app = Flask(__name__)

#Decorators
#In Flask, decorators are used to define routes for your application. A route is a URL pattern that is associated with a specific function, which is called when the route is accessed. Decorators allow you to easily map URLs to functions in your Flask application. 
# /The @app.route('/') decorator is used to define a route for the root URL of the application. When a user accesses the root URL (e.g., http://localhost:5000/), the function associated with this route will be executed.

@app.route('/')

#Define the function to display a message when the root URL is accessed. The function returns a simple string "Hello, World!" as the response to the user's request. This message will be displayed in the browser when the root URL is visited.
def home():
    #return "Hello, World!"
    
   return "<h1>Welcome to my Flask App!</h1>"

#@app.route('/')
#def home():
#    return render_template('index.html')

#Routing about page
@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is the about page of my Flask app.</p>"


#Exercise 1
#Map the following URLs
#/myStory
@app.route('/myStory')
def my_story():
    return "<h1>My Story</h1><p>This is my story page.</p>"
#/contact
@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1><p>This is the contact page of my Flask app.</p>"

#Dynamic Routing
@app.route('/user/<username>')
def user_profile(username):
    return f"<h1>User Profile</h1><p>Welcome, {username}!</p>"

from flask import Flask, render_template

app = Flask(__name__)

# Exe 2: Create a Dynamic Route on myStory to display your myStory
@app.route('/myStory/<story_id>')
def my_story(story_id):
    # You can use the story_id to fetch the corresponding story from a database or any other data source.
    # For demonstration purposes, we'll just return a simple message with the story_id.
    return f"<h1>My Story</h1><p>This is my story with ID: {story_id}</p>"

@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = {"name": "Divine", "role": "Software Engineer"}
    return render_template('profile.html', user=user, id=user_id)

#To ensure your server runs only if the script is executed directly (not imported as a module), you can use the following code. This is a common practice in Python to prevent certain code from being run when the module is imported elsewhere.
if __name__ == '__main__':
    #Run the Flask application in debug mode, which provides helpful error messages and automatically reloads the server when code changes are detected.
    app.run(debug=True)     


