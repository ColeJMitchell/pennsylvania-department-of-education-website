# Generated by Django 5.1.1 on 2024-12-07 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_district_career_and_technical_center_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='districtkeystonestats',
            name='group',
        ),
        migrations.AddField(
            model_name='districtkeystone',
            name='group',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
