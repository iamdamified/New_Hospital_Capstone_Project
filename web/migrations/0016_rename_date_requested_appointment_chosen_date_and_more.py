# Generated by Django 4.2.2 on 2023-06-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_rename_name_appointment_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date_requested',
            new_name='chosen_date',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='time',
            new_name='chosen_time',
        ),
    ]
