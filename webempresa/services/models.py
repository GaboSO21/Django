from django.db import models

# Create your models here.

class Service(models.Model):
    
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='services')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['created']

    def __str__(self):
        return self.title
