# Generated by Django 4.2.2 on 2023-07-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
