from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# add the model to the settings

# Create a migration
# go into the terminal and enter python manage.py makemigrations

# Migrate
# terminal: python manage.py migrate

# Add to the admin
