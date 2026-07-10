#FLASK
#What is flask?
# Flask is a micro web framework written in Python. 
# It is designed to be lightweight and easy to use, allowing developers to build web applications quickly. 
# Flask provides the necessary tools and features to create web applications, such as routing, request handling, and template rendering, while keeping the core simple and extensible.
# It is often used for small to medium-sized projects and is popular for its flexibility and ease of integration with other libraries and tools.    

#Flask is a lightweight web framework used to build web applications and APIs. It follows a minimal design and provides core features like routing, request handling and template rendering while allowing developers to add extensions as needed.

#why use flask?
# Flask is a popular choice for web development due to its simplicity, flexibility, and ease of use. 
# It allows developers to quickly build web applications and APIs without the overhead of larger frameworks. 
# Flask's modular design enables developers to choose the components they need, making it suitable for small to medium-sized projects. 
# Additionally, Flask has a large community and extensive documentation, making it easier to find resources and support.
#Excellent for API development, prototyping, and small to medium-sized web applications. 
# It is also highly extensible, allowing developers to add functionality as needed.

#Flask ARCHITECTURE
# Flask follows a modular architecture, allowing developers to build applications by combining different components.
#Browser sends a request to the server, which is handled by the Flask application. The application processes the request, interacts with databases or other services if needed, and generates a response. The response is then sent back to the browser for rendering.
#Templates are used to separate the presentation layer from the application logic, allowing developers to create dynamic web pages. Flask uses the Jinja2 templating engine to render templates and generate HTML content.

#Whats routing in flask?
# Routing in Flask refers to the process of mapping URLs to specific functions or views in your application. It allows you to define how your application responds to different URL patterns and HTTP methods (GET, POST, etc.).
# In Flask, you define routes using decorators, which are special functions that modify the behavior of other functions. The most common decorator used for routing is @app.route(), which associates a URL pattern with a specific function that will be executed when that URL is accessed.

#Dynamic routing allows you to create routes that can accept parameters, enabling you to build more flexible and interactive web applications. For example, you can define a route that accepts a user ID as a parameter and displays the corresponding user's profile page.    
#How is dynamic routing done in flask?
# Dynamic routing in Flask is done by defining route parameters in the URL pattern. You can specify variable parts of the URL by using angle brackets (< >) in the route definition. These parameters can then be passed to the associated view function as arguments.  

#Templates in flask.
#What is a template?
#A template is a file that contains the structure and layout of a web page, along with placeholders for dynamic content. In Flask, templates are typically written in HTML and can include special syntax provided by the Jinja2 templating engine. This allows developers to create reusable templates that can be populated with data from the application, making it easier to generate dynamic web pages.

#Why do we use templates?
#To separate the presentation layer from the application logic, making it easier to manage and maintain the code. Templates allow developers to create reusable components and layouts, reducing duplication and improving consistency across the application. They also enable dynamic content generation, allowing web pages to be customized based on user input or data from the server.
#To create dynamic web pages that can display different content based on user input or data from the server. Templates allow developers to define placeholders for dynamic content, which can be populated with data at runtime, enabling the creation of personalized and interactive web experiences.
#To improve code organization and maintainability by separating the HTML structure from the application logic. This separation allows developers to work on the presentation layer independently of the backend code, making it easier to update and modify the user interface without affecting the underlying functionality.