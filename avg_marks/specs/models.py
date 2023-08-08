from django.db import models


class Spec(models.Model):
    code = models.CharField(max_length=10, unique=True)
    spec_name = models.CharField(max_length=255)
    after_09 = models.BooleanField(default=True)
    after_11 = models.BooleanField(default=True)
    address = models.CharField(max_length=255, blank=True)
    period_of_study_09 = models.CharField(max_length=100, blank=True)
    period_of_study_11 = models.CharField(max_length=100, blank=True)
    plan_priema_09 = models.PositiveSmallIntegerField(null=True, blank=True)
    plan_priema_11 = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.code} - {self.spec_name}'
