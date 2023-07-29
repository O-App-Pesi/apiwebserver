## Identification of the problem you are trying to solve by building this particular app.

Keeping track of different foods and how they affect our body.

## Why is it a problem that needs solving?

It is easy to lose track of what you have eaten. Often we reach for snacks or something quick to eat but don't have the time to consider how this might affect us. If we keep track of this in a diary then we can become aware of our habits and use the data to inform our future choices. This may not just be about weightloss but also about how different foods affect our bodies or just to know how often we eat. Especially if we go out to eat, we might not be able to find out every ingredient but keeping track of how the food made us feel can be very useful. We want to have a balanced diet but our confirmation bias and memory can often let us down, having a diary to track everything uniformly can help keep us accountable.

## Why have you chosen this database system. What are the drawbacks compared to others?



## Identify and discuss the key functionalities and benefits of an ORM

**Database Abstraction Layer**   
Each database uses its own query structure. For example, if you start building an application for the Oracle database but then later switch to using PostgreSQL, you will have to alter the queries. If you build your an application with an ORM then you will not need to change your application's code if you decide the switch databases. The syntax used by ORM's is independent of the database and so can interact with any database.  
**Object Oriented Programming**  
Using an ORM allows developers to create an API which uses the OOP concepts of inheritance, encapsulation and polymorphism. Developers can use classes, build with functions and use things like loops to build the database queries. This makes it much easier for developers since they can work with a language that they already know and don't have to learn the SQL syntax for the database. This is because the ORM handles the data persistence in the database.  
Using a programming language like Python makes the API much more readable than the raw SQL syntax. It also makes it easier to be maintained for developers who are comfortable using Python. Development time can be spent elsewhere since developers don't need to spend time working with the database interactions. The schema in the database are managed by the ORM which maintains the data consistency. 
**Lazy Loading, Eager Loading, and Caching**  
ORMs provide the ability to manage the way the data is accessed. For example, lazy loading allows developers to query only the specific data that they need, such as just the user data. Eager loading is the opposite of this, where everything is loaded. Caching allows query results to be stored for later, this reduces the number of times the database needs to be accessed. With these three different options, developers have a way to regulate the data access and manage things like the network load.  

## Document all endpoints for your API

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
	"diaries": [],
	"meals": []
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