from django.db import models

# Create your models here.

class MoviePost(models.Model):
    STREAMING_SERVICES = (('netflix', 'Netflix'),
                        ('primevideo', 'Primevideo'),
                        ('hotstar', 'Disney+ Hotstar'),
                        ('sonyliv', 'SonyLiv'),
                        ('zee5', 'Zee5'),
                        ('youtube', 'YouTube'),
                        ('hbomax', 'HBO Max'),
                        ('altbalaji', 'ALT Balaji'))
    # YES_NO = (('yes', 'Yes'), ('no', 'No'))
    # personal_post_id = models.AutoField()
    movie_title = models.CharField(verbose_name = "Movie Title",max_length=50)
    movie_description = models.TextField(verbose_name = "Movie Description", default=None, null=True, blank=True)
    movie_date = models.DateField(verbose_name = "Date", null=True, blank=True)
    movie_images = models.ImageField(verbose_name = "Upload Poster", upload_to='posters', default=None, null=True, blank=True)
    movie_imdb_plugin = models.TextField(verbose_name = "IMDB Plugin", default=None, null=True, blank=True)
    movie_video_length = models.CharField(verbose_name = "Movie Duration",max_length=50, default=None, null=True, blank=True)
    movie_director = models.CharField(verbose_name = "Movie Director",max_length=100, default=None, null=True, blank=True)
    movie_actors = models.CharField(verbose_name = "Movie Actors",max_length=100, default=None, null=True, blank=True)
    movie_genres = models.CharField(verbose_name = "Movie Genres",max_length=100, default=None, null=True, blank=True)
    movie_trailer = models.CharField(verbose_name = "Movie Trailer",max_length=50, default=None, null=True, blank=True)

    movie_streaming_partner = models.CharField(verbose_name = "Movie Stream", max_length=1000, choices=STREAMING_SERVICES, default=None, null=True, blank=True)
    movie_streaming_link = models.TextField(verbose_name = "Streaming Link", default=None, null=True, blank=True)
    movie_audio = models.CharField(verbose_name = "Audio", max_length=100, default=None, null=True, blank=True)
    movie_available_youtube = models.CharField(verbose_name = "Available on Youtube", max_length=50, default=None, null=True, blank=True)

    def __str__(self):
        return self.movie_title