from django.db import models




class FeedingEvent(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()  # Duration in seconds
    amount = models.FloatField()  # Amount of food dispensed

    def __str__(self):
        return f"{self.timestamp} - {self.duration}s - {self.amount}g"

