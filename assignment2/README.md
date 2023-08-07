# Prerequisite:- Virtual environment should be activated

# 1.) For starting the server, use this command : python3 manage.py runserver

# 2.) Then, to acces the web application, follow the url http://127.0.0.1:8000/ , Homepage will open

# 3.) Now search any movie with title only or title with year
Note: If we don't use year, then the latest movie with that name will render on the browser with detail,

# 4.) OMDB API return only one movie at a time in response

# 5.) We can rate the movie and on submit rating with tha name and year will be save in the database

# 6.) On Movie details page we shows 2 ratings, one is IMDB rating that comes from OMDB API response, and one is our average rating that we save in our database.

# 7.) Used Cache so that unnecessary requests can be avoided.