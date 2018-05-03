# Week 1 Day 5

## SQL, MySQL, and ERDs  

<img src="https://d1eq8vvyuam4eq.cloudfront.net/sql_logo.svg?ver=1520522243" alt="SQL" width="300px">

### SQL and MySQL

1. <details> 
    <summary>What is SQL?</summary>
    <strong>Structured Query Language</strong> is a language used for storing, retreiving and manipulating data in a relational database.
</details>

2. <details> 
    <summary>What is MySQL?</summary>
    MySQL is a popular, open source, database. Think of MySQL as a brand of SQL database. Other examples of SQL databases include: MariaDB, PostgreSQL, SQLite, etc...
</details>

### ERD

3. <details> 
    <summary>What is an ERD?</summary>
    An <strong>Entity Relationship Diagram</strong> is a visual representation of how your database looks and behaves
</details>

An Example ERD:

| students   |              |
|------------|--------------|
| id         | INT          |
| name       | VARCHAR(255) |
| email      | VARCHAR(255) |
| created_at | DATETIME     |
| updated_at | DATETIME     |

4. <details> 
    <summary>What is a Primary Key? What is the Primary Key in the above ERD?</summary>
    A Primary Key is a database column designated to uniquely identify each table record. In the above ERD the primary key is <code>id</code>.
</details>

5. <details> 
    <summary>What type of data is an INT?</summary>
    A number. In MySQL an INT can be between -2147483648 and 2147483647	for a signed integer or 0 and 4294967295 for unsigned.
</details>

6. <details> 
    <summary>What type of data is an VARCHAR? What does the 255 represent?</summary>
    A VARCHAR is a string, 255 is the maximum length of that string.
</details>

7. <details> 
    <summary>What type of data is a DATETIME?</summary>
    Just like it sounds, DATETIME stores date and time information.
</details>

### Relationships

The reason why we call MySQL a relational database is because we can store relationships between tables.

8. <details> 
    <summary>What types of relationships exist?</summary>
    <ul>
      <li>One to One</li>
      <li>One to Many</li>
      <li>Many to Many</li>
      <li>Self Join</li>
    </ul>
</details>

### One to One

An example of a One to One relationship:

| customers   |              |
|-------------|--------------|
| id          | INT          |
| name        | VARCHAR(255) |
| email       | VARCHAR(255) |
| created_at  | DATETIME     |
| updated_at  | DATETIME     |
| address_id  | INT          |

| billing_addresses   |              |
|---------------------|--------------|
| id                  | INT          |
| street              | VARCHAR(255) |
| city                | VARCHAR(255) |
| state               | VARCHAR(255) |
| zipcode             | VARCHAR(255) |
| created_at          | DATETIME     |
| updated_at          | DATETIME     |

9. <details> 
    <summary>What is a Foreign Key? What column in the above ERD is the Foreign Key?</summary>
    A Foreign Key is used to link two tables together. It is the same number as the Primary Key of the row of data in the related table.
    In the above example <code>address_id</code> is the Foreign Key
</details>

### One to Many

| owners     |              |
|------------|--------------|
| id         | INT          |
| name       | VARCHAR(255) |
| email      | VARCHAR(255) |
| created_at | DATETIME     |
| updated_at | DATETIME     |

| pets       |              |
|------------|--------------|
| id         | INT          |
| name       | VARCHAR(255) |
| species    | VARCHAR(255) |
| breed      | VARCHAR(255) |
| age        | TINYINT      |
| created_at | DATETIME     |
| updated_at | DATETIME     |
| owner_id   | INT          | 

10. <details> 
    <summary>How is a one to many different than a One to One?</summary>
    In the above example, an owner can own more than one pet
</details>

### Many to Many

| actors     |              |
|------------|--------------|
| id         | INT          |
| name       | VARCHAR(255) |
| created_at | DATETIME     |
| updated_at | DATETIME     |

| movies      |              |
|-------------|--------------|
| id          | INT          |
| title       | VARCHAR(255) |
| year        | INT          |
| created_at  | DATETIME     |
| updated_at  | DATETIME     |  

| casts       |     |
|-------------|-----|
| actor_id    | INT |
| movie_id    | INT |

11. <details> 
    <summary>How is a Many to Many different than a One to Many?</summary>
    An actor or actress can start in more than one movie, <strong>and</strong> a movie can have more than one actress or actor.
</details>
