# Generated by Django 4.1.6 on 2023-11-05 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userId',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]