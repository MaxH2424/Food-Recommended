# Generated by Django 2.2.7 on 2019-11-19 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAPI', '0009_auto_20191117_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='rest',
            name='banner',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
