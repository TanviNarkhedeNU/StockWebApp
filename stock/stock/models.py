from django.db import models
class Equities(models.Model):
    id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    ticker = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    def __str__(self):
         return self.id

class Returns(models.Model):
    date = models.DateTimeField()
    returns = models.FloatField()
    equity_id = models.ForeignKey(Equities, on_delete=models.CASCADE)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    def __str__(self):
        return self.date