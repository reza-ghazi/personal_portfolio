from django.db import models


class Blog(models.Model):
    # Each field is defines by Django database field types.
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    url = models.URLField(blank=True)

    # Showing the title of blog in the list of blogs in Admin portal instead of showing 'blog 1', 'blog 2', and so on.
    def __str__(self):
        return self.title
