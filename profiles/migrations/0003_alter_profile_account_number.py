# Generated by Django 4.0.4 on 2022-10-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_avatar_profile_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
