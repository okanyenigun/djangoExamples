from django.db import models

class Customers(models.Model):
    person = models.TextField(blank=True, null=True) 
    website = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.person

