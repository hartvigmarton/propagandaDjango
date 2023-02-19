from django.db import models

# Create your models here.
class Choice(models.Model):
    first_choice = models.CharField(max_length=200)
    second_choice = models.CharField(max_length=200)
    whatever = models.PositiveBigIntegerField(max_length=200)


    def __str__(self):
        return self.first_choice + ' ' + self.second_choice + ' ' + self.whatever