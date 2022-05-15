from django.db import models


class PredResults(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=30)
    ml_algorithm = models.CharField(max_length=30, default= "KNeighborsClassifier(n_neighbors=1)")

    def __str__(self):
        return self.classification