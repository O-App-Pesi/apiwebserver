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

## 



