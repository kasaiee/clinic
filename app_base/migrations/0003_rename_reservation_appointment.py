# Generated by Django 4.0.2 on 2022-02-24 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0002_service_alter_speciality_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservation',
            new_name='Appointment',
        ),
    ]
