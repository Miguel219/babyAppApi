from django.db import models
from django.contrib.auth.models import User


class Baby(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    parent = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return 'Baby: {}'.format(self.firstName)
