1. First step. Create a virtual environment through anaconda.
`conda create -n flask_app python=3.7.3`


2. Install all the dependencies in your application
`pip install -r requirements.txt`
(when is available)
dependencies is are all the pip libraries needed eg. flask, sqlalchemy. 
2a. To generate requirements.text run `pip freeze >> requirements.txt`
run this anytime you run a new library. 

3. Export Flask app.

`export FLASK_APP=flask_app.py `
and then `flask run` 


What are forms?

Web forms are one of the most basic building blocks in any web application. The Flask-WTF extension uses Python classes to represent web forms. A form class simply defines the fields of the form as class variables.

from forms to page templates.

The next step is to add the form to an HTML template so that it can be rendered on a web page.



