# Generated by Django 4.0.5 on 2022-07-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_rename_category_post_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
