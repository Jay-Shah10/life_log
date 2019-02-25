from django.db import models

# Create your models here.
class Event(models.Model):
    """An Event in the user's life"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific about this Event."""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else: 
            return self.text


    