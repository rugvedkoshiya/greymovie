from django.shortcuts import render, get_object_or_404
from .models import MoviePost

# Create your views here.

def homePage(request):
    movies = MoviePost.objects.all()
    params = {'movies': movies}
    return render(request, 'index.html', params)

def moviePage(request, id):
    movie = get_object_or_404(MoviePost, pk=id)
    params = {'movie_id': movie}
    return render(request, 'moviePage.html', params)