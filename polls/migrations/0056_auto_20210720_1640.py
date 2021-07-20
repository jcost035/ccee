# Generated by Django 3.1.5 on 2021-07-20 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0055_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailydose',
            old_name='title',
            new_name='topic',
        ),
        migrations.RemoveField(
            model_name='dailydose',
            name='description',
        ),
        migrations.RemoveField(
            model_name='dailydose',
            name='first_article_url',
        ),
        migrations.RemoveField(
            model_name='dailydose',
            name='fourth_article_url',
        ),
        migrations.RemoveField(
            model_name='dailydose',
            name='name',
        ),
        migrations.RemoveField(
            model_name='dailydose',
            name='second_article_url',
        ),
        migrations.RemoveField(
            model_name='dailydose',
            name='third_article_url',
        ),
        migrations.AddField(
            model_name='dailydose',
            name='banner_photo',
            field=models.ImageField(blank=True, default='', upload_to='programs'),
        ),
        migrations.AddField(
            model_name='dailydose',
            name='first_resource_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dailydose',
            name='fourth_resource_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dailydose',
            name='second_resource_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dailydose',
            name='third_resource_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dailydose',
            name='first_panel_image',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailydose',
            name='grade_band',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dailydose',
            name='second_panel_image',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailydose',
            name='tags',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
