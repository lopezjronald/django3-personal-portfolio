from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='templates/portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.id, self.title
