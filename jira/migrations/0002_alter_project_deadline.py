# Generated by Django 5.1.6 on 2025-03-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jira', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
