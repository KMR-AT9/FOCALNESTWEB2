# Generated by Django 4.2.7 on 2023-11-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FocalNest', '0005_remove_blogpost_date_published_alter_blogpost_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='blog_images/'),
        ),
    ]
