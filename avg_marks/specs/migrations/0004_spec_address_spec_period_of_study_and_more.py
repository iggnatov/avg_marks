# Generated by Django 4.2.3 on 2023-07-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0003_alter_spec_after_09_alter_spec_after_11'),
    ]

    operations = [
        migrations.AddField(
            model_name='spec',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='spec',
            name='period_of_study',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='spec',
            name='plan_priema_09',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spec',
            name='plan_priema_11',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
