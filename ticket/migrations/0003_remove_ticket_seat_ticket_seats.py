# Generated by Django 5.0.1 on 2024-01-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_alter_seat_price'),
        ('ticket', '0002_rename_customer_profile_ticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='seat',
        ),
        migrations.AddField(
            model_name='ticket',
            name='seats',
            field=models.ManyToManyField(to='cinema.seat'),
        ),
    ]
