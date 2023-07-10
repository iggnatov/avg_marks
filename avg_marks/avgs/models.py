from django.db import models


class Application(models.Model):
    spec_code = models.ForeignKey('specs.Spec', to_field='code', on_delete=models.CASCADE)
    financing_type = models.CharField(max_length=255)
    originals = models.CharField(max_length=10, default="Не сдан")
    avg_marks = models.DecimalField(max_digits=3, decimal_places=2)
    certificate_number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.spec_code} - {self.financing_type} - {self.avg_marks}'

