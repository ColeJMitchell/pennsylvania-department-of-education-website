# Generated by Django 5.1.1 on 2024-12-07 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_districtkeystone_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districtkeystone',
            name='group',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='districtkeystone',
            name='numbers_scored',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='districtkeystone',
            name='percent_advanced',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='districtkeystone',
            name='percent_basic',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='districtkeystone',
            name='percent_below_basic',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='districtkeystone',
            name='percent_proficient',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='districtkeystone',
            name='year',
            field=models.IntegerField(),
        ),
    ]
