from django.db import models
from django.contrib.auth.models import User

class PredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.username}'

class PredResults(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=45)
    ml_algorithm = models.CharField(max_length=60, default= "default")
    ml_param = models.CharField(max_length=60, default= "default")

    username = models.CharField(max_length=60, default= "admin")
    user = models.ForeignKey(PredUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.classification} : {self.ml_algorithm} | {self.ml_param}'

# ###
# user
# 1234
# ###

