from django.db import models

class Prediction(models.Model):
    actual_x = models.IntegerField()
    predicted_x = models.IntegerField();
    date = models.CharField(max_length=255)
    team_x = models.CharField(max_length=255)
    opponent_x = models.CharField(max_length=255)
    result_x = models.CharField(max_length=255)
    new_team_x = models.CharField(max_length=255)
    actual_y = models.IntegerField()
    predicted_y = models.IntegerField()
    team_y = models.CharField(max_length=255)
    opponent_y = models.CharField(max_length=255)
    result_y = models.CharField(max_length=255)
    new_team_y = models.CharField(max_length=255)
# Create your models here.
