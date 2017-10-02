# Week 1 Day 1

## Python
<img src="https://www.python.org/static/opengraph-icon-200x200.png" alt="Python" width="200px">

### Python intro

* Created by Guido Van Rossum in 1991, Python is a mature language
* Popular with lots of libraries like: NumPy, SciPy, BeautifulSoup, Scrapy, Twisted
* Used for all sorts of things, not just web design
* Easy to learn with a readable syntax

2. <details> 
	<summary>Why version 2.7 and not 3.6?</summary>
	2.7 is forward compatible with 3.6, but 3.6 is not backward compatible with 2.7. There are sill a lot of peole using Python 2.7 as well. Some Python libraries may still work best in 2.7.
</details>

An example of JavaScript Code

```javascript
function print1to255(){
	for(var i = 1; i < 256; i++){
		console.log(i);
	}
}
```

would look like this

```python
def print1to255():
	for i in range(1, 256):
		print i
```

### The Request Response Cycle

<img src="https://lh4.googleusercontent.com/Wcd9eyXs79rItZ6FP8A_MRhFscsZqDheO9KxFKXlkZV6pOC-uoCPKpLI_XOHltmuG0ZQAE8wfaFvg7Q=w1920-h931-rw" alt="req-res">

2. <details> 
	<summary>What is a web server?</summary>
	A computer system that processes HTTP requests.
</details>

3. <details>
	<summary>What is in the HTTP Response?</summary>
	HTML, CSS, and JavaScript
</details>

4. <details>
	<summary>Where is Python running?</summary>
	On the server, Python (specifically the Flask microframework or the Django framework) will handle the logic of what to do with each HTTP request and what to return in the HTTP repsonse.
</details>

### How do we declare variables?
```python
a = 3
b = True
c = 'd'
d = "abacus"
```

### How can we write a loop?
```python
# the range method
for i in range(1,11):
	print i

# the not range method
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in array:
	print i
```

### How can we write conditionals?
```python
thingThatIsTrue = True

if thingThatIsTrue:
	print "thingThatIsTrue is True"

aCertainNumber = 7

if aCertainNumber % 2 == 0:
	print "aCertainNumber is even"
elif aCertainNumber % 3 == 0:
	print "aCertainNumber is divisible by three"
else:
	print "aCertainNumber is neither of those things"
```

### How do we run Python code?

5. <details> 
	<summary>How do we run Python code?</summary>
	We can run Python in the Python shell directly, or save our code to a file that ends in the <code>.py</code> file extension and tell python to run that file from our terminal.

	Python is an interpreted language, although it does compile our code into bytecode <code>.pyc</code> to be run in the Python shell from time to time.
</details>

### Easter Egg
```python
# Try this in the Python shell
import this
```