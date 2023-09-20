from django.db import models

# Create your models here.
    
class Standard(models.Model):
    name = models.CharField(max_length=12)
    threshold_1 = models.IntegerField()
    threshold_2 = models.IntegerField()
    def __str__(self) -> str : 
        return self.name

class MeasurementPoint(models.model):
    name = models.CharField(max_length=20)
    standard = models.ForeignKey(Standard)
    def __str__(self) -> str : 
        return self.name

class MeasurementPointResults(models.Model):
    point = models.ForeignKey(MeasurementPoint)
    result_x = models.IntegerField()
    result_y = models.IntegerField() 
    result_z = models.IntegerField()
    severity = models.CharField(max_length=20)

class Report(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    overall_severity = models.CharField()
    results = models.ForeignKey()
