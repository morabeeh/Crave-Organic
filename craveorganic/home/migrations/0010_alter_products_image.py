# Generated by Django 3.2.9 on 2022-10-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='blog/%Y/%m/%d'),
        ),
    ]
