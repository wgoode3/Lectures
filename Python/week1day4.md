# Week 1 Day 4

## Flask

<img src="http://flask.pocoo.org/static/logo/flask.png" alt="Python" width="400px">

### Virtual Environment

1. <details> 
    <summary>What is a Virtual Environment?</summary>
    A virtual environment is a clean python environment that is seperate from the global python environment that can have just the version of python and libraries and scripts installed that are needed for a project.
</details>

We can install virtualenvironment using:

| OS                 | Command                          |
|:------------------:|:--------------------------------:|
| Mac/Linux:         | pip install virtualenv           |
| Windows:           | python -m pip install virtualenv |


We can create a virtualenvironment named ```flaskEnv``` using:

| OS         | Command                                  |
|:----------:|:----------------------------------------:|
| Mac/Linux: | virtualenv flaskEnv -p python3           |
| Windows:   | python -m virtualenv flaskEnv -p python3 |

We can activate a virtualenvironment named ```flaskEnv``` using:

| OS                            | Command                                        |
|:-----------------------------:|:----------------------------------------------:|
| Mac/Linux:                    | source flaskEnv/bin/activate                   |
| Windows command prompt :      | call flaskEnv/Scripts/activate                 |
| Windows 10 command prompt :   | . flaskEnv/Scripts/activate                    |
| Windows git bash :            |  source flaskEnv/Scripts/activate              |


### Flask

2. <details> 
    <summary>What is a Framework?</summary>
    It's a standard structure for how to implement a software project. Contains both the tools needed to do repetitive tasks and the may generate needed project files as well.
</details>

3. <details> 
    <summary>What is a Microframework?</summary>
    Like a framework but for a minimalistic web application. Less complex than a full stack framework. 
</details>

The following code is an example of a flask server.

```python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)

```

### Templates

By making a new folder called templates in our project folder we can return a file like ```index.html``` to our users instead of a string as we did above.

```
|-> HelloWorld/
	|-> server.py
	|-> templates/
		|-> index.html
```

```html
<!DOCTYPE html>
<html>
<head>
	<title>Hello World</title>
</head>
<body>
	<h1>Hello World</h1>
</body>
</html>
```

We will need to change our ```server.py``` accordingly.

```python

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### Routing

Routes are the part of the url that comes after our main url, anything after the slash.

```
eg. url = "http://www.myawesomeurl.com/This/is/the/route"
```

They are used to allow users to interact with our website and request additional resources from it.

4. <details> 
    <summary>How do we specify a route in flask?</summary>
    <code>@app.route("/route")</code> 
</details>

We can create additional routes by adding them to the ```server.py```.

```
@app.route("/another_route")
def another_function():
	return render_template("another.html")
```

### Static

5. <details> 
    <summary>What is a static file?</summary>
    A file that doesn't change, in the context of our webapp the css, js, and images. 
</details>

To link to static files we can create a new folder called static. In order to keep the static folder organized we can also create subfolders for css, js and images.

```
|-> HelloWorld/
    |-> server.py
    |-> templates/
        |-> index.html
    |-> static/
        |-> css/
            |-> style.css
        |-> js/
            |-> script.js
        |-> img/
            |-> flask.png
```

Then we can use the following tags to access these in our ```index.html```.

```html

<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">

<script type="text/javascript" src="{{ url_for('static', filename='js/script.js') }}"></script>

<img src="{{ url_for('static', filename='img/flask.png') }}">

``` 
