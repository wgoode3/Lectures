# Week 1 Day 3

## OOP

<img src="https://www.python.org/static/opengraph-icon-200x200.png" alt="Python" width="200px">

1. <details> 
    <summary>What is OOP?</summary>
    OOP stands for Object Oriented Programming, it is an important programming paradigm in which data and certain methods can be contained within objects.
</details>

2. <details>
    <summary>What are the advantages of OOP?</summary>
    <ul>
        <li>Helps us DRY out our code (don't repeat yourself)</li>
        <li>Forces you to plan ahead which leads to higher quality code</li>
        <li>Don't need to know how an object works exactly to use it</li>
        <li>If you need to change the code you can change the object itself and not hunt down every use of the object in your project</li>
        <li>Widely used in web design and game design</li>
        <li>Most importantly: the frameworks we'll be using will use OOP</li>
    </ul>
</details>

## How do we write a class?

```python
class Student(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.numberOfBelts = 0
    def addBelt(self):
        self.numberOfBelts += 1
        return self
    def say(self, thing):
        print(self.name, "says", thing)
        return self
```

3. <details>
    <summary>How do we make (instantiate) a student?</summary>
    <code>student1 = Student("Amina", "amina@google.com")</code>
</details>

4. <details>
    <summary>What is <code>self</code>?</summary>
    <code>self</code> is whatever that object happens to be. Think of it as a placeholder for the names of the objects that we will be making.
    If you remember the <code>this</code> from JavaScript, <code>self</code> does essentially the same thing.
</details>

5. <details>
    <summary>What are the attributes in the class <code>Student</code>?</summary>
    The attributes are the variables: <code>self.name</code>, <code>self.email</code>, and <code>self.numberOfBelts</code>
</details>

6. <details>
    <summary>What are the methods in the class <code>Student</code>?</summary>
    <code>addBelt()</code> and <code>say()</code>
</details>

```python
student1.addBelt().addBelt()
print(student1.numberOfBelts)
```

7. <details>
    <summary>What is printed in the above code?</summary>
    2<br>
    We are able to run add belt twice in the same line because we are using chaining (<code>return self</code>). This is a powerful concept, but be careful as we don't always want to <code>return self</code>.
</details>

## Inheritance

We can rewrite the above Student class into two seperate classes to illustrate inheritance.

```python
class Person(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def say(self, thing):
        print(self.name, "says", thing)

class Student(Person):
    def __init__(self, name, email):
        super(Student, self).__init__(name, email)
        self.numberOfBelts = 0
    def addBelt(self):
        self.numberOfBelts += 1
        return self
    def show(self):
        print self.name, "has", self.numberOfBelts, "belt(s)"
        return self
```

8. <details>
    <summary>What does <code>super</code> do?</summary>
    <code>super</code> runs the <code>__init__</code> method in the class <code>Person</code> which creates the <code>self.name</code> and <code>self.email</code> attributes.
</details>

```python
bob = Person("Bob", "bob@gmail.com")
bob.say("hello")

jenny = Student("Jenny", "jenny@gmail.com")
jenny.say("goodbye")
```

9. <details>
    <summary>What will happen when we run the following code?</summary>
    <code>"Bob says hello"</code><br>
    <code>"Jenny says goodbye"</code>
</details>

10. <details>
    <summary>Why?</summary>
    The class <code>Student</code> inherits the method <code>say()</code> from the class <code>Person</code>
</details>

## Modules and Packages

The beauty of OOP is how we don't have to write all the code ourself, there are fantastic libraries that already exist that we can use.

Give the following code a try sometime.

```python
from datetime import datetime
print(datetime.now())
print(datetime.now().strftime("%m/%d/%Y"))

from random import random, randrange
print(random())
print(randrange(1,11))
```

## Multi-Arguments

```python
def testingArgs(*args):
    for arg in args:
        print(arg)

testingArgs("hello", 2, False)

def testingKwargs(**kwargs):
    for kw in kwargs:
        print(kw, kwargs[kw])

testingKwargs(color="red", number=6, price="$5.99")
```

Using the "splat operator" ```*``` we can turn all our arguments into a list of arguments. This way our function can receive any number of arguments. We can also use ```**``` to create a dictionary of key value pairs from our arguments. You may not need to do these much, but they are handy to know. 
