# Week 2 Day 3

## Flask + MySQL

<img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/62/MySQL.svg/440px-MySQL.svg.png" alt="MySQL" width="200px">

Up until now, we have been forced to use ```session``` to store data when users are interacting with our website. Session is a useful tool but it has some limitations. **One**, it is unique to each user who visits our website and **Two** it is being stored not on our server, but on the browser of our users. Session will not be a suitable way for us to store data for a long period of time or in a manner that isn't specific to the user. So how could we store data longer term and on our server?

Databases will be the answer, and perhaps the most popular one in use today is MySQL. MySQL is an open source relational-database and it uses SQL (Structured Query Language). Up until now we have been interacting with MySQL using MySQL Workbench. We will still be making use of this tool to create ERDs and forward-engineer them into working databases. However the Workbench is simply a visual tool for interacting with our MySQL Server. We can interact with that MySQL server using Python using the ```PyMySQL``` library.

```shell
source flaskEnv/bin/activate
pip install PyMySQL
```

### Let's take a look at the following code

In the folder were we created our Flask server we will create a new file called ```mysqlconnection.py```.

```python
import pymysql.cursors
class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root',
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        self.connection = connection
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
            finally:
                self.connection.close() 
                
def connectToMySQL(db):
    return MySQLConnection(db)
```

And in our ```server.py```...

```python
from flask import Flask
from mysqlconnection import connectToMySQL

app = Flask(__name__)
mysql = connectToMySQL('mydb')

print("all the users", mysql.query_db("SELECT * FROM users;"))

if __name__ == "__main__":
    app.run(debug=True)
```

<details>
  <summary>When we run <code>server.py</code> what happens with our <code>mysqlconnection.py</code></summary>
    We create a variable called <code>mysql</code> and set it equal to what is returned by the function <code>connectToMySQL('mydb')</code>.
</details><br>

<details>
    <summary>What does <code>connectToMySQL(db)</code> in our <code>mysqlconnection.py</code> return?</summary>
    It returns an instance of the MySQLConnection class.
</details><br>

<details>
    <summary>What attributes does the MySQLConnection class have?</summary>
    only <code>self.connection</code>
</details><br>

<details>
    <summary>What methods does the MySQLConnection class have?</summary>
    only <code>query_db</code>
</details><br>

<details>
    <summary>In our server.py, when we run <code>mysql.query_db("SELECT * FROM users;")</code> which variable of query_db is <code>"SELECT * FROM users;"</code>?</summary>
    This string is the query variable.
</details>

<details>
    <summary>What is <code>query.lower().find("insert")</code> checking for? What about <code>query.lower().find("select")</code>?</summary>
    Checking if the type of query is an <code>INSERT</code> statement. The other is checking for a <code>SELECT</code> statement.
</details>

