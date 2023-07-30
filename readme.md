## R1: Identification of the problem you are trying to solve by building this particular app.

Keeping track of different foods and how they affect our body.

## R2: Why is it a problem that needs solving?

It is easy to lose track of what you have eaten. Often we reach for snacks or something quick to eat but don't have the time to consider how this might affect us. If we keep track of this in a diary then we can become aware of our habits and use the data to inform our future choices. This may not just be about weightloss but also about how different foods affect our bodies or just to know how often we eat. Especially if we go out to eat, we might not be able to find out every ingredient but keeping track of how the food made us feel can be very useful. We want to have a balanced diet but our confirmation bias and memory can often let us down, having a diary to track everything uniformly can help keep us accountable.

## R3: Why have you chosen this database system?

PostgreSQL is an open source database management system. This means that it is good for students because it doesn't require any cost to use. PostgreSQL also natively supports JSON and Binary JSON making it perfect for developing a webserver API.

## What are the drawbacks compared to others?

When there are a lot of small read-operations to the database, PostgreSQL performs poorly. This is because of the way PostgreSQL handles new client connections, it uses about 10MB of data to fork a new process every time. If there are many small read-operations that need to be completed, PostgreSQL handles them cumbersomely. MySQL is a database that can handle lots of connections more efficiently as it was developed to prioritize speed (Drake, 2014).   
PostgreSQL is fully open source which means that it is maintained by volunteer contributors. Anyone can add to PostgreSQL and the code base can be manipulated to suit an individuals needs even for commercial operations. However, this has the drawback of having an inconsistent and incomplete documentation since it is not managed by any singular entity. Databases systems such as Oracle and even MySQL, which also has an open source version, are owned by the company Oracle so there is a more strict of cohesive development plan in place. This means the documentation is likely to be more consistent and up to date.   
PostgreSQL has a high skill ceiling and requires a knowledgeable team of engineers to get the most out its functionality. PostgreSQL is well known for its complex queries meaning that it can be used to narrow down data for high level functions. This means that it is not as beginner friendly as a database system like MySQL which is more simple. To put it simply, the bar to entry is quite high and PostgreSQL would take time to implement and understand for those unfamiliar with it.

## R4: Identify and discuss the key functionalities and benefits of an ORM

**Database Abstraction Layer**   
Each database uses its own query structure. For example, if you start building an application for the Oracle database but then later switch to using PostgreSQL, you will have to alter the queries. If you build your an application with an ORM then you will not need to change your application's code if you decide the switch databases. The syntax used by ORM's is independent of the database and so can interact with any database.  

**Object Oriented Programming**  
Using an ORM allows developers to create an API which uses the OOP concepts of inheritance, encapsulation and polymorphism. Developers can use classes, build with functions and use things like loops to build the database queries. This makes it much easier for developers since they can work with a language that they already know and don't have to learn the SQL syntax for the database. This is because the ORM handles the data persistence in the database.  
Using a programming language like Python makes the API much more readable than the raw SQL syntax. It also makes it easier to be maintained for developers who are comfortable using Python. Development time can be spent elsewhere since developers don't need to spend time working with the database interactions. The schema in the database are managed by the ORM which maintains the data consistency.  

**Lazy Loading, Eager Loading, and Caching**   
ORMs provide the ability to manage the way the data is accessed. For example, lazy loading allows developers to query only the specific data that they need, such as just the user data. Eager loading is the opposite of this, where everything is loaded. Caching allows query results to be stored for later, this reduces the number of times the database needs to be accessed. With these three different options, developers have a way to regulate the data access and manage things like the network load.  

## R5: Document all endpoints for your API

Endpoint documentation should include
HTTP request verb
Required data where applicable
Expected response data
Authentication methods where applicable

### 1. Diary_Entry

**GET | Response Data:**  
```
[
	{
		"diaries_diary_id": 1,
		"meals_meal_id": 1,
		"health_analysis_ha_id": 1,
		"timestamp": "2023-07-29T02:10:50.865732",
		"diary": {
			"diary_title": "My First Diary"
		},
		"meal": {
			"meal_name": "Delicious Teriyaki",
			"is_takeaway": true,
			"kilojoules": 8000,
			"notes": "made me fart"
		},
		"health_analysis": {
			"ha_id": 1,
			"physical_change": "felt lethargic",
			"mood_change": "was angry"
		}
	},
	{
		"diaries_diary_id": 2,
		"meals_meal_id": 2,
		"health_analysis_ha_id": 2,
		"timestamp": "2023-07-29T07:15:55.773737",
		"diary": {
			"diary_title": "After Work Diary"
		},
		"meal": {
			"meal_name": "Chicken Special",
			"is_takeaway": true,
			"kilojoules": 5000,
			"notes": "rejuvenating"
		},
		"health_analysis": {
			"ha_id": 2,
			"physical_change": "explosive diarrhoea",
			"mood_change": "Felt Bubbly"
		}
	}
]
```

**GET (Single) | localhost:8080/diaryentry/1/2/2 | Response Data:**

```
{
	"diaries_diary_id": 1,
	"meals_meal_id": 2,
	"health_analysis_ha_id": 2,
	"timestamp": "2023-07-29T02:58:41.328041",
	"diary": {
		"diary_title": "My First Diary"
	},
	"meal": {
		"meal_name": "Chicken Special",
		"is_takeaway": true,
		"kilojoules": 5000,
		"notes": "rejuvenating"
	},
	"health_analysis": {
		"ha_id": 2,
		"physical_change": "explosive diarrhoea",
		"mood_change": "Felt Bubbly"
	}
}
```

**POST | Required Data:**
```
{
	"diaries_diary_id": 1,
	"meals_meal_id": 2,
	"health_analysis_ha_id": 1,
	"timestamp": "2023-07-29 07:15:55.773737"
}
```
**Response Data:**
```
{
	"diaries_diary_id": 1,
	"meals_meal_id": 2,
	"health_analysis_ha_id": 1,
	"timestamp": "2023-07-29T07:15:55.773737",
	"diary": {
		"diary_title": "My First Diary"
	},
	"meal": {
		"meal_name": "Chicken Special",
		"is_takeaway": true,
		"kilojoules": 5000,
		"notes": "rejuvenating"
	},
	"health_analysis": {
		"ha_id": 1,
		"physical_change": "felt lethargic",
		"mood_change": "was angry"
	}
}
```
**DELETE | localhost:8080/diaryentry/1/2/1 | Response Data After POST:**

```
{
	"message": "Diary Entry with keys 1, 2, 1, deleted"
}
```
**DELETE | if no Entry:**
```
{
	"error": "Diary not found with one or more specified IDs"
}
```
**PUT/PATCH | localhost:8080/diaryentry/1/2/2 | Required Data:**
```
{
	"timestamp": "2023-07-29 07:15:55.773737",
	"diaries_diary_id": "2"
}
```
**Response Data:**
```
{
	"diaries_diary_id": 2,
	"meals_meal_id": 2,
	"health_analysis_ha_id": 2,
	"timestamp": "2023-07-29T07:15:55.773737",
	"diary": {
		"diary_title": "After Work Diary"
	},
	"meal": {
		"meal_name": "Chicken Special",
		"is_takeaway": true,
		"kilojoules": 5000,
		"notes": "rejuvenating"
	},
	"health_analysis": {
		"ha_id": 2,
		"physical_change": "explosive diarrhoea",
		"mood_change": "Felt Bubbly"
	}
}
```

### User/Authorisation

**GET (Single) | localhost:8080/auth/1 | JSON Web Token | Response Data:**
```
{
	"user_id": 1,
	"email": "user@user.com"
}
```

**POST | localhost:8080/auth/login | JSON Web Token | Required Data:**
```
{
	"email": "user@user.com",
	"password": "user123"
}
```
**Response Data:**
```
{
	"email": "user@user.com",
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU5NzAzNiwianRpIjoiOGNlMWNhZDYtY2I5MS00ZWZmLTlhYzktOTA1NzJhOGM1MmI1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE2OTA1OTcwMzYsImV4cCI6MTY5MDY4MzQzNn0.vWP9Au-Cv-BmVL3_82SraAaI4TKGGJLCHHSYNE2qndQ"
}
```
**POST | localhost:8080/auth/register | JSON Web Token | Required Data:**
```
{
	"email": "user2@user.com",
	"password": "user2pw"
}
```
**Response Data:**
```
{
	"user_id": 2,
	"email": "user2@user.com",
}
```
**PUT/PATCH | localhost:8080/auth/update/2 | JSON Web Token | Required Data:**
```
{
	"email": "newemail@user.com",
	"password": "newpassword"
}
```
**Response Data:**
```
{
	"email": "newemail@user.com",
	"user_id": 2
}
```
**DELETE | localhost:8080/auth/2 | JSON Web Token | Response Data:**
```
{
	"message": "User with email: newemail@user.com deleted successfully"
}
```
**DELETE | if no Entry:**
```
{
	"error": "User not found with specified email"
}
```

## Diary

**GET | JSON Web Token | Response Data:**
```
[
	{
		"diary_id": 1,
		"users_user_id": 1,
		"diary_title": "My First Diary"
	},
	{
		"diary_id": 2,
		"users_user_id": 1,
		"diary_title": "After Work Diary"
	}
]
```
**GET (Single)| localhost:8080/diary/2 | JSON Web Token | Response Data:**
```
{
	"diary_id": 2,
	"users_user_id": 1,
	"diary_title": "After Work Diary"
}
``` 
**POST | JSON Web Token | Required Data:**
```
{
	"diary_title": "Weekend Diary"
}
```
**Response Data:**
```
{
	"diary_id": 3,
	"users_user_id": 1,
	"diary_title": "Weekend Diary"
}
```
**DELETE | localhost:8080/diary/3 | JSON Web Token | Response Data:**
```
{
	"message": "Diary: Weekend Diary deleted successfully"
}
```
**DELETE | if no Entry:**
```
{
	"error": "Diary not found with id 3"
}
```

**PUT/PATCH | localhost:8080/diary/2 | JSON Web Token | Required Data:**
```
{
	"diary_title": "Updated Weekend Diary"
}
```
**Response Data:**
```
{
	"diary_id": 2,
	"users_user_id": 1,
	"diary_title": "Updated Weekend Diary"
}
```

## Meal

**GET | JSON Web Token | Response Data:**
```
[
	{
		"meal_id": 1,
		"users_user_id": 1,
		"meal_name": "Delicious Teriyaki",
		"is_takeaway": true,
		"kilojoules": 8000,
		"notes": "made me fart"
	},
	{
		"meal_id": 2,
		"users_user_id": 1,
		"meal_name": "Chicken Special",
		"is_takeaway": true,
		"kilojoules": 5000,
		"notes": "rejuvenating"
	}
]
```
**GET | localhost:8080/meals/1 | JSON Web Token | Response Data:**
```
{
	"meal_id": 1,
	"users_user_id": 1,
	"meal_name": "Delicious Teriyaki",
	"is_takeaway": true,
	"kilojoules": 8000,
	"notes": "made me fart"
}
```
**POST | JSON Web Token | Required Data:**
```
{
	"meal_name": "Tea Egg",
	"is_takeaway": false,
	"kilojoules": 50,
	"notes": "very delicious"
}
```
**Response Data:**
```
{
	"meal_id": 3,
	"users_user_id": 1,
	"meal_name": "Tea Egg",
	"is_takeaway": false,
	"kilojoules": 50,
	"notes": "very delicious"
}
```
**DELETE | localhost:8080/meals/3 | JSON Web Token | Response Data:**
```
{
	"message": "Meal: Tea Egg deleted successfully"
}
```
**DELETE | if no Entry:**
```
{
	"error": "Meal not found with id 3"
}
```
**PUT/PATCH | localhost:8080/meals/1 | JSON Web Token | Required Data:**
```
{
	"meal_name": "Chicken Nugget",
	"is_takeaway": true,
	"kilojoules": 300,
	"notes": "oily"
}
```
**Response Data:**
```
{
	"meal_id": 1,
	"users_user_id": 1,
	"meal_name": "Chicken Nugget",
	"is_takeaway": true,
	"kilojoules": 300,
	"notes": "oily"
}
```

## Health_Analysis

**GET | Response Data:**
```
[
	{
		"mood_change": "was angry",
		"ha_id": 1,
		"physical_change": "felt lethargic"
	},
	{
		"mood_change": "Felt Bubbly",
		"ha_id": 2,
		"physical_change": "explosive diarrhoea"
	}
]
```
**GET (Single) | localhost:8080/healthanalysis/2 | Response Data:**
```
{
	"mood_change": "Felt Bubbly",
	"ha_id": 2,
	"physical_change": "explosive diarrhoea"
}
```
**POST | Required Data:**
```
{
	"physical_change": "Wet my pants",
	"mood_change": "tired"
}
```
**Response Data:**
```
{
	"mood_change": "tired",
	"ha_id": 3,
	"physical_change": "Wet my pants"
}
```

**DELETE | localhost:8080/healthanalysis/3 | Response Data:**
```
{
	"message": "Health Analysis 3 deleted successfully"
}
```
**DELETE | if no Entry:**
```
{
	"error": "Health Analysis not found with id 3"
}
```
**PUT/PATCH | localhost:8080/healthanalysis/2 | Required Data:**
```
{
	"physical_change": "felt hungry"	
}
```
**Response Data:**
```
{
	"mood_change": "Felt Bubbly",
	"ha_id": 2,
	"physical_change": "felt hungry"
}
```

## R6: An ERD for your App

![ERD](docs/ERD%20Final.jpg)


## R7: Detail any third party services that your app will use

### Flask  
Flask is a python web framework. It uses the Web Server Gateway Interface (WSGI), Werkzeug and jinja2 to creates apps that are simple and scalable. Flask is known as a microframework because it can be built on with other python libraries (Python Tutorial, 2021).

### Marshmallow
Marshmallow is an Object Relational Mapper (ORM). ORMs enable apps written in a language like Python to communicate with relational databases. Marshmallow does not depend on any specific framework to function. Marshmallow converts complex data types to Python native data types (Loria, 2023). 

### Bcrypt  
Bcrypt is used to create hashed passwords. Hashed passwords are hidden passwords that do not represent the actual password but a string of characters. This way, passwords are stored on the database by a representation and cannot be directly intercepted during queries.

### Flask-JWT-Extended
JWT-Extended provides functionality for using JSON Web Tokens. It allows the use of JWTs to protect controller routes. 
Further functionalities include: "Adding custom claims to JSON Web Tokens, automatic user loading (current_user), custom claims validation on received tokens, refresh tokens, first class support for fresh tokens for making sensitive changes,token revoking/blocklisting, storing tokens in cookies and CSRF protection" (Gilbert, 2023, Features).

## R8 Describe your projects models in terms of the relationships they have with each other

The user model has:  
- a user_id which is a primary key, and an integer
- an email which is a String of 255 characters, not nullable and must be unique
- a password which is a String of 255 characters and not nullable.
- a diaries field which nests the related data from the diaries table and will cascade delete the related entities
- a meals field which nests the related data from the meals table and will cascade delete the related entities   

The diary model has:
- a diary_id which is a primary key, and an integer
- users_user_id which is a foreign key, an integer and not nullable
- a diary_title which is a String of 100 characters
- a user fields which nests the related data from the user table 
- a diary_entries field which nests the related data from the diary_entries table

The meal model has:
- a meal_id which is a primary key, and an integer
- a users_user_id which is a foreign key, an integer and is not nullable
- a meal_name which is a String with 100 characters
- an is_takeaway field which is a boolean
- kilojoules which is an integer and is not nullable
- notes which is a String of 255 characters
- a user fields which nests the related data from the user table 
- a diary_entries field which nests the related data from the diary_entries table  

The diary_entry model has:
- a diaries_diary_id which is a composite key, an integer and not nullable
- a meals_meal_id which is a composite key, an integer and not nullable
- a health_analysis_ha_id which is a composite key, an integer and not nullable
- a diary field which nests the related data from the diaries table
- a meal field which nests the related data from the meals table
- a health_analysis field which nests the related data from the health_analysis table   

The heal_analysis model has:
- a ha_id which is a primary key, and an integer
- a physical_change which is a String with 255 characters and not nullable
- a mood_change which is a String with 255 characters and not nullable
- a diary_entries field which nests the related data from the meals table and cascade deletes the related entities

## R9: Discuss the database relations to be implemented in your application  

Each entity of the users relation has a user_id, email and password field. User_id is the primary key. Users shares its primary key with the meals and diaries relations. One user has zero or many diaries, and one user has zero or many meals.  
Each entity of the diaries relation has a diary_id, users_user_id and a diary_title. The users_user_id is the foreign key pointing back to an entity in the users relation. The diary_id is the primary key. Diaries shares its primary key with the diary_entries relation. One diaries entity has zero or many diary_entries, but each diary_entries entity has one and only one diaries entity.   
Each entity of the meals relation has a meal_id, users_user_id, meal_name, is_takeaway, kilojoules and notes field. The users_user_id is the foreign key pointing back to an entity in the users relation. The meal_id is the primary key. Meals shares its primary key with the diary_entries relation. One meals entity has zero or many diary_entries, but each diary_entries entity has one and only one meals entity.   
The meals and diaries relations have a many to many relationship with diary_entries as the join relation.   
Each entity of the health_analysis relation has a ha_id, physical_change and mood_change field. The ha_id is the primary key. Health_analysis shares its primary key with the diary_entries relation. One health_analysis entity has zero or more diary_entries, but each diary_entries entity has one and only one health_analysis entity.   
Health_analysis also has a many to many relationship with meals and diaries. Each health_analysis entity can have zero or many diaries and zero or many meals. Each meals entity can have zero or many health_analysis. Each diaries entity can have zero or many health_analysis.   
Each entity of the diary_entries relation has a diaries_diary_id, meals_meal_id, health_analysis_ha_id, and a timestamp. The diary_entries relation exists as a join table for the diaries, meals and health_analysis relation. The diaries_diary_id, meals_meal_id and health_analysis_ha_id act as a composite primary key, each is also a foreign key pointing back to their respective relations of diaries, meals and health_analysis.

## R10: Describe the way tasks are allocated and tracked in your project

https://trello.com/invite/b/492R6pVv/ATTI7ad0644517782521b274457e0c5b32ce923D87AB/webserver-api

![trello board 1](docs/Trello%20Board%201.jpg)

I used Trello to allocate tasks and track my project. I had 5 lists on my board with titles Workbook, Coding, Doing, Pending Review and Done. Workbook was where I listed each requirement for the documentation on a card. Coding was where I listed the programming requirements for the project. When I was working on a specific task, I would move the card to Doing until it was done. If I felt like I needed to review it again later, I would move the card to Pending Review. Once everything on the card was completed, I would finally move the card to Done.

![R5](docs/R5%20Trello%20Board.jpg)

For the documentation requirements that had specific criteria, I added a description.

![Model](docs/Diary%20Entry%20Model.jpg)

For each model, I added a CRUD checklist.

## References 

Abba, IV 2022, *What is an ORM -- The Meaning of Object Relational Mapping Database Tools*, July 30, 2023, https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/.

altexsoft 2019, "Comparing Database Management Systems: MySQL, PostgreSQL, MSSQL Server, MongoDB, Elasticsearch and others," *AltexSoft*, July 30, 2023, https://www.altexsoft.com/blog/business/comparing-database-management-systems-mysql-postgresql-mssql-server-mongodb-elasticsearch-and-others/.

Boltic 2023, "PostgreSQL vs MySQL: Critical Differences & Key Features (Advantages & Disadvantages)," *Boltic*, July 30, 2023, https://www.boltic.io/blog/postgresql-performance-vs-mysql.

Countryman, M 2011, *Flask-Bcrypt --- Flask-Bcrypt 1.0.1 documentation*, July 30, 2023, https://flask-bcrypt.readthedocs.io/en/1.0.1/.

Drake, M 2014, *SQLite vs MySQL vs PostgreSQL: A Comparison Of Relational Database Management Systems*, July 30, 2023, https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems#postgresql.

Gilbert, L 2023, *Flask-JWT-Extended*, July 30, 2023, https://pypi.org/project/Flask-JWT-Extended/.

Kong, Q, Siauw, T & Bayen, A 2020, *Python programming and Numerical Methods: A Guide for Engineers and Scientists*, Academic Press, https://pythonnumericalmethods.berkeley.edu/notebooks/chapter07.03-Inheritance-Encapsulation-and-Polymorphism.html.

Linked In Team *How can you implement eager loading in ORM with different frameworks?*, July 16, 2023, https://www.linkedin.com/advice/3/how-can-you-implement-eager-loading.

Linked In Team & Adnan Rafiq, M *What are some best practices for using ORM caching and lazy loading?*, July 16, 2023, https://www.linkedin.com/advice/1/what-some-best-practices-using-orm-1e.

Loria, S 2023, *marshmallow*, July 30, 2023, https://pypi.org/project/marshmallow/.

MongoDB *An Introduction to Data Persistence*, July 16, 2023, https://www.mongodb.com/databases/data-persistence.

Python Basics *What is Flask Python - Python Tutorial*, July 30, 2023, https://pythonbasics.org/what-is-flask-python/.

'Tofunmi O., P 2015, "A Brief Explanation of Database abstraction Layer: Writing database queries for the future," *Medium*, July 16, 2023, https://medium.com/@paultofunmi/a-brief-explanation-of-database-abstraction-layer-writing-database-queries-for-the-future-7a1c84c9a45d.

TrustRadius 2021, *What's the best RDBMS? PostgreSQL vs MySQL*, *YouTube*, July 30, 2023, https://www.youtube.com/watch?v=EOTY-p5h74E.

uniwebsidad *8.1. Why Use an ORM and an Abstraction Layer? (The definitive guide of Symfony 1.2)*, July 16, 2023, https://uniwebsidad.com/libros/symfony-1-2-en/chapter-8/why-use-an-orm-and-an-abstraction-layer.