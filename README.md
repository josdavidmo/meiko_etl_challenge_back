# Meiko ETL Challenge Back

This is the Django Project. Let's describe the solution for each point:

Download the necessary movies file

1. Generate a relational model using the entities you are able to identify when decomposing the movie file. write the basic unit tests using Pytest.

It is really hard to tell you that I take all data and put it into one model, but I have a reason for that: I am using Postgres. So, I take advantage on it Array Fields in order to make it extensible for all gendres, directors, and actors. This is the model:

![alt text](https://github.com/josdavidmo/meiko_etl_challenge_back/blob/master/doc/models.png?raw=true)

I do not have enought time to made the pytest. But, I know how to do it.

2. Develop a new Django custom command that allows transforming the content of the movies file to a JSON format so that the initial loading of the database is done through fixtures. At this point the performance is important, show by console the time it takes the command to do its work.

The command that I develop was [importdata](https://github.com/josdavidmo/meiko_etl_challenge_back/blob/master/movies/management/commands/importmovies.py) it receives the movie csv [file](https://github.com/josdavidmo/meiko_etl_challenge_back/blob/master/data/movie_metadata.tar.xz) compress. You can set the workers number with `k` in order to runing in a multitask. So the taken time will going down based on the number of workers. By default, it takes the number of CPU to runing.

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

![alt text](https://github.com/josdavidmo/meiko_etl_challenge_back/blob/master/doc/admin.png?raw=true)

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

![alt text](https://github.com/josdavidmo/meiko_etl_challenge_back/blob/master/doc/admin2.png?raw=true)

5. Expose through an API-Rest the necessary endpoints that allow:

- Return all movies in which an actor has participated. Go to [http://localhost/movies/moviebyactor/](http://localhost/movies/moviebyactor/)
```
{
    "count": 2096,
    "next": "http://localhost/movies/moviebyactor/?page=2",
    "previous": null,
    "results": [
        {
            "actor_1_name": "50 Cent",
            "movie_titles": [
                "Get Rich or Die Tryin'",
                "Get Rich or Die Tryin'",
                "Get Rich or Die Tryin'",
                "Get Rich or Die Tryin'"
            ],
            "total": 4
        },
        {
            "actor_1_name": "A.J. Buckley",
            "movie_titles": [
                "The Good Dinosaur",
                "The Good Dinosaur",
                "The Good Dinosaur",
                "The Good Dinosaur"
            ],
            "total": 4
        },
       ...
```
- Return all films directed by a director, sorted by year of publication. Go to [http://localhost/movies/moviebydirector/](http://localhost/movies/moviebydirector/)
```
{
    "count": 2398,
    "next": null,
    "previous": "http://localhost/movies/moviebydirector/?page=239",
    "results": [
        {
            "director_name": "Zackary Adler",
            "movie_titles": [
                "The Rise of the Krays",
                "The Rise of the Krays",
                "The Rise of the Krays",
                "The Rise of the Krays"
            ],
            "total": 4
        },
       ...
```
- Return to the movies grouped by gender and order by major collection. Go to [http://localhost/movies/moviebygender/](http://localhost/movies/moviebygender/)
```
{
    "count": 26,
    "next": "http://localhost/movies/moviebygender/?page=2",
    "previous": null,
    "results": [
        {
            "genre": "Drama",
            "movie_titles": [
                "The Skulls",
                "My Summer of Love",
                "The Lunchbox",
                "Yes",
                "You Can't Take It with You",
                "From Here to Eternity",
                "Grace Unplugged",
                "Foolish",
                "N-Secure",
                "Caramel",
                "The Bubble",
                "The Conversation",
                "Mississippi Mermaid",
                "I Love Your Work",
                ...
```

The above endpoints are read-only.


