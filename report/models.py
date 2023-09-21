from django.db import models
from django.utils.translation import gettext_lazy as _

class Machine(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name

class Standard(models.Model):
    name = models.CharField(max_length=30)
    threshold_1 = models.IntegerField()
    threshold_2 = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Reading(models.Model):
    class Severity(models.TextChoices):
        SAFE = 'S', _('Safe')
        ALARM = 'A', _('Alarm')
        DANGER = 'D', _('Danger')
    value = models.IntegerField()
    severity = models.CharField(
        max_length=1,
        choices=Severity.choices
    )

class MeasurementPoint(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        

class Report(models.Model):
    class Severity(models.TextChoices):
        SAFE = 'S', _('Safe')
        ALARM = 'A', _('Alarm')
        DANGER = 'D', _('Danger')

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    overall_severity = models.CharField(
        max_length=1,
        choices=Severity.choices,
        null=True
    )
    measurement_points = models.ManyToManyField(MeasurementPoint, through='ReportMeasurementPoint')

    def __str__(self) -> str:
        return '{self.machine.name} - {self.date}'

class ReportMeasurementPoint(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    measurement_point = models.ForeignKey(MeasurementPoint, on_delete=models.CASCADE)
    x_reading = models.ForeignKey(Reading, on_delete=models.CASCADE, related_name="x_reading")
    y_reading = models.ForeignKey(Reading, on_delete=models.CASCADE, related_name="y_reading")
    z_reading = models.ForeignKey(Reading, on_delete=models.CASCADE, related_name="z_reading")


