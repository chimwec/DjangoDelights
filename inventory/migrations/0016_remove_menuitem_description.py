# Generated by Django 5.0.3 on 2024-06-10 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='description',
        ),
    ]
