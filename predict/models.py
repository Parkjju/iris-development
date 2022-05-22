from django.db import models


class PredResults(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=30)
    ml_algorithm = models.CharField(max_length=30, default= "default")
    ml_param = models.CharField(max_length=30, default= "default")

    def __str__(self):
        return f'{self.classification} : {self.ml_algorithm} | {self.ml_param}'

