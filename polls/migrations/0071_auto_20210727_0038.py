# Generated by Django 3.1.5 on 2021-07-27 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0070_auto_20210727_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailydose',
            name='first_panel_is_image',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='dailydose',
            name='second_panel_is_image',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
