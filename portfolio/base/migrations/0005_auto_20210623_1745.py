# Generated by Django 3.1.3 on 2021-06-24 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210623_1743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['sorting']},
        ),
        migrations.AddField(
            model_name='card',
            name='sorting',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
