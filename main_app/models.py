from django.db import models

class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name