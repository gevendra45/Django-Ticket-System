# Generated by Django 3.0.6 on 2020-05-10 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='req',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('In-Progress', 'In-Progress'), ('Completed', 'Completed')], default='Pending', max_length=15),
        ),
    ]
