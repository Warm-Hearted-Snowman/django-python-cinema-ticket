# Generated by Django 5.0.1 on 2024-01-06 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='customer_profile',
            new_name='user',
        ),
    ]
