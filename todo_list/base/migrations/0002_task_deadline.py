# Generated by Django 4.1.5 on 2023-02-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
