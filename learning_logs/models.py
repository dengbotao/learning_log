from django.db import models

# Create your models here.
class Topic(models.Model):
    """the learning topics"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return the string of model"""
        return self.text

class Entry(models.Model):
    pass
