# Generated by Django 3.2.9 on 2021-12-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='states',
            field=models.IntegerField(choices=[(0, 'Unpublished'), (1, 'published')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
