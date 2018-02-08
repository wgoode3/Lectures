# Week 1 Day 4

## Flask

<img src="http://flask.pocoo.org/static/logo/flask.png" alt="Python" width="200px">

### Virtual Environment

1. <details> 
    <summary>What is a Virtual Environment?</summary>
    A virtual environment is a clean python environment that is seperate from the global python environment that can have just the version of python and libraries and scripts installed that are needed for a project.
</details>

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

app.run(debug=True)
```

### Routing

Routes are the part of the url that comes after our main url, anything after the slash.

```
eg. url = "http://www.myawesomeurl.com/This/is/the/route"
```

They are used to allow users to interact with our website and request additional resources from it.

3. <details> 
    <summary>How do we specify a route in flask?</summary>
    <code>@app.run("/route")</code> 
</details>

We can create additional routes by adding them to the ```server.py```.

```
@app.route("/another_route")
def another_function():
	return render_template("another.html")
```
