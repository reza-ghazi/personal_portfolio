from django.db import models


# We need to create a class which is inherits from models.Model in Django.
# Inside this class, we will define all database field that we want.
class Project(models.Model):
    # Each field is defines by Django database field types.
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    link_label = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.title
