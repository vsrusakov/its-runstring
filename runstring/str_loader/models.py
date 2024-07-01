from django.db import models

# Create your models here.

class Video(models.Model):

    user_ip = models.GenericIPAddressField()
    text = models.TextField()
    fps = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text