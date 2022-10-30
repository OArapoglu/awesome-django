from django.db import models


class FilmData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    type = models.CharField(max_length=200, default="action")
    image = models.ImageField(
        upload_to="Images/", default="Images/image_placeholder.jpg"
    )

    def __str__(self):
        return self.name
