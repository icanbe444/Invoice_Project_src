# Generated by Django 4.0.4 on 2022-08-23 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/silihouette.jpeg', upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_logo',
            field=models.ImageField(default='images/logo.png', upload_to=''),
        ),
    ]
