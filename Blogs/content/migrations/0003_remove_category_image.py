# Generated by Django 4.0.5 on 2022-07-24 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_rename_cat_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
