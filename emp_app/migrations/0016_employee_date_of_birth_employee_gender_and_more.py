# Generated by Django 5.1.5 on 2025-02-27 05:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0015_remove_weekly_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2004, 1, 1)),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Single', max_length=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='profile_photo',
            field=models.ImageField(default='profile_photos/default.png', upload_to='profile_photos/'),
        ),
    ]
