# Generated by Django 5.1.1 on 2024-12-07 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_rename_school_enrollment_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='district_enrollment',
        ),
        migrations.RemoveField(
            model_name='district',
            name='number_of_schools',
        ),
    ]
