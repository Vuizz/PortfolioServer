# Generated by Django 4.2.4 on 2023-08-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_workexperiences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperiences',
            name='year',
        ),
        migrations.AddField(
            model_name='workexperiences',
            name='somethinghere',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
