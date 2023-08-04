from django.db import models


class Application(models.Model):
    spec_code = models.ForeignKey('specs.Spec', to_field='code', on_delete=models.CASCADE)
    financing_type = models.BooleanField(default=False)
    originals = models.BooleanField(default=False)
    avg_marks = models.DecimalField(max_digits=3, decimal_places=2)
    certificate_number = models.CharField(max_length=50)
    grade = models.BooleanField(default=True)  # if true - after 9; false - after 11

    def __str__(self):
        return f'{self.spec_code} - {self.financing_type} - {self.avg_marks}'


class AppRQty(models.Model):
    today = models.CharField(max_length=10)
    day = models.CharField(max_length=10)
    q_ty = models.PositiveSmallIntegerField(null=True, blank=True)
