# Generated by Django 3.1.5 on 2021-10-15 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0074_program_registration_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.CharField(blank=True, default='12:00 PM', max_length=200),
        ),
    ]
