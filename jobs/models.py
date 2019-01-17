from django.db import models

# you usually have one model per app - but you can have more


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
