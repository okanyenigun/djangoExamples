from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    def speak(self):
        return 'The %s says "%s"' % (self.name, self.sound)
    
class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    top_speed = models.IntegerField()
    is_electric = models.BooleanField(default=False)

    def description(self):
        return f"{self.name} can go up to {self.top_speed} km/h."

    def is_fast(self):
        return self.top_speed > 200