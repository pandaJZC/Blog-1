# Generated by Django 2.1.7 on 2019-04-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190416_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail'),
        ),
    ]