# Generated by Django 4.1.6 on 2023-10-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userbookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbookings',
            name='date',
            field=models.CharField(default='NA', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userbookings',
            name='time',
            field=models.CharField(default='NA', max_length=255),
            preserve_default=False,
        ),
    ]