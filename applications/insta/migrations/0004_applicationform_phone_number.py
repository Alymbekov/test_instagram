# Generated by Django 2.2.1 on 2020-11-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_applicationform'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationform',
            name='phone_number',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
