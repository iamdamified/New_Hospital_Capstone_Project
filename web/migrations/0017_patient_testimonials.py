# Generated by Django 4.2.2 on 2023-06-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_rename_date_requested_appointment_chosen_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='testimonials',
            field=models.TextField(blank=True),
        ),
    ]
