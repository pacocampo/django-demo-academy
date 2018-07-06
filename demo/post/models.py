from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length=500, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

