# Generated by Django 3.2.9 on 2022-10-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_products_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='images',
            field=models.ImageField(upload_to='blog/%Y/%m/%d'),
        ),
    ]
