# Generated by Django 4.0.5 on 2022-07-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post/'),
        ),
    ]
