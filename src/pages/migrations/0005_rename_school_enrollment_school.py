# Generated by Django 5.1.1 on 2024-10-16 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_enrollment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='School',
            new_name='school',
        ),
    ]
