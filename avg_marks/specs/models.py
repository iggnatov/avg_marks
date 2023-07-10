from django.db import models


class Spec(models.Model):
    code = models.CharField(max_length=10, unique=True)
    spec_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.code} - {self.spec_name}'
