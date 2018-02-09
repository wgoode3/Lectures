# Week 1 Day 5

## Flask Part 2

<img src="http://flask.pocoo.org/static/logo/flask.png" alt="Python" width="400px">

### Forms

You should have seen something like this before.

```html
<form action="/process" method="post">
	Your Name: <input type="text" name="name" placeholder="Your name:"><br>
	Your Email: <input type="text" name="email" placeholder="Your email:"><br>
	<input type="submit" value="Sign Up!">
</form>
```

1. <details> 
    <summary>When a user submits this form where does it go?</summary>
    The form is submitted to the server.
</details>

### Request, GET, and POST

```python
from flask import Flask, render_template, request, redirect
```

2. <details> 
    <summary>What is request?</summary>
    Request is the HTTP request. We can use it to access the form data.
</details>

We can access the data in a route that looks like ```"/process"```

```python
@app.route("/process", methods=["POST"])
def process():
	print(request.form)
	return redirect("/")
```

3. <details> 
    <summary>What is a GET request?</summary>
    If we submit the form with a <code>method="get"</code> it will pass the form data through the url like <code>"localhost:5000/process?name=example&email=example@example.com"</code>. This is fine for a simple form like a search, but might be insecure if the form has a password or credit card number.
</details>

4. <details> 
    <summary>What is a POST request?</summary>
    If we submit the form with a <code>method="post"</code> it doesn't pass the form data in the url and instead sends it as part of the HTTP request. We can access this data in flask using <code>request.form</code>.
</details>

### Session

5. <details> 
    <summary>What is Session?</summary>
    Session is a variable we can store on the user's web browser and we can access in our <code>server.py</code> or in our templates. We can set session and access session as if it were a dictionary.
</details>

```python
from flask import Flask, render_template, session

# also don't forget to set a secrey key

app.secret_key = "This is a secret key!"
```

We can set a variable like this in our ```server.py```.

```python
session["example"] = "This is an example"
```

And access it in ```index.html``` like this.

```html
<p>{{ session["example"] }}</p>

<!-- This also works -->

<p>{{ session.example }}</p>
```

When would we want to use session?

Are their any drawbacks to using session?

### Hidden Inputs

```html
<input type="hidden" name="secret" value="I am a secret">
```

6. <details> 
    <summary>What is hidden input?</summary>
	Exactly what it sounds like, an input that isn't displayed in a form.
</details>

### Route Parameters

We can also pass information as part of a route.

```html
<table>
	<tr>
		<td>Product</td>
		<td>Price</td>
		<Action</td>
	</tr>
	<tr>
		<td>Dojo t-shirt</td>
		<td>$15.99</td>
		<td><a href="/buy/1">Buy</a></td>
	</tr>
	<tr>
		<td>Dojo Hat</td>
		<td>$11.99</td>
		<td><a href="/buy/2">Buy</a></td>
	</tr>
	<tr>
		<td>Dojo Algorithm Book</td>
		<td>$34.99</td>
		<td><a href="/buy/3">Buy</a></td>
	</tr>
</table>
```

In the ```server.py```

```python
@app.route("/buy/<id>")
def buy(id):
	print("Someone is buying product " + id)
	return redirect("/")
```

We can access the ```id``` as a variable.

### Validations

7. <details> 
    <summary>Why would we need to validate form data?</summary>
	To insure data that we might want to save into a database is correct or in the right format. Later we will use these same strategies to enable users to authenticate themselves to your application.
</details>

8. <details> 
    <summary>How do we validate data?</summary>
	Use lots of conditionals!
	
	<code>
		valid = True
		if len(request.form["name"]) < 1:
			valid = False<br>
	</code>
</details>

#### Flash

To display validation errors to your users use Flash!

9. <details> 
    <summary>What is Flash?</summary>
	Flash is like a session variable that is only displayed to your user once. Then it dissapears in a <i>flash!</i>
</details>

```python
from flask import Flask, render_template, session, flash, request
```

```python
valid = True
if len(request.form["name"]) < 1:
	flash("Name is required!")
	valid = False
```

And we can display the errors in our html with.

```html
{% with messages = get_flashed_messages() %}
	{% if messages %}
		<ul>
		{% for message in messages %}
			<li>{{message}}</li>
		{% endfor %}
		</ul>
	{% endif %}
{% endwith %}
```

#### Regex?

10. <details> 
    <summary>What is Regex?</summary>
	Regex is short for Regular Expressions. It is a way we can find patterns in text or even search text.
</details>

```python
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
```

```python
valid = True
if not EMAIL_REGEX.match(request.form["email"]:
	flash("Invalid Email!")
	valid = False
```

Let's dissect the regex above.

In the pattern above the ```^``` signifies the beginning of a pattern and the ```$``` signifies the end of a pattern. The ```[a-zA-Z0-9.+_-]+``` means that there can be as many letters between ```a``` and ```z``` and or ```A``` and ```Z``` and or numbers between ```0``` and ```9``` and any of the special characters ```.```, ```+```, ```_```, and ```-```. the ```@``` means there must be an ```@``` in between those two blocks of letters and numbers. The ```\.``` means there must be a ```.``` in the sequence after the second block of characters. The last block after the ```.``` can only be composed of capital or lowercase letters and it can also be of any length.
