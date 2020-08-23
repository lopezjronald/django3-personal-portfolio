from django.db import models

class WeeklyAccountabilityMeeting(models.Model):
    theme = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='templates/wam/images')
    url = models.URLField()

    def __str__(self):
        return self.id, self.theme