# Generated by Django 4.0.4 on 2022-06-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='file_uploaded_time',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
