# Generated by Django 4.1.6 on 2023-10-27 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accessLevel',
            field=models.CharField(default='Admin', max_length=255),
        ),
    ]