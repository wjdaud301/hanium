# Generated by Django 2.2.12 on 2020-05-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartfarm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_values',
            old_name='control',
            new_name='fan_ctl',
        ),
        migrations.AddField(
            model_name='data_values',
            name='light_ctl',
            field=models.BooleanField(default=0, verbose_name=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data_values',
            name='water_ctl',
            field=models.BooleanField(default=0, verbose_name=False),
            preserve_default=False,
        ),
    ]