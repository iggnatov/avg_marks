# Generated by Django 4.2.3 on 2023-08-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0005_alter_spec_after_09_alter_spec_after_11'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spec',
            old_name='period_of_study',
            new_name='period_of_study_09',
        ),
        migrations.AddField(
            model_name='spec',
            name='period_of_study_11',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
