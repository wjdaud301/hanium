# Generated by Django 2.2.12 on 2020-08-06 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0004_auto_20200806_1016'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addresses',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]