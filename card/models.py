from django.db import models

class box (models.Model):
    pic = models.ImageField(upload_to='images', blank=True)
    message = models.TextField()
    name = models.CharField(max_length = 200, default = 'joe')

    def __str__(self):
        return self.name
