# Generated by Django 3.1.3 on 2021-06-24 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['pub_date']},
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
