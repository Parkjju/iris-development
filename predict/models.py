from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from accounts.models import PredUser

class PredResults(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=45)
    ml_algorithm = models.CharField(max_length=60, default= "default")
    ml_param = models.CharField(max_length=60, default= "default")

    username = models.CharField(max_length=60, default= "admin")
    user = models.ForeignKey(PredUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.classification} : {self.ml_algorithm} | {self.ml_param}'

# ###
# user
# 1234

'''
user_first
1234
'''
# ###

