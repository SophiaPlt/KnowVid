# Generated by Django 5.0.4 on 2024-05-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='file',
            field=models.FileField(upload_to='lessons/'),
        ),
    ]