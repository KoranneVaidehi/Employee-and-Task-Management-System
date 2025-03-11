# Generated by Django 5.1.5 on 2025-02-26 16:38

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0013_chatroom_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('activity', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('daily_hours', models.IntegerField()),
                ('weekly_hours', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
