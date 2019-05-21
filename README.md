# Meiko ETL Challenge Back

This is the Django Project. Let's describe the solution for each point:

Download the necessary movies file

1. Generate a relational model using the entities you are able to identify when decomposing the movie file. write the basic unit tests using Pytest.

It is really hard to tell you that I take all data and put it into one model, but I have a reason for that: I am using Postgres. So, I take advantage on it Array Fields in order to make it extensible for all gendres, directors, and actors. This is the model:


2. Develop a new Django custom command that allows transforming the content of the movies file to a JSON format so that the initial loading of the database is done through fixtures. At this point the performance is important, show by console the time it takes the command to do its work.

The command that I develop was `importdata` it receives the movie csv file compress. You can set the workers number with `k` in order to runing in a multitask. So the taken time will going down based on the number of workers. By default, it takes the number of CPU to runing.

```
movies_1    | Successfully creation fixtures: 0.491 <-- csv to json just take this!
movies_1    | 
movies_1    | real	0m1.601s
movies_1    | user	0m1.593s
movies_1    | sys	0m0.252s
movies_1    | Installed 5042 object(s) from 11 fixture(s) <-- using loaddata command
movies_1    | 
movies_1    | real	0m16.588s
movies_1    | user	0m11.256s
movies_1    | sys	0m0.819s
```
It will be created into fixtures folder.

3. Using the Django’ Admin, register the models you consider in order to generate a dashboard that is close enough to the structure of the movies file.

You can see it in admin.py file. Here is some screen shots:

4. In the admin, generate the necessary custom filters for these in ability to show the result of the following questions:

- Which are the 10 movies that raised the most money?
- What are the 10 films that raised the least money?
- Which are the 7 films that spent the most money to produce?
- What are the 7 films that spent the least money to produce?
- Which movie genre raised the most money for each year?
- Which genre do people like best?
- Which 5 directors have the best reputation?

At least 5 of the above filters must be implemented, an additional score is given if all are implemented.

Just clic on filter menu.

5. Expose through an API-Rest the necessary endpoints that allow:

- Return all movies in which an actor has participated
- Return all films directed by a director, sorted by year of publication
- Return to the movies grouped by gender and order by major collection

The above endpoints are read-only.
