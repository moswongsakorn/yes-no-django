# Generated by Django 3.0 on 2020-01-08 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='image',
            new_name='images',
        ),
    ]
