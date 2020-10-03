# Generated by Django 2.2.12 on 2020-06-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartfarm', '0005_auto_20200520_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ctl_values_1F',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fan_ctl', models.BooleanField()),
                ('water_ctl', models.BooleanField()),
                ('light_ctl', models.BooleanField()),
                ('slide', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ctl_values_2F',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fan_ctl', models.BooleanField()),
                ('water_ctl', models.BooleanField()),
                ('light_ctl', models.BooleanField()),
                ('slide', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Data_values_1F',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('tem_data', models.FloatField()),
                ('hum_data', models.FloatField()),
                ('light_data', models.FloatField()),
                ('sm_data', models.FloatField()),
                ('co2', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data_values_2F',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('tem_data', models.FloatField()),
                ('hum_data', models.FloatField()),
                ('light_data', models.FloatField()),
                ('sm_data', models.FloatField()),
                ('co2', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Ctl_values',
        ),
        migrations.DeleteModel(
            name='Data_values',
        ),
    ]