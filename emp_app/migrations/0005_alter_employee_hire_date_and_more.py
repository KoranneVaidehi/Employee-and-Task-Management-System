# Generated by Django 5.1.5 on 2025-02-24 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0004_alter_employee_hire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='task_manager',
            name='task_priority',
            field=models.CharField(choices=[('Medium', 'Medium'), ('Low', 'Low'), ('High', 'High')], max_length=10),
        ),
        migrations.AlterField(
            model_name='task_manager',
            name='task_status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Not Started', 'Not Started'), ('In Progress', 'In Progress')], max_length=15),
        ),
    ]
