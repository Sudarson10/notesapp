# Generated by Django 4.2.4 on 2024-02-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]
