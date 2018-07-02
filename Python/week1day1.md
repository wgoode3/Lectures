# Week 1 Day 1

## Python

<img src="https://www.python.org/static/opengraph-icon-200x200.png" alt="Python" width="200px">

### Python intro

* Created by Guido Van Rossum in 1991, Python is a mature language
* Popular with lots of libraries like: NumPy, SciPy, BeautifulSoup, Scrapy, Twisted
* Used for all sorts of things, not just web design
* Easy to learn with a readable syntax

An example of JavaScript Code

```javascript
function print1to255(){
    for(var i = 1; i < 256; i++){
        console.log(i);
    }
}
```

would look like this in Python

```python
def print1to255():
    for i in range(1, 256):
        print i
```

1. <details> 
    <summary>Why version 3.6 and not 2.7?</summary>
    The changes between 3.6 and 2.7 are very minimal, and support for 2.7 will end in 2020. Most libraries written in 2.7 have versions for 3.6. 3.6 has some really nice improvements like the way division works and the way the range function works.
</details>

### The Request Response Cycle

<img src="https://i.imgur.com/fVHiuUz.png" alt="req-res">

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
    print(i)
    
# the not range method
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in array:
    print(i)
```

### How can we write conditionals?
```python
thingThatIsTrue = True

if thingThatIsTrue:
    print("thingThatIsTrue is True")

aCertainNumber = 7

if aCertainNumber % 2 == 0:
    print("aCertainNumber is even")
elif aCertainNumber % 3 == 0:
    print("aCertainNumber is divisible by three")
else:
    print("aCertainNumber is neither of those things")

# it can read just like plain english

groceryList = ["beef stock", "thyme", "pearl onions", "cremini mushrooms"]

if "carrots" not in groceryList:
    groceryList.append("carrots")

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
