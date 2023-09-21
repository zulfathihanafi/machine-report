# Generated by Django 4.2.5 on 2023-09-21 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='overall_severity',
            field=models.CharField(choices=[('S', 'Safe'), ('A', 'Alarm'), ('D', 'Danger')], max_length=1, null=True),
        ),
    ]
