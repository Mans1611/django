# Generated by Django 4.2.2 on 2023-07-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_tasks_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='icons',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
