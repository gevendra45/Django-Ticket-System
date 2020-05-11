# Generated by Django 3.0.6 on 2020-05-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0002_auto_20200511_0356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='req',
            old_name='ccode',
            new_name='CoutryCode',
        ),
        migrations.RenameField(
            model_name='req',
            old_name='reqdesc',
            new_name='RequestDescription',
        ),
        migrations.RenameField(
            model_name='req',
            old_name='sec_num',
            new_name='SecodaryNumber',
        ),
        migrations.RemoveField(
            model_name='req',
            name='req',
        ),
        migrations.AddField(
            model_name='req',
            name='RequestType',
            field=models.CharField(blank=True, choices=[('Plumbing', 'Plumbing'), ('Electrical', 'Electrical'), ('Painting', 'Painting'), ('Cleaning', 'Cleaning')], max_length=15),
        ),
    ]
