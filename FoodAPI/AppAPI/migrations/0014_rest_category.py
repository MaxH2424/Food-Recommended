# Generated by Django 2.2.7 on 2019-11-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAPI', '0013_auto_20191121_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='rest',
            name='category',
            field=models.PositiveIntegerField(default=0),
        ),
    ]