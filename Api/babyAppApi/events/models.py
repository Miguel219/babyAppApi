from django.db import models


class Event(models.Model):
    eventType = models.CharField(max_length=50)
    notes = models.CharField(max_length=500)
    date = models.DateField()
    baby = models.ForeignKey('babies.Baby', on_delete=models.CASCADE)

    def __str__(self):
        return 'Event: {}'.format(self.notes)
