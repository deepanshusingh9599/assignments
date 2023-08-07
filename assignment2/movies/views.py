from django.shortcuts import render, HttpResponseRedirect
import requests
import json
from django.core.cache import cache
from .serializers import MoviesSerializers
from .models import Movies
from django.db.models import Avg
from django.urls import reverse


# Create your views here.

def homepage(request):
    """
    This API function is for POST Method for searching the movie by movie title and GET Method for normally render the homepage.
    """
    if request.method == "POST":
        payload = request.POST
        title = payload.get('t', None)
        year = payload.get('y', None)
        plot = payload.get('plot', None)
        url = "http://www.omdbapi.com/?apikey=7bdf66a5"
        if not title:
            msg = {"info": "Please enter a movie name to search"}
            return render(request, 'movies/base.html', msg)
        else:
            url += f"&t={title}"
        if year:
            url += f"&y={year}"
        if plot:
            url += f"&plot={plot}"
        key = url
        # getting data from cache if exists
        cache_data = cache.get(key.upper())
        if cache_data is None:
            data = requests.get(url)
        else:
            data = cache_data
        response_data = json.loads(data.text)

        if not str(response_data.get('Response')) == "False":
            # adding data in cache table if not exists
            cache.add(key.upper(), data, timeout=None)
            # For calculating our average rating that is stored in our database.
            average_rating = Movies.objects.filter(name=response_data['Title'], year=response_data['Year'])
            if average_rating.exists():
                rating = average_rating.aggregate(Avg('rating'))
                response_data['rating'] = rating
            return render(request, 'movies/home.html', response_data)
        else:
            msg = {"info": "Please enter a correct movie name to search."}
            return render(request, 'movies/base.html', msg)
    else:
        return render(request, 'movies/base.html')


def rating(request):
    """
       This API function is Saving the movie rating record in our database.
       """
    data = request.POST
    name = data.get('movie')
    rating = data.get('stars', 0)
    year = data.get('year')
    movie_data = {
        "name": name,
        "year": int(year),
        "rating": int(rating)
    }
    movie_ser = MoviesSerializers(data=movie_data)

    if movie_ser.is_valid():
        movie_ser.save()
    return HttpResponseRedirect('/')
